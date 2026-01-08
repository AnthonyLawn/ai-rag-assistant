from src.ingestion.embedder import Embedder
from src.retrieval.vectorstore import VectorStore


def retrieve(query: str, k: int = 5):
    embedder = Embedder()
    vectorstore = VectorStore()

    query_embedding = embedder.embed([query])[0]

    results = vectorstore.query(query_embedding, n_results=k)

    return results