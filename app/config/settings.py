"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Application configuration.
"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.
    """

    # API Keys
    openai_api_key: str = ""

    # Providers
    embedding_provider: str = "openai"
    vector_store_provider: str = "chroma"
    llm_provider: str = "openai"

    # Models
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-5-mini"

    # Storage
    chroma_db_path: Path = Path("data/chroma")

    # Chunking
    chunk_size: int = 1000
    chunk_overlap: int = 200

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()