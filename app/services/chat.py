"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Chat service.
"""

from app.llms.factory import LLMFactory

from app.config.settings import settings
from app.models.llm_config import (
    LLMConfig,
    LLMProvider,
)
from app.models.query import Query
from app.models.retriever_config import RetrieverConfig
from app.prompts.factory import PromptBuilderFactory
from app.services.retriever import RetrieverService


class ChatService:
    """
    Orchestrates the RAG pipeline.
    """

    def __init__(self):

        self.retriever = RetrieverService(
            RetrieverConfig(),
        )

        self.prompt_builder = (
            PromptBuilderFactory.create()
        )

        self.llm = self.llm = LLMFactory.create(
                    LLMConfig(
                        provider=LLMProvider(
                            settings.llm_provider,
                        ),
                        model=settings.llm_model,
                    )
            )

    def chat(
        self,
        query: Query,
    ) -> str:

        results = self.retriever.retrieve(
            query,
        )

        prompt = self.prompt_builder.build(
            query,
            results,
        )

        print("=" * 80)
        print(prompt)
        print("=" * 80)

        return self.llm.generate(
            prompt,
        )