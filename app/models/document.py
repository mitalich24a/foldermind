"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from pydantic import BaseModel


class Document(BaseModel):
    name: str
    source: str
    content: str