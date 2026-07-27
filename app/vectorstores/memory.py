"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

In-memory vector store.
"""

from collections.abc import Iterator

from app.models.embedding import Embedding
from app.models.search_result import SearchResult
from app.vectorstores.base import VectorStore

from math import sqrt


class MemoryVectorStore(VectorStore):
    """
    In-memory vector store.
    """

    def __init__(self):
        self._embeddings: list[Embedding] = []
    
    @staticmethod
    def _cosine_similarity(
            vector1: list[float],
            vector2: list[float],
        ) -> float:
            """
            Compute cosine similarity between two vectors.
            """

            dot_product = sum(
                a * b
                for a, b in zip(vector1, vector2)
            )

            magnitude1 = sqrt(
                sum(a * a for a in vector1)
            )

            magnitude2 = sqrt(
                sum(b * b for b in vector2)
            )

            if magnitude1 == 0 or magnitude2 == 0:
                return 0.0

            return dot_product / (
                magnitude1 * magnitude2
            )

    def upsert(
        self,
        embeddings: Iterator[Embedding],
    ) -> None:

        self._embeddings.extend(embeddings)

    def search(
        self,
        query: list[float],
        limit: int = 5,
    ) -> list[SearchResult]:

        results: list[SearchResult] = []

        for embedding in self._embeddings:

            score = self._cosine_similarity(
                query,
                embedding.vector,
            )

            results.append(
                SearchResult(
                    chunk=embedding.chunk,
                    score=score,
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:limit]