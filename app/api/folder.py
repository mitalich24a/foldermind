"""
FolderMind
Copyright (c) 2026 Mitali Choubisa.
All rights reserved.

Folder API.
"""

from fastapi import APIRouter

from app.models.folder_request import FolderRequest
from app.models.folder_response import FolderResponse
from app.services.folder import FolderService

router = APIRouter()


@router.post(
    "/folder",
    response_model=FolderResponse,
)
def add_folder(
    request: FolderRequest,
) -> FolderResponse:
    FolderService().add_folder(
        request.path,
    )

    return FolderResponse(
        message="Folder indexed successfully.",
    )