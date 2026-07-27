"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for PDF documents.
"""

from pathlib import Path

from pypdf import PdfReader

from app.models.document import Document
from app.readers.base import DocumentReader


class PDFReader(DocumentReader):
    """
    Reader for PDF files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        reader = PdfReader(path)

        text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text)