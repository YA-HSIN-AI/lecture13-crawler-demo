import requests
import time
import os
import json

# URL to crawl
URL = "https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-A0010-001?Authorization=CWA-777A875C-4258-446E-AD60-3B06160B5F80&downloadType=WEB&format=JSON"

# Output folder
OUT_DIR = "weather_data"
os.makedirs(OUT_DIR, exist_ok=True)

def fetch_data(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

def save_json(data, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {filename}")

def main():
    print("📡 Crawling:", URL)
    data = fetch_data(URL)

    if data:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(OUT_DIR, f"weather_{timestamp}.json")
        save_json(data, filename)

if __name__ == "__main__":
    main()