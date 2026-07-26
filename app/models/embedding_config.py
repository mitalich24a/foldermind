"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Embedding configuration.
"""

from enum import Enum

from pydantic import BaseModel


class EmbeddingProvider(str, Enum):
    """
    Supported embedding providers.
    """

    FAKE = "fake"
    OPENAI = "openai"
    OLLAMA = "ollama"


class EmbeddingConfig(BaseModel):
    """
    Embedding configuration.
    """

    provider: EmbeddingProvider = EmbeddingProvider.FAKE