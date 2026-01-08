from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    groq_api_key: str | None = None
    vectorstore_path: str = "data/vectorstore"
    default_embedding_model: str = "BAAI/bge-small-en-v1.5"

    class Config:
        env_file = ".env"

settings = Settings()