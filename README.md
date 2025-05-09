# 🔍 Job Scraper App (Full-Stack Python)

This is a full-stack web application that scrapes real job listings from the [Adzuna Job Search API](https://developer.adzuna.com/), filters for data and database-related roles, stores them in a MySQL database, and displays them on a simple web interface built with Flask.

---

## 🚀 Features

✅ Scrapes jobs related to:

- Database Administration  
- Data Engineering  
- SQL, ETL, Data Pipelines, PostgreSQL, MySQL

✅ Filters and avoids duplicate job listings  
✅ Saves matching jobs to a MySQL database  
✅ Web UI to browse jobs by title, company, and location  
✅ Secure configuration using `.env` file  
✅ Clean full-stack architecture ready to scale  

---

## 🧱 Tech Stack

| Layer       | Technology       | Purpose                       |
|-------------|------------------|-------------------------------|
| Frontend    | HTML + Jinja2    | Displays job listings         |
| Backend     | Flask + Python   | Web server, routing           |
| Scraper     | `requests`       | Pulls job data from Adzuna API |
| Database    | MySQL + SQLAlchemy | Stores job listings          |
| Config      | `python-dotenv`  | Loads secrets and DB creds    |

---

## 📂 Project Structure

job-scraper-app/
│
├── app/
│ ├── scraper.py # Fetch & store jobs from Adzuna API
│ ├── models.py # SQLAlchemy job model
│ ├── init.py # (optional for packaging)
│
├── templates/
│ └── index.html # Web UI to list jobs
│
├── config.py # Flask + DB config
├── run.py # Entry point for web app
├── .env # API keys and DB secrets (not tracked)
├── requirements.txt # Python dependencies
├── README.md # Project overview

---

## 🧪 How It Works

### ➤ Scraper

Run the scraper manually or on a schedule:

```bash
python -m app.scraper

Connects to Adzuna API

Filters for keywords like SQL, ETL, Data, etc.

Prevents duplicate entries using job URL

Saves new listings to the MySQL database

➤ Web App
Start the web app locally:

python run.py

