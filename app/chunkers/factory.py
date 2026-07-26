"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Factory for creating document chunkers.
"""

from app.chunkers.base import DocumentChunker
from app.chunkers.recursive import RecursiveChunker
from app.models.chunking import ChunkingConfig


class ChunkerFactory:
    """
    Creates document chunkers.
    """

    @classmethod
    def create(
        cls,
        config: ChunkingConfig | None = None,
    ) -> DocumentChunker:

        if config is None:
            config = ChunkingConfig()

        return RecursiveChunker(config)