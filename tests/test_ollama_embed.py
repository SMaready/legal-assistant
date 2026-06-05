import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

payload = {
    "model" : "nomic-embed-text",
    "prompt" : "This case is about breach of contract and damages"
}

response = requests.post(f"{OLLAMA_URL}/api/embeddings", json=payload)

print("Status code: ", response.status_code)

if response.status_code != 200:
    print(response.text)
else:
    data = response.json()
    embedding = data["embedding"]
    
    print("Embedding length: ", len(embedding))
    print("first 10 values: ", embedding[:10])