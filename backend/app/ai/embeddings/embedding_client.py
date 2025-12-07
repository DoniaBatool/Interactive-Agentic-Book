"""
Embedding Client

Provides functions for generating text embeddings for semantic search.
Embeddings are used in the RAG pipeline to find relevant chapter content.
"""

from app.config.settings import settings
from openai import AsyncOpenAI
from typing import List
import logging

# TODO: Add proper logging configuration
logger = logging.getLogger(__name__)

# Initialize OpenAI client for embeddings
_client: AsyncOpenAI = None


def _get_client() -> AsyncOpenAI:
    """Get or create OpenAI client instance for embeddings."""
    global _client
    if _client is None:
        if not settings.openai_api_key:
            raise ValueError("OpenAI API key not configured. Set OPENAI_API_KEY environment variable.")
        _client = AsyncOpenAI(api_key=settings.openai_api_key)
    return _client


def _get_embedding_model(chapter_id: int = 1) -> str:
    """Get embedding model for chapter."""
    if chapter_id == 2 and settings.ch2_embedding_model:
        return settings.ch2_embedding_model
    elif chapter_id == 3 and settings.ch3_embedding_model:
        return settings.ch3_embedding_model
    else:
        return settings.embedding_model or "text-embedding-3-small"


def _truncate_text(text: str, max_tokens: int = 8191) -> str:
    """
    Truncate text if it exceeds max tokens.
    
    Simple implementation: approximate token count (1 token ≈ 4 characters).
    """
    max_chars = max_tokens * 4
    if len(text) > max_chars:
        # TODO: Use proper tokenizer for accurate truncation
        return text[:max_chars]
    return text


async def generate_embedding(text: str, chapter_id: int = 1) -> List[float]:
    """
    Generate embedding vector for text.
    
    Args:
        text: Input text to embed (non-empty string)
        chapter_id: Chapter identifier (default: 1 for Chapter 1)
    
    Returns:
        List of float values representing embedding vector.
        Dimension depends on embedding model (e.g., 1536 for text-embedding-3-small).
        Example: [0.123, -0.456, 0.789, ...]
    """
    try:
        if not text:
            raise ValueError("Text cannot be empty")
        
        client = _get_client()
        model = _get_embedding_model(chapter_id)
        
        # Truncate text if exceeds max tokens
        truncated_text = _truncate_text(text)
        
        # Call OpenAI embeddings API
        response = await client.embeddings.create(
            model=model,
            input=truncated_text
        )
        
        # Extract embedding vector
        embedding = response.data[0].embedding
        
        return embedding
        
    except Exception as e:
        # TODO: Add proper error logging
        logger.error(f"Embedding generation error: {str(e)}")
        raise


async def batch_embed(chunks: List[str], chapter_id: int = 1) -> List[List[float]]:
    """
    Generate embeddings for multiple text chunks.
    
    Args:
        chunks: List of text strings to embed
        chapter_id: Chapter identifier (default: 1)
    
    Returns:
        List of embedding vectors (one per chunk).
        Example: [[0.123, ...], [0.456, ...], ...]
    """
    try:
        if not chunks:
            return []
        
        client = _get_client()
        model = _get_embedding_model(chapter_id)
        
        # Handle large batches (split if needed, e.g., 100 chunks per batch)
        batch_size = 100
        all_embeddings = []
        
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            
            # Truncate each chunk
            truncated_batch = [_truncate_text(chunk) for chunk in batch]
            
            # Call OpenAI embeddings API for batch
            response = await client.embeddings.create(
                model=model,
                input=truncated_batch
            )
            
            # Extract embeddings
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)
        
        return all_embeddings
        
    except Exception as e:
        # TODO: Add proper error logging
        logger.error(f"Batch embedding error: {str(e)}")
        raise


async def batch_embed_ch2(chunks: List[str]) -> List[List[float]]:
    """
    Generate batch embeddings for Chapter 2 chunks.
    
    Args:
        chunks: List of text chunks from Chapter 2
    
    Returns:
        List of embedding vectors (one per chunk).
        Example: [[0.123, ...], [0.456, ...], ...]
    """
    return await batch_embed(chunks, chapter_id=2)


async def batch_embed_ch3(chunks: List[str]) -> List[List[float]]:
    """
    Generate batch embeddings for Chapter 3 chunks.
    
    Args:
        chunks: List of text chunks from Chapter 3
    
    Returns:
        List of embedding vectors (one per chunk).
        Example: [[0.123, ...], [0.456, ...], ...]
    """
    return await batch_embed(chunks, chapter_id=3)

