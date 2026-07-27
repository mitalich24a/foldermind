"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Base model for embeddable content.
"""

from abc import ABC, abstractmethod


class Embeddable(ABC):
    """
    Base class for embeddable models.
    """

    @property
    @abstractmethod
    def text(self) -> str:
        """
        Text to embed.
        """
        pass