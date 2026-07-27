"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Query model.
"""

from pydantic import BaseModel, Field


class Query(BaseModel):
    """
    Represents a search query.
    """

    text: str = Field(
        min_length=1,
    )