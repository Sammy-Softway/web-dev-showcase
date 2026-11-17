# Cafe & Wifi Directory

A full-stack web application built with **Flask** and **SQLAlchemy 2.0** that helps remote workers and coffee lovers discover cafes with reliable Wi-Fi, power sockets, restrooms, and call-friendly environments. Users can browse cafes in a responsive card grid, filter by neighborhood and amenities, add new spots, and remove outdated listings.

---

## Features

* **Responsive Cafe Directory:** Displays cafes in a clean Bootstrap 5 card grid with uniform photography, seating capacity, coffee pricing, and amenity badges.
* **Dynamic Search & Filtering:** Filter cafes in real time using case-insensitive location matching (`ILIKE`) combined with boolean amenity checkboxes (`Sockets`, `Toilet`, `Wi-Fi`) via bookmarkable `GET` query parameters.
* **Add New Cafes:** Server-side validated form powered by **Flask-WTF** and **Bootstrap-Flask** with URL validation, length constraints, and graceful `IntegrityError` handling for duplicate cafe names.
* **CSRF-Protected Deletion:** Removes cafe listings securely via `POST` requests protected with `CSRFProtect` and `get_or_404` lookups.
* **Modular Architecture:** Separates database models (`models.py`), form schemas (`forms.py`), routes (`app.py`), and Jinja2 templates (`templates/`).

---

## Tech Stack

* **Backend:** Python 3, Flask, Flask-SQLAlchemy (SQLAlchemy 2.0), Flask-WTF, WTForms
* **Database:** SQLite (`instance/cafes.db`)
* **Frontend:** HTML5, CSS3, Jinja2, Bootstrap 5 (`Bootstrap-Flask`)
* **Configuration & Security:** `python-dotenv`, CSRF protection, environment-based debug controls

---

## Project Structure

```text
cafe-website/
├── instance/
│   └── cafes.db              # SQLite database
├── static/
│   └── css/
│       └── styles.css        # Custom card image styling
├── templates/
│   ├── base.html             # Base layout, navbar, and flash alerts
│   ├── index.html            # Search filter bar and responsive cafe grid
│   └── add_cafe.html         # Form page for adding new cafes
├── app.py                    # Flask application setup and routes
├── forms.py                  # Flask-WTF form definitions and validators
├── models.py                 # SQLAlchemy 2.0 declarative database models
├── .env.example              # Environment variable template
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Local Setup & Installation

1. **Clone the repository and navigate into the project folder:**
   ```bash
   git clone https://github.com/Sammy-Softway/web-dev-showcase.git
   cd cafe-website
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and set your own secret key:
   ```bash
   cp .env.example .env
   ```
   Update `.env` for local development:
   ```env
   TOP_SECRET_KEY=your-random-secret-key
   FLASK_DEBUG=True
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   Open your browser and visit `http://127.0.0.1:5000`.

---


## Project Reflection & Takeaways

### 1. What was easy?

Answer: Once the database schema was mapped out properly, the core Flask routing and setting up the WTForms validation felt straightforward. Breaking the project into small stages from the very beginning also made the workflow smooth—starting with a basic HTML table to verify the backend logic before worrying about Bootstrap styling kept things manageable.

### 2. What was hard?

Answer: Building the dynamic search and filter feature in SQLAlchemy 2.0 was tricky at first. Learning how to chain .where() clauses conditionally onto a select() statement without executing it prematurely—and keeping the checkbox states sticky in Jinja after a GET request—took some trial and error. Handling boolean coercion properly with WTForms RadioFields so SQLite saved actual 1s and 0s instead of strings was another good puzzle to work through.

### 3. How I might improve for the next project? / What I would do differently?

Answer: Next time, I will separate my files (models.py and forms.py) right from the start instead of putting everything into app.py and refactoring later. I would also inspect existing database column constraints—like UNIQUE rules and nullable fields—more closely upfront so I can write try/except IntegrityError rollbacks and optional form validators on the first pass.

### 4. What was my biggest learning from today?

Answer: My biggest takeaway was shifting from just writing code that runs locally to writing code with real-world best practices in mind. I learned why destructive actions like deleting a record should always use a CSRF-protected POST form rather than a simple GET link, how to keep secrets and debug flags safe with .env and .env.example templates, and how clean separation of concerns makes debugging much easier.