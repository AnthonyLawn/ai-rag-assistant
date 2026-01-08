import os
import tempfile
from fastapi import UploadFile, File, APIRouter
from ingestion.loaders import load_pdf, load_text
from ingestion.chunking import chunk_text
from ingestion.indexing import index_documents
from pydantic import BaseModel
from llm.generator import answer_query

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    k: int = 5


@router.post("/query")
async def query_endpoint(payload: QueryRequest):
    """
    Accepts a user query, runs the full RAG pipeline,
    and returns the LLM-generated answer.
    """
    answer = answer_query(payload.query, k=payload.k)
    return {"answer": answer}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    suffix = os.path.splitext(file.filename)[1]

    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        # Load based on type
        if suffix.lower() == ".pdf":
            doc = load_pdf(tmp_path)
        else:
            doc = load_text(tmp_path)

        # Chunk
        chunks = chunk_text(doc)

        # Index
        index_documents(chunks)

        return {"status": "ok", "chunks_indexed": len(chunks)}

    finally:
        # Always delete the temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)