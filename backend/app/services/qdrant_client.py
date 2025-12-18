from typing import Iterable, Optional, Sequence, Tuple

from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels

from backend.app.core.config import get_settings
from backend.app.models.schemas.chunk import DocumentChunk


settings = get_settings()


def get_qdrant_client() -> QdrantClient:
    if not settings.qdrant_url:
        raise RuntimeError("QDRANT_URL is not set")
    # Ensure we pass a plain string URL to QdrantClient
    return QdrantClient(url=str(settings.qdrant_url), api_key=settings.qdrant_api_key)


def ensure_collection(client: QdrantClient, name: str, vector_size: int) -> None:
    collections = client.get_collections().collections
    if any(c.name == name for c in collections):
        return
    client.create_collection(
        collection_name=name,
        vectors_config=qmodels.VectorParams(size=vector_size, distance=qmodels.Distance.COSINE),
    )


def upsert_chunks(
    client: QdrantClient,
    collection: str,
    vectors_payloads: Sequence[Tuple[str, Sequence[float], dict]],
    vector_size: int,
) -> int:
    ensure_collection(client, collection, vector_size)
    points = [
        qmodels.PointStruct(id=pid, vector=vector, payload=payload)
        for pid, vector, payload in vectors_payloads
    ]
    result = client.upsert(collection_name=collection, points=points)
    return len(points)


def search_chunks(
    client: QdrantClient,
    collection: str,
    query_vector: Sequence[float],
    top_k: int,
    filters: Optional[dict] = None,
) -> list[qmodels.ScoredPoint]:
    if filters:
        must = []
        for key, value in filters.items():
            if value:
                must.append(qmodels.FieldCondition(key=key, match=qmodels.MatchValue(value=value)))
        qfilter = qmodels.Filter(must=must) if must else None
    else:
        qfilter = None

    return client.search(
        collection_name=collection,
        query_vector=query_vector,
        limit=top_k,
        query_filter=qfilter,
        with_payload=True,
        with_vectors=False,
    )


