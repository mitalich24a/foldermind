"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from app.models.source import BaseSourceDetails


class LocalSourceDetails(BaseSourceDetails):
    path: str

