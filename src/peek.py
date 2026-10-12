import json
import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENFDA_API_KEY")

URL = "https://api.fda.gov/drug/event.json"

params = {"limit": 5}
if API_KEY:
    params["api_key"] = API_KEY

response = httpx.get(URL, params=params, timeout=60)
response.raise_for_status()
reports = response.json()["results"]

print(f"{len(reports)} meldingen opgehaald\n")
print(json.dumps(reports[0], indent=2))

json.dump(reports, open("drills/sample.json", "w"))
