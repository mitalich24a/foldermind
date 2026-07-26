"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Service for generating embeddings.
"""

from collections.abc import Iterator

from app.embedders.factory import EmbedderFactory
from app.models.chunk import Chunk
from app.models.embedding import Embedding
from app.models.embedding_config import EmbeddingConfig


class EmbeddingService:
    """
    Orchestrates embedding generation.
    """

    def __init__(
        self,
        config: EmbeddingConfig | None = None,
    ):
        self.config = config or EmbeddingConfig()

    def embed(
        self,
        chunks: Iterator[Chunk],
    ) -> Iterator[Embedding]:

        embedder = EmbedderFactory.create(
            self.config,
        )

        yield from embedder.embed(chunks)