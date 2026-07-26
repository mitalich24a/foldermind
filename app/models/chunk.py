"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Chunk model.
"""

from pydantic import BaseModel


class Chunk(BaseModel):
    """
    Represents a chunk of a document.
    """

    document_name: str
    document_source: str
    chunk_id: int
    content: str