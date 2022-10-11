from flask import current_app as app
from wtforms import SelectField


class CountryField(SelectField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        countries = app.geo.country_repository.all()
        self.choices = [(country.code, country.name) for country in countries]
