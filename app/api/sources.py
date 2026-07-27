"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from fastapi import APIRouter, HTTPException

from app.models.source import SourceConfig
from app.sources.factory import SourceFactory

from app.models.local import LocalSourceConfig

from app.services.ingestion import IngestionService

from app.readers.factory import ReaderFactory
from app.services.embedding import EmbeddingService

from app.models.embedding_config import (
    EmbeddingConfig,
    EmbeddingProvider,
)

from app.models.vectorstore_config import (
    VectorStoreConfig,
    VectorStoreProvider,
)
from app.services.vectorstore import (
    VectorStoreService,
)

router = APIRouter(
    prefix="/sources",
    tags=["Sources"],
)


@router.post("/register")
def register_source(config: LocalSourceConfig):
    try:
        source = SourceFactory.create(
            config.source_type,
            config.config.model_dump(),
        )

        source.validate()

        return {
            "message": "Source validated successfully."
        }

    except FileNotFoundError as ex:
        raise HTTPException(
            status_code=404,
            detail=str(ex),
        )

    except NotADirectoryError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )

@router.post("/discover")
def discover_documents(config: LocalSourceConfig):
    try:
        source = SourceFactory.create(
            config.source_type,
            config.config.model_dump(),
        )

        source.validate()

        return source.discover_documents()

    except FileNotFoundError as ex:
        raise HTTPException(
            status_code=404,
            detail=str(ex),
        )

    except NotADirectoryError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )

@router.post("/read")
def read_documents(config: LocalSourceConfig):
    try:
        ingestion_service = IngestionService()
        embedding_service = EmbeddingService(
                EmbeddingConfig(
                    provider=EmbeddingProvider.FAKE,
                )
            )
        vectorstore_service = VectorStoreService(
                VectorStoreConfig(
                    provider=VectorStoreProvider.MEMORY,
                )
            )
        chunks = ingestion_service.read(config)
        embeddings = embedding_service.embed(chunks)
        vectorstore_service.upsert(embeddings)

        return list(embeddings)

    except FileNotFoundError as ex:
        raise HTTPException(
            status_code=404,
            detail=str(ex),
        )

    except NotADirectoryError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )

    except ValueError as ex:
        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )