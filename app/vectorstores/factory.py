"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Factory for vector stores.
"""

from app.models.vectorstore_config import (
    VectorStoreConfig,
    VectorStoreProvider,
)
from app.vectorstores.base import VectorStore
from app.vectorstores.chroma import ChromaVectorStore
from app.vectorstores.memory import MemoryVectorStore
from app.vectorstores.qdrant import QdrantVectorStore


_memory_store = MemoryVectorStore()
_chroma_store = ChromaVectorStore()
_qdrant_store = QdrantVectorStore()

class VectorStoreFactory:
    """
    Creates vector stores.
    """

    @classmethod
    def create(
        cls,
        config: VectorStoreConfig,
    ) -> VectorStore:

        if config.provider == VectorStoreProvider.MEMORY:
            return _memory_store

        if config.provider == VectorStoreProvider.CHROMA:
            return _chroma_store

        if config.provider == VectorStoreProvider.QDRANT:
            return _qdrant_store

        raise ValueError(
            f"Unsupported vector store: {config.provider}"
        )