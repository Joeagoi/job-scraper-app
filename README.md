# 🌍 Job Scraper App for Database/Data Engineer Roles

This is a basic job scraping application that scans job listing websites (starting with [unjobs.org](https://unjobs.org)) for roles related to **Database Administration**, **Data Engineering**, and related keywords such as:
- "Database Administrator"
- "SQL"
- "MySQL"
- "PostgreSQL"
- "ETL"
- "Data Pipeline"

It stores the results in a **MySQL database** to prevent duplicates and provides a simple **web UI** to browse matching jobs.

---

## 🧩 Features

- ✅ Scrapes jobs from [https://unjobs.org](https://unjobs.org)
- ✅ Filters by job keywords
- ✅ Stores results in a MySQL database
- ✅ Avoids duplicate job entries
- ✅ Web-based UI to view job results

---

## 🛠 Tech Stack

- **Backend:** Python, Flask (API), BeautifulSoup (web scraping)
- **Database:** MySQL
- **Frontend:** Flask HTML templates (or can be extended to React/Vue later)
- **Web Server:** Uvicorn (optional if converted to FastAPI)
- **Scheduler (optional):** APScheduler for periodic scraping

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/job-scraper-app.git
cd job-scraper-app
