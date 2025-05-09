from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    company = db.Column(db.String(128))
    location = db.Column(db.String(128))
    url = db.Column(db.String(512), unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
