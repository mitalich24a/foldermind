from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.models.query import Query
from app.services.chat import ChatService

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest) -> ChatResponse:

    service = ChatService()

    answer = service.chat(
        Query(text=request.text),
    )

    return ChatResponse(
        answer=answer,
    )