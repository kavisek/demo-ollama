import json
from collections.abc import AsyncIterator

import httpx

from app.chat.schemas import Message


class OllamaUnavailable(Exception):
    pass


async def list_models(client: httpx.AsyncClient) -> list[str]:
    try:
        response = await client.get("/api/tags")
        response.raise_for_status()
    except httpx.HTTPError as exc:
        raise OllamaUnavailable(str(exc)) from exc
    return [m["name"] for m in response.json().get("models", [])]


async def stream_chat(
    client: httpx.AsyncClient, model: str, messages: list[Message]
) -> AsyncIterator[str]:
    """Yield NDJSON lines of {"content", "thinking"} deltas, ending with {"done": true}."""
    payload = {"model": model, "messages": [m.model_dump() for m in messages], "stream": True}
    try:
        async with client.stream("POST", "/api/chat", json=payload) as response:
            if response.status_code != 200:
                body = await response.aread()
                error = json.loads(body).get("error", body.decode()) if body else "error"
                yield json.dumps({"error": error}) + "\n"
                return
            async for line in response.aiter_lines():
                if not line:
                    continue
                chunk = json.loads(line)
                message = chunk.get("message", {})
                yield (
                    json.dumps(
                        {
                            "content": message.get("content", ""),
                            "thinking": message.get("thinking", ""),
                            "done": chunk.get("done", False),
                        }
                    )
                    + "\n"
                )
    except httpx.HTTPError as exc:
        yield json.dumps({"error": f"Could not reach Ollama: {exc}"}) + "\n"
