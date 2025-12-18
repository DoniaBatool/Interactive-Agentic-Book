from functools import lru_cache
from typing import List, Optional, Any
import os

from pydantic import AnyHttpUrl, Field, NonNegativeInt
from pydantic_settings import BaseSettings, SettingsConfigDict, DotEnvSettingsSource


class FilteredDotEnvSettingsSource(DotEnvSettingsSource):
    """Custom env source that filters out ALLOWED_ORIGINS to avoid parsing errors"""
    def __call__(self) -> dict[str, Any]:
        data = super().__call__()
        # Remove ALLOWED_ORIGINS if present to avoid parsing errors
        data.pop("ALLOWED_ORIGINS", None)
        data.pop("allowed_origins", None)
        return data


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_ignore_empty=True,
    )
    
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        # Replace dotenv_settings with our filtered version
        return (
            init_settings,
            env_settings,
            FilteredDotEnvSettingsSource(settings_cls),
            file_secret_settings,
        )

    app_name: str = "rag-backend"

    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    qdrant_url: Optional[AnyHttpUrl] = Field(default=None, env="QDRANT_URL")
    qdrant_api_key: Optional[str] = Field(default=None, env="QDRANT_API_KEY")
    database_url: Optional[str] = Field(default=None, env="DATABASE_URL")

    qdrant_collection: str = Field(default="textbook-chunks", env="QDRANT_COLLECTION")
    embedding_model: str = Field(default="text-embedding-3-small", env="EMBEDDING_MODEL")
    embedding_dimensions: NonNegativeInt = Field(default=1536, env="EMBEDDING_DIM")
    retrieval_top_k: NonNegativeInt = Field(default=5, env="RETRIEVAL_TOP_K")
    chat_model: str = Field(default="gpt-4o-mini", env="CHAT_MODEL")
    default_stream: bool = Field(default=False, env="CHAT_STREAM")

    # Note: allowed_origins is not defined here to avoid .env parsing issues
    # It's set as a regular attribute after initialization in get_settings()


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    # Set allowed_origins as a regular attribute (not a pydantic field)
    # to avoid parsing issues with ALLOWED_ORIGINS in .env
    # Use object.__setattr__ to bypass pydantic's field validation
    object.__setattr__(settings, "allowed_origins", [AnyHttpUrl("http://localhost:3000")])
    return settings

