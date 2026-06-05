import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

if not token:
	raise ValueError("TOKEN not found. Make sure your .env file has TOKEN=your_api_token")

url = "https://www.courtlistener.com/api/rest/v4/search/"

headers = {
	"Authorization": f"Token {token}"
}

params = {
	"q": '"breach of contract"',
	"type": "o",
	"page_size": 20
}

target_rows = 100
all_results = []
next_url = url

while next_url and len(all_results) < target_rows:
	response = requests.get(
		next_url,
		headers=headers,
		params=params if next_url == url else None
	)

	print("Status code:", response.status_code)

	if response.status_code == 429:
		print("Rate limited. Waiting 60 seconds...")
		time.sleep(60)
		continue

	if response.status_code != 200:
		print(response.text)
		break

	data = response.json()
	results = data.get("results", [])

	all_results.extend(results)
	print("Total rows collected:", len(all_results))

	next_url = data.get("next")

	if next_url and len(all_results) < target_rows:
		time.sleep(13)

all_results = all_results[:target_rows]

output_path = os.path.join(os.path.dirname(__file__), "courtlistener_contract_opinions.jsonl")
with open(output_path, "w", encoding="utf-8") as f:
	for item in all_results:
		record = {
			"id": item.get("id"),
			"cluster_id": item.get("cluster_id"),
			"case_name": item.get("caseName"),
			"court": item.get("court"),
			"date_filed": item.get("dateFiled"),
			"absolute_url": "https://www.courtlistener.com" + item.get("absolute_url", ""),
			"snippet": item.get("snippet"),
			"plain_text": item.get("plain_text") or item.get("text"),
			"practice_area": "contract_law"
		}

		f.write(json.dumps(record, ensure_ascii=False) + "\n")

print("Saved rows:", len(all_results))
print(f"Saved to {output_path}")