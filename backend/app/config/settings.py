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
