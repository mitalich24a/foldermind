"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Service for orchestrating document ingestion.
"""

from collections.abc import Iterator

from app.chunkers.factory import ChunkerFactory
from app.models.chunk import Chunk
from app.models.document import Document
from app.models.local import LocalSourceConfig
from app.readers.factory import ReaderFactory
from app.sources.factory import SourceFactory

from app.models.chunking import ChunkingConfig

from pathlib import Path

from app.models.metadata import DocumentMetadata


class IngestionService:
    """
    Orchestrates the document ingestion workflow.
    """

    def read(
        self,
        config: LocalSourceConfig,
    ) -> Iterator[Chunk]:
        """
        Read and chunk documents from the configured source.
        """
        source = SourceFactory.create(
            config.source_type,
            config.config.model_dump(),
        )

        source.validate()

        chunker = ChunkerFactory.create(
                        ChunkingConfig(
                            chunk_size=500,
                            chunk_overlap=100,
                        )
                )

        for local_document in source.discover_documents():
            reader = ReaderFactory.create(
                local_document.path,
            )

            document = Document(
                    name=local_document.name,
                    content=reader.read(local_document),
                    metadata=DocumentMetadata(
                        source=str(local_document.path),
                        extension=Path(local_document.path).suffix,
                        size=local_document.size,
                    ),
            )

            yield from chunker.chunk(document)