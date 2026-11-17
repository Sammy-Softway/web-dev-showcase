import os

from dotenv import load_dotenv
from flask import Flask, render_template, request,flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from forms import AddCafeForm
from models import db, Cafe


# --- Configuration & Secrets ---
load_dotenv()
TOP_SECRET_KEY = os.environ["TOP_SECRET_KEY"]
DEBUG_MODE = os.environ.get("FLASK_DEBUG", "False").lower() == "true"

# --- App & Extensions Setup ---
app = Flask(__name__)
app.config["SECRET_KEY"] = TOP_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"

db.init_app(app)
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


@app.route("/")
def home():
    # all_cafes = db.session.execute(db.select(Cafe)).scalars().all()

    cafe_stmt = db.select(Cafe)

    query_location = request.args.get("location", "").strip()
    has_sockets = request.args.get("sockets")
    has_toilet = request.args.get("toilet")
    has_wifi = request.args.get("wifi")

    if query_location:
        cafe_stmt = cafe_stmt.where(Cafe.location.ilike(f"%{query_location}%"))

    if has_sockets:
        cafe_stmt = cafe_stmt.where(Cafe.has_sockets.is_(True))

    if has_toilet:
        cafe_stmt = cafe_stmt.where(Cafe.has_toilet.is_(True))

    if has_wifi:
        cafe_stmt = cafe_stmt.where(Cafe.has_wifi.is_(True))

    cafes = db.session.execute(cafe_stmt).scalars().all()

    return render_template("index.html",
                           cafes=cafes,
                           query_location=query_location,
                           has_sockets=has_sockets,
                           has_toilet=has_toilet,
                           has_wifi=has_wifi)

@app.route("/add_cafe", methods=["GET", "POST"])
def add_cafe():
    form = AddCafeForm()

    if form.validate_on_submit():
        cafe_name = form.name.data

        new_cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )

        try:
            db.session.add(new_cafe)
            db.session.commit()

            flash(f"{cafe_name} added successfully", "success")

            return redirect(url_for("home"))
        except IntegrityError:
            db.session.rollback()

            flash(f"A cafe with name '{cafe_name}' already exists.", "warning")

    return render_template("add_cafe.html", form=form)

@app.route("/delete_cafe/<int:cafe_id>", methods=["POST"])
def delete_cafe(cafe_id):
    target_cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(target_cafe)
    db.session.commit()

    flash(f"{target_cafe.name} deleted.", category="info")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=DEBUG_MODE)
