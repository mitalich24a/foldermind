"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Service for indexing a folder.
"""

from app.models.local import (
    LocalConfig,
    LocalSourceConfig,
    SourceType,
)
from app.services.embedding import EmbeddingService
from app.services.ingestion import IngestionService
from app.services.vectorstore import VectorStoreService


class FolderService:
    """
    Orchestrates folder indexing.
    """

    def __init__(self) -> None:
        self.ingestion_service = IngestionService()
        self.embedding_service = EmbeddingService()
        self.vectorstore_service = VectorStoreService()

    def add_folder(
        self,
        folder_path: str,
    ) -> None:
        """
        Read, chunk, embed and index all supported
        documents from a folder.
        """

        config = LocalSourceConfig(
            source_type=SourceType.LOCAL,
            config=LocalConfig(
                path=folder_path,
            ),
        )

        chunks = self.ingestion_service.read(
            config,
        )

        embeddings = self.embedding_service.embed(
            chunks,
        )

        self.vectorstore_service.upsert(
            embeddings,
        )