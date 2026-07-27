"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Service for generating query embeddings.
"""

from app.embedders.factory import EmbedderFactory
from app.models.embedding_config import EmbeddingConfig
from app.models.query import Query
from app.models.query_embedding import QueryEmbedding


class QueryEmbeddingService:
    """
    Orchestrates query embedding generation.
    """

    def __init__(
        self,
        config: EmbeddingConfig | None = None,
    ):
        self.config = config or EmbeddingConfig()

    def embed(
        self,
        query: Query,
    ) -> QueryEmbedding:

        embedder = EmbedderFactory.create(
            self.config,
        )

        return embedder.embed_query(
            query,
        )