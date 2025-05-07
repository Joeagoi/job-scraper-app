# app/scraper.py

import requests
from bs4 import BeautifulSoup

# Define your keywords
KEYWORDS = [
    "Database Administrator", "SQL", "MySQL", "PostgreSQL", "ETL", "Data Pipeline", "Data"
]

# Convert keywords to lowercase for easier matching
KEYWORDS = [kw.lower() for kw in KEYWORDS]

#BASE_URL = "https://unjobs.org"
BASE_URL = "https://www.unep.org"
TARGET_URL = f"{BASE_URL}/work-with-us"

def fetch_jobs():
    print(f"Fetching jobs from {TARGET_URL}...")
    #response = requests.get(TARGET_URL)
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    response = requests.get(TARGET_URL, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch jobs: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_rows = soup.select("div#content div.job")
    results = []

    for job in job_rows:
        title_elem = job.find("a")
        location_elem = job.select_one("span.location")
        
        if not title_elem:
            continue
        
        title = title_elem.text.strip()
        url = BASE_URL + title_elem["href"]
        location = location_elem.text.strip() if location_elem else "N/A"

        # Keyword filtering
        if any(keyword in title.lower() for keyword in KEYWORDS):
            results.append({
                "title": title,
                "url": url,
                "location": location,
            })

    return results


if __name__ == "__main__":
    jobs = fetch_jobs()
    print(f"\nFound {len(jobs)} matching jobs:\n")
    for job in jobs:
        print(f"- {job['title']} ({job['location']})")
        print(f"  {job['url']}\n")
