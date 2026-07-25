"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from app.models.source import SourceConfig, SourceType


class S3SourceConfig(SourceConfig):
    source_type: SourceType = SourceType.S3