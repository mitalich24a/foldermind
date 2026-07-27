"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Vector store configuration.
"""

from enum import Enum

from pydantic import BaseModel

from app.config.settings import settings


class VectorStoreProvider(str, Enum):
    """
    Supported vector stores.
    """

    MEMORY = "memory"
    CHROMA = "chroma"
    QDRANT = "qdrant"


class VectorStoreConfig(BaseModel):
    """
    Vector store configuration.
    """

    provider: VectorStoreProvider = (
        VectorStoreProvider(
            settings.vector_store_provider,
        )
    )