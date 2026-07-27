"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for plain text documents.
"""

from pathlib import Path

from app.models.document import Document
from app.readers.base import DocumentReader


class TXTReader(DocumentReader):
    """
    Reader for plain text files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        return path.read_text(
            encoding="utf-8"
        )