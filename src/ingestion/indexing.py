from src.ingestion.embedder import Embedder
from src.retrieval.vectorstore import VectorStore


def index_documents(chunks):
    embedder = Embedder()
    vectorstore = VectorStore()

    embeddings = embedder.embed([c["text"] for c in chunks])

    ids = [c["id"] for c in chunks]
    metadatas = [{"source": c["source"]} for c in chunks]
    documents = [c["text"] for c in chunks]

    vectorstore.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents,
    )