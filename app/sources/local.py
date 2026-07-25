"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Local filesystem document source.
"""
from typing import Any
from pathlib import Path

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

    def list_documents(self) -> list[Path]:
        """
        Return all files under the configured directory.
        """
        return [
            file
            for file in self.path.rglob("*")
            if file.is_file()
        ]

    def read_document(self, document_path: Path) -> str:
        """
        Read and return the contents of a document.
        """
        return document_path.read_text(
            encoding="utf-8"
        )