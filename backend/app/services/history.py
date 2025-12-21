"""
History service for managing chat message persistence.
Feature 012: Postgres Persistence
"""

import logging
from typing import List, Optional, Dict, Any

from sqlalchemy import select, delete, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.session import Session
from app.models.message import Message
from app.core.database import is_db_available

logger = logging.getLogger(__name__)


async def get_or_create_session(
    db: AsyncSession,
    session_id: str
) -> Optional[Session]:
    """
    Get existing session or create a new one.
    
    Args:
        db: Database session
        session_id: UUID session identifier
        
    Returns:
        Session object or None if database unavailable
    """
    if not is_db_available():
        logger.debug("Database not available, skipping session creation")
        return None
    
    try:
        # Try to find existing session
        result = await db.execute(
            select(Session).where(Session.session_id == session_id)
        )
        session = result.scalar_one_or_none()
        
        if session:
            return session
        
        # Create new session
        session = Session(session_id=session_id)
        db.add(session)
        await db.commit()
        await db.refresh(session)
        
        logger.info(f"Created new session: {session_id}")
        return session
        
    except Exception as e:
        logger.error(f"Error in get_or_create_session: {e}")
        await db.rollback()
        return None


async def save_message(
    db: AsyncSession,
    session_id: str,
    role: str,
    content: str,
    chapter: Optional[str] = None,
    citations: Optional[List[Dict[str, Any]]] = None
) -> Optional[Message]:
    """
    Save a chat message to the database.
    
    Args:
        db: Database session
        session_id: UUID session identifier
        role: 'user' or 'assistant'
        content: Message content
        chapter: Optional chapter context
        citations: Optional list of citations (for assistant messages)
        
    Returns:
        Message object or None if save failed
    """
    if not is_db_available():
        logger.debug("Database not available, skipping message save")
        return None
    
    try:
        # Ensure session exists
        session = await get_or_create_session(db, session_id)
        if not session:
            return None
        
        # Create message
        message = Message(
            session_id=session_id,
            role=role,
            content=content,
            chapter=chapter,
            citations=citations
        )
        db.add(message)
        await db.commit()
        await db.refresh(message)
        
        logger.debug(f"Saved {role} message for session {session_id}")
        return message
        
    except Exception as e:
        logger.error(f"Error saving message: {e}")
        await db.rollback()
        return None


async def get_history(
    db: AsyncSession,
    session_id: str,
    chapter: Optional[str] = None,
    limit: int = 100,
    offset: int = 0
) -> List[Message]:
    """
    Retrieve chat history for a session.
    
    Args:
        db: Database session
        session_id: UUID session identifier
        chapter: Optional chapter filter
        limit: Maximum messages to return
        offset: Pagination offset
        
    Returns:
        List of Message objects
    """
    if not is_db_available():
        logger.debug("Database not available, returning empty history")
        return []
    
    try:
        # Build query
        conditions = [Message.session_id == session_id]
        if chapter:
            conditions.append(Message.chapter == chapter)
        
        query = (
            select(Message)
            .where(and_(*conditions))
            .order_by(Message.created_at.asc())
            .limit(limit)
            .offset(offset)
        )
        
        result = await db.execute(query)
        messages = result.scalars().all()
        
        logger.debug(f"Retrieved {len(messages)} messages for session {session_id}")
        return list(messages)
        
    except Exception as e:
        logger.error(f"Error getting history: {e}")
        return []


async def get_history_count(
    db: AsyncSession,
    session_id: str,
    chapter: Optional[str] = None
) -> int:
    """
    Get total message count for a session.
    
    Args:
        db: Database session
        session_id: UUID session identifier
        chapter: Optional chapter filter
        
    Returns:
        Total message count
    """
    if not is_db_available():
        return 0
    
    try:
        from sqlalchemy import func as sql_func
        
        conditions = [Message.session_id == session_id]
        if chapter:
            conditions.append(Message.chapter == chapter)
        
        query = select(sql_func.count(Message.id)).where(and_(*conditions))
        result = await db.execute(query)
        count = result.scalar() or 0
        
        return count
        
    except Exception as e:
        logger.error(f"Error counting messages: {e}")
        return 0


async def clear_history(
    db: AsyncSession,
    session_id: str,
    chapter: Optional[str] = None
) -> int:
    """
    Clear chat history for a session.
    
    Args:
        db: Database session
        session_id: UUID session identifier
        chapter: Optional - only clear specific chapter
        
    Returns:
        Number of messages deleted
    """
    if not is_db_available():
        logger.debug("Database not available, skipping history clear")
        return 0
    
    try:
        # Build delete query
        conditions = [Message.session_id == session_id]
        if chapter:
            conditions.append(Message.chapter == chapter)
        
        # Get count before delete
        count = await get_history_count(db, session_id, chapter)
        
        # Delete messages
        query = delete(Message).where(and_(*conditions))
        await db.execute(query)
        await db.commit()
        
        logger.info(f"Cleared {count} messages for session {session_id}")
        return count
        
    except Exception as e:
        logger.error(f"Error clearing history: {e}")
        await db.rollback()
        return 0


async def delete_session(
    db: AsyncSession,
    session_id: str
) -> bool:
    """
    Delete a session and all its messages.
    
    Args:
        db: Database session
        session_id: UUID session identifier
        
    Returns:
        True if deleted, False otherwise
    """
    if not is_db_available():
        return False
    
    try:
        # Delete session (messages will be cascade deleted)
        query = delete(Session).where(Session.session_id == session_id)
        result = await db.execute(query)
        await db.commit()
        
        deleted = result.rowcount > 0
        if deleted:
            logger.info(f"Deleted session: {session_id}")
        return deleted
        
    except Exception as e:
        logger.error(f"Error deleting session: {e}")
        await db.rollback()
        return False

