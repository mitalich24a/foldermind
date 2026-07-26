"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Document model.
"""

from pydantic import BaseModel

from app.models.metadata import DocumentMetadata


class Document(BaseModel):
    """
    Represents an ingested document.
    """

    name: str
    content: str
    metadata: DocumentMetadata