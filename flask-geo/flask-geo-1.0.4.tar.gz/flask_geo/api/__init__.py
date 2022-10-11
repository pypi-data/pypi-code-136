from flask import Flask

from .views import bp


def init_app(app: Flask) -> None:
    app.register_blueprint(bp)
