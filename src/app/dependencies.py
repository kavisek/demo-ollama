from typing import Annotated

import httpx
from fastapi import Depends, Request


def get_ollama_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.ollama


OllamaDep = Annotated[httpx.AsyncClient, Depends(get_ollama_client)]
