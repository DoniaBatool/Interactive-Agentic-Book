import json
import logging
import time
from typing import AsyncIterable, List, Tuple

from fastapi import HTTPException
from openai import OpenAI

from app.core.config import get_settings
from app.models.schemas.chat import ChatRequest, ChatResponse, Citation
from app.services.retrieval import retrieve_chunks


logger = logging.getLogger(__name__)
settings = get_settings()


def _log_event(event: str, **fields) -> None:
    """Structured JSON logging for chat telemetry."""
    payload = {"event": event, **fields}
    logger.info(json.dumps(payload))


def _prepare_context(payload: ChatRequest) -> Tuple[List[str], List[Citation], List[Tuple[str, str, str, str, float]]]:
    top_k = settings.retrieval_top_k
    retrieved = retrieve_chunks(payload.question, payload.filters, top_k)

    context_blocks = []
    citations: List[Citation] = []
    for text, path, chapter, section, score in retrieved:
        context_blocks.append(f"[{chapter}] {text}")
        citations.append(Citation(path=path, chapter=chapter, section=section, score=score))

    return context_blocks, citations, retrieved


def _format_sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


def _log_start(payload: ChatRequest, stream: bool) -> None:
    filters = payload.filters.model_dump(exclude_none=True) if payload.filters else None
    _log_event(
        "chat.start",
        stream=stream,
        filters=filters,
        question_length=len(payload.question),
    )


def _log_done(stream: bool, duration_ms: int, retrieved_count: int) -> None:
    _log_event(
        "chat.done",
        stream=stream,
        duration_ms=duration_ms,
        retrieved=retrieved_count,
    )


async def generate_answer(payload: ChatRequest) -> ChatResponse:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    stream = payload.stream if payload.stream is not None else settings.default_stream
    _log_start(payload, stream)

    start = time.time()
    context_blocks, citations, retrieved = _prepare_context(payload)

    prompt = (
        "You are a textbook assistant. Answer using the provided context; cite sources.\n\n"
        f"Context:\n{'\n'.join(context_blocks)}\n\nQuestion: {payload.question}\nAnswer:"
    )

    client = OpenAI(api_key=settings.openai_api_key)

    response = client.chat.completions.create(
        model=settings.chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that cites sources."},
            {"role": "user", "content": prompt},
        ],
        stream=False,
    )

    if isinstance(response, dict) or getattr(response, "choices", None) is None:
        raise HTTPException(status_code=500, detail="OpenAI chat response error")

    answer = response.choices[0].message.content if getattr(response, "choices", None) else ""

    duration_ms = int((time.time() - start) * 1000)
    _log_done(False, duration_ms, len(retrieved))
    return ChatResponse(answer=answer, citations=citations, stream=False)


async def stream_answer(payload: ChatRequest) -> AsyncIterable[str]:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    _log_start(payload, True)
    start = time.time()

    context_blocks, citations, retrieved = _prepare_context(payload)

    prompt = (
        "You are a textbook assistant. Answer using the provided context; cite sources.\n\n"
        f"Context:\n{'\n'.join(context_blocks)}\n\nQuestion: {payload.question}\nAnswer:"
    )

    client = OpenAI(api_key=settings.openai_api_key)

    try:
        stream = client.chat.completions.create(
            model=settings.chat_model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that cites sources."},
                {"role": "user", "content": prompt},
            ],
            stream=True,
        )

        yield _format_sse(
            "metadata",
            {"citations": [c.model_dump() for c in citations], "stream": True},
        )

        for chunk in stream:
            if not chunk or not getattr(chunk, "choices", None):
                continue
            delta = chunk.choices[0].delta.content
            if delta:
                yield _format_sse("token", {"text": delta})

        duration_ms = int((time.time() - start) * 1000)
        _log_done(True, duration_ms, len(retrieved))
        yield _format_sse("done", {"duration_ms": duration_ms})
    except Exception as exc:
        logger.exception("chat.stream.error")
        _log_event("chat.error", stream=True, error=str(exc))
        yield _format_sse("error", {"message": "Chat stream failed"})

