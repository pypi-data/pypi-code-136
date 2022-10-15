from flask import Flask
from pymongo import MongoClient
import copy

from pymongo.database import Database

from .mongo_config import MongoConfig

global_mongodb_client: MongoClient = None
global_mongo_config: MongoConfig = None


def assert_mongo_config(mongo_config):
    assert mongo_config is not None, f"No config provided, get {type(mongo_config)}"
    assert isinstance(mongo_config, MongoConfig), f"Config must be instance of MongoConfig, get {type(mongo_config)}"


def assert_mongo_client(mongo_client):
    assert mongo_client is not None, "You must call MongoDBInit.init_app or " \
                                              "MongoDBInit.init_client first"


class MongoDBInit(object):
    app = None

    @staticmethod
    def init_client(mongo_config: MongoConfig):
        global global_mongodb_client
        global global_mongo_config

        if global_mongo_config is None:
            global_mongo_config = copy.deepcopy(mongo_config)

        assert_mongo_config(global_mongo_config)
        if global_mongodb_client is None:
            global_mongodb_client = MongoClient(global_mongo_config.mongo_uri, connect=False)

        from .setup_collection import setup_collection_model
        setup_collection_model()

    @staticmethod
    def init_app(app: Flask):
        global global_mongodb_client
        global global_mongo_config

        if global_mongo_config is None:
            global_mongo_config = copy.deepcopy(app.config.get("MONGO_DB_SETTINGS"))

        assert_mongo_config(global_mongo_config)
        if global_mongodb_client is None:
            global_mongodb_client = MongoClient(global_mongo_config.mongo_uri)

        from .setup_collection import setup_collection_model
        setup_collection_model()

    @staticmethod
    def get_db(db_name: str = None, mongo_uri: dict = None) -> Database:

        if db_name is None:
            assert_mongo_config(global_mongo_config)
            db_name = global_mongo_config.db_name

        if mongo_uri is None:
            assert_mongo_client(global_mongodb_client)
            return global_mongodb_client.get_database(db_name)

        return MongoClient(mongo_uri, connect=False).get_database(db_name)

    @staticmethod
    def get_mongo_db_client() -> MongoClient:
        assert_mongo_client(global_mongodb_client)
        return global_mongodb_client

    @staticmethod
    def get_mongo_config() -> MongoConfig:
        assert_mongo_config(global_mongo_config)
        return global_mongo_config
