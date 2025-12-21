"""
Translation caching service for fast retrieval of translated content.
"""
import hashlib
import logging
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.sql import func

from backend.app.models.translation import TranslationCache

logger = logging.getLogger(__name__)


class TranslationCacheService:
    """
    Fast caching service for translated content.
    """
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.default_ttl_hours = 24  # Cache TTL in hours
    
    async def get_translation(
        self,
        chapter_path: str,
        content_hash: str,
        target_language: str
    ) -> Optional[str]:
        """
        Get cached translation if available and not expired.
        
        Args:
            chapter_path: Chapter identifier
            content_hash: Hash of source content
            target_language: Target language code
            
        Returns:
            Cached translated content or None if not found/expired
        """
        cache_key = self._generate_cache_key(chapter_path, content_hash, target_language)
        
        try:
            result = await self.db.execute(
                select(TranslationCache).where(
                    TranslationCache.cache_key == cache_key,
                    # Check if not expired (or no expiry set)
                    (TranslationCache.expires_at.is_(None)) | 
                    (TranslationCache.expires_at > func.now())
                )
            )
            
            cache_entry = result.scalar_one_or_none()
            
            if cache_entry:
                # Update access statistics
                await self._update_access_stats(cache_entry.id)
                
                logger.debug(f"Cache hit for key: {cache_key}")
                return cache_entry.translated_content
            else:
                logger.debug(f"Cache miss for key: {cache_key}")
                return None
                
        except Exception as e:
            logger.error(f"Error retrieving from cache: {e}")
            return None
    
    async def store_translation(
        self,
        chapter_path: str,
        content_hash: str,
        translated_content: str,
        target_language: str,
        ttl_hours: Optional[int] = None
    ) -> bool:
        """
        Store translation in cache.
        
        Args:
            chapter_path: Chapter identifier
            content_hash: Hash of source content
            translated_content: Translated content to cache
            target_language: Target language code
            ttl_hours: Time to live in hours (default: 24)
            
        Returns:
            True if stored successfully, False otherwise
        """
        cache_key = self._generate_cache_key(chapter_path, content_hash, target_language)
        ttl = ttl_hours or self.default_ttl_hours
        
        try:
            # Calculate expiry time
            expires_at = datetime.utcnow() + timedelta(hours=ttl)
            
            # Check if entry already exists
            existing_result = await self.db.execute(
                select(TranslationCache).where(
                    TranslationCache.cache_key == cache_key
                )
            )
            
            existing_entry = existing_result.scalar_one_or_none()
            
            if existing_entry:
                # Update existing entry
                existing_entry.translated_content = translated_content
                existing_entry.expires_at = expires_at
                existing_entry.updated_at = func.now()
                logger.debug(f"Updated cache entry: {cache_key}")
            else:
                # Create new entry
                cache_entry = TranslationCache(
                    cache_key=cache_key,
                    chapter_path=chapter_path,
                    target_language=target_language,
                    translated_content=translated_content,
                    expires_at=expires_at,
                    access_count=0
                )
                
                self.db.add(cache_entry)
                logger.debug(f"Created cache entry: {cache_key}")
            
            await self.db.commit()
            return True
            
        except Exception as e:
            logger.error(f"Error storing in cache: {e}")
            await self.db.rollback()
            return False
    
    async def clear_cache(
        self,
        chapter_path: Optional[str] = None,
        target_language: Optional[str] = None
    ) -> int:
        """
        Clear cache entries.
        
        Args:
            chapter_path: Clear cache for specific chapter (optional)
            target_language: Clear cache for specific language (optional)
            
        Returns:
            Number of entries cleared
        """
        try:
            query = delete(TranslationCache)
            
            # Add filters if provided
            if chapter_path:
                query = query.where(TranslationCache.chapter_path == chapter_path)
            
            if target_language:
                query = query.where(TranslationCache.target_language == target_language)
            
            result = await self.db.execute(query)
            await self.db.commit()
            
            cleared_count = result.rowcount
            logger.info(f"Cleared {cleared_count} cache entries")
            return cleared_count
            
        except Exception as e:
            logger.error(f"Error clearing cache: {e}")
            await self.db.rollback()
            return 0
    
    async def clear_expired_cache(self) -> int:
        """
        Clear expired cache entries.
        
        Returns:
            Number of expired entries cleared
        """
        try:
            result = await self.db.execute(
                delete(TranslationCache).where(
                    TranslationCache.expires_at < func.now()
                )
            )
            
            await self.db.commit()
            
            cleared_count = result.rowcount
            if cleared_count > 0:
                logger.info(f"Cleared {cleared_count} expired cache entries")
            
            return cleared_count
            
        except Exception as e:
            logger.error(f"Error clearing expired cache: {e}")
            await self.db.rollback()
            return 0
    
    async def get_cache_stats(self) -> dict:
        """
        Get cache statistics.
        
        Returns:
            Dictionary with cache statistics
        """
        try:
            # Total entries
            total_result = await self.db.execute(
                select(func.count(TranslationCache.id))
            )
            total_entries = total_result.scalar()
            
            # Expired entries
            expired_result = await self.db.execute(
                select(func.count(TranslationCache.id)).where(
                    TranslationCache.expires_at < func.now()
                )
            )
            expired_entries = expired_result.scalar()
            
            # Total access count
            access_result = await self.db.execute(
                select(func.sum(TranslationCache.access_count))
            )
            total_accesses = access_result.scalar() or 0
            
            # Most accessed entries
            popular_result = await self.db.execute(
                select(
                    TranslationCache.chapter_path,
                    TranslationCache.access_count
                ).order_by(
                    TranslationCache.access_count.desc()
                ).limit(5)
            )
            popular_entries = popular_result.all()
            
            return {
                "total_entries": total_entries,
                "expired_entries": expired_entries,
                "active_entries": total_entries - expired_entries,
                "total_accesses": total_accesses,
                "popular_chapters": [
                    {"chapter": row[0], "access_count": row[1]}
                    for row in popular_entries
                ]
            }
            
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
            return {
                "total_entries": 0,
                "expired_entries": 0,
                "active_entries": 0,
                "total_accesses": 0,
                "popular_chapters": []
            }
    
    async def _update_access_stats(self, cache_id: int):
        """Update access statistics for cache entry."""
        try:
            await self.db.execute(
                TranslationCache.__table__.update()
                .where(TranslationCache.id == cache_id)
                .values(
                    access_count=TranslationCache.access_count + 1,
                    last_accessed=func.now()
                )
            )
            await self.db.commit()
        except Exception as e:
            logger.error(f"Error updating access stats: {e}")
    
    def _generate_cache_key(
        self,
        chapter_path: str,
        content_hash: str,
        target_language: str
    ) -> str:
        """Generate unique cache key."""
        key_string = f"{chapter_path}:{content_hash}:{target_language}"
        return hashlib.sha256(key_string.encode('utf-8')).hexdigest()[:32]
