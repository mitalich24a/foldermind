"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Persistent ChromaDB vector store.
"""

from collections.abc import Iterator

import chromadb

from app.models.chunk import Chunk
from app.models.embedding import Embedding
from app.models.metadata import DocumentMetadata
from app.models.search_result import SearchResult
from app.vectorstores.base import VectorStore


class ChromaVectorStore(VectorStore):
    """
    ChromaDB implementation of VectorStore.
    """

    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(
            path="data/chroma",
        )

        self.collection = self.client.get_or_create_collection(
            name="foldermind",
        )

    def upsert(
        self,
        embeddings: Iterator[Embedding],
    ) -> None:
        ids = []
        documents = []
        vectors = []
        metadatas = []

        for embedding in embeddings:
            ids.append(str(embedding.chunk.chunk_id))
            documents.append(
                embedding.chunk.content,
            )
            vectors.append(
                embedding.vector,
            )
            metadatas.append(
                embedding.chunk.metadata.model_dump(),
            )

        if ids:
            self.collection.upsert(
                ids=ids,
                documents=documents,
                embeddings=vectors,
                metadatas=metadatas,
            )

    def search(
        self,
        query: list[float],
        limit: int = 5,
    ) -> list[SearchResult]:

        response = self.collection.query(
            query_embeddings=[query],
            n_results=limit,
        )

        results = []

        ids = response["ids"][0]
        docs = response["documents"][0]
        metas = response["metadatas"][0]
        distances = response["distances"][0]

        for chunk_id, content, metadata, score in zip(
            ids,
            docs,
            metas,
            distances,
        ):
                chunk = Chunk(
                    chunk_id=chunk_id,
                    content=content,
                    metadata=DocumentMetadata(
                        **metadata,
                    ),
                )

                results.append(
                    SearchResult(
                        chunk=chunk,
                        score=score,
                    )
                )

        return results