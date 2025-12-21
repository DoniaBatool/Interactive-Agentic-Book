from typing import List, Optional, Dict, Any

from pydantic import BaseModel

from backend.app.models.schemas.chunk import DocumentChunk


class ChatFilters(BaseModel):
    chapter: Optional[str] = None
    section: Optional[str] = None


class UserContext(BaseModel):
    """User profile context for personalized responses."""
    software_level: Optional[str] = None  # beginner, intermediate, advanced
    hardware_level: Optional[str] = None  # none, some, extensive
    technologies: Optional[Dict[str, Any]] = None  # Known technologies
    learning_goals: Optional[str] = None


class ChatRequest(BaseModel):
    question: str
    filters: Optional[ChatFilters] = None
    stream: Optional[bool] = None
    user_context: Optional[UserContext] = None  # For personalized responses


class Citation(BaseModel):
    path: str
    chapter: str
    section: Optional[str] = None
    score: Optional[float] = None


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    stream: bool = False

