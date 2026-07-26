"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Local filesystem document source.
"""

from pathlib import Path
from typing import Any

from app.models.local import LocalDocument
from app.sources.base import DocumentSource


class LocalSource(DocumentSource):
    """
    Local filesystem implementation of a document source.
    """

    def __init__(self, config: dict[str, Any]):
        for key, value in config.items():
            setattr(self, key, value)

        self.path = Path(self.path)

    def validate(self) -> None:
        """
        Validate that the configured path exists and is a directory.
        """
        if not self.path.exists():
            raise FileNotFoundError(
                f"Directory not found: {self.path}"
            )

        if not self.path.is_dir():
            raise NotADirectoryError(
                f"Not a directory: {self.path}"
            )

    def discover_documents(self) -> list[LocalDocument]:
        """
        Discover all documents under the configured directory.
        """
        documents = []

        for file in self.path.rglob("*"):
            if file.is_file():
                documents.append(
                    LocalDocument(
                        name=file.name,
                        path=file,
                        size=file.stat().st_size,
                    )
                )

        return documents

    def read_document(
        self,
        document: LocalDocument,
    ) -> str:
        """
        Read and return the contents of a document.
        """
        return document.path.read_text(
            encoding="utf-8"
        )