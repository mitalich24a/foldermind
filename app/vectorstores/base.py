"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Base class for vector stores.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator

from app.models.embedding import Embedding
from app.models.search_result import SearchResult


class VectorStore(ABC):
    """
    Base class for vector stores.
    """

    @abstractmethod
    def upsert(
        self,
        embeddings: Iterator[Embedding],
    ) -> None:
        """
        Store embeddings.
        """
        pass

    @abstractmethod
    def search(
        self,
        query: list[float],
        limit: int = 5,
    ) -> list[SearchResult]:
        """
        Search for similar embeddings.
        """
        pass