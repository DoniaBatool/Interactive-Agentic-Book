"""
Qdrant Vector Database Store

Provides functions for Qdrant vector database operations:
- Collection creation
- Vector upsert operations
- Similarity search
"""

from qdrant_client import QdrantClient, AsyncQdrantClient, models
from typing import List, Dict, Any, Optional
from app.config.settings import settings

# Initialize Qdrant client (async for consistency)
_qdrant_client = None

def _get_qdrant_client() -> AsyncQdrantClient:
    global _qdrant_client
    if _qdrant_client is None:
        if not settings.qdrant_url and not settings.qdrant_host:
            raise ValueError("QDRANT_URL or QDRANT_HOST must be set in environment variables.")
        
        if settings.qdrant_url:
            _qdrant_client = AsyncQdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
        elif settings.qdrant_host:
            # For local Qdrant, often just host is enough, or host:port
            _qdrant_client = AsyncQdrantClient(host=settings.qdrant_host, api_key=settings.qdrant_api_key)
        else:
            raise ValueError("Invalid Qdrant configuration. Provide QDRANT_URL or QDRANT_HOST.")
    return _qdrant_client

async def create_collection(collection_name: str, vector_size: int = 1536) -> bool:
    """
    Create Qdrant collection for chapter content.
    
    Args:
        collection_name: Name of collection to create (e.g., "chapter_1")
        vector_size: Size of embedding vectors (default: 1536 for text-embedding-3-small)
    
    Returns:
        True if successful, False otherwise
    """
    client = _get_qdrant_client()
    try:
        if await client.collection_exists(collection_name=collection_name):
            print(f"Collection '{collection_name}' already exists.")  # TODO: Add structured logging
            return True
        
        await client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
            # Optional HNSW config for performance
            hnsw_config=models.HnswConfigDiff(m=16, ef_construct=100)
        )
        print(f"Collection '{collection_name}' created successfully.")  # TODO: Add structured logging
        return True
    except Exception as e:
        print(f"Error creating Qdrant collection '{collection_name}': {e}")  # TODO: Add structured logging
        return False

async def upsert_vectors(
    collection_name: str,
    vectors: List[Dict[str, Any]]
) -> bool:
    """
    Insert or update vectors in Qdrant collection.
    
    Args:
        collection_name: Name of collection
        vectors: List of vector documents with structure:
            {
                "id": str,                    # Unique document ID
                "vector": List[float],        # Embedding vector
                "payload": Dict[str, Any]     # Metadata (text, chapter_id, section_id, etc.)
            }
    
    Returns:
        True if successful, False otherwise
    """
    client = _get_qdrant_client()
    try:
        points = []
        for vec_data in vectors:
            points.append(
                models.PointStruct(
                    id=vec_data["id"],
                    vector=vec_data["vector"],
                    payload=vec_data["payload"]
                )
            )
        
        # Qdrant client can handle batching internally, but for very large lists,
        # manual chunking might be considered. For now, send all at once.
        operation_info = await client.upsert(
            collection_name=collection_name,
            points=points,
            wait=True  # Wait for the operation to be applied
        )
        print(f"Upsert operation for '{collection_name}' status: {operation_info.status}")  # TODO: Add structured logging
        return operation_info.status == models.UpdateStatus.COMPLETED
    except Exception as e:
        print(f"Error upserting vectors to Qdrant collection '{collection_name}': {e}")  # TODO: Add structured logging
        return False

async def similarity_search(
    collection_name: str,
    query_embedding: List[float],
    top_k: int = 5,
    chapter_id: Optional[int] = None,
    section_id: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Perform similarity search in Qdrant collection.
    
    Args:
        collection_name: Name of collection to search
        query_embedding: Query embedding vector (not text - must be pre-embedded)
        top_k: Number of results to return (default: 5)
        chapter_id: Optional chapter ID to filter results
        section_id: Optional section ID to filter results
    
    Returns:
        List of similar documents sorted by similarity score (highest first):
        [
            {
                "id": str,                # Document ID
                "score": float,           # Similarity score (0.0-1.0)
                "text": str,              # Chunk text from payload
                "chapter_id": int,        # Chapter ID from payload
                "section_id": str,        # Section ID from payload
                "position": int,          # Position from payload
                "metadata": Dict[str, Any]  # Full payload as metadata
            },
            ...
        ]
    """
    client = _get_qdrant_client()
    try:
        # Build query filters if section_id or chapter_id are provided
        query_filter = None
        if chapter_id is not None or section_id is not None:
            must_conditions = []
            if chapter_id is not None:
                must_conditions.append(models.FieldCondition(
                    key="chapter_id",
                    range=models.Range(gte=chapter_id, lte=chapter_id)
                ))
            if section_id is not None:
                must_conditions.append(models.FieldCondition(
                    key="section_id",
                    match=models.MatchValue(value=section_id)
                ))
            if must_conditions:
                query_filter = models.Filter(must=must_conditions)

        search_result = await client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            query_filter=query_filter,  # Apply filter
            limit=top_k,
            with_payload=True  # Ensure payload (metadata) is returned
        )
        
        results = []
        for hit in search_result:
            results.append({
                "id": hit.id,
                "score": hit.score,
                "text": hit.payload.get("text"),
                "chapter_id": hit.payload.get("chapter_id"),
                "section_id": hit.payload.get("section_id"),
                "position": hit.payload.get("position"),
                "metadata": hit.payload  # Full payload as metadata
            })
        return results
    except Exception as e:
        print(f"Error performing Qdrant similarity search in '{collection_name}': {e}")  # TODO: Add structured logging
        return []
