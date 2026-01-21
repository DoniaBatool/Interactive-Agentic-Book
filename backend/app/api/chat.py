from typing import Optional
from fastapi import APIRouter, HTTPException, Header, Depends, Request
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from app.core.config import get_settings
from app.core.database import get_db, is_db_available
from app.models.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import generate_answer, stream_answer
from app.services.agents import generate_agent_answer, stream_agent_answer
from app.services import history as history_service
from app.services import user as user_service

router = APIRouter()
settings = get_settings()
logger = logging.getLogger(__name__)


async def get_optional_db() -> Optional[AsyncSession]:
    """Get database session if available, otherwise return None."""
    if not is_db_available():
        return None
    
    try:
        async for session in get_db():
            return session
    except Exception:
        return None
    
    return None


async def get_user_from_session(request: Request, db: Optional[AsyncSession]) -> Optional[dict]:
    """Extract user profile from BetterAuth session cookie."""
    if not db:
        return None
    
    try:
        # Get session cookie from BetterAuth (better-auth.session_token)
        session_token = request.cookies.get("better-auth.session_token")
        if not session_token:
            return None
        
        # For now, we'll implement a simple lookup by session token
        # In production, you'd verify the JWT token from BetterAuth
        # This is a simplified implementation for the integration
        
        # TODO: Implement proper BetterAuth session verification
        # For now, return None (no user context)
        return None
        
    except Exception as e:
        logger.debug(f"Error extracting user from session: {e}")
        return None


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    """Basic RAG chat endpoint (existing implementation)."""
    try:
        logger.info(f"Received chat request: question={payload.question[:50]}..., stream={payload.stream}")
        stream = payload.stream if payload.stream is not None else settings.default_stream
        if stream:
            return StreamingResponse(stream_answer(payload), media_type="text/event-stream")
        return await generate_answer(payload)
    except RuntimeError as e:
        logger.error(f"RuntimeError in chat endpoint: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Exception in chat endpoint: {e}")
        msg = str(e)
        if (
            "insufficient_quota" in msg
            or "You exceeded your current quota" in msg
            or "Error code: 429" in msg
            or ("429" in msg and "quota" in msg.lower())
        ):
            raise HTTPException(
                status_code=429,
                detail="AI chat is temporarily unavailable (OpenAI quota exceeded). Please update billing / API key and try again.",
            )
        raise HTTPException(status_code=500, detail="Chat service error")


@router.post("/chat/agent", response_model=ChatResponse)
async def agent_chat_endpoint(
    payload: ChatRequest,
    request: Request,
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
):
    """Agents/ChatKit endpoint using OpenAI function calling."""
    try:
        logger.info(f"Received agent chat request: question={payload.question[:50]}..., stream={payload.stream}")
        
        # Get optional database session
        db = await get_optional_db()
        
        # Get user profile for personalized responses
        user_profile = await get_user_from_session(request, db)
        if user_profile:
            logger.info(f"Chat request from user with profile: {user_profile.get('software_level', 'unknown')}")
        
        # Add user context to payload for personalized responses
        if user_profile:
            from app.models.schemas.chat import UserContext
            payload.user_context = UserContext(
                software_level=user_profile.get('software_level'),
                hardware_level=user_profile.get('hardware_level'),
                technologies=user_profile.get('technologies', {}),
                learning_goals=user_profile.get('learning_goals')
            )
        
        # Save user message if database is available
        if db and x_session_id:
            chapter = payload.filters.chapter if payload.filters else None
            await history_service.save_message(
                db=db,
                session_id=x_session_id,
                role="user",
                content=payload.question,
                chapter=chapter
            )
        
        stream = payload.stream if payload.stream is not None else settings.default_stream
        if stream:
            return StreamingResponse(stream_agent_answer(payload), media_type="text/event-stream")
        
        # Generate response
        response = await generate_agent_answer(payload)
        
        # Save assistant message if database is available
        if db and x_session_id:
            chapter = payload.filters.chapter if payload.filters else None
            citations_data = [c.model_dump() for c in response.citations] if response.citations else None
            await history_service.save_message(
                db=db,
                session_id=x_session_id,
                role="assistant",
                content=response.answer,
                chapter=chapter,
                citations=citations_data
            )
        
        return response
        
    except RuntimeError as e:
        logger.error(f"RuntimeError in agent chat endpoint: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Exception in agent chat endpoint: {e}")
        msg = str(e)
        if (
            "insufficient_quota" in msg
            or "You exceeded your current quota" in msg
            or "Error code: 429" in msg
            or ("429" in msg and "quota" in msg.lower())
        ):
            raise HTTPException(
                status_code=429,
                detail="AI agent chat is temporarily unavailable (OpenAI quota exceeded). Please update billing / API key and try again.",
            )
        raise HTTPException(status_code=500, detail="Agent chat service error")

