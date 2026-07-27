"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Recursive document chunker.
"""

from collections.abc import Iterator

from app.chunkers.base import DocumentChunker
from app.models.chunk import Chunk
from app.models.document import Document
from app.models.chunking import ChunkingConfig


class RecursiveChunker(DocumentChunker):
    """
    Fixed-size chunker.

    A recursive chunking strategy will be introduced later.
    """

    def __init__(self,config: ChunkingConfig,):
        self.config = config

    

    def chunk(self, document: Document,) -> Iterator[Chunk]:

        text = document.content

        chunk_size = self.config.chunk_size
        overlap = self.config.chunk_overlap

        if overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size."
            )

        start = 0
        chunk_index = 0

        while start < len(text):

            end = start + chunk_size

            yield Chunk(
                chunk_id=f"{document.metadata.source}:{chunk_index}",
                content=text[start:end],
                metadata=document.metadata,
            )

            chunk_index += 1

            start += chunk_size - overlap