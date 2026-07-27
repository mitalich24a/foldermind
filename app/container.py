"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Application dependency container.
"""

from app.models.embedding_config import EmbeddingConfig
from app.models.vectorstore_config import VectorStoreConfig
from app.services.embedding import EmbeddingService
from app.services.query_embedding import QueryEmbeddingService
from app.services.retriever import RetrieverService
from app.services.vectorstore import VectorStoreService


class Container:
    """
    Application dependency container.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService(
            EmbeddingConfig(),
        )

        self.query_embedding_service = (
            QueryEmbeddingService(
                EmbeddingConfig(),
            )
        )

        self.vectorstore_service = (
            VectorStoreService(
                VectorStoreConfig(),
            )
        )

        self.retriever_service = (
            RetrieverService()
        )