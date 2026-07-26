"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Base class for all document chunkers.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator

from app.models.chunk import Chunk
from app.models.document import Document


class DocumentChunker(ABC):
    """
    Base class for all document chunkers.
    """

    @abstractmethod
    def chunk(
        self,
        document: Document,
    ) -> Iterator[Chunk]:
        """
        Yield chunks for a document.
        """
        pass