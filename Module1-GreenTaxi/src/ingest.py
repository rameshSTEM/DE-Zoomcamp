import os
import requests

URLS = [
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet",
    "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv",
]

BATCH_SIZE = 1          # simulate batch ingestion
DATA_DIR = "data/raw"
TIMEOUT = 30


def download_file(url):
    os.makedirs(DATA_DIR, exist_ok=True)
    filename = url.split("/")[-1]
    file_path = os.path.join(DATA_DIR, filename)

    # idempotency: skip if already exists
    if os.path.exists(file_path):
        print(f"Skipping (already exists): {filename}")
        return

    print(f"Downloading: {filename}")

    with requests.get(url, stream=True, timeout=TIMEOUT) as r:
        r.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    print(f"Saved: {file_path}")


def main():
    for i in range(0, len(URLS), BATCH_SIZE):
        batch = URLS[i:i + BATCH_SIZE]
        print(f"\nProcessing batch {i // BATCH_SIZE + 1}")

        for url in batch:
            download_file(url)


if __name__ == "__main__":
    main()
