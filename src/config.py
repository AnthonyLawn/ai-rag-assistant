from pydantic import BaseSettings

class Settings(BaseSettings):
    groq_api_key: str | None = None
    vectorstore_path: str = "data/vectorstore"

    class Config:
        env_file = ".env"

settings = Settings()