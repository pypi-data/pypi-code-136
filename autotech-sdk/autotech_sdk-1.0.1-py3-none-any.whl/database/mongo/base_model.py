import typing

from pymongo import IndexModel

from .index_create import create_mongo_indexes
from .base_model_meta import BaseModelMeta
from pymongo.collection import Collection


class BaseMongoDB(object, metaclass=BaseModelMeta):
    COLLECTION_NAME: str = None
    conn_primary: Collection = None
    conn_secondary: Collection = None
    indexes: typing.Sequence[IndexModel] = []

    @classmethod
    def create_indexes(cls, indexes: typing.Sequence[IndexModel] = None):

        if not isinstance(indexes, typing.Iterable) and indexes is not None:
            indexes = [indexes]

        if indexes is None and cls.indexes:
            indexes = cls.indexes

        if indexes is None:
            print(f"No indexes provided for {cls.COLLECTION_NAME}, skip create index.")
            return

        create_mongo_indexes(cls.conn_primary, indexes)
        print(f"Collection {cls.COLLECTION_NAME}: successfully create index: {indexes}")
