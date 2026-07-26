"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Embedding model.
"""

from pydantic import BaseModel

from app.models.chunk import Chunk


class Embedding(BaseModel):
    """
    Represents a vector embedding for a chunk.
    """

    chunk: Chunk
    vector: list[float]