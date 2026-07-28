"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for JSON documents.
"""

import json
from pathlib import Path

from app.models.document import Document
from app.readers.base import DocumentReader


class JSONReader(DocumentReader):
    """
    Reader for JSON files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )