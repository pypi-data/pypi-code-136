from datetime import datetime, date
from typing import Any

from sanic.request import File

from insanic.utils import Container, ContainerField


class FieldValidationError(Exception):
    def __init__(self, error_code: str):
        super().__init__()
        self.error_code = error_code

class Field(ContainerField):
    ERROR_REQUIRED = 'required'

    def __init__(self, *args: Any, required: bool = True, default: Any | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self.required = required
        if self.required and default:
            raise UserWarning('Cannot set default for required field')

        self.default = default

    def validate_value(self, value: Any) -> Any | None: # pylint: disable=no-self-use
        return value # pragma: no cover

    def validate(self, value: Any) -> Any | None:
        if value:
            return self.validate_value(value)

        if self.required:
            raise FieldValidationError(self.ERROR_REQUIRED)

        return self.default

class FileField(Field):
    ERROR_INVALID_FILE_TYPE = 'invalid_file_type'

    allowed_file_types: list[str]

    def __init__(self, *args: Any, file_type: str | list[str] | None = None, **kwargs: Any) -> None:
        self.allowed_file_types = [file_type] if isinstance(file_type, str) else file_type
        super().__init__(*args, **kwargs)

    def validate_value(self, value: File) -> File:
        if value.type not in self.allowed_file_types:
            raise FieldValidationError(self.ERROR_INVALID_FILE_TYPE)

        return value

class IntegerField(Field):
    ERROR_NOT_INTEGER = 'invalid_integer'

    def validate_value(self, value) -> None:
        try:
            return int(value)
        except ValueError as error:
            raise FieldValidationError(self.ERROR_NOT_INTEGER) from error

class DateTimeField(Field):
    ERROR_INVALID_DATE = 'invalid_date'

    def __init__(self, *args, parse_format='%Y-%m-%d %H:%M:%S', **kwargs) -> None:
        self.parse_format = parse_format
        super().__init__(*args, **kwargs)

    def validate_value(self, value) -> datetime:
        try:
            return datetime.strptime(value, self.parse_format)
        except ValueError as error:
            raise FieldValidationError(self.ERROR_INVALID_DATE) from error

class DateField(DateTimeField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs['parse_format'] = kwargs.pop('parse_format', '%Y-%m-%d')
        super().__init__(*args, **kwargs)

    def validate_value(self, value) -> date:
        value = super().validate_value(value)
        return value.date()
