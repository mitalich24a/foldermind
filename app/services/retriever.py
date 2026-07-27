"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Retriever service.
"""

from app.models.query import Query
from app.models.retriever_config import RetrieverConfig
from app.models.search_result import SearchResult
from app.retrievers.factory import RetrieverFactory


class RetrieverService:
    """
    Orchestrates retrieval.
    """

    def __init__(
        self,
        config: RetrieverConfig | None = None,
    ):
        self.config = config or RetrieverConfig()

        self.retriever = RetrieverFactory.create(
            self.config,
        )

    def retrieve(
        self,
        query: Query,
    ) -> list[SearchResult]:

        return self.retriever.retrieve(
            query,
        )