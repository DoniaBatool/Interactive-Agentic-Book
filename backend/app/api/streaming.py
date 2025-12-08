"""
Streaming API Endpoints

API endpoints for real-time AI block streaming.
"""

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from typing import Dict, Any, Optional
from app.ai.streaming.stream_manager import StreamManager
import json

router = APIRouter(prefix="/api/stream", tags=["streaming"])


@router.get("/ai-block/{block_type}")
async def stream_ai_block(
    block_type: str,
    chapter_id: int = Query(..., description="Chapter ID"),
    question: Optional[str] = Query(None, description="Question (for ask-question)"),
    concept: Optional[str] = Query(None, description="Concept (for explain-like-el10)"),
    num_questions: Optional[int] = Query(None, description="Number of questions (for quiz)"),
    diagram_type: Optional[str] = Query(None, description="Diagram type (for diagram-generator)")
) -> StreamingResponse:
    """
    Stream AI block response in real-time.
    
    Args:
        block_type: Type of AI block ("ask-question", "explain-like-el10", "interactive-quiz", "diagram-generator")
        chapter_id: Chapter ID
        question: Question text (for ask-question)
        concept: Concept text (for explain-like-el10)
        num_questions: Number of questions (for quiz)
        diagram_type: Diagram type (for diagram-generator)
    
    Returns:
        StreamingResponse with text/event-stream content type
    
    TODO: Implement real streaming from LLM providers
    TODO: Connect to runtime engine
    TODO: Stream tokens as they're generated
    TODO: Handle different block types
    """
    # Build user_input from query parameters
    user_input: Dict[str, Any] = {"chapterId": chapter_id}
    if question:
        user_input["question"] = question
    if concept:
        user_input["concept"] = concept
    if num_questions:
        user_input["numQuestions"] = num_questions
    if diagram_type:
        user_input["diagramType"] = diagram_type
    
    # Create stream manager
    stream_manager = StreamManager()
    
    async def generate_stream():
        """Generate SSE stream."""
        async for chunk in stream_manager.stream_ai_response(block_type, chapter_id, user_input):
            # Format as SSE
            sse_chunk = stream_manager.format_sse_chunk(chunk)
            yield sse_chunk
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable buffering in nginx
        }
    )

