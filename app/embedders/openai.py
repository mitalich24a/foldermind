"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

OpenAI embedding provider.
"""

from collections.abc import Iterator

from app.embedders.base import Embedder
from app.models.chunk import Chunk
from app.models.embedding import Embedding

from app.models.query import Query
from app.models.query_embedding import QueryEmbedding


class OpenAIEmbedder(Embedder):
    """
    Generates embeddings using OpenAI.
    """

    def embed(
        self,
        chunks: Iterator[Chunk],
    ) -> Iterator[Embedding]:

        raise NotImplementedError(
            "OpenAI embedder not implemented yet."
        )
    
    def embed_query(
    self,
    query: Query,
) -> QueryEmbedding:

        raise NotImplementedError(
            "OpenAI embedder not implemented yet."
        )