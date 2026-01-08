def build_prompt(query: str, context: str) -> str:
    return f"Context:\n{context}\n\nQuery:\n{query}"