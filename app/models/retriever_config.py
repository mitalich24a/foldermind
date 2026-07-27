"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Retriever configuration.
"""

from enum import Enum

from pydantic import BaseModel


class RetrieverProvider(str, Enum):
    """
    Supported retrievers.
    """

    VECTOR = "vector"


class RetrieverConfig(BaseModel):
    """
    Retriever configuration.
    """

    provider: RetrieverProvider = (
        RetrieverProvider.VECTOR
    )

    limit: int = 5