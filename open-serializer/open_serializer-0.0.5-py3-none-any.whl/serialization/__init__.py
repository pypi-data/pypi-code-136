from .general import *  # TODO: this import cannot be remove now, due to require registration of handlers
from .handler import Serializer

serialize_object = Serializer.serialize_object
deserialize_object = Serializer.deserialize_object
