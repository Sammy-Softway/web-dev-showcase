import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash,request
from flask_bootstrap import Bootstrap5

from models import db, Todo
from forms import TodoForm, ActionForm


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
    form = ActionForm()
    all_tasks = db.session.execute(db.select(Todo).order_by(Todo.created_at.desc())).scalars().all()
    return render_template("index.html", todos=all_tasks, form=form)

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

    return render_template("task_form.html", form=form, page_title="Add Task")

@app.route("/task/<int:task_id>")
def task_detail(task_id):
    form = ActionForm()
    task = db.get_or_404(Todo, task_id)
    return render_template("task_detail.html", task=task, form=form)

@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404

@app.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = db.get_or_404(Todo, task_id)

    form = TodoForm(obj=task)
    form.submit.label.text = "Save Changes"
    if form.validate_on_submit():
        task.title = (form.title.data or "").strip()
        task.description = (form.description.data or "").strip() or None
        task.is_completed = form.is_completed.data

        db.session.commit()

        flash("Task updated successfully!", "success")
        return redirect(url_for("task_detail", task_id=task.id))

    return render_template("task_form.html", form=form, page_title="Edit Task")

@app.route("/task/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    form = ActionForm()
    if form.validate_on_submit():
        task = db.get_or_404(Todo, task_id)

        task.is_completed = not task.is_completed
        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(request.referrer or url_for("home"))

    flash("Invalid request.", "danger")
    return redirect(url_for('home'))

@app.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    form = ActionForm()
    if form.validate_on_submit():
        task = db.get_or_404(Todo, task_id)

        db.session.delete(task)
        db.session.commit()
        flash("Task deleted successfully!", "info")
        return redirect(url_for("home"))

    flash("Invalid request.", "danger")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)