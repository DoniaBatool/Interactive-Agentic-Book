"""
Translation API Endpoints

API endpoints for translation services.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from app.translation.pipeline import translate_chapter, translate_snippet, get_translation_provider

router = APIRouter(prefix="/api/translation", tags=["translation"])


class TranslateSnippetRequest(BaseModel):
    """Request model for snippet translation."""
    text: str
    target_language: str
    source_language: Optional[str] = "en"


class TranslateChapterRequest(BaseModel):
    """Request model for chapter translation."""
    target_language: str
    source_language: Optional[str] = "en"
    include_glossary: Optional[bool] = True


@router.post("/snippet")
async def translate_snippet_endpoint(request: TranslateSnippetRequest) -> Dict[str, Any]:
    """
    Translate a text snippet.
    
    Args:
        request: TranslateSnippetRequest with text and target_language
    
    Returns:
        Translation result with structure:
        {
            "source": str,
            "translated": str,
            "language": str,
            "source_language": str
        }
    
    TODO: Implement real translation logic
    TODO: Validate language codes
    TODO: Call translate_snippet() from pipeline
    TODO: Return structured result
    """
    # Placeholder: Return mock translation for now
    # TODO: Implement real translation
    result = await translate_snippet(
        text=request.text,
        target_language=request.target_language,
        source_language=request.source_language
    )
    return result


@router.post("/chapter/{chapter_id}")
async def translate_chapter_endpoint(
    chapter_id: int,
    request: TranslateChapterRequest
) -> Dict[str, Any]:
    """
    Translate entire chapter content.
    
    Args:
        chapter_id: Chapter ID (1, 2, 3, ...)
        request: TranslateChapterRequest with target_language
    
    Returns:
        Translated chapter content
    
    TODO: Implement real chapter translation
    TODO: Validate chapter_id exists
    TODO: Validate language codes
    TODO: Call translate_chapter() from pipeline
    TODO: Return structured result
    """
    # Placeholder: Return mock translation for now
    # TODO: Implement real translation
    result = await translate_chapter(
        chapter_id=chapter_id,
        target_language=request.target_language
    )
    return result


@router.get("/languages")
async def get_supported_languages() -> Dict[str, List[str]]:
    """
    Get list of supported language codes.
    
    Returns:
        Dictionary with languages list:
        {
            "languages": ["en", "ur", "ru", "ar"]
        }
    """
    # Get languages from any provider (they all support the same languages)
    provider = get_translation_provider()
    languages = provider.supported_languages()
    return {"languages": languages}

