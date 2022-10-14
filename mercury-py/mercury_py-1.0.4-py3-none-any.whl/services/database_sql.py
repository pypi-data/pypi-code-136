# coding=utf-8

from os import makedirs
from os import path

from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_cli = AppGroup('database')


def init_app(app):
    """Initializes the application database (SQL).

    :param app: The Flask application object.
    """
    db.init_app(app)
    app.cli.add_command(db_cli)

    try:
        # Ensure the database folder exists
        database_folder = path.join(app.instance_path, app.config['DATABASE_FOLDER'])
        if not path.isdir(database_folder):
            makedirs(database_folder)
            raise Exception(f'Directory not found, so just created: {database_folder}')
    except OSError as ex:
        app.logger.error(str(ex))
    except Exception as ex:
        app.logger.exception(str(ex))

    # Check if sql database exists
    if not path.isfile(app.config['DATABASE_FILENAME']):
        app.logger.warning(f'Database SQL not found! File: {app.config["DATABASE_FILENAME"]}')


@db_cli.command('create-tables', help='Create all SQL database tables.')
def create_tables():
    """Create all SQL database tables."""
    db.create_all()
    print('SQL Database\'s tables created')


@db_cli.command('drop-tables', help='Drop all SQL database tables.')
def drop_database():
    """Drop all SQL database tables."""
    if input('Are you really sure to delete all SQL database tables? [y/N]:').lower() == 'y':
        db.drop_all()
        print('SQL Database\'s tables dropped')
    else:
        print('Aborted!')
