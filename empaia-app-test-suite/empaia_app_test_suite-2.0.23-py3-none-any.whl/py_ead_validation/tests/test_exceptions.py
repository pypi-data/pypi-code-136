import pytest

from py_ead_validation.exceptions import (
    EadContentValidationError,
    EadSchemaMissingError,
    EadSchemaNotAvailableError,
    EadSchemaValidationError,
    EadValidationError,
)


def test_ead_schema_missing_error_can_be_caught_as_ead_validation_error():
    with pytest.raises(EadValidationError):
        raise EadSchemaMissingError()


def test_ead_schema_notavailable_error_can_be_caught_as_ead_validation_error():
    with pytest.raises(EadValidationError):
        raise EadSchemaNotAvailableError()


def test_ead_schema_validation_error_can_be_caught_as_ead_validation_error():
    with pytest.raises(EadValidationError):
        raise EadSchemaValidationError()


def test_ead_content_validation_error_can_be_caught_as_ead_validation_error():
    with pytest.raises(EadValidationError):
        raise EadContentValidationError()
