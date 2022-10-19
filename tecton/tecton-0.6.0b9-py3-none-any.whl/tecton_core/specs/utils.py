from typing import Any
from typing import List
from typing import Tuple

import attrs
import typeguard
from attrs import validators
from google import protobuf


def get_field_or_none(proto: protobuf.message, field: str) -> Any:
    """Get the proto message's field. Return None if the field is not set (instead of the default value).

    When filling specs, `None` should be typically filled when the underlying proto field is unset - except in cases
    where the proto default (e.g. 0) is the desired for the Python value.
    """
    if proto.HasField(field):
        return getattr(proto, field)
    else:
        return None


def get_tuple_from_repeated_field(proto: protobuf.message) -> Tuple:
    return tuple(value for value in proto)


def type_validator(instance: Any, attribute: attrs.Attribute, value: Any):
    """An attrs validator that asserts that an attribute matches its declared type."""
    assert attribute.type is not None, "Type annotations are required."
    typeguard.check_type(attribute.name, value, attribute.type)


def add_strict_type_validation(cls: type, fields: List[attrs.Attribute]) -> List[attrs.Attribute]:
    """An attrs field transformer that add type assertions to all fields."""
    new_fields = []
    for field in fields:
        if field.validator:
            new_validator = validators.and_(type_validator, field.validator)
        else:
            new_validator = type_validator
        new_fields.append(field.evolve(validator=new_validator))
    return new_fields


def frozen_strict(cls):
    """A decorator used to define a frozen attrs class where all attribute type annotations are enforced at runtime."""
    return attrs.frozen(cls, field_transformer=add_strict_type_validation)
