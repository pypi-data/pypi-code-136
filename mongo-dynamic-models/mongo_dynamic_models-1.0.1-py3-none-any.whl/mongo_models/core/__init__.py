import re

import mongoengine
from mongoengine import DynamicDocument


class MongoModels(object):
    """
    examples:
        >>> from mongo_models import MongoModels
        >>> uri = 'mongodb://USER:PASSWORD@HOST_OR_IP:PORT/DB'
        >>> models = MongoModels(uri)
        >>> print(models)
        >>> print(models.collection_names)
        >>> print(models.users.objects)
    """

    def __init__(self, uri, timeout=1000):
        self.uri = uri
        self.timeout = timeout
        self.check_connect()

    def check_connect(self):
        """check connection of mongo uri
        """
        mongoengine.disconnect()
        client = mongoengine.connect(host=self.uri, serverselectiontimeoutms=self.timeout)
        db = client.get_database()
        try:
            collection_names = db.list_collection_names()
            self.auto_create(collection_names)
            self.db = db
            self.collection_names = collection_names
        except Exception as e:
            raise Exception(e)

    def auto_create(self, collection_names):
        """create dynamic document for all collections
        """
        for collection in collection_names:
            collection = re.sub(r'\s+', '_', collection)
            create_class_str = f'{collection}=type("{collection}", (DynamicDocument,), {{}})'
            exec(create_class_str)
            setattr(self, collection, locals()[collection])

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return f'MongoModels[{self.uri}]'

    def __str__(self):
        return f'mongo uri: {self.uri}\ncollections: {", ".join(self.collection_names)}'
