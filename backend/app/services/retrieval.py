from typing import List, Optional, Tuple

from openai import OpenAI

from backend.app.core.config import get_settings
from backend.app.models.schemas.chat import ChatFilters
from backend.app.models.schemas.chunk import DocumentChunk
from backend.app.services.qdrant_client import get_qdrant_client, search_chunks


settings = get_settings()


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
            filter_dict["chapter"] = filters.chapter
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

