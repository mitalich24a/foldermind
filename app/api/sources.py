"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.
"""

from fastapi import APIRouter, HTTPException

from app.models.source import SourceConfig
from app.sources.factory import SourceFactory

from app.models.local import LocalSourceConfig

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
