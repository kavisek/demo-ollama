from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "demo-ollama"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3.5"


settings = Settings()
