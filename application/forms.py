from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class BandForm(FlaskForm):
    band_name = StringField('Band name',
            validators = [
                DataRequired(),
                Length(min=2, max=100)
            ]
    )
    submit = SubmitField('Add Band')

class VenueForm(FlaskForm):
    venue_name = StringField('Venue name',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    submit = SubmitField('Add Venue')
