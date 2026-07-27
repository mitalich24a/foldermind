"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Ollama LLM.
"""

from ollama import Client

from app.config.settings import settings
from app.llms.base import LLM


class OllamaLLM(LLM):
    """
    Ollama LLM implementation.
    """

    def __init__(self):
        self.client = Client()

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat(
            model=settings.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]