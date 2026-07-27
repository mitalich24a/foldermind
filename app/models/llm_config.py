"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

LLM configuration.
"""

from enum import Enum

from pydantic import BaseModel


class LLMProvider(str, Enum):
    """
    Supported LLM providers.
    """

    FAKE = "fake"
    OPENAI = "openai"
    OLLAMA = "ollama"


class LLMConfig(BaseModel):
    """
    LLM configuration.
    """

    provider: LLMProvider = LLMProvider.FAKE
    model: str = "gpt-4.1-mini"