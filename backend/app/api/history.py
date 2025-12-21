"""
History API endpoints for chat message persistence.
Feature 012: Postgres Persistence
"""

import logging
from typing import Optional, List
from datetime import datetime

from fastapi import APIRouter, Query, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db, is_db_available
from app.services import history as history_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["history"])


# Response models
class CitationResponse(BaseModel):
    path: str
    chapter: str
    section: Optional[str] = None
    score: Optional[float] = None


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str
    citations: Optional[List[dict]] = None
    created_at: datetime

    class Config:
        from_attributes = True


class HistoryResponse(BaseModel):
    session_id: str
    chapter: Optional[str] = None
    messages: List[MessageResponse]
    total: int


class ClearResponse(BaseModel):
    deleted: int
    message: str


class HistoryStatusResponse(BaseModel):
    available: bool
    message: str


@router.get("/history/status", response_model=HistoryStatusResponse)
async def get_history_status():
    """
    Check if chat history persistence is available.
    """
    available = is_db_available()
    return HistoryStatusResponse(
        available=available,
        message="Chat history is available" if available else "Chat history is not configured"
    )


@router.get("/history", response_model=HistoryResponse)
async def get_chat_history(
    session_id: str = Query(..., description="Session ID (UUID)"),
    chapter: Optional[str] = Query(None, description="Filter by chapter"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum messages to return"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve chat history for a session.
    
    - **session_id**: UUID session identifier (required)
    - **chapter**: Optional chapter filter
    - **limit**: Maximum messages to return (default: 100, max: 1000)
    - **offset**: Pagination offset (default: 0)
    """
    if not is_db_available():
        raise HTTPException(
            status_code=503,
            detail="Chat history is not available"
        )
    
    # Get messages
    messages = await history_service.get_history(
        db=db,
        session_id=session_id,
        chapter=chapter,
        limit=limit,
        offset=offset
    )
    
    # Get total count
    total = await history_service.get_history_count(
        db=db,
        session_id=session_id,
        chapter=chapter
    )
    
    # Convert to response
    message_responses = [
        MessageResponse(
            id=msg.id,
            role=msg.role,
            content=msg.content,
            citations=msg.citations,
            created_at=msg.created_at
        )
        for msg in messages
    ]
    
    return HistoryResponse(
        session_id=session_id,
        chapter=chapter,
        messages=message_responses,
        total=total
    )


@router.delete("/history", response_model=ClearResponse)
async def clear_chat_history(
    session_id: str = Query(..., description="Session ID (UUID)"),
    chapter: Optional[str] = Query(None, description="Only clear specific chapter"),
    db: AsyncSession = Depends(get_db)
):
    """
    Clear chat history for a session.
    
    - **session_id**: UUID session identifier (required)
    - **chapter**: Optional - only clear messages from this chapter
    """
    if not is_db_available():
        raise HTTPException(
            status_code=503,
            detail="Chat history is not available"
        )
    
    deleted = await history_service.clear_history(
        db=db,
        session_id=session_id,
        chapter=chapter
    )
    
    return ClearResponse(
        deleted=deleted,
        message=f"Deleted {deleted} messages" + (f" from {chapter}" if chapter else "")
    )

