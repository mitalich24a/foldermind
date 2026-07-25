"""
FolderMind
Copyright (c) 2026 Mitali Choubisa. All rights reserved.

Description:
Abstract base class for all document sources.
"""

from abc import ABC, abstractmethod


class DocumentSource(ABC):
    """
    Contract implemented by every document source.
    """

    @abstractmethod
    def validate(self) -> None:
        """Validate that the source is accessible."""

    @abstractmethod
    def list_documents(self) -> list[str]:
        """Return all available documents."""

    @abstractmethod
    def read_document(self, document_path: str) -> str:
        """Return document contents."""