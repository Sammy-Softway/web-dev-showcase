import os

from dotenv import load_dotenv
from flask import Flask

from models import db


# --- Configuration & Secrets ---
load_dotenv()
TOP_SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG_MODE = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///todos.db")

# --- App & Extensions Setup ---
app = Flask(__name__)
app.config["SECRET_KEY"] = TOP_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    pass

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)