"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Abstract base class for all document sources.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator


class DocumentSource(ABC):
    """
    Base class for all document sources.
    """

    @abstractmethod
    def validate(self) -> None:
        """
        Validate the source configuration.
        """
        pass

    @abstractmethod
    def discover_documents(self) -> Iterator:
        """
        Yield discovered documents.
        """
        pass