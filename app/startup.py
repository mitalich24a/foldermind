"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Application startup checks.
"""

from pathlib import Path


def ensure_directories() -> None:
    """
    Create required directories if they don't exist.
    """

    directories = [
        Path("data"),
        Path("data/chroma"),
        Path("logs"),
    ]

    for directory in directories:
        directory.mkdir(
            parents=True,
            exist_ok=True,
        )