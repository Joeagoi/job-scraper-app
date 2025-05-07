# app/scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

# 🔍 Define your keywords
KEYWORDS = [
    "Database Administrator", "SQL", "MySQL", "PostgreSQL", "ETL", "Data Pipeline", "Data","Manager"
]
KEYWORDS = [kw.lower() for kw in KEYWORDS]

BASE_URL = "https://unjobs.org"
TARGET_URL = f"{BASE_URL}/new"

# 🔧 Update this path to your local chromedriver.exe if needed
CHROMEDRIVER_PATH = "chromedriver.exe"  # or just "chromedriver" if in PATH

def fetch_jobs(max_pages=10):
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    #driver = uc.Chrome()

    results = []

    for page_num in range(1, max_pages + 1):
        page_url = f"{BASE_URL}/new/{page_num}"
        print(f"Opening {page_url} in browser...")
        driver.get(page_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "job"))
)
        #time.sleep(2)  # Let JS run

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        #job_rows = soup.select("table.joblist tr.job")
        job_rows = soup.select("div.job")

        if not job_rows:
            print(f"No jobs found on page {page_num}. Stopping.")
            break

        for job in job_rows:
            title_elem = job.find("a", class_="jtitle")
            if not title_elem:
                continue            

            title = title_elem.text.strip()
            url = title_elem["href"]
            location = "N/A"

            # Sometimes location might be inferred from title
            
            if "," in title:
                parts = title.split(",")
                if len(parts) > 1:
                    location = parts[-1].strip()

            if any(keyword in title.lower() for keyword in KEYWORDS):
                results.append({
                    "title": title,
                    "url": url,
                    "location": location
                })

    driver.quit()
    return results


'''
def fetch_jobs():
    # Configure Selenium
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no browser window)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    print(f"Opening {TARGET_URL} in browser...")
    driver.get(TARGET_URL)

    # Let the page fully load
    time.sleep(2)

    # Get page source after JavaScript runs
    html = driver.page_source
    driver.quit()

    # Use BeautifulSoup to parse content
    soup = BeautifulSoup(html, "html.parser")
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

        # Filter by keywords
        if any(keyword in title.lower() for keyword in KEYWORDS):
            results.append({
                "title": title,
                "url": url,
                "location": location
            })

    return results

'''
if __name__ == "__main__":
    jobs = fetch_jobs()
    print(f"\nFound {len(jobs)} matching jobs:\n")
    for job in jobs:
        print(f"- {job['title']} ({job['location']})")
        print(f"  {job['url']}\n")
