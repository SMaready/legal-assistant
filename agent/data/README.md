# Data Ingestion

This folder contains the CourtListener data ingestion script and the sample contract-law dataset used for the legal assistant project.

## Files

### ingest.py

Downloads contract-law related opinions from the CourtListener API using the search endpoint.

Current search query:

"breach of contract"

### courtlistener_contract_opinions.jsonl

A 100-row JSON Lines dataset generated from CourtListener search results for breach-of-contract related cases.

Each row contains these fields:

- id
- cluster_id
- case_name
- court
- date_filed
- absolute_url
- snippet
- plain_text
- practice_area

## Environment Variables

The ingestion script requires a CourtListener API token stored in a local .env file at the project root.

Example .env:

TOKEN=your_courtlistener_api_token_here

Do not commit the real .env file.

## How to Run

From the project root:

1. Activate the virtual environment(need to create venv first : python3 -m venv .venv):

source .venv/bin/activate

2. Run the ingestion script:

python3 agent/data/ingest.py

The script writes the output file to:

agent/data/courtlistener_contract_opinions.jsonl

## Notes

The script includes delays between API requests to avoid CourtListener rate limits.

The current dataset contains metadata/search results for contract-law related cases. Some rows may not include full plain_text because the CourtListener search endpoint does not always return full opinion text.

Later, Week 2 will use this dataset for chunking, embeddings, and semantic search.