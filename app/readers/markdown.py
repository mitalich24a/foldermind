"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Reader for Markdown documents.
"""

from app.readers.base import DocumentReader


class MarkdownReader(DocumentReader):
    """
    Reader for Markdown files.
    """

    def read(self, document) -> str:
        raise NotImplementedError("Markdown reader not implemented yet.")