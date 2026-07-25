"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from pydantic import BaseModel

from app.models.source import BaseSourceConfig, SourceType

class LocalConfig(BaseModel):
    path: str

class LocalSourceConfig(BaseSourceConfig):
    source_type: SourceType = SourceType.LOCAL
    config: LocalConfig