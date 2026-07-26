"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Factory for embedding providers.
"""

from app.embedders.base import Embedder
from app.embedders.fake import FakeEmbedder
from app.embedders.ollama import OllamaEmbedder
from app.embedders.openai import OpenAIEmbedder
from app.models.embedding_config import (
    EmbeddingConfig,
    EmbeddingProvider,
)


class EmbedderFactory:
    """
    Creates embedding providers.
    """

    @classmethod
    def create(
        cls,
        config: EmbeddingConfig,
    ) -> Embedder:

        if config.provider == EmbeddingProvider.FAKE:
            return FakeEmbedder()

        if config.provider == EmbeddingProvider.OPENAI:
            return OpenAIEmbedder()

        if config.provider == EmbeddingProvider.OLLAMA:
            return OllamaEmbedder()

        raise ValueError(
            f"Unsupported provider: {config.provider}"
        )