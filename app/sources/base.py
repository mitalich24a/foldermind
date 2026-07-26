"""
FolderMind
Copyright (c) 2026 Mitali Choubisa. All rights reserved.

Description:
Abstract base class for all document sources.
"""

from abc import ABC, abstractmethod


class DocumentSource(ABC):

    @abstractmethod
    def validate(self) -> None:
        pass

    @abstractmethod
    def discover_documents(self):
        pass