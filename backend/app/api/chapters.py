"""
FastAPI router for chapter metadata endpoints.

This module provides REST API endpoints for retrieving chapter information,
including metadata, content summaries, and section lists.
"""

from fastapi import APIRouter, HTTPException, status
from app.models.chapter import ChapterMetadata
from app.services.chapter_service import ChapterService

router = APIRouter(
    prefix="/chapters",
    tags=["chapters"],
    responses={
        404: {"description": "Chapter not found"},
        500: {"description": "Internal server error"},
    },
)

# Initialize service
chapter_service = ChapterService()


@router.get(
    "/{chapter_id}",
    response_model=ChapterMetadata,
    summary="Get chapter metadata",
    description="Retrieve metadata for a specific chapter including title, summary, and sections",
    responses={
        200: {
            "description": "Chapter metadata retrieved successfully",
            "content": {
                "application/json": {
                    "example": {
                        "chapter": 1,
                        "title": "Introduction to Physical AI & Robotics",
                        "summary": "Placeholder summary for Chapter 1 introduction",
                        "sections": []
                    }
                }
            }
        },
        404: {
            "description": "Chapter not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Chapter not found"}
                }
            }
        }
    }
)
async def get_chapter(chapter_id: int):
    """
    Get metadata for a specific chapter.
    
    Args:
        chapter_id: The chapter number (e.g., 1, 2, 3)
        
    Returns:
        ChapterMetadata: Chapter metadata including title, summary, and sections
        
    Raises:
        HTTPException: 404 if chapter does not exist
        
    Example:
        GET /chapters/1
        
        Response:
        {
            "chapter": 1,
            "title": "Introduction to Physical AI & Robotics",
            "summary": "Placeholder summary for Chapter 1 introduction",
            "sections": []
        }
    """
    chapter = chapter_service.get_chapter(chapter_id)
    
    if chapter is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Chapter not found"
        )
    
    return chapter


@router.get(
    "/",
    response_model=list[ChapterMetadata],
    summary="List all chapters",
    description="Retrieve a list of all available chapters"
)
async def list_chapters():
    """
    Get a list of all available chapters.
    
    Returns:
        List[ChapterMetadata]: List of all chapter metadata
        
    Example:
        GET /chapters/
        
        Response:
        [
            {
                "chapter": 1,
                "title": "Introduction to Physical AI & Robotics",
                "summary": "Placeholder summary for Chapter 1 introduction",
                "sections": []
            }
        ]
    """
    return chapter_service.list_chapters()
