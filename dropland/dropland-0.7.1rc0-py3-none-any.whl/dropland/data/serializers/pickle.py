import pickle
from typing import Optional, Any

from . import Serializer, Deserializer


class PickleSerializer(Serializer):
    def serialize(self, data: Optional[Any] = None) -> bytes:
        return pickle.dumps(data)


class PickleDeserializer(Deserializer):
    def deserialize(self, data: bytes) -> Optional[Any]:
        try:
            values = pickle.loads(data) if data else None
        except (pickle.UnpicklingError, ValueError, ModuleNotFoundError, MemoryError):
            return None

        return values
