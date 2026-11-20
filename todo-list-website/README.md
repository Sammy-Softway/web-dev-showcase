# Task Manager — Todo List Web Application

A clean, full-stack task management web application built with **Python**, **Flask**, **SQLAlchemy 2.0**, and **Bootstrap 5**. Originally developed as part of the *100 Days of Code: The Complete Python Pro Bootcamp* (Day 89), this project emphasizes production-ready backend architecture, secure state mutations, and modular separation of concerns.

---

## Key Features (MVP)

* **Create Tasks:** Add tasks with a validated title (max 120 characters, whitespace-trimmed) and an optional multi-line description.
* **Dashboard & Detail Views:** View all tasks ordered chronologically (newest first) with truncated previews, or open dedicated detail pages (`/task/<id>`) showing full descriptions and UTC creation timestamps.
* **Edit Tasks:** Update task titles, descriptions, and completion status via pre-populated WTForms.
* **One-Click Status Toggle:** Quickly mark tasks as **Completed** or **Pending** directly from the dashboard or detail view.
* **Secure Task Deletion:** Permanently remove tasks with a confirmation prompt and CSRF-protected `POST` requests.
* **Custom Error Handling:** Graceful HTTP `404` error page for non-existent task IDs or invalid routes.

---

## Tech Stack & Architecture

* **Backend:** Python 3, Flask
* **Database & ORM:** SQLite, Flask-SQLAlchemy (SQLAlchemy 2.0 `Mapped` declarative syntax)
* **Forms & Security:** Flask-WTF, WTForms (CSRF protection on all `POST` mutations)
* **Frontend:** Jinja2 Template Inheritance, Bootstrap 5 (`Bootstrap-Flask`)
* **Configuration:** `python-dotenv` environment variable management

### Project Structure

```text
todo-list-website/
├── docs/
│   └── requirements.md     # Product scope, validation rules & non-functional specs
├── templates/
│   ├── base.html           # Shared layout, navbar & flash message alerts
│   ├── index.html          # Main task dashboard
│   ├── task_detail.html    # Individual task view
│   ├── task_form.html      # Shared form template for creating & editing tasks
│   └── 404.html            # Custom 404 error page
├── forms.py                # WTForms definitions (TodoForm, ActionForm)
├── models.py               # SQLAlchemy 2.0 Todo database model
├── main.py                 # Application entry point, configuration & routes
├── .env.example            # Template for required environment variables
├── .gitignore              # Excludes .env, instance/, .venv/, and __pycache__/
└── requirements.txt        # Pinned Python dependencies
```

---

## Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Sammy-Softway/web-dev-showcase.git
cd todo-list-website
```

### 2. Create & Activate a Virtual Environment
```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and add your own secret key:
```bash
cp .env.example .env
```
Update `.env`for local development:
```env
SECRET_KEY=replace-with-a-strong-random-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///todos.db
FLASK_DEBUG=True
```

### 5. Run the Application
```bash
python main.py
```
Visit `http://127.0.0.1:5000` in your browser. The SQLite database (`instance/todos.db`) will initialize automatically on first launch.

---

## Engineering Best Practices Applied

* **CSRF-Protected Mutations:** State-changing actions (`Create`, `Edit`, `Toggle`, `Delete`) strictly use `POST` requests validated with Flask-WTF CSRF tokens—never `GET` links.
* **UTC Timestamp Storage:** All task creation timestamps are recorded in timezone-aware `UTC` (`datetime.now(timezone.utc)`).
* **Post/Redirect/Get (PRG) Pattern:** Prevents duplicate form submissions on browser refresh and provides immediate feedback via Flask flash messages.
* **Separation of Concerns:** Database schemas (`models.py`), form validation (`forms.py`), routing (`main.py`), and presentation (`templates/`) live in isolated modules.

---

## Future Enhancements (Phase 2 Roadmap)

* **Authentication & Multi-User Support:** User registration, login (`Flask-Login`), and per-user task ownership via foreign keys.
* **Organization & Scheduling:** Task priority levels (Low, Medium, High), categories/tags, and due dates.
* **Search & Filtering:** Filter dashboard tasks by completion status or priority and search by keyword.



## Project Reflection

### 1. What was easy?
Setting up the core Flask structure, wiring up the routes, and working with SQLAlchemy 2.0 felt very natural once the database schema was locked in. Breaking the project into small stages—starting with a clear requirements document before writing any code—made the backend logic for creating, reading, updating, and deleting tasks straightforward to build and debug step by step.

### 2. What was hard?
Dealing with the frontend layout and CSS alignment was easily the most frustrating part for me. Seeing how a simple long paragraph could completely break the dashboard layout and push buttons out of place took some patience to fix. Also, wrapping my head around small subtle details—like why a form needs CSRF protection even for a simple toggle or delete button, or why static type checkers flag optional form fields—took a bit of trial and error before everything clicked.

### 3. How I might improve for the next project? / What I would do differently?
Next time, I won't leave edge-case testing until the end—testing with messy, realistic data (like huge blocks of text or whitespace-only inputs) right away saves a lot of layout rework later. I also want to plan for multi-user authentication from the very beginning so user ownership and database relationships are baked into the initial schema rather than added later.

### 4. What was my biggest learning from today?
My biggest takeaway is that writing code that simply "works" isn't enough—good backend engineering is about protecting data and keeping things clean and predictable. Learning why destructive actions like deleting or toggling tasks must use CSRF-protected `POST` requests instead of simple `GET` links, why storing timestamps in UTC matters regardless of where I'm coding from, and how separating models, forms, and routes makes debugging painless completely changed how I approach building web apps.
