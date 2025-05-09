import requests
import os
from dotenv import load_dotenv
from app.models import db, Job
from flask import Flask
from config import Config

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

COUNTRY = "gb"
MAX_PAGES = 2

KEYWORDS = [
    "Database Administrator", "SQL", "MySQL", "PostgreSQL", "ETL", "Data Pipeline", "Data"
]
KEYWORDS = [kw.lower() for kw in KEYWORDS]

API_URL = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search"

# Initialize Flask app to use DB
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def fetch_jobs():
    all_jobs = []

    for page in range(1, MAX_PAGES + 1):
        print(f"\nFetching page {page}...")

        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": "data"
        }

        response = requests.get(f"{API_URL}/{page}", params=params)
        print(f"→ Request URL: {response.url}")
        if response.status_code != 200:
            print(f"❌ Error {response.status_code}: {response.text}")
            continue

        jobs = response.json().get("results", [])

        for job in jobs:
            title = job.get("title", "")
            if not any(kw in title.lower() for kw in KEYWORDS):
                continue

            job_data = {
                "title": title,
                "company": job.get("company", {}).get("display_name", "Unknown"),
                "location": job.get("location", {}).get("display_name", "Unknown"),
                "url": job.get("redirect_url", "N/A")
            }

            all_jobs.append(job_data)

    return all_jobs


if __name__ == "__main__":
    jobs = fetch_jobs()
    print(f"\n✅ Found {len(jobs)} matching jobs:\n")
    
    with app.app_context():
        db.create_all()  # ensure table exists

        new_jobs = 0
        for job in jobs:
            if not Job.query.filter_by(url=job["url"]).first():
                db.session.add(Job(**job))
                new_jobs += 1
        db.session.commit()

        print(f"✅ Inserted {new_jobs} new job(s) into the database.\n")

    for job in jobs:
        print(f"- {job['title']} ({job['company']}, {job['location']})")
        print(f"  {job['url']}\n")
