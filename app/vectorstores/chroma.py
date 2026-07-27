"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Chroma vector store.
"""

from collections.abc import Iterator

from app.models.embedding import Embedding
from app.models.search_result import SearchResult
from app.vectorstores.base import VectorStore


class ChromaVectorStore(VectorStore):

    def add(
        self,
        embeddings: Iterator[Embedding],
    ) -> None:
        raise NotImplementedError()

    def search(
        self,
        query: list[float],
        limit: int = 5,
    ) -> list[SearchResult]:
        raise NotImplementedError()