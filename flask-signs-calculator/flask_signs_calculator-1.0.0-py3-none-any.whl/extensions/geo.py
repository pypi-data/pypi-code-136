from flask import Flask
from flask_geo import FlaskGeo

from signs_calculator.repositories import CityRepository, CountryRepository


def init_app(app: Flask) -> None:
    FlaskGeo(app, country_repository=CountryRepository(), city_repository=CityRepository())
