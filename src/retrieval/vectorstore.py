from chromadb import PersistentClient
from chromadb.utils import embedding_functions
from src.config import settings


class VectorStore:
    def __init__(self, collection_name: str = "documents"):
        self.client = PersistentClient(path=settings.vectorstore_path)
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def add(self, ids, embeddings, metadatas, documents):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=documents,
        )

    def query(self, embedding, n_results: int = 5):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )