import time
import uuid
from enum import Enum
from typing import Any
from typing import Callable
from typing import Generic
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import TypeVar
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from pydantic.generics import GenericModel


EnumType = TypeVar("EnumType")


def as_enum(
    value: Any, enum_type: Callable[[Any], EnumType], default: Optional[EnumType] = None
) -> Optional[EnumType]:
    try:
        return enum_type(value)
    except ValueError:
        return default


class Header(BaseModel):
    src: str
    dst: str = ""
    message_type: str
    message_id: str = ""
    type_name: str = Field("gridworks.header.000", const=True)


PayloadT = TypeVar("PayloadT")

PAYLOAD_TYPE_FIELDS = ["type_name", "type_alias", "TypeAlias"]


class Message(GenericModel, Generic[PayloadT]):
    header: Header
    payload: PayloadT
    type_name: str = Field("gridworks.message.000", const=True)

    def __init__(self, **kwargs: Any):
        kwargs["header"] = self._header_from_kwargs(kwargs)
        super().__init__(**kwargs)

    def mqtt_topic(self) -> str:
        return f"{self.header.src}/{self.type_name.replace('.', '-')}"

    @classmethod
    def _header_from_kwargs(cls, kwargs: dict) -> Header:
        header_kwargs = dict()
        payload = kwargs["payload"]
        for header_field, payload_fields in [
            ("src", ["src"]),
            ("dst", ["dst"]),
            ("message_id", ["message_id"]),
            ("message_type", PAYLOAD_TYPE_FIELDS),
        ]:
            val = kwargs.get(header_field, None)
            if val is None:
                for payload_field in payload_fields:
                    if hasattr(payload, payload_field):
                        val = getattr(payload, payload_field)
                    elif isinstance(payload, Mapping) and payload_field in payload:
                        val = payload[payload_field]
            if val is not None:
                header_kwargs[header_field] = val
        header: Optional[Union[Header, dict]] = kwargs.get("header", None)
        if isinstance(header, Header):
            header = header.copy(update=header_kwargs, deep=True)
        else:
            if header is not None:
                header_kwargs = dict(header, **header_kwargs)
            header = Header(**header_kwargs)
        return header
