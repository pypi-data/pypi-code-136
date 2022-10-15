import typing

from pymongo import ReadPreference
from pymongo.database import Database

from .mongo_client import MongoDBInit


models: typing.List = []


def register_collection(class_model):
    global models
    models.append(class_model)


def setup_collection_model():
    db_default = MongoDBInit.get_db()
    for model in models:
        db: Database = None
        if hasattr(model, 'DB_NAME'):
            db = MongoDBInit.get_mongo_db_client().get_database(model.DB_NAME)

        if db is None:
            db = db_default

        model.conn_primary = db.get_collection(model.COLLECTION_NAME)
        model.conn_secondary = db.get_collection(
            model.COLLECTION_NAME, read_preference=ReadPreference.SECONDARY_PREFERRED
        )
        model.create_indexes()

