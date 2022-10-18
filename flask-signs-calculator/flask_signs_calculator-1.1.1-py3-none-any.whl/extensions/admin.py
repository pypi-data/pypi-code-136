from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from signs_calculator.models import CountryModel, StateModel, CityModel


def init_app(app: Flask) -> None:
    admin = Admin(app, name='signs_calculator_admin')
    admin.add_view(ModelView(CountryModel, app.db_session))
    admin.add_view(ModelView(StateModel, app.db_session))
    admin.add_view(ModelView(CityModel, app.db_session))
