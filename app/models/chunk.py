"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Chunk model.
"""

from pydantic import BaseModel

from app.models.metadata import DocumentMetadata


class Chunk(BaseModel):
    """
    Represents a chunk of a document.
    """

    chunk_id: int
    content: str
    metadata: DocumentMetadata