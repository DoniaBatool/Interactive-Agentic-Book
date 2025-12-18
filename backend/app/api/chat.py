from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from backend.app.core.config import get_settings
from backend.app.models.schemas.chat import ChatRequest, ChatResponse
from backend.app.services.chat import generate_answer, stream_answer

router = APIRouter()
settings = get_settings()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    try:
        stream = payload.stream if payload.stream is not None else settings.default_stream
        if stream:
            return StreamingResponse(stream_answer(payload), media_type="text/event-stream")
        return await generate_answer(payload)
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Chat service error")

