from flask import Flask
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from importlib import import_module

from .views import bp


class SignsCalculator:

    def __init__(self, app: Flask = None, db: Engine = None) -> None:
        if app is not None and db is not None:
            self.init_app(app, db)

    def init_app(self, app: Flask, db: Engine) -> None:
        app.db = db
        app.db_session = Session(db)
        app.signs_calculator = self
        import_module('signs_calculator.extensions.geo').init_app(app)
        app.register_blueprint(bp)
