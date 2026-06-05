# Legal Assistant

A Qt/C++ legal assistant application with a Python agent backend for legal data ingestion, retrieval, and LLM-based analysis.

## Project Structure

- `src/` - Qt/C++ application source code
- `agent/` - Python agent, data ingestion, and future retrieval/LLM logic
- `agent/data/` - CourtListener dataset scripts and sample data
- `scripts/` - helper scripts
- `tests/` - tests

## Python Agent Setup

From the project root:

1. Create a virtual environment:

python3 -m venv .venv

2. Activate the virtual environment:

source .venv/bin/activate

3. Install Python dependencies:

pip install -r agent/requirements.txt

4. Create a local `.env` file:

cp .env.example .env

5. Add your CourtListener API token inside `.env`:

TOKEN=your_actual_courtlistener_token_here

Do not commit `.env`.

## CourtListener Data Ingestion

The ingestion script downloads 100 contract-law related CourtListener search results using the query:

"breach of contract"

Run:

python3 agent/data/ingest.py

Output file:

agent/data/courtlistener_contract_opinions.jsonl

## Ollama Setup

Install Ollama locally, then pull the required models:

ollama pull llama3
ollama pull nomic-embed-text

Verify the Ollama API is running:

curl http://localhost:11434/api/tags

Verify llama3 text generation:

curl http://localhost:11434/api/generate -d '{"model":"llama3","prompt":"Summarize what a legal opinion is in one sentence.","stream":false}'

Verify embeddings:

curl http://localhost:11434/api/embeddings -d '{"model":"nomic-embed-text","prompt":"This case is about breach of contract and damages."}'

## Week 1 Partner Work Completed

- Python virtual environment setup documented
- Python requirements added
- CourtListener contract-law ingestion script added
- 100-row contract-law JSONL sample dataset added
- Ollama llama3 REST API verified
- Ollama nomic-embed-text REST API verified
- Databricks raw Delta table created manually from the JSONL dataset