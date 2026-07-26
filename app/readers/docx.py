"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for DOCX documents.
"""

from app.readers.base import DocumentReader


class DOCXReader(DocumentReader):
    """
    Reader for Microsoft Word documents.
    """

    def read(self, document) -> str:
        raise NotImplementedError("DOCX reader not implemented yet.")