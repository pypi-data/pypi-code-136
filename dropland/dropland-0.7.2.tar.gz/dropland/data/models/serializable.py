from typing import Set, List, Optional, Dict, Any

from .base import ModelProtocol
from .fields import ModelFieldsMixin
from ..serializers import Serializer, Deserializer
from ..serializers.pickle import PickleSerializer, PickleDeserializer


class SerializableModel(ModelFieldsMixin):
    class Meta(ModelFieldsMixin.Meta):
        serializer: Serializer
        deserializer: Deserializer

    def __init_subclass__(
            cls, serializer: Optional[Serializer] = None,
            deserializer: Optional[Deserializer] = None,
            **kwargs):
        super().__init_subclass__(**kwargs)
        cls.Meta.serializer = serializer or PickleSerializer()
        cls.Meta.deserializer = deserializer or PickleDeserializer()

    # noinspection PyProtectedMember
    @classmethod
    def get_serializable_fields(cls) -> Set[str]:
        key = cls._fields_cache_key()
        if key not in cls.Meta._fields_cache:
            cls._calculate_fields()
        return cls.Meta._fields_cache[key].ser

    def get_serializable_values(self, only_fields: List[str] = None) -> Optional[Dict[str, Any]]:
        serializable_fields = self.get_serializable_fields()
        only_fields = set(only_fields) if only_fields else set()

        return {
            name: getattr(self, name) for name in serializable_fields
            if hasattr(self, name) and (not only_fields or name in only_fields)
        }

    def serialize(self, only_fields: List[str] = None) -> bytes:
        return self.Meta.serializer.serialize(self.get_serializable_values(only_fields))

    @classmethod
    def deserialize(cls, data: bytes) -> Optional[ModelProtocol]:
        if deserialized := cls.Meta.deserializer.deserialize(data):
            return cls._construct(deserialized)
        return None
