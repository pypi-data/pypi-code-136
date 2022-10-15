from typing import Any

from datetime import date

from insanic.utils import (
    get_property_value,
    ContainerField,
)


__all__ = (
    'Field',
    'StringField',
)

class FieldSerializationError(Exception):
    pass

class Field(ContainerField):
    async def serialize_value(self, value: Any) -> Any: # pylint: disable=no-self-use
        return value # pragma: no cover

    async def serialize(self, value: Any) -> Any:
        return await self.serialize_value(value)

class BooleanField(Field):
    async def serialize_value(self, value: Any) -> bool | None:
        if value is None:
            return None

        return bool(value)

class IntegerField(Field):
    async def serialize_value(self, value: Any) -> int | None:
        if value is None:
            return None

        return int(value)

class FloatField(Field):
    async def serialize_value(self, value: Any) -> float | None:
        if value is None:
            return None

        return float(value)

class StringField(Field):
    async def serialize_value(self, value: Any) -> str | None:
        if value is None:
            return None

        return str(value)

class DateField(Field):
    def __init__(self, date_format: str = '%Y-%m-%d', **kwargs: Any) -> None:
        self.date_format = date_format
        super().__init__(**kwargs)

    # @TODO: Check if value a proper date?
    async def serialize_value(self, value: date | None) -> str | None:
        if value is None:
            return None

        return value.strftime(self.date_format)

class DictKeyField(Field):
    def __init__(self, key: str, **kwargs: Any) -> None:
        self.key = key
        super().__init__(**kwargs)

    async def serialize_value(self, value: dict) -> Any:
        return get_property_value(value, self.key)
