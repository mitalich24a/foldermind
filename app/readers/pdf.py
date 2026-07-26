"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for PDF documents.
"""

from app.readers.base import DocumentReader


class PDFReader(DocumentReader):
    """
    Reader for PDF files.
    """

    def read(self, document) -> str:
        raise NotImplementedError("PDF reader not implemented yet.")