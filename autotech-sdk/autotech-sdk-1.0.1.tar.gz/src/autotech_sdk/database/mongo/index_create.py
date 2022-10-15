import typing

from pymongo import IndexModel
from pymongo.collection import Collection


def create_mongo_indexes(collection: Collection, indexes: typing.Sequence[IndexModel] = None):

    try:
        collection.create_indexes(indexes)
    except Exception as er:
        print("error={}".format(er))
        print(f"Collection {collection}: failed create index: {indexes}.")
