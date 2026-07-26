"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Chunking configuration.
"""

from pydantic import BaseModel, Field


class ChunkingConfig(BaseModel):
    """
    Configuration for document chunking.
    """

    chunk_size: int = Field(
        default=500,
        gt=0,
    )

    chunk_overlap: int = Field(
        default=100,
        ge=0,
    )