"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for HTML documents.
"""

from pathlib import Path

from bs4 import BeautifulSoup

from app.models.document import Document
from app.readers.base import DocumentReader


class HTMLReader(DocumentReader):
    """
    Reader for HTML files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        html = path.read_text(
            encoding="utf-8"
        )

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        return soup.get_text(
            separator="\n",
            strip=True,
        )