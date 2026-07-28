"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for CSV documents.
"""

import csv
from pathlib import Path

from app.models.document import Document
from app.readers.base import DocumentReader


class CSVReader(DocumentReader):
    """
    Reader for CSV files.
    """

    def read(self, document: Document) -> str:
        path = Path(document.path)

        rows = []

        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.reader(file)

            for row in reader:
                rows.append(", ".join(row))

        return "\n".join(rows)