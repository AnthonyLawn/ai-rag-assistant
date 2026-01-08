from groq import Groq
from ..config import settings

class LLMGenerator:
    def generate(self, prompt: str):
        raise NotImplementedError


class GroqLLM(LLMGenerator):
    def __init__(self, model_name: str = "llama3-8b-8192"):
        self.client = Groq(api_key=settings.groq_api_key)
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message["content"]