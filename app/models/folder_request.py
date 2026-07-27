"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Folder request model.
"""

from pydantic import BaseModel


class FolderRequest(BaseModel):
    path: str