"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Folder response model.
"""

from pydantic import BaseModel


class FolderResponse(BaseModel):
    message: str