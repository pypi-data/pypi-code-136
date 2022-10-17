# General imports
from json import loads as json_loads
from json import dumps as json_dumps
from logging import getLogger
from pathlib import Path
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

# 3rd party imports
from jsonschema import RefResolver
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

logger = getLogger(__name__)


class AlphaValidator:
    def __init__(self):
        self.schema_store: dict[str, dict] = self.__load_schema_store()
        logger.debug(f"The schema store looks like:\n-----------------\n{json_dumps(self.schema_store, indent=4, sort_keys=True)}\n---------------")
        self.resolver = RefResolver("", "", self.schema_store)

    def validate(self, file_path: Path, data: dict) -> bool:
        if data is None:
            return False

        # Isolates for which version we need to get
        version: str = data.get("version")
        if version is None:
            return False

        # Isolates for which schema type we need to get
        schema_type: str = data.get("schema")
        if schema_type is None:
            return False

        identified_schema = self.schema_store.get(f"{version}.{data.get('schema')}.json")
        logger.debug(f"The identified schema to use in validation is:\n{json_dumps(identified_schema, indent=4, sort_keys=True)}\n")

        validator = Draft202012Validator(identified_schema, resolver=self.resolver)
        try:
            validator.validate(data)
            logger.debug(f"Validation: Successfully validated file path: {file_path} using schema: pydotfiles.resources.schemas.{version}.{schema_type}")
            return True
        except ValidationError:
            logger.exception(f"Error when attempting to validate configuration file:\n{data=}\n")
            return False

    def __load_schema_store(self) -> dict[str, dict]:
        """
        Hardcoded for now to avoid doing a path walk and because this shouldn't change often
        """
        common_schema = self.__get_schema("alpha", "common")
        core_schema = self.__get_schema("alpha", "core")
        default_settings_schema = self.__get_schema("alpha", "default_settings")
        developer_environments_schema = self.__get_schema("alpha", "developer_environments")
        manifest_schema = self.__get_schema("alpha", "manifest")
        return {
            "alpha.common.json": common_schema,
            "alpha.core.json": core_schema,
            "alpha.default_settings.json": default_settings_schema,
            "alpha.developer_environments.json": developer_environments_schema,
            "alpha.manifest.json": manifest_schema,
        }

    def __get_schema(self, version: str, schema: str) -> dict:
        my_resources = files("pydotfiles")
        data = (my_resources / "resources" / "schemas" / version / f"{schema}.json").read_text()
        return json_loads(data)
