from typing import Any

from insanic.utils import Container

from .fields import Field, FieldValidationError


class FormValidationError(Exception):
    def __init__(self, field_errors: dict[str, FieldValidationError]):
        super().__init__()
        self.errors = field_errors


FormData = dict[str, Any]
FormErrors = dict[str, FieldValidationError]
class Form(Container):
    FIELD_BASE_CLASS = Field
    RESERVED_ATTRS = ['is_validated', 'errors', 'data']

    def __init__(self, data: FormData | object, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._raw_data: FormData | object = data
        self._data: FormData = {}
        self._errors: FormErrors = {}

    @property
    def is_validated(self) -> bool:
        return len(self._data.keys()) > 0 or len(self._errors.keys()) > 0

    @property
    def errors(self) -> FormErrors:
        assert self.is_validated, 'Form hasn\'t been validated'
        return self._errors

    @property
    def data(self) -> FormData:
        assert self.is_validated, 'Form hasn\'t been validated'
        return self._data

    def add_error(self, field_name: str, error: FieldValidationError) -> None:
        self.errors[field_name] = error

    async def run_validation(self) -> None:
        pass

    async def validate(self) -> FormData:
        self._data = {}
        self._errors = {}

        for field_name, field_value, field in self._field_values(self._raw_data):
            try:
                self._data[field_name] = field.validate(field_value)
            except FieldValidationError as validation_error:
                self._errors[field_name] = validation_error

        await self.run_validation()

        if len(self._errors) > 0:
            self._data = {}
            raise FormValidationError(self._errors)

        return self.data

    async def is_valid(self) -> bool:
        if not self.is_validated:
            try:
                await self.validate()
            except FormValidationError as _exc:
                pass

        return len(self._errors) == 0
