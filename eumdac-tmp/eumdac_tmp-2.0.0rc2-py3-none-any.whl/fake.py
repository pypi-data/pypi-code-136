# type: ignore
"""Fake DataStore DataTailor and Product that will be used when adding the --test
option in favour of the real implementations. Only useful for unittests."""

import io
from contextlib import contextmanager


class FakeDataStore:
    def get_collection(self, collection_id):
        return FakeCollection(collection_id)

    def get_product(self, collection_id, product_id):
        return FakeProduct(collection_id, product_id)


class FakeProduct:
    def __init__(self, collection_id, product_id):
        self._id = product_id
        self.collection = FakeCollection(collection_id)
        self.entries = ["entry1.nc", "entry2.nc"]

    def __str__(self):
        return str(self._id)

    def open(self, entry):
        return fake_stream(self._id)


@contextmanager
def fake_stream(name):
    ret = io.BytesIO(b"Content")
    ret.name = name
    ret.decode_content = True
    yield ret


class FakeCollection:
    def __init__(self, collection_id):
        self._id = collection_id

    def __str__(self):
        return str(self._id)

    def search(self, **query):
        dtstart = query["dtstart"]
        dtend = query["dtend"]
        return [
            FakeProduct(self._id, f"prod_{dtstart.isoformat().strip().replace(':', '-')}"),
            FakeProduct(self._id, f"prod_{dtend.isoformat().strip().replace(':', '-')}"),
        ]


class FakeDataTailor:
    pass
