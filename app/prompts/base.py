"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Prompt builder interface.
"""

from abc import ABC, abstractmethod

from app.models.query import Query
from app.models.search_result import SearchResult


class PromptBuilder(ABC):
    """
    Builds prompts for the LLM.
    """

    @abstractmethod
    def build(
        self,
        query: Query,
        results: list[SearchResult],
    ) -> str:
        pass