from typing import List, Dict


def chunk_text(
    doc: Dict,
    chunk_size: int = 500,
    overlap: int = 100
) -> List[Dict]:
    """
    Splits a document into overlapping chunks suitable for embedding.

    Args:
        doc: A dict with keys {id, text, source}
        chunk_size: Number of characters per chunk
        overlap: Number of characters to overlap between chunks

    Returns:
        List of chunk dicts with keys {id, text, source}
    """

    text = doc["text"]
    chunks = []

    start = 0
    doc_id = doc["id"]

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]

        chunk_id = f"{doc_id}_{start}"

        chunks.append({
            "id": chunk_id,
            "text": chunk_text,
            "source": doc["source"]
        })

        # Move forward with overlap
        start += chunk_size - overlap

    return chunks