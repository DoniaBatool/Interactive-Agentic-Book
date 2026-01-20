from typing import Iterable, Optional, Sequence, Tuple
from urllib.parse import urlsplit, urlunsplit

from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels

from app.core.config import get_settings
from app.models.schemas.chunk import DocumentChunk


settings = get_settings()


def get_effective_qdrant_url() -> Optional[str]:
    """
    Return the URL we should actually use for Qdrant.

    Common production footgun: Qdrant Cloud REST endpoint requires port 6333.
    If someone configures `https://<cluster>.cloud.qdrant.io` (no port), many setups
    respond with a plain-text 404 ("404 page not found").
    """
    if not settings.qdrant_url:
        return None

    raw = str(settings.qdrant_url)
    parts = urlsplit(raw)
    host = parts.hostname
    if not host:
        return raw

    # If a path is configured, don't try to "fix" it automatically.
    # QdrantClient expects the base URL, and an unexpected path can break requests.
    if parts.path not in ("", "/"):
        return raw

    # Heuristic: Qdrant Cloud uses port 6333 for REST.
    if parts.port is None and host.endswith("cloud.qdrant.io"):
        netloc = f"{host}:6333"
        return urlunsplit((parts.scheme, netloc, "", "", ""))

    return raw


def get_qdrant_client() -> QdrantClient:
    effective_url = get_effective_qdrant_url()
    if not effective_url:
        raise RuntimeError("QDRANT_URL is not set")
    # Ensure we pass a plain string URL to QdrantClient
    return QdrantClient(url=effective_url, api_key=settings.qdrant_api_key)


def ensure_collection(client: QdrantClient, name: str, vector_size: int) -> None:
    """Ensure the collection exists (vector size + distance)."""
    collections = client.get_collections().collections
    if any(c.name == name for c in collections):
        return
    client.create_collection(
        collection_name=name,
        vectors_config=qmodels.VectorParams(size=vector_size, distance=qmodels.Distance.COSINE),
    )


def ensure_payload_indexes(client: QdrantClient, name: str) -> None:
    """
    Ensure payload indexes exist for fields we filter on.

    Qdrant Cloud requires an index for string filter fields like `chapter` and `section`
    (of type KEYWORD). Without this, filtered searches return 400 Bad Request.
    """
    # We call create_payload_index unconditionally and ignore "already exists" errors.
    # This keeps the logic simple and idempotent.
    try:
        client.create_payload_index(
            collection_name=name,
            field_name="chapter",
            field_schema=qmodels.PayloadSchemaType.KEYWORD,
        )
    except Exception:
        # Index may already exist or collection may be read-only; ignore.
        pass

    try:
        client.create_payload_index(
            collection_name=name,
            field_name="section",
            field_schema=qmodels.PayloadSchemaType.KEYWORD,
        )
    except Exception:
        pass


def upsert_chunks(
    client: QdrantClient,
    collection: str,
    vectors_payloads: Sequence[Tuple[str, Sequence[float], dict]],
    vector_size: int,
) -> int:
    ensure_collection(client, collection, vector_size)
    # Ensure payload indexes are present before we start using filters.
    ensure_payload_indexes(client, collection)
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
    # Make sure payload indexes exist before we run filtered searches.
    # This is safe to call repeatedly.
    ensure_payload_indexes(client, collection)

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


