"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

LLM factory.
"""

from app.llms.base import LLM
from app.llms.fake import FakeLLM
from app.llms.ollama import OllamaLLM
from app.llms.openai import OpenAILLM
from app.models.llm_config import (
    LLMConfig,
    LLMProvider,
)


class LLMFactory:
    """
    Creates LLM instances.
    """

    @staticmethod
    def create(
        config: LLMConfig,
    ) -> LLM:

        if config.provider == LLMProvider.FAKE:
            return FakeLLM()

        if config.provider == LLMProvider.OPENAI:
            return OpenAILLM()

        if config.provider == LLMProvider.OLLAMA:
            return OllamaLLM()

        raise ValueError(
            f"Unsupported LLM provider: {config.provider}"
        )