"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Document metadata model.
"""

from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    """
    Metadata associated with a document.
    """

    source: str
    extension: str
    size: int