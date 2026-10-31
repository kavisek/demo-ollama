from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.chat.router import router as chat_router
from app.config import settings

STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # One shared client for all Ollama calls; no read timeout so long generations can stream.
    app.state.ollama = httpx.AsyncClient(
        base_url=settings.ollama_url, timeout=httpx.Timeout(10.0, read=None)
    )
    yield
    await app.state.ollama.aclose()


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.include_router(chat_router, prefix="/api", tags=["chat"])

    @app.get("/", include_in_schema=False)
    async def index() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
