"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Fake LLM.
"""

from app.llms.base import LLM


class FakeLLM(LLM):

    def generate(
        self,
        prompt: str,
    ) -> str:

        return "Fake response."