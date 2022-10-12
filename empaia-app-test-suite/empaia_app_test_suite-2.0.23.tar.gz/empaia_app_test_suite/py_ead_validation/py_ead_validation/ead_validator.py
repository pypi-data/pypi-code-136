import json
from importlib import import_module
from pathlib import Path

import jsonschema

from .exceptions import EadSchemaMissingError, EadSchemaNotAvailableError, EadSchemaValidationError, EadValidationError


class EadValidator:
    def __init__(self, ead_schema_dir_path, namespaces_dir_path, ead_settings_path, enable_legacy_support=False):
        ead_settings = self._load_settings(ead_settings_path)
        self.ead_schemas = self._load_schemas(ead_schema_dir_path, ead_settings, enable_legacy_support)
        self.namespaces = self._load_namespaces(namespaces_dir_path)
        self.name_mappings = ead_settings["mappings"]

    @staticmethod
    def _load_settings(ead_settings_path):
        with open(ead_settings_path, encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _load_schemas(ead_schema_dir_path, ead_settings, enable_legacy_support):
        names = ead_settings["allowed"]
        if enable_legacy_support:
            names += ead_settings["allowed_legacy"]

        ead_schemas = {}

        for name in names:
            with open(Path(ead_schema_dir_path, name), encoding="utf-8") as f:
                ead_schemas[name] = json.load(f)

        for alt_name, name in ead_settings["mappings"].items():
            if name in ead_schemas:
                ead_schemas[alt_name] = ead_schemas[name]

        return ead_schemas

    @staticmethod
    def _load_namespaces(namespaces_dir_path):
        namespaces = {}
        for namespace_path in namespaces_dir_path.glob("*.json"):
            with open(namespace_path, encoding="utf-8") as namespace_file:
                namespace = json.load(namespace_file)
                namespace_id = namespace["namespace"]
                assert namespace_id not in namespaces
                namespaces[namespace_id] = namespace
        return namespaces

    @staticmethod
    def _get_schema_name(ead):
        if "$schema" not in ead:
            raise EadSchemaMissingError("EAD does not define a $schema.")
        return ead["$schema"].split("/")[-1]

    @staticmethod
    def _import_custom_validation_module_by_schema(schema_name):
        schema_stem = Path(schema_name).stem
        module_name = schema_stem.replace("-", "_")
        module_name = module_name.replace(".", "_")
        try:
            # we need to do it that complicated in order to let
            # this code work also in submodule usage of the library
            parent_package_name = ".".join(__name__.split(".")[:-1])
            return import_module(f".indepth.{module_name}", parent_package_name)
        except ModuleNotFoundError as e:
            raise EadValidationError(f"No custom EAD validation module found for {schema_name}") from e

    def validate(self, ead):
        self._validate_ead(ead)

    def validate_with_config(self, ead, config):
        self._validate_ead(ead)
        self._validate_config(config, ead)

    def _validate_ead(self, ead):
        self._validate_schema(ead)
        self._validate_in_depth(ead)

    def _validate_schema(self, ead):
        schema_name = self._get_schema_name(ead)
        if schema_name not in self.ead_schemas:
            raise EadSchemaNotAvailableError(f"EAD schema with name {schema_name} not found or not allowed.")
        try:
            jsonschema.validate(ead, self.ead_schemas[schema_name])
        except jsonschema.ValidationError as e:
            raise EadSchemaValidationError(f"EAD does not match schema: {e.message}") from e

    def _validate_in_depth(self, ead):
        validation_module = self._import_custom_validation_module(ead)
        validation_module.validate_ead(ead, self.namespaces)

    def _validate_config(self, config, ead):
        validation_module = self._import_custom_validation_module(ead)
        validation_module.validate_config(config, ead)

    def _import_custom_validation_module(self, ead):
        schema_name = self._get_schema_name(ead)
        if schema_name in self.name_mappings:
            schema_name = self.name_mappings[schema_name]
        return self._import_custom_validation_module_by_schema(schema_name)


def validate_ead(ead, enable_legacy_support=False):
    validator = _create_validator(ead, enable_legacy_support)
    validator.validate(ead)


def validate_ead_with_config(ead, config, enable_legacy_support=False):
    validator = _create_validator(ead, enable_legacy_support)
    validator.validate_with_config(ead, config)


def _create_validator(ead, enable_legacy_support):
    definitions_dir_path = Path(__file__).parent.resolve() / "definitions"
    ead_schema_dir_path = definitions_dir_path / "ead"
    namespaces_dir_path = definitions_dir_path / "namespaces"
    ead_settings_path = definitions_dir_path / "ead-settings.json"
    return EadValidator(ead_schema_dir_path, namespaces_dir_path, ead_settings_path, enable_legacy_support)
