"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Vector retriever.
"""

from app.models.query import Query
from app.models.retriever_config import RetrieverConfig
from app.models.search_result import SearchResult
from app.retrievers.base import Retriever
from app.services.query_embedding import QueryEmbeddingService
from app.services.vectorstore import VectorStoreService


class VectorRetriever(Retriever):
    """
    Retrieves chunks using vector similarity.
    """

    def __init__(
        self,
        config: RetrieverConfig,
    ):
        self.config = config

        self.query_embedding_service = (
            QueryEmbeddingService()
        )

        self.vectorstore_service = (
            VectorStoreService()
        )

    def retrieve(
        self,
        query: Query,
    ) -> list[SearchResult]:

        query_embedding = (
            self.query_embedding_service.embed(
                query,
            )
        )

        return self.vectorstore_service.search(
            query=query_embedding.vector,
            limit=self.config.limit,
        )