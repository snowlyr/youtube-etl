from dotenv import load_dotenv
import os
import requests
import pandas as pd
import json
from datetime import datetime
from pathlib import Path

# Declaring Environment/Config Variables
load_dotenv()
YT_API_KEY = os.getenv("YT_API_KEY")
MAX_RESULTS = 50

# Declaring Functions & Helper Functions
def fetch_youtube_trending(api_key, region_code='US', max_results=MAX_RESULTS):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={region_code}&maxResults={max_results}&key={api_key}"
    response = requests.get(url)
    return response.json()

def extract_data(api_key, regions=['US', 'GB', 'DE', 'FR', 'CA']):
    all_data = []
    for region in regions:
        data = fetch_youtube_trending(api_key, region)
        data['region'] = region
        data['extracted_at'] = datetime.now().isoformat()
        all_data.append(data)

    # Save raw data
    raw_path = Path('data/raw') / f"youtube_trending_{datetime.now().strftime('%Y%m%d')}.json"
    with open(raw_path, 'w') as f:
        json.dump(all_data, f)

    return raw_path

