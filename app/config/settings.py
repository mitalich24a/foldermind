"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Application settings.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    openai_api_key: str = ""

    embedding_provider: str = "fake"
    embedding_model: str = "text-embedding-3-small"

    llm_provider: str = "fake"
    llm_model: str = "gpt-4.1-mini"

    class Config:
        env_file = ".env"


settings = Settings()