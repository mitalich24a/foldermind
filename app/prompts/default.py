"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Default prompt builder.
"""

from app.models.query import Query
from app.models.search_result import SearchResult
from app.prompts.base import PromptBuilder


class DefaultPromptBuilder(PromptBuilder):
    """
    Default RAG prompt.
    """

    def build(
        self,
        query: Query,
        results: list[SearchResult],
    ) -> str:

        context = "\n\n".join(
            result.chunk.content
            for result in results
        )

        return f"""Answer the question using only the provided context.

Context:
{context}

Question:
{query.text}

Answer:
"""