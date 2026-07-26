"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Base class for embedding providers.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator

from app.models.chunk import Chunk
from app.models.embedding import Embedding


class Embedder(ABC):
    """
    Base class for embedding providers.
    """

    @abstractmethod
    def embed(
        self,
        chunks: Iterator[Chunk],
    ) -> Iterator[Embedding]:
        """
        Yield embeddings for chunks.
        """
        pass