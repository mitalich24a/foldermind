"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Service for vector stores.
"""

from collections.abc import Iterator

from app.models.embedding import Embedding
from app.models.search_result import SearchResult
from app.models.vectorstore_config import (
    VectorStoreConfig,
)
from app.vectorstores.factory import (
    VectorStoreFactory,
)


class VectorStoreService:
    """
    Orchestrates vector store operations.
    """

    def __init__(
        self,
        config: VectorStoreConfig | None = None,
    ):
        self.config = (
            config or VectorStoreConfig()
        )

        self.vector_store = (
            VectorStoreFactory.create(
                self.config,
            )
        )

    def upsert(
        self,
        embeddings: Iterator[Embedding],
    ) -> None:
        """
        Store embeddings.
        """

        self.vector_store.upsert(
            embeddings,
        )

    def search(
        self,
        query: list[float],
        limit: int = 5,
    ) -> list[SearchResult]:
        """
        Search for similar embeddings.
        """

        return self.vector_store.search(
            query=query,
            limit=limit,
        )