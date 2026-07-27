"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Base class for all document readers.
"""

from abc import ABC, abstractmethod

from app.models.document import Document


class DocumentReader(ABC):
    """
    Base class for all document readers.
    """

    @abstractmethod
    def read(self, document: Document) -> str:
        """
        Read and return the document contents.
        """
        raise NotImplementedError