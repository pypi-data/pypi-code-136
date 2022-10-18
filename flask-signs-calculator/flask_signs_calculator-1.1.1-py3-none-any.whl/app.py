from flask import Flask
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from importlib import import_module

from . import SignsCalculator
from .models import Base


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'unsecret'
    load_dotenv('.env')
    app.testing = testing
    db = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    Base.metadata.create_all(db)
    SignsCalculator(app, db)
    import_module('signs_calculator.extensions.admin').init_app(app)
    return app
