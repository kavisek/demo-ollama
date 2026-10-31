.PHONY: run pull start

MODEL ?= qwen3.5
PORT ?= 8080

run:
	ollama run deepseek-r1:1.5b

pull:
	ollama pull $(MODEL)

start: pull
	OLLAMA_MODEL=$(MODEL) uv run fastapi dev src/app/main.py --port $(PORT)
