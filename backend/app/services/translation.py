"""
Translation service for Urdu content translation using OpenAI.
"""
import asyncio
import hashlib
import logging
import time
from typing import Optional, Dict, Any, List, Tuple

from openai import OpenAI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.config import get_settings
from app.models.translation import Translation, TranslationMetadata
from app.services.translation_cache import TranslationCacheService

logger = logging.getLogger(__name__)
settings = get_settings()


class TranslationResult:
    """Result of a translation operation."""
    
    def __init__(
        self,
        translated_content: str,
        cached: bool = False,
        translation_time_ms: int = 0,
        word_count: int = 0,
        quality_score: Optional[float] = None
    ):
        self.translated_content = translated_content
        self.cached = cached
        self.translation_time_ms = translation_time_ms
        self.word_count = word_count
        self.quality_score = quality_score


class TranslationService:
    """
    Service for translating chapter content to Urdu using OpenAI.
    """
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.openai_client = OpenAI(api_key=settings.openai_api_key)
        self.cache_service = TranslationCacheService(db)
        
    async def translate_chapter(
        self,
        chapter_path: str,
        content: str,
        target_language: str = "ur",
        force_retranslate: bool = False
    ) -> TranslationResult:
        """
        Translate chapter content to target language.
        
        Args:
            chapter_path: Path identifier for the chapter
            content: Source content to translate
            target_language: Target language code (default: "ur" for Urdu)
            force_retranslate: Force new translation even if cached
            
        Returns:
            TranslationResult with translated content and metadata
        """
        start_time = time.time()
        
        # Generate content hash for caching
        content_hash = self._generate_content_hash(content)
        
        # Check cache first (unless forced retranslation)
        if not force_retranslate:
            cached_result = await self._get_cached_translation(
                chapter_path, content_hash, target_language
            )
            if cached_result:
                logger.info(f"Cache hit for chapter: {chapter_path}")
                return cached_result
        
        logger.info(f"Translating chapter: {chapter_path} to {target_language}")
        
        try:
            # Perform translation (this doesn't use database session)
            translated_content = await self._translate_with_openai(content, target_language)
            
            # Calculate metrics
            translation_time_ms = int((time.time() - start_time) * 1000)
            word_count = len(content.split())
            
            # Store translation in database (after translation completes)
            # This is safe because we're not in parallel operations anymore
            try:
                await self._store_translation(
                    chapter_path=chapter_path,
                    source_content=content,
                    translated_content=translated_content,
                    content_hash=content_hash,
                    target_language=target_language,
                    translation_time_ms=translation_time_ms,
                    word_count=word_count
                )
                
                # Store in cache for fast access
                await self.cache_service.store_translation(
                    chapter_path, content_hash, translated_content, target_language
                )
            except Exception as db_error:
                # Log database error but don't fail the translation
                logger.error(f"Failed to store translation in database: {db_error}")
                # Translation was successful, so we continue
            
            logger.info(f"Translation completed for {chapter_path} in {translation_time_ms}ms")
            
            return TranslationResult(
                translated_content=translated_content,
                cached=False,
                translation_time_ms=translation_time_ms,
                word_count=word_count
            )
            
        except Exception as e:
            logger.error(f"Translation failed for {chapter_path}: {e}")
            
            # Store error metadata
            await self._store_translation_metadata(
                chapter_path=chapter_path,
                target_language=target_language,
                translation_status="failed",
                error_message=str(e),
                translation_time_ms=int((time.time() - start_time) * 1000)
            )
            
            raise RuntimeError(f"Translation failed: {str(e)}")
    
    async def _get_cached_translation(
        self,
        chapter_path: str,
        content_hash: str,
        target_language: str
    ) -> Optional[TranslationResult]:
        """Get translation from cache if available."""
        
        # Check database cache first
        result = await self.db.execute(
            select(Translation).where(
                Translation.chapter_path == chapter_path,
                Translation.target_language == target_language,
                Translation.content_hash == content_hash
            )
        )
        
        translation = result.scalar_one_or_none()
        if translation:
            return TranslationResult(
                translated_content=translation.translated_content,
                cached=True,
                translation_time_ms=translation.translation_time_ms or 0,
                word_count=translation.word_count or 0
            )
        
        # Check fast cache
        cached_content = await self.cache_service.get_translation(
            chapter_path, content_hash, target_language
        )
        if cached_content:
            return TranslationResult(
                translated_content=cached_content,
                cached=True,
                translation_time_ms=0,
                word_count=0
            )
        
        return None
    
    async def _translate_with_openai(self, content: str, target_language: str) -> str:
        """Perform translation using OpenAI API with chunking for large content."""
        
        # Estimate content size (rough approximation: 1 token ≈ 4 characters)
        content_size = len(content)
        max_chunk_size = 15000  # ~3750 tokens per chunk (optimized for parallel processing)
        
        # If content is small, translate directly
        if content_size <= max_chunk_size:
            return await self._translate_chunk(content, target_language)
        
        # For large content, split into chunks and translate in parallel
        logger.info(f"Large content detected ({content_size} chars), splitting into chunks")
        chunks = self._split_content_into_chunks(content, max_chunk_size)
        
        # Safety check: ensure we have chunks
        if not chunks or len(chunks) == 0:
            logger.warning("No chunks generated, translating entire content as single chunk")
            return await self._translate_chunk(content, target_language)
        
        logger.info(f"Split into {len(chunks)} chunks for parallel translation")
        
        # Translate chunks in parallel for faster processing
        async def translate_chunk_with_index(index: int, chunk: str) -> Tuple[int, str]:
            """Translate a chunk and return its index and result."""
            try:
                logger.info(f"Translating chunk {index+1}/{len(chunks)} ({len(chunk)} chars)")
                translated = await self._translate_chunk(chunk, target_language)
                logger.info(f"Successfully translated chunk {index+1}/{len(chunks)}")
                return (index, translated)
            except Exception as e:
                logger.error(f"Error translating chunk {index+1}: {e}")
                logger.error(f"Chunk {index+1} error details: {type(e).__name__}: {str(e)}")
                # If chunk translation fails, keep original chunk
                return (index, chunk)
        
        # Create tasks for all chunks
        tasks = [translate_chunk_with_index(i, chunk) for i, chunk in enumerate(chunks)]
        
        # Execute all translations in parallel with error handling
        logger.info(f"Starting parallel translation of {len(chunks)} chunks...")
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Process results and handle exceptions
            processed_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    logger.error(f"Chunk {i+1} raised exception: {result}")
                    # Use original chunk if translation failed
                    processed_results.append((i, chunks[i]))
                else:
                    processed_results.append(result)
            
            # Sort results by index to maintain original order
            processed_results.sort(key=lambda x: x[0])
            translated_chunks = [result[1] for result in processed_results]
            
            logger.info(f"Completed parallel translation of {len(chunks)} chunks")
            
        except Exception as e:
            logger.error(f"Critical error in parallel translation: {e}")
            # Fallback to sequential translation if parallel fails
            logger.warning("Falling back to sequential translation...")
            translated_chunks = []
            for i, chunk in enumerate(chunks):
                try:
                    translated = await self._translate_chunk(chunk, target_language)
                    translated_chunks.append(translated)
                except Exception as chunk_error:
                    logger.error(f"Sequential translation also failed for chunk {i+1}: {chunk_error}")
                    translated_chunks.append(chunk)  # Keep original on failure
        
        # Combine translated chunks
        return "\n\n".join(translated_chunks)
    
    def _split_content_into_chunks(self, content: str, max_chunk_size: int) -> List[str]:
        """Split content into chunks while preserving markdown structure."""
        chunks = []
        
        # Try to split by markdown headers first (preserves structure)
        import re
        
        # Split by double newlines (paragraph breaks) first
        paragraphs = content.split('\n\n')
        
        current_chunk = ""
        for para in paragraphs:
            # If adding this paragraph would exceed max size, save current chunk
            if current_chunk and len(current_chunk) + len(para) + 2 > max_chunk_size:
                chunks.append(current_chunk.strip())
                current_chunk = para
            else:
                if current_chunk:
                    current_chunk += "\n\n" + para
                else:
                    current_chunk = para
        
        # Add remaining chunk
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        # If any chunk is still too large, split it further by single newlines
        final_chunks = []
        for chunk in chunks:
            if len(chunk) <= max_chunk_size:
                final_chunks.append(chunk)
            else:
                # Split by single newlines
                lines = chunk.split('\n')
                current_subchunk = ""
                for line in lines:
                    if current_subchunk and len(current_subchunk) + len(line) + 1 > max_chunk_size:
                        final_chunks.append(current_subchunk.strip())
                        current_subchunk = line
                    else:
                        if current_subchunk:
                            current_subchunk += "\n" + line
                        else:
                            current_subchunk = line
                if current_subchunk.strip():
                    final_chunks.append(current_subchunk.strip())
        
        return final_chunks if final_chunks else [content]
    
    async def _translate_chunk(self, chunk: str, target_language: str) -> str:
        """Translate a single chunk using OpenAI API."""
        prompt = self._get_translation_prompt(chunk, target_language)
        
        try:
            # Use faster model for translation
            translation_model = "gpt-4o-mini"  # Faster and cheaper than gpt-4o
            
            response = self.openai_client.chat.completions.create(
                model=translation_model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": chunk}
                ],
                temperature=0.2,  # Lower temperature for consistent translations
                max_tokens=16000,  # Increased for longer chunks
                timeout=90,  # 90 second timeout (reduced since parallel processing is faster)
            )
            
            translated_content = response.choices[0].message.content
            
            if not translated_content:
                raise ValueError("Empty translation response from OpenAI")
            
            return translated_content.strip()
            
        except Exception as e:
            logger.error(f"OpenAI translation error for chunk: {e}")
            raise RuntimeError(f"OpenAI translation failed: {str(e)}")
    
    def _get_translation_prompt(self, content: str, target_language: str) -> str:
        """Generate translation prompt for OpenAI."""
        
        language_names = {
            "ur": "Urdu (اردو)",
            "en": "English"
        }
        
        target_lang_name = language_names.get(target_language, target_language)
        
        return f"""You are an expert technical translator specializing in robotics, AI, and computer science content.

Translate the following English technical content to {target_lang_name}:

CRITICAL TRANSLATION GUIDELINES:
1. **Preserve ALL markdown formatting** (headers, lists, code blocks, links, tables)
2. **Keep code blocks in English** - only translate comments inside code
3. **Preserve mathematical formulas and equations exactly**
4. **Keep proper nouns and brand names in English** (ROS 2, Gazebo, NVIDIA Isaac, etc.)
5. **Technical term translations:**
   - "Robot" → "روبوٹ"
   - "Artificial Intelligence" → "مصنوعی ذہانت"
   - "Machine Learning" → "مشین لرننگ"
   - "Neural Network" → "نیورل نیٹ ورک"
   - "Sensor" → "سینسر"
   - "Algorithm" → "الگورتھم"
6. **Use formal/academic Urdu register** appropriate for educational content
7. **Maintain cultural appropriateness** for Pakistani/Indian Urdu speakers
8. **Preserve all URLs, file paths, and technical references**
9. **Keep HTML tags and markdown syntax intact**
10. **Translate headings and section titles appropriately**

IMPORTANT: Return ONLY the translated content. Do not add explanations or comments."""
    
    async def _store_translation(
        self,
        chapter_path: str,
        source_content: str,
        translated_content: str,
        content_hash: str,
        target_language: str,
        translation_time_ms: int,
        word_count: int
    ):
        """Store translation in database."""
        
        translation = Translation(
            chapter_path=chapter_path,
            source_language="en",
            target_language=target_language,
            source_content=source_content,
            translated_content=translated_content,
            content_hash=content_hash,
            word_count=word_count,
            translation_time_ms=translation_time_ms,
            is_cached=True
        )
        
        self.db.add(translation)
        
        # Also store metadata
        await self._store_translation_metadata(
            chapter_path=chapter_path,
            target_language=target_language,
            total_words=word_count,
            translation_time_ms=translation_time_ms,
            translation_status="completed"
        )
        
        await self.db.commit()
    
    async def _store_translation_metadata(
        self,
        chapter_path: str,
        target_language: str,
        translation_status: str = "completed",
        total_words: Optional[int] = None,
        translation_time_ms: Optional[int] = None,
        error_message: Optional[str] = None
    ):
        """Store translation metadata for analytics."""
        
        metadata = TranslationMetadata(
            chapter_path=chapter_path,
            target_language=target_language,
            total_words=total_words,
            translation_time_ms=translation_time_ms,
            translation_status=translation_status,
            error_message=error_message
        )
        
        self.db.add(metadata)
        await self.db.commit()
    
    def _generate_content_hash(self, content: str) -> str:
        """Generate SHA-256 hash of content for caching."""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    async def get_translation_status(self, chapter_path: str, target_language: str = "ur") -> Dict[str, Any]:
        """Get translation status for a chapter."""
        
        # Check if translation exists
        result = await self.db.execute(
            select(Translation).where(
                Translation.chapter_path == chapter_path,
                Translation.target_language == target_language
            ).order_by(Translation.created_at.desc()).limit(1)
        )
        
        translation = result.scalar_one_or_none()
        
        if translation:
            return {
                "exists": True,
                "cached": True,
                "created_at": translation.created_at.isoformat(),
                "word_count": translation.word_count,
                "translation_time_ms": translation.translation_time_ms
            }
        else:
            return {
                "exists": False,
                "cached": False
            }
    
    async def clear_translation_cache(self, chapter_path: str, target_language: str = "ur") -> bool:
        """Clear cached translation for a chapter."""
        
        try:
            # Delete from main translations table
            await self.db.execute(
                Translation.__table__.delete().where(
                    Translation.chapter_path == chapter_path,
                    Translation.target_language == target_language
                )
            )
            
            # Clear from cache service
            await self.cache_service.clear_cache(chapter_path, target_language)
            
            await self.db.commit()
            
            logger.info(f"Cleared translation cache for {chapter_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to clear translation cache: {e}")
            await self.db.rollback()
            return False
