"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Ollama embedder.
"""

from collections.abc import Iterator

from ollama import Client

from app.config.settings import settings
from app.embedders.base import Embedder
from app.models.chunk import Chunk
from app.models.embedding import Embedding
from app.models.query import Query
from app.models.query_embedding import QueryEmbedding


class OllamaEmbedder(Embedder):
    """
    Ollama embedding implementation.
    """

    def __init__(self):
        self.client = Client()

    def embed(
        self,
        chunks: Iterator[Chunk],
    ) -> Iterator[Embedding]:

        for chunk in chunks:

            response = self.client.embed(
                model=settings.embedding_model,
                input=chunk.content,
            )

            yield Embedding(
                chunk=chunk,
                vector=response["embeddings"][0],
            )

    def embed_query(
        self,
        query: Query,
    ) -> QueryEmbedding:

        response = self.client.embed(
            model=settings.embedding_model,
            input=query.text,
        )

        return QueryEmbedding(
            query=query,
            vector=response["embeddings"][0],
        )