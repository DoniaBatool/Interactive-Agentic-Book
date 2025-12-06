"""
Application configuration management.

Loads environment variables using Pydantic Settings for type-safe configuration.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    All API keys and credentials are optional in this initial phase.
    Future features will require these values and add validation.
    """

    # === OpenAI Configuration ===
    openai_api_key: Optional[str] = None

    # === Qdrant Vector Database ===
    qdrant_url: Optional[str] = None
    qdrant_api_key: Optional[str] = None

    # === Database Configuration ===
    database_url: Optional[str] = None

    # === Authentication ===
    betterauth_secret: Optional[str] = None

    # === Email Configuration ===
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None

    # === AI Runtime Configuration ===
    ai_provider: str = "openai"  # Options: "openai", "gemini", "deepseek"
    qdrant_collection_ch1: Optional[str] = None  # Qdrant collection name for Chapter 1
    embedding_model: Optional[str] = None  # Embedding model identifier (e.g., "text-embedding-3-small")
    llm_model: Optional[str] = None  # LLM model identifier (e.g., "gpt-4o", "gemini-pro")
    
    # === Chapter 2 Runtime Configuration ===
    qdrant_collection_ch2: Optional[str] = None  # Qdrant collection name for Chapter 2 RAG operations
    ch2_embedding_model: Optional[str] = None  # Embedding model for Chapter 2 (e.g., "text-embedding-3-small")
    ch2_llm_model: Optional[str] = None  # LLM model for Chapter 2 (e.g., "gpt-4o-mini")
    default_ch2_model: Optional[str] = None  # Default LLM model for Chapter 2 runtime (e.g., "gpt-4o-mini")
    default_ch2_embeddings: Optional[str] = None  # Default embedding model for Chapter 2 (e.g., "text-embedding-3-small")
    enable_chapter_2_runtime: bool = True  # Enable/disable Chapter 2 runtime engine

    # === Diagram Generation Configuration ===
    diagram_model: Optional[str] = None  # Diagram model identifier (e.g., "gpt-4o", "gemini-flash")
    diagram_provider: str = "openai"  # Diagram provider selection (openai, gemini)

    # === Application Configuration ===
    environment: str = "development"
    backend_port: int = 8000
    cors_origins: list[str] = ["http://localhost:3000"]  # Frontend URL

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Allow both OPENAI_API_KEY and openai_api_key


# Singleton instance
settings = Settings()
