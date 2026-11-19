import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5

from models import db, Todo
from forms import TodoForm


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
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_tasks = db.session.execute(db.select(Todo).order_by(Todo.created_at.desc())).scalars().all()
    return render_template("index.html", todos=all_tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    form = TodoForm()

    if form.validate_on_submit():
        new_task = Todo(
            title=form.title.data.strip(),
            description=form.description.data.strip() if form.description.data else None,
        )

        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for("home"))

    return render_template("add_task.html", form=form)

@app.route("/task/<int:task_id>")
def task_detail(task_id):
    task = db.get_or_404(Todo, task_id)
    return render_template("task_detail.html", task=task)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)