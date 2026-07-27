"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Prompt builder factory.
"""

from app.prompts.base import PromptBuilder
from app.prompts.default import DefaultPromptBuilder


class PromptBuilderFactory:

    @staticmethod
    def create() -> PromptBuilder:
        return DefaultPromptBuilder()