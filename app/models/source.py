"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from enum import Enum

from pydantic import BaseModel


class SourceType(str, Enum):
    LOCAL = "local"
    S3 = "s3"
    AZURE_BLOB = "azure_blob"
    GDRIVE = "gdrive"
    ONEDRIVE = "onedrive"
    SHAREPOINT = "sharepoint"
    GITHUB = "github"
    DROPBOX = "dropbox"
    BOX = "box"
    CONFLUENCE = "confluence"
    JIRA = "jira"


class BaseSourceConfig(BaseModel):
    """
    Base class for connector-specific configuration.
    """


class SourceConfig(BaseModel):
    source_type: SourceType
    config: dict[str, str]