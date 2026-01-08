from typing import Dict
from pypdf import PdfReader


def load_pdf(file_path: str) -> Dict:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return {
        "id": file_path,
        "text": text,
        "source": file_path
    }


def load_text(file_path: str) -> Dict:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return {
        "id": file_path,
        "text": text,
        "source": file_path
    }