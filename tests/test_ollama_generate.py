import requests
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")

payload = {
    "model" : "llama3",
    "prompt" : "Summarize what a legal opinion is in one sentence.",
    "stream" : False
}

response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload)

print("Status code: ", response.status_code)

if response.status_code != 200:
    print(response.text)
else:
    data = response.json()
    print(data["response"])