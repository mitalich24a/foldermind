"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Fake embedding provider for development.
"""

from collections.abc import Iterator

from app.embedders.base import Embedder
from app.models.chunk import Chunk
from app.models.embedding import Embedding


class FakeEmbedder(Embedder):
    """
    Generates dummy embeddings for development.
    """

    EMBEDDING_DIMENSION = 10

    def embed(
        self,
        chunks: Iterator[Chunk],
    ) -> Iterator[Embedding]:

        for chunk in chunks:
            yield Embedding(
                chunk=chunk,
                vector=[0.0] * self.EMBEDDING_DIMENSION,
            )