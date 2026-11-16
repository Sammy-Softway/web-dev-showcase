from flask_wtf import FlaskForm
from wtforms import StringField, URLField, RadioField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, URL, Optional


class AddCafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired(), Length(min=4, max=250)])
    map_url = URLField('Map Url', validators=[DataRequired(), URL(message="Please enter a valid URL.")])
    img_url = URLField('Image Url', validators=[DataRequired(), URL(message="Please enter a valid URL.")])
    location = StringField('Location', validators=[DataRequired(), Length(min=4, max=250)])
    has_sockets = RadioField('Has Sockets?', choices=[('True', 'Yes'), ('False', 'No')],
                             coerce=lambda x: x == "True",
                              validators=[InputRequired(message="Please select a valid option.")])
    has_toilet = RadioField('Has Toilet?', choices=[('True', 'Yes'), ('False', 'No')],
                             coerce=lambda x: x == "True",
                              validators=[InputRequired(message="Please select a valid option.")])
    has_wifi = RadioField('Has Wifi?', choices=[('True', 'Yes'), ('False', 'No')],
                             coerce=lambda x: x == "True",
                              validators=[InputRequired(message="Please select a valid option.")])
    can_take_calls = RadioField('Can Take Calls?', choices=[('True', 'Yes'), ('False', 'No')],
                             coerce=lambda x: x == "True",
                              validators=[InputRequired(message="Please select a valid option.")])
    seats = StringField('Range of Seats Available', validators=[Optional(), Length(min=1, max=20)])
    coffee_price = StringField('Coffee Price', validators=[Optional(), Length(min=1, max=20)])
    submit = SubmitField('Add')