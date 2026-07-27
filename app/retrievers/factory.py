"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Factory for retrievers.
"""

from app.models.retriever_config import (
    RetrieverConfig,
    RetrieverProvider,
)
from app.retrievers.base import Retriever
from app.retrievers.vector import VectorRetriever


class RetrieverFactory:
    """
    Creates retrievers.
    """

    @classmethod
    def create(
        cls,
        config: RetrieverConfig,
    ) -> Retriever:

        if config.provider == RetrieverProvider.VECTOR:
            return VectorRetriever(config)

        raise ValueError(
            f"Unsupported retriever: {config.provider}"
        )