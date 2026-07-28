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
from app.readers.markdown import MarkdownReader
from app.readers.csv import CSVReader
from app.readers.json import JSONReader
from app.readers.xml import XMLReader
from app.readers.html import HTMLReader
from app.readers.xlsx import XLSXReader
from app.readers.pptx import PPTXReader


class ReaderFactory:
    """
    Creates the appropriate reader based on file extension.
    """

    _READERS: dict[str, Type[DocumentReader]] = {
        ".txt": TXTReader,
        ".md": MarkdownReader,
        ".pdf": PDFReader,
        ".docx": DOCXReader,
        ".md": MarkdownReader,
        ".csv": CSVReader,
        ".json": JSONReader,
        ".xml": XMLReader,
        ".html": HTMLReader,
        ".htm": HTMLReader,
        ".xlsx": XLSXReader,
        ".pptx": PPTXReader,
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