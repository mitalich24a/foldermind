"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for Microsoft Word documents.
"""

from pathlib import Path

from docx import Document as DocxDocument

from app.models.document import Document
from app.readers.base import DocumentReader


class DOCXReader(DocumentReader):
    """
    Reader for DOCX files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        doc = DocxDocument(path)

        paragraphs = []

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return "\n".join(paragraphs)