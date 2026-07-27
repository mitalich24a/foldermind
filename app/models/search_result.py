"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Search result model.
"""

from pydantic import BaseModel

from app.models.chunk import Chunk


class SearchResult(BaseModel):
    """
    Represents a vector search result.
    """

    chunk: Chunk
    score: float