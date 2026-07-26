"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Ollama embedding provider.
"""

from collections.abc import Iterator

from app.embedders.base import Embedder
from app.models.chunk import Chunk
from app.models.embedding import Embedding


class OllamaEmbedder(Embedder):
    """
    Generates embeddings using Ollama.
    """

    def embed(
        self,
        chunks: Iterator[Chunk],
    ) -> Iterator[Embedding]:
        raise NotImplementedError(
            "Ollama embedder not implemented yet."
        )