from groq import Groq
from ..config import settings
from .models import GROQ_DEFAULT_MODEL
from llm.prompts import build_prompt
from retrieval.search import retrieve

class LLMGenerator:
    def generate(self, prompt: str):
        raise NotImplementedError


class GroqLLM(LLMGenerator):
    def __init__(self, model_name: str = GROQ_DEFAULT_MODEL):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message["content"]


def answer_query(query: str, k: int = 5) -> str:
    """
    Full RAG pipeline:
    1. Retrieve top-k relevant chunks
    2. Build a prompt with context + query
    3. Call the Groq LLM
    4. Return the answer
    """

    # 1. Retrieve relevant chunks
    results = retrieve(query, k=k)

    # Chroma returns nested lists: documents[0] is the list of chunk texts
    documents = results["documents"][0]

    # 2. Build context string
    context = "\n\n".join(documents)

    # 3. Build final prompt
    prompt = build_prompt(query=query, context=context)

    # 4. Call LLM
    llm = GroqLLM()
    answer = llm.generate(prompt)

    return answer
