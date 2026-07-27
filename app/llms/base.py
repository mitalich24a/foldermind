"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

LLM interface.
"""

from abc import ABC, abstractmethod


class LLM(ABC):
    """
    Large Language Model interface.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        pass