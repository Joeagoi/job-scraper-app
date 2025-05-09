from flask import Flask, render_template
from app.models import db, Job
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    jobs = Job.query.order_by(Job.date_added.desc()).all()
    return render_template("index.html", jobs=jobs)

print("DB URI:", Config.SQLALCHEMY_DATABASE_URI)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
'''

import os
from dotenv import load_dotenv

load_dotenv()

print("User:", os.getenv("DB_USER"))
print("Pass:", os.getenv("DB_PASS"))
print("Host:", os.getenv("DB_HOST"))
'''