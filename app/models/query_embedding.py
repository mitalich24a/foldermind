"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Query embedding model.
"""

from pydantic import BaseModel

from app.models.query import Query


class QueryEmbedding(BaseModel):
    """
    Represents an embedded query.
    """

    query: Query
    vector: list[float]