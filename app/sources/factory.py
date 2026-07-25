"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Factory for creating document sources.
"""

from app.sources.azure_blob import AzureBlobSource
from app.sources.base import DocumentSource
from app.sources.box import BoxSource
from app.sources.confluence import ConfluenceSource
from app.sources.dropbox import DropboxSource
from app.sources.gdrive import GoogleDriveSource
from app.sources.github import GitHubSource
from app.sources.jira import JiraSource
from app.sources.local import LocalSource
from app.sources.onedrive import OneDriveSource
from app.sources.s3 import S3Source
from app.sources.sharepoint import SharePointSource


class SourceFactory:
    """
    Creates the appropriate document source.
    """

    _SOURCES = {
        "local": LocalSource,
        "s3": S3Source,
        "azure_blob": AzureBlobSource,
        "gdrive": GoogleDriveSource,
        "onedrive": OneDriveSource,
        "sharepoint": SharePointSource,
        "github": GitHubSource,
        "dropbox": DropboxSource,
        "box": BoxSource,
        "confluence": ConfluenceSource,
        "jira": JiraSource,
    }

    @classmethod
    def create(cls, source_type: str, path: str) -> DocumentSource:
        source_class = cls._SOURCES.get(source_type)

        if source_class is None:
            raise ValueError(f"Unsupported source type: {source_type}")

        return source_class(path)