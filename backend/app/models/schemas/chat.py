from typing import List, Optional

from pydantic import BaseModel

from backend.app.models.schemas.chunk import DocumentChunk


class ChatFilters(BaseModel):
    chapter: Optional[str] = None
    section: Optional[str] = None


class ChatRequest(BaseModel):
    question: str
    filters: Optional[ChatFilters] = None
    stream: Optional[bool] = None


class Citation(BaseModel):
    path: str
    chapter: str
    section: Optional[str] = None
    score: Optional[float] = None


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    stream: bool = False

