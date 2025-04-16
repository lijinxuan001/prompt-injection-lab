
import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def query_model(prompt: str) -> str:
    response = requests.post(
        OLLAMA_API_URL,
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
        timeout=60
    )
    response.raise_for_status()
    return response.json()["response"]
