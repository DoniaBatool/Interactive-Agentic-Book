"""
Shared Test Fixtures

Pytest fixtures for E2E tests.
"""

import pytest
from typing import Dict, Any
from unittest.mock import Mock, AsyncMock

# TODO: Import FastAPI TestClient when available
# from fastapi.testclient import TestClient
# from app.main import app


@pytest.fixture
def test_client():
    """
    FastAPI TestClient fixture.
    
    TODO: Create real TestClient instance
    TODO: from fastapi.testclient import TestClient
    TODO: return TestClient(app)
    """
    # Placeholder: Return mock for now
    return Mock(name="TestClient")


@pytest.fixture
def mock_openai_provider():
    """
    Mock OpenAI provider fixture.
    
    TODO: Create mock OpenAI provider
    TODO: Mock generate() method to return placeholder response
    """
    mock = AsyncMock()
    mock.generate.return_value = {
        "text": "Mock OpenAI response",
        "metadata": {"model": "gpt-4o-mini", "tokens": 100, "finish_reason": "stop"}
    }
    return mock


@pytest.fixture
def mock_gemini_provider():
    """
    Mock Gemini provider fixture.
    
    TODO: Create mock Gemini provider
    TODO: Mock generate() method to return placeholder response
    """
    mock = AsyncMock()
    mock.generate.return_value = {
        "text": "Mock Gemini response",
        "metadata": {"model": "gemini-pro", "tokens": 100, "finish_reason": "stop"}
    }
    return mock


@pytest.fixture
def mock_qdrant_client():
    """
    Mock Qdrant client fixture.
    
    TODO: Create mock Qdrant client
    TODO: Mock similarity_search() to return placeholder results
    TODO: Mock upsert_vectors() to return success
    TODO: Mock create_collection() to return success
    """
    mock = AsyncMock()
    mock.similarity_search.return_value = [
        {"id": "1", "score": 0.9, "text": "Mock chunk text", "chapter_id": 1, "section_id": "section-1"}
    ]
    mock.upsert_vectors.return_value = True
    mock.create_collection.return_value = True
    return mock


@pytest.fixture
def mock_embedding_client():
    """
    Mock embedding client fixture.
    
    TODO: Create mock embedding client
    TODO: Mock generate_embedding() to return placeholder vector
    TODO: Mock batch_embed() to return placeholder vectors
    """
    mock = AsyncMock()
    mock.generate_embedding.return_value = [0.1] * 1536  # Placeholder 1536-dim vector
    mock.batch_embed.return_value = [[0.1] * 1536 for _ in range(10)]  # Placeholder batch
    return mock

