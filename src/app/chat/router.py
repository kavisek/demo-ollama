from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse

from app.chat import service
from app.chat.schemas import ChatRequest, ModelsRead
from app.config import settings
from app.dependencies import OllamaDep

router = APIRouter()


@router.get("/models", response_model=ModelsRead)
async def get_models(client: OllamaDep) -> ModelsRead:
    try:
        models = await service.list_models(client)
    except service.OllamaUnavailable as exc:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "Ollama is not running") from exc
    return ModelsRead(default=settings.ollama_model, models=models)


@router.post("/chat")
async def chat(payload: ChatRequest, client: OllamaDep) -> StreamingResponse:
    model = payload.model or settings.ollama_model
    return StreamingResponse(
        service.stream_chat(client, model, payload.messages),
        media_type="application/x-ndjson",
    )
