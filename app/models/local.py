"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from pydantic import BaseModel
from pathlib import Path
from app.models.source import BaseSourceConfig, SourceType

class LocalConfig(BaseModel):
    path: str

class LocalSourceConfig(BaseSourceConfig):
    source_type: SourceType = SourceType.LOCAL
    config: LocalConfig

class LocalDocument(BaseModel):
    name: str
    path: Path
    size: int