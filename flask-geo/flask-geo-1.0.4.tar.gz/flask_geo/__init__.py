from flask import Flask
from importlib import import_module


class FlaskGeo:

    def __init__(self, app: Flask = None, **kwargs):
        self.city_repository = kwargs.get('city_repository')
        self.country_repository = kwargs.get('country_repository')
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.geo = self
        import_module('flask_geo.api').init_app(app)
