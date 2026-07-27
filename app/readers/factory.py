"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Factory for creating document readers.
"""

from pathlib import Path
from typing import Type

from app.readers.base import DocumentReader
from app.readers.docx import DOCXReader
from app.readers.markdown import MarkdownReader
from app.readers.pdf import PDFReader
from app.readers.txt import TXTReader
from app.readers.docx import DOCXReader


class ReaderFactory:
    """
    Creates the appropriate reader based on file extension.
    """

    _READERS: dict[str, Type[DocumentReader]] = {
        ".txt": TXTReader,
        ".md": MarkdownReader,
        ".pdf": PDFReader,
        ".docx": DOCXReader,
    }

    @classmethod
    def create(cls, file_path: Path) -> DocumentReader:
        extension = file_path.suffix.lower()

        reader_class = cls._READERS.get(extension)

        if reader_class is None:
            raise ValueError(
                f"Unsupported document type: {extension}"
            )

        return reader_class()