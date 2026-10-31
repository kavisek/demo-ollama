# demo-ollama

Run local LLMs with [Ollama](https://ollama.com), either in the terminal or through a browser chat page served by FastAPI.

## Requirements

- [Ollama](https://ollama.com/download), running on `http://localhost:11434`
- [uv](https://docs.astral.sh/uv/) for the Python app (Python 3.12+)
- Docker, only if you run Ollama in a container

## Quick start

Start the web chat UI:

```bash
make start
```

Then open http://localhost:8080.

`make start` pulls the default model, `qwen3.5` (about 6.6 GB), if it is not installed yet, then starts the FastAPI dev server on port 8080 with auto-reload. Later runs skip the download.

To use a different model, pass `MODEL`:

```bash
make start MODEL=qwen3.8:27b
```

You can also switch between any installed model from the dropdown on the page.

## Make targets

| Target | What it does |
| --- | --- |
| `make start` | Pulls `MODEL` and starts the web chat UI on `PORT` (default 8080). |
| `make pull` | Pulls `MODEL` (default `qwen3.5`) with `ollama pull`. |
| `make run` | Starts a terminal chat with `deepseek-r1:1.5b`. |

## Web chat UI

The page streams replies as the model generates them. For reasoning models such as `qwen3.5` and `deepseek-r1`, the model's thinking appears in a collapsible **Thinking** section above the answer. Select **New chat** to clear the conversation.

### Configuration

The app reads these environment variables, or a `.env` file in the repo root. Copy `.env.example` to get started.

| Variable | Default | Description |
| --- | --- | --- |
| `OLLAMA_URL` | `http://localhost:11434` | Address of the Ollama server. |
| `OLLAMA_MODEL` | `qwen3.5` | Model selected when the page loads. `make start` sets this from `MODEL`. |

### API

| Method and path | Description |
| --- | --- |
| `GET /` | The chat page. |
| `GET /api/models` | The default model and all installed models. Returns 503 if Ollama is not running. |
| `POST /api/chat` | Streams a reply as NDJSON. Body: `{"model": "qwen3.5", "messages": [{"role": "user", "content": "Hi"}]}`. `model` is optional. |
| `GET /health` | Liveness check. |
| `GET /docs` | Interactive API docs. |

### Project layout

```
src/app/
  main.py            # create_app(), lifespan (shared httpx client), page and health routes
  config.py          # Settings (OLLAMA_URL, OLLAMA_MODEL)
  dependencies.py    # OllamaDep: the shared httpx client
  chat/
    router.py        # /api/models and /api/chat
    schemas.py       # request and response models
    service.py       # calls the Ollama API and streams the reply
  static/index.html  # the chat page
```

## Terminal chat

Start a conversation in the terminal:

```bash
ollama run qwen3.5
```

End the conversation with:

```bash
/bye
```

## Ollama in Docker

To run Ollama in a container, start the server, then open a conversation inside it:

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run qwen3.5
```

The container publishes port 11434, so `make start` works against it too.

## Models

Browse all models at https://ollama.com/search.

### Qwen

```bash
ollama run qwen3.5
# Model Size: 6.6GB

ollama run qwen3.8:27b
# Model Size: 17GB

ollama run qwen2.5:3b
```

### DeepSeek

```bash
# These models will run quickly on an M3 Max with 128 GB of RAM.

ollama run deepseek-r1:1.5b
# Model Size: 1.1GB
# RAM Usage: 1.1GB
# CPU Usage: 55%

ollama run deepseek-r1:7b
# Model Size: 4.7GB
# RAM Usage: 1.27 GB
# CPU Usage: 4%

ollama run deepseek-r1:8b
# Model Size: 5GB
# RAM Usage: 1.27 GB
# CPU Usage: 4%

ollama run deepseek-r1:14b
# Model Size: 7GB
# RAM Usage: 1.74 GB
# CPU Usage: 3%

ollama run deepseek-r1:32b
# Model Size: 19GB
# RAM Usage: 2.3GB
# CPU Usage: 3%

ollama run deepseek-r1:70b
# Model Size: 2.77GB
# RAM Usage: 2.3GB
# CPU Usage: 3%
```

### Vision models

Vision models on Ollama can read images. They can do the following without any extra setup:

- Optical character recognition (OCR)
- Interpreting charts and tables
- Answering questions about an image
- Reading handwriting

```bash
ollama run llama3.2-vision
# Model Size: 6GB

>>> What's in this image? ./images/lava.jpg
Added image './images/lava.jpg'
 The image you've provided appears to show an erupting volcano with lava flowing down the mountain. The background is dark, suggesting it may be nighttime or
early morning, and there are smoke and steam rising from the eruption. Additionally, the ground around the eruption looks to be covered in snow or ice, which
contrasts with the hot, molten lava from the volcano.
```

The web chat UI is text only. Use the terminal for images.
