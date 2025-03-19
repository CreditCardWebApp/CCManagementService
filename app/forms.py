from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from datetime import datetime
from wtforms.validators import DataRequired, Length, ValidationError

def validate_date(form, field):
    # Check if the date is in the correct format and valid
    try:
        # Attempt to parse the date
        date_value = datetime.strptime(field.data.strip(), '%d/%m/%Y')  # Strip any whitespace
        # Check if the year is before 2006
        if date_value.year >= 2006:
            raise ValidationError('Year must be before 2006.')
    except ValidationError as ve:
        raise ValidationError(ve)
    except ValueError:
        raise ValidationError('Invalid date format. Please use DD/MM/YYYY.')

class CreditCardForm(FlaskForm):
    card_number = StringField('Card Number', validators=[DataRequired(), Length(min=16, max=16)])
    cardholder_name = StringField('Cardholder Name', validators=[DataRequired(), Length(max=100)])
    expiration_date = StringField('Expiration Date (MM/YY)', validators=[DataRequired()])
    cvv = StringField('CVV', validators=[DataRequired(), Length(min=3, max=3)])
    submit = SubmitField('Add Card')