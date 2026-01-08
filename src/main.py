from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from src.api.routes import router as api_router

app = FastAPI()

# Serve the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
def serve_index():
    return FileResponse("static/index.html")

# Include your API routes
app.include_router(api_router)