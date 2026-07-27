"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Vector retriever.
"""

from app.models.query import Query
from app.models.search_result import SearchResult
from app.retrievers.base import Retriever


class VectorRetriever(Retriever):
    """
    Vector-based retriever.
    """

    def retrieve(
        self,
        query: Query,
    ) -> list[SearchResult]:
        raise NotImplementedError(
            "Retriever not implemented yet."
        )