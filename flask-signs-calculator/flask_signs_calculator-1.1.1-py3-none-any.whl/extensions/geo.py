from flask import Flask
from flask_geo import FlaskGeo

from signs_calculator.repositories import CityRepository, CountryRepository, FakeCountryRepository, FakeCityRepository


def init_app(app: Flask) -> None:
    if app.testing:
        FlaskGeo(app,
                 country_repository=FakeCountryRepository(),
                 city_repository=FakeCityRepository())
    else:
        FlaskGeo(app,
                 country_repository=CountryRepository(),
                 city_repository=CityRepository())
