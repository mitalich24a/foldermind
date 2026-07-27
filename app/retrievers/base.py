"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Base retriever.
"""

from abc import ABC, abstractmethod

from app.models.query import Query
from app.models.search_result import SearchResult


class Retriever(ABC):
    """
    Base class for retrievers.
    """

    @abstractmethod
    def retrieve(
        self,
        query: Query,
    ) -> list[SearchResult]:
        """
        Retrieve relevant chunks.
        """
        pass