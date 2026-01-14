from typing import List, Optional, Tuple

from openai import OpenAI

from app.core.config import get_settings
from app.models.schemas.chat import ChatFilters
from app.models.schemas.chunk import DocumentChunk
from app.services.qdrant_client import get_qdrant_client, search_chunks


settings = get_settings()


def _normalize_chapter_filter(chapter: str) -> str:
    """
    Normalize frontend "display" chapter names to match the chapter names stored in Qdrant.

    Today our ingestion stores `metadata.chapter` as `Path(stem).title()`.
    Example: `docs/modules/vla-capstone.md` -> "Vla Capstone"

    The frontend, however, uses human-friendly titles (e.g. "Vision-Language-Action Capstone").
    This normalizer keeps filtering working without requiring a full re-ingest.
    """
    raw = (chapter or "").strip()
    if not raw:
        return raw

    aliases = {
        # Frontend display names -> ingestion-derived names
        "introduction to physical ai": "Intro",
        "ros 2 nervous system": "Ros2",
        "gazebo & unity digital twin": "Gazebo Unity",
        "nvidia isaac ai brain": "Nvidia Isaac",
        "vision-language-action capstone": "Vla Capstone",
        # Common variants / abbreviations
        "vla capstone": "Vla Capstone",
        "vla": "Vla Capstone",
        "course overview": "Course Overview",
    }

    lowered = raw.lower()
    if lowered in aliases:
        return aliases[lowered]

    # If the user passes the ingestion-style title already, keep it.
    return raw


def embed_question(client: OpenAI, question: str) -> List[float]:
    emb = client.embeddings.create(model=settings.embedding_model, input=question)
    return emb.data[0].embedding


def retrieve_chunks(question: str, filters: Optional[ChatFilters], top_k: int) -> List[Tuple[str, str, Optional[str], str, float]]:
    if not settings.qdrant_url:
        raise RuntimeError("QDRANT_URL is not set")

    client = get_qdrant_client()
    openai_client = OpenAI(api_key=settings.openai_api_key)

    query_vector = embed_question(openai_client, question)

    filter_dict = {}
    if filters:
        if filters.chapter:
            filter_dict["chapter"] = _normalize_chapter_filter(filters.chapter)
        if filters.section:
            filter_dict["section"] = filters.section

    results = search_chunks(
        client=client,
        collection=settings.qdrant_collection,
        query_vector=query_vector,
        top_k=top_k,
        filters=filter_dict if filter_dict else None,
    )

    extracted: List[Tuple[str, str, Optional[str], str, float]] = []
    for r in results:
        payload = r.payload or {}
        text = payload.get("text", "")
        path = payload.get("path", "")
        chapter = payload.get("chapter", "")
        section = payload.get("section")
        extracted.append((text, path, chapter, section, r.score or 0.0))

    return extracted

