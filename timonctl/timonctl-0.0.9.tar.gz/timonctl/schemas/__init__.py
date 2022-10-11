import os
import pkg_resources

import yamale

from .. import logger

SCHEMA_PATH = pkg_resources.resource_filename("timonctl", "schemas/")


def validate_content(content: str, schema: str):
    logger.debug(f"Validating YAML content with {schema} schema")
    schema = yamale.make_schema(os.path.join(SCHEMA_PATH, f"schema.{schema}.yaml"))
    data = yamale.make_data(content=content)

    try:
        yamale.validate(schema, data)
    except Exception as e:
        raise e
