"""
Translation API endpoints for Urdu content translation.
"""
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.translation import TranslationService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/translate", tags=["translation"])


class TranslationRequest(BaseModel):
    """Request to translate chapter content."""
    chapter_path: str = Field(..., description="Chapter path identifier (e.g., '/docs/intro')")
    content: str = Field(..., description="Markdown content to translate")
    target_language: str = Field(default="ur", description="Target language code (ur for Urdu)")
    force_retranslate: bool = Field(default=False, description="Force new translation even if cached")


class TranslationResponse(BaseModel):
    """Response with translated content."""
    translated_content: str = Field(..., description="Translated markdown content")
    cached: bool = Field(..., description="Whether result was retrieved from cache")
    translation_time_ms: int = Field(..., description="Translation time in milliseconds")
    word_count: int = Field(..., description="Number of words in source content")
    chapter_path: str = Field(..., description="Chapter path that was translated")
    target_language: str = Field(..., description="Target language code")


class TranslationStatusResponse(BaseModel):
    """Response with translation status."""
    chapter_path: str
    target_language: str
    exists: bool = Field(..., description="Whether translation exists in cache")
    cached: bool = Field(..., description="Whether translation is cached")
    created_at: Optional[str] = Field(None, description="When translation was created (ISO format)")
    word_count: Optional[int] = Field(None, description="Number of words translated")
    translation_time_ms: Optional[int] = Field(None, description="Time taken for translation")


class CacheStatsResponse(BaseModel):
    """Response with cache statistics."""
    total_entries: int
    expired_entries: int
    active_entries: int
    total_accesses: int
    popular_chapters: list


@router.post("/chapter", response_model=TranslationResponse)
async def translate_chapter(
    request: TranslationRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Translate chapter content to target language.
    
    This endpoint translates markdown content using OpenAI and caches the result
    for fast subsequent access. The translation preserves markdown formatting,
    code blocks, and technical terminology.
    """
    try:
        # Validate input
        if not request.content.strip():
            raise HTTPException(status_code=400, detail="Content cannot be empty")
        
        if len(request.content) > 100000:  # 100KB limit
            raise HTTPException(
                status_code=400, 
                detail="Content too large. Maximum size is 100KB."
            )
        
        if request.target_language not in ["ur", "en"]:
            raise HTTPException(
                status_code=400,
                detail="Unsupported target language. Supported: 'ur' (Urdu), 'en' (English)"
            )
        
        logger.info(f"Translation request for chapter: {request.chapter_path}")
        
        # Initialize translation service
        translation_service = TranslationService(db)
        
        # Perform translation
        result = await translation_service.translate_chapter(
            chapter_path=request.chapter_path,
            content=request.content,
            target_language=request.target_language,
            force_retranslate=request.force_retranslate
        )
        
        logger.info(
            f"Translation completed for {request.chapter_path}: "
            f"cached={result.cached}, time={result.translation_time_ms}ms"
        )
        
        return TranslationResponse(
            translated_content=result.translated_content,
            cached=result.cached,
            translation_time_ms=result.translation_time_ms,
            word_count=result.word_count,
            chapter_path=request.chapter_path,
            target_language=request.target_language
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Translation error for {request.chapter_path}: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Translation failed: {str(e)}"
        )


@router.get("/status/{chapter_path:path}", response_model=TranslationStatusResponse)
async def get_translation_status(
    chapter_path: str,
    target_language: str = "ur",
    db: AsyncSession = Depends(get_db)
):
    """
    Get translation status for a specific chapter.
    
    Returns information about whether a translation exists in cache,
    when it was created, and performance metrics.
    """
    try:
        translation_service = TranslationService(db)
        
        status = await translation_service.get_translation_status(
            chapter_path=chapter_path,
            target_language=target_language
        )
        
        return TranslationStatusResponse(
            chapter_path=chapter_path,
            target_language=target_language,
            **status
        )
        
    except Exception as e:
        logger.error(f"Error getting translation status: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get translation status: {str(e)}"
        )


@router.delete("/cache/{chapter_path:path}")
async def clear_translation_cache(
    chapter_path: str,
    target_language: str = "ur",
    db: AsyncSession = Depends(get_db)
):
    """
    Clear cached translation for a specific chapter.
    
    This endpoint is typically used by administrators when source content
    has been updated and translations need to be refreshed.
    """
    try:
        translation_service = TranslationService(db)
        
        success = await translation_service.clear_translation_cache(
            chapter_path=chapter_path,
            target_language=target_language
        )
        
        if success:
            return {
                "message": f"Translation cache cleared for {chapter_path}",
                "chapter_path": chapter_path,
                "target_language": target_language
            }
        else:
            raise HTTPException(
                status_code=500,
                detail="Failed to clear translation cache"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error clearing translation cache: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to clear cache: {str(e)}"
        )


@router.get("/cache/stats", response_model=CacheStatsResponse)
async def get_cache_statistics(db: AsyncSession = Depends(get_db)):
    """
    Get translation cache statistics.
    
    Returns information about cache usage, popular chapters,
    and performance metrics for monitoring purposes.
    """
    try:
        from app.services.translation_cache import TranslationCacheService
        
        cache_service = TranslationCacheService(db)
        stats = await cache_service.get_cache_stats()
        
        return CacheStatsResponse(**stats)
        
    except Exception as e:
        logger.error(f"Error getting cache stats: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get cache statistics: {str(e)}"
        )


@router.post("/cache/cleanup")
async def cleanup_expired_cache(db: AsyncSession = Depends(get_db)):
    """
    Clean up expired cache entries.
    
    This endpoint removes expired translations from the cache
    to free up storage space and maintain performance.
    """
    try:
        from app.services.translation_cache import TranslationCacheService
        
        cache_service = TranslationCacheService(db)
        cleared_count = await cache_service.clear_expired_cache()
        
        return {
            "message": f"Cleaned up {cleared_count} expired cache entries",
            "cleared_count": cleared_count
        }
        
    except Exception as e:
        logger.error(f"Error cleaning up cache: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to cleanup cache: {str(e)}"
        )


@router.get("/health")
async def translation_health_check():
    """Health check for translation service."""
    return {
        "status": "ok",
        "service": "translation",
        "supported_languages": ["ur", "en"],
        "features": [
            "chapter_translation",
            "caching",
            "markdown_preservation",
            "technical_terminology"
        ]
    }
