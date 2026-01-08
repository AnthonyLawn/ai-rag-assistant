from fastapi import FastAPI
from .routes import router

app = FastAPI(title="AI RAG Assistant")
app.include_router(router)