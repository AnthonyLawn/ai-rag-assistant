class VectorStore:
    def add(self, embeddings, metadata):
        raise NotImplementedError

    def search(self, query_embedding, top_k: int = 5):
        raise NotImplementedError