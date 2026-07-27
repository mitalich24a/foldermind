"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

OpenAI LLM.
"""

from openai import OpenAI
from openai import OpenAI, OpenAIError

from app.config.settings import settings
from app.llms.base import LLM


class OpenAILLM(LLM):
    """
    OpenAI LLM implementation.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openai_api_key,
        )

    def generate(
    self,
    prompt: str,
) -> str:

        try:
            response = self.client.responses.create(
                model=settings.llm_model,
                input=prompt,
            )

            return response.output_text

        except OpenAIError as e:
            raise RuntimeError(
                f"OpenAI request failed: {e}"
            ) from e