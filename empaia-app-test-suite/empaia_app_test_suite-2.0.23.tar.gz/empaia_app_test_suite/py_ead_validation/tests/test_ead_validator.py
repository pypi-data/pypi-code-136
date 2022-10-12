import contextlib
import json
import re
from os import mkdir
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

import pytest

from py_ead_validation import ead_validator
from py_ead_validation.exceptions import (
    EadSchemaMissingError,
    EadSchemaNotAvailableError,
    EadSchemaValidationError,
    EadValidationError,
)


@contextlib.contextmanager
def configured_validator(settings, *namespaces, enable_legacy_support=False, **schemes):
    with TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        namespace_dir_path = temp_dir_path / "namespaces"
        namespace_dir_path.mkdir()
        for namespace in namespaces:
            with open(namespace_dir_path / f"{namespace['namespace']}.json", "w") as namespace_file:
                json.dump(namespace, namespace_file)

        ead_schema_dir_path = temp_dir_path / "schemes"
        ead_schema_dir_path.mkdir()
        for name, schema in schemes.items():
            with open(ead_schema_dir_path / name, "w") as schema_file:
                json.dump(schema, schema_file)

        settings_path = temp_dir_path / "settings.json"
        with open(settings_path, "w") as settings_file:
            json.dump(settings, settings_file)

        validator = ead_validator.EadValidator(
            ead_schema_dir_path, namespace_dir_path, settings_path, enable_legacy_support
        )
        yield validator


def test_validation_without_schema():
    settings = {"allowed": [], "allowed_legacy": [], "mappings": {}}
    ead = {}
    with configured_validator(settings) as validator:
        with pytest.raises(EadSchemaMissingError, match=re.escape("EAD does not define a $schema")):
            validator.validate(ead)


def test_validation_with_non_existing_schema():
    settings = {"allowed": [], "allowed_legacy": [], "mappings": {}}
    ead = {"$schema": "https://www.example.org/non-existing-schema.json"}
    with configured_validator(settings) as validator:
        with pytest.raises(
            EadSchemaNotAvailableError,
            match=re.escape("EAD schema with name non-existing-schema.json not found or not allowed."),
        ):
            validator.validate(ead)


def test_validation_with_existing_but_not_allowed_schema():
    settings = {"allowed": [], "allowed_legacy": [], "mappings": {}}
    schemes = {
        "existing-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
        }
    }
    ead = {"$schema": "https://www.example.org/existing-schema.json"}
    with configured_validator(settings, **schemes) as validator:
        with pytest.raises(
            EadSchemaNotAvailableError,
            match=re.escape("EAD schema with name existing-schema.json not found or not allowed."),
        ):
            validator.validate(ead)


def test_validation_with_existing_allowed_and_indepth_schema():
    schemes = {
        "existing-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
        }
    }
    settings = {"allowed": ["existing-schema.json"], "allowed_legacy": [], "mappings": {}}
    ead = {"$schema": "https://www.example.org/existing-schema.json"}
    custom_validation_module = {".indepth.existing_schema": mock.Mock()}
    with configured_validator(settings, **schemes) as validator:
        with mock.patch.object(ead_validator, "import_module", new=custom_validation_module.get):
            validator.validate(ead)
        custom_validation_module[".indepth.existing_schema"].validate_ead.assert_called_once_with(ead, {})


def test_validation_with_existing_legacy_allowed_and_indepth_schema():
    schemes = {
        "existing-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
        }
    }
    settings = {"allowed": [], "allowed_legacy": ["existing-schema.json"], "mappings": {}}
    ead = {"$schema": "https://www.example.org/existing-schema.json"}
    custom_validation_module = {".indepth.existing_schema": mock.Mock()}
    with configured_validator(settings, **schemes, enable_legacy_support=True) as validator:
        with mock.patch.object(ead_validator, "import_module", new=custom_validation_module.get):
            validator.validate(ead)
        custom_validation_module[".indepth.existing_schema"].validate_ead.assert_called_once_with(ead, {})


def test_validation_with_existing_allowed_and_indpeth_schema_with_mapping():
    schemes = {
        "existing-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
        }
    }
    settings = {
        "allowed": ["existing-schema.json"],
        "allowed_legacy": [],
        "mappings": {"alternative-name.json": "existing-schema.json"},
    }
    ead = {"$schema": "https://www.example.org/alternative-name.json"}
    custom_validation_module = {".indepth.existing_schema": mock.Mock()}
    with configured_validator(settings, **schemes) as validator:
        with mock.patch.object(ead_validator, "import_module", new=custom_validation_module.get):
            validator.validate(ead)
        custom_validation_module[".indepth.existing_schema"].validate_ead.assert_called_once_with(ead, {})


def test_validation_with_existing_legacy_allowed_and_indpeth_schema_with_mapping():
    schemes = {
        "existing-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
        }
    }
    settings = {
        "allowed": [],
        "allowed_legacy": ["existing-schema.json"],
        "mappings": {"alternative-name.json": "existing-schema.json"},
    }
    ead = {"$schema": "https://www.example.org/alternative-name.json"}
    custom_validation_module = {".indepth.existing_schema": mock.Mock()}
    with configured_validator(settings, **schemes, enable_legacy_support=True) as validator:
        with mock.patch.object(ead_validator, "import_module", new=custom_validation_module.get):
            validator.validate(ead)
        custom_validation_module[".indepth.existing_schema"].validate_ead.assert_called_once_with(ead, {})


def test_failing_schema_validation_with_existing_allowed_and_indepth_schema():
    schemes = {
        "existing-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
            "properties": {"something": {"type:": "number"}},
            "required": ["something"],
        }
    }
    settings = {"allowed": ["existing-schema.json"], "allowed_legacy": [], "mappings": {}}
    ead = {"$schema": "https://www.example.org/existing-schema.json"}
    with configured_validator(settings, **schemes) as validator:
        with pytest.raises(
            EadSchemaValidationError, match="EAD does not match schema: 'something' is a required property"
        ):
            validator.validate(ead)


def test_succeeding_schema_validation_with_failing_indepth_validation():
    schemes = {
        "some-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
            "properties": {"something": {"type:": "number"}},
            "required": ["something"],
        }
    }
    settings = {"allowed": ["some-schema.json"], "allowed_legacy": [], "mappings": {}}
    ead = {"$schema": "https://www.example.org/some-schema.json", "something": 42}

    class RaisingInDepthValidator:
        @staticmethod
        def validate_ead(ead, namespaces):
            raise EadValidationError("Something is not correct")

    custom_validation_module = {".indepth.some_schema": RaisingInDepthValidator}
    with configured_validator(settings, **schemes) as validator:
        with mock.patch.object(ead_validator, "import_module", new=custom_validation_module.get):
            with pytest.raises(EadValidationError, match="Something is not correct"):
                validator.validate(ead)


def test_namespaces_are_passed_as_dict_to_indepth_validation():
    schemes = {
        "some-schema.json": {
            "$schema": "http://json-schema.org/draft-07/schema",
            "type": "object",
            "properties": {"something": {"type:": "number"}},
            "required": ["something"],
        }
    }
    namespaces = [{"namespace": "org.empaia.global.v1", "stuff": {"foo": {"name": "FOO"}}}]
    settings = {"allowed": ["some-schema.json"], "allowed_legacy": [], "mappings": {}}
    ead = {"$schema": "https://www.example.org/some-schema.json", "something": 42}
    custom_validation_module = {".indepth.some_schema": mock.Mock()}
    with configured_validator(settings, *namespaces, **schemes, enable_legacy_support=True) as validator:
        with mock.patch.object(ead_validator, "import_module", new=custom_validation_module.get):
            validator.validate(ead)
        namespaces_dict = {"org.empaia.global.v1": namespaces[0]}
        custom_validation_module[".indepth.some_schema"].validate_ead.assert_called_once_with(ead, namespaces_dict)
