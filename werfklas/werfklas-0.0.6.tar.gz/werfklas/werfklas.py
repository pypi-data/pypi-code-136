# Hier komt alles samen
from flask import Flask, render_template
from flask_assets import Environment  # Import `Environment`
from flask_bootstrap import Bootstrap
from src.classes.database import create_database, sessionSetup, test_database
from src.modules.config import load_config
exec(open('__version__.py').read())

config = load_config()
databasefile = config["database"]["path"] + config["database"]["name"]
test_database(databasefile)


def create_app():
    """Create Flask application."""
    #https://hackersandslackers.com/configure-flask-applications
    _app = Flask(__name__, instance_relative_config=False)
    _app.config['SECRET_KEY'] = config["flask"]["secretKey"]
    assets = Environment()  # Create an assets environment
    assets.init_app(_app)  # Initialize Flask-Assets

    with _app.app_context():
        # Import parts of our application
        import frontend.routes
        import frontend.teachers.routes
        import frontend.classrooms.routes
        import frontend.parents.routes
        import frontend.families.routes
        import frontend.children.routes

        # Register Blueprints
        _app.register_blueprint(frontend.routes.templates_bp)
        _app.register_blueprint(frontend.teachers.routes.teachers_bp)
        _app.register_blueprint(frontend.classrooms.routes.classroom_bp)
        _app.register_blueprint(frontend.parents.routes.parents_bp)
        _app.register_blueprint(frontend.families.routes.families_bp)
        _app.register_blueprint(frontend.children.routes.children_bp)

        return _app


app = create_app()
Bootstrap(app)
session = sessionSetup()


if __name__ == '__main__':
    # import webbrowser
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run(debug=False)

