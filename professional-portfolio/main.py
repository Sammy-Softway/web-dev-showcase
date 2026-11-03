from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email
import os


SECRET_KEY = os.environ.get("SECRET_KEY")


app = Flask(__name__)
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone_number = form.phone_number.data
    return render_template('contact.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)