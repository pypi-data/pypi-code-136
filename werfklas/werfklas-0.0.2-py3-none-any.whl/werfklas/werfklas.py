# Hier komt alles samen
from flask import Flask, render_template
from flask_assets import Environment  # Import `Environment`
from flask_bootstrap import Bootstrap

import frontend.children.routes
import frontend.families.routes
import frontend.teachers.routes
import frontend.classrooms.routes
from src.classes.database import create_database, sessionSetup
from src.modules.config import load_config

config = load_config()

def create_app():
    """Create Flask application."""
    #https://hackersandslackers.com/configure-flask-applications
    _app = Flask(__name__, instance_relative_config=False)
    _app.config['SECRET_KEY'] = config["flask"]["secretKey"]
    assets = Environment()  # Create an assets environment
    assets.init_app(_app)  # Initialize Flask-Assets

    with _app.app_context():
        # Import parts of our application
        from frontend import routes
        from frontend.teachers import routes
        from frontend.classrooms import routes
        from frontend.children import routes
        from frontend.families import routes
        from frontend.parents import routes

        # Register Blueprints
        _app.register_blueprint(frontend.routes.templates_bp)
        _app.register_blueprint(frontend.teachers.routes.teachers_bp)
        _app.register_blueprint(frontend.classrooms.routes.classroom_bp)
        _app.register_blueprint(frontend.children.routes.children_bp)
        _app.register_blueprint(frontend.families.routes.families_bp)
        _app.register_blueprint(frontend.parents.routes.parents_bp)

        return _app


app = create_app()
Bootstrap(app)
databasefile = config["database"]["path"] + config["database"]["name"]
session = sessionSetup()


if __name__ == '__main__':
    from os.path import exists
    import webbrowser

    file_exists = exists(databasefile)
    if not file_exists:
        print(f'Database aanmaken..')
        create_database(databasefile=databasefile)
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run(debug=True)
