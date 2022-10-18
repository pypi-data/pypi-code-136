from flask_wtf import FlaskForm
from wtforms import TimeField, BooleanField, StringField, DateField
from wtforms.validators import DataRequired

from flask_geo.fields import CountryField


class SignsCalculatorForm(FlaskForm):
    birth_date = DateField('Data de nascimento:', validators=[DataRequired()])
    birth_time = TimeField('Hora:')
    not_know_the_time = BooleanField('Não sei a hora:', default=False)
    country = CountryField('País:')
    city = StringField('Cidade:', validators=[DataRequired()])
