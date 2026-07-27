"""
Tests for retrieval.
"""

from app.models.chunk import Chunk
from app.models.embedding import Embedding
from app.models.metadata import DocumentMetadata
from app.models.query import Query
from app.models.vectorstore_config import (
    VectorStoreConfig,
    VectorStoreProvider,
)
from app.services.query_embedding import QueryEmbeddingService
from app.services.vectorstore import VectorStoreService


def test_vector_search():

    vectorstore = VectorStoreService(
        VectorStoreConfig(
            provider=VectorStoreProvider.MEMORY,
        )
    )

    chunk = Chunk(
        chunk_id=0,
        content="Python is an amazing language.",
        metadata=DocumentMetadata(
            source="test.txt",
            extension=".txt",
            size=100,
        ),
    )

    embedding = Embedding(
        chunk=chunk,
        vector=[0.0] * 10,
    )

    vectorstore.upsert(iter([embedding]))

    query = Query(
        text="python",
    )

    query_embedding = QueryEmbeddingService().embed(
        query,
    )

    results = vectorstore.search(
        query_embedding.vector,
    )

    assert len(results) == 1
    assert (
        results[0].chunk.content
        == "Python is an amazing language."
    )