import uuid
from typing import Any
from django.db import models
from .validators import validate_number


class StringField(models.CharField):
    """
    A field used to store a reasonable-sized string. It's a shortcut
    to always having to declare max_length on CharField. Value stored
    in this field should be smaller that what TextField can store.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["max_length"] = 150
        super().__init__(*args, **kwargs)


class ShortStringField(models.CharField):
    """
    A field used to store typically single-word type of strings. Examples
    include a primary key value, status and type values, etc.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["max_length"] = 40
        super().__init__(*args, **kwargs)


class PrimaryKeyField(ShortStringField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["editable"] = False
        kwargs["primary_key"] = True
        kwargs["default"] = uuid.uuid4
        super().__init__(*args, **kwargs)


class PhoneNumberField(ShortStringField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["validators"] = [validate_number]
        super().__init__(*args, **kwargs)
