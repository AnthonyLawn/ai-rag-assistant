from fastembed import TextEmbedding
from typing import List
from src.config import settings


class Embedder:
    def __init__(self, model_name: str = settings.default_embedding_model):
        self.model = TextEmbedding(model_name)

    def embed(self, texts: List[str]) -> List[List[float]]:
        return list(self.model.embed(texts))