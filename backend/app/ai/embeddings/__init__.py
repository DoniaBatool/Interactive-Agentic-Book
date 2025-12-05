"""
Embedding Client Module

This package provides text-to-vector embedding functionality for RAG pipeline.
"""

from app.ai.embeddings.embedding_client import generate_embedding, batch_embed

__all__ = ["generate_embedding", "batch_embed"]

