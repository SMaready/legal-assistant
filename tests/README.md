# Tests

This folder contains small verification scripts for local development.

## Ollama Tests

### test_ollama_generate.py

Checks that the local Ollama REST API can generate text using `llama3`.

Run from the project root:

python3 tests/test_ollama_generate.py

Expected result:

- Status code: 200
- A short generated response about legal opinions

### test_ollama_embed.py

Checks that the local Ollama REST API can generate embeddings using `nomic-embed-text`.

Run from the project root:

python3 tests/test_ollama_embed.py

Expected result:

- Status code: 200
- Embedding length: 768
- First 10 embedding values printed

## Requirements

Ollama must be installed and running locally.

Required models:

ollama pull llama3
ollama pull nomic-embed-text