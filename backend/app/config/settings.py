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

    # === Gemini Configuration ===
    gemini_api_key: Optional[str] = None  # Google Gemini API key

    # === Qdrant Vector Database ===
    qdrant_url: Optional[str] = None
    qdrant_api_key: Optional[str] = None

    # === Database Configuration ===
    database_url: Optional[str] = None

    # === Authentication ===
    betterauth_secret: Optional[str] = None
    betterauth_public_key: Optional[str] = None  # BetterAuth public key
    betterauth_secret_key: Optional[str] = None  # BetterAuth secret key
    betterauth_issuer: str = "interactive-agentic-book"  # BetterAuth issuer identifier
    default_user_role: str = "student"  # Default user role for RBAC

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

    # === Chapter 3 Runtime Configuration ===
    qdrant_collection_ch3: Optional[str] = None  # Qdrant collection name for Chapter 3 RAG operations
    ch3_embedding_model: Optional[str] = None  # Embedding model for Chapter 3 (e.g., "text-embedding-3-small")
    ch3_llm_model: Optional[str] = None  # LLM model for Chapter 3 (e.g., "gpt-4o-mini")
    default_ch3_model: Optional[str] = None  # Default LLM model for Chapter 3 runtime (e.g., "gpt-4o-mini")
    default_ch3_embeddings: Optional[str] = None  # Default embedding model for Chapter 3 (e.g., "text-embedding-3-small")
    enable_chapter_3_runtime: bool = True  # Enable/disable Chapter 3 runtime engine

    # === Diagram Generation Configuration ===
    diagram_model: Optional[str] = None  # Diagram model identifier (e.g., "gpt-4o", "gemini-flash")
    diagram_provider: str = "openai"  # Diagram provider selection (openai, gemini)

    # === System Integration Configuration ===
    # Default runtime model settings
    default_runtime_model: Optional[str] = None  # Default LLM model for runtime (e.g., "gpt-4o-mini")
    default_runtime_provider: str = "openai"  # Default provider for runtime (e.g., "openai", "gemini")
    
    # === Translation Configuration ===
    translation_provider: Optional[str] = None  # Translation provider ("openai" or "gemini")
    translation_model: Optional[str] = None  # Translation model (e.g., "gpt-4o-mini")
    
    # === Streaming Configuration ===
    ai_streaming_enabled: bool = False  # Enable AI streaming mode
    streaming_backend: str = "sse"  # Streaming backend ("sse" or "websocket")
    
    # Provider defaults (placeholder)
    # TODO: Implement provider defaults dictionary
    # PROVIDER_DEFAULTS = {
    #     "openai": {"model": "gpt-4o-mini", "temperature": 0.7},
    #     "gemini": {"model": "gemini-pro", "temperature": 0.7}
    # }

    # === Application Configuration ===
    environment: str = "development"
    backend_port: int = 8000
    cors_origins: str = "http://localhost:3000"  # Comma-separated list from env, will be parsed
    
    def get_cors_origins(self) -> list[str]:
        """Parse CORS origins from environment variable or use default."""
        if self.cors_origins:
            # Split by comma and strip whitespace
            origins = [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]
            return origins
        return ["http://localhost:3000"]  # Default

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Allow both OPENAI_API_KEY and openai_api_key


# Singleton instance
settings = Settings()
