"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for XML documents.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

from app.models.document import Document
from app.readers.base import DocumentReader


class XMLReader(DocumentReader):
    """
    Reader for XML files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        tree = ET.parse(path)
        root = tree.getroot()

        lines = []

        for element in root.iter():
            if element.text and element.text.strip():
                lines.append(
                    f"{element.tag}: {element.text.strip()}"
                )

        return "\n".join(lines)