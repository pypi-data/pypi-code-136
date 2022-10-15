from __future__ import annotations

from datetime import date, datetime
import json
import random
import string
from typing import List, Optional, Union

from benchling_api_client.v2.alpha.models.app_config_item import AppConfigItem
from benchling_api_client.v2.alpha.models.base_manifest_config import BaseManifestConfig
from benchling_api_client.v2.alpha.models.benchling_app_manifest import BenchlingAppManifest
from benchling_api_client.v2.alpha.models.boolean_app_config_item import BooleanAppConfigItem
from benchling_api_client.v2.alpha.models.boolean_app_config_item_type import BooleanAppConfigItemType
from benchling_api_client.v2.alpha.models.date_app_config_item import DateAppConfigItem
from benchling_api_client.v2.alpha.models.date_app_config_item_type import DateAppConfigItemType
from benchling_api_client.v2.alpha.models.datetime_app_config_item import DatetimeAppConfigItem
from benchling_api_client.v2.alpha.models.datetime_app_config_item_type import DatetimeAppConfigItemType
from benchling_api_client.v2.alpha.models.dropdown_dependency import DropdownDependency
from benchling_api_client.v2.alpha.models.entity_schema_dependency import EntitySchemaDependency
from benchling_api_client.v2.alpha.models.field_app_config_item import FieldAppConfigItem
from benchling_api_client.v2.alpha.models.field_app_config_item_type import FieldAppConfigItemType
from benchling_api_client.v2.alpha.models.float_app_config_item import FloatAppConfigItem
from benchling_api_client.v2.alpha.models.float_app_config_item_type import FloatAppConfigItemType
from benchling_api_client.v2.alpha.models.generic_app_config_item import GenericAppConfigItem
from benchling_api_client.v2.alpha.models.generic_app_config_item_type import GenericAppConfigItemType
from benchling_api_client.v2.alpha.models.integer_app_config_item import IntegerAppConfigItem
from benchling_api_client.v2.alpha.models.integer_app_config_item_type import IntegerAppConfigItemType
from benchling_api_client.v2.alpha.models.json_app_config_item import JsonAppConfigItem
from benchling_api_client.v2.alpha.models.json_app_config_item_type import JsonAppConfigItemType
from benchling_api_client.v2.alpha.models.manifest_scalar_config import ManifestScalarConfig
from benchling_api_client.v2.alpha.models.resource_dependency import ResourceDependency
from benchling_api_client.v2.alpha.models.schema_dependency import SchemaDependency
from benchling_api_client.v2.alpha.models.secure_text_app_config_item import SecureTextAppConfigItem
from benchling_api_client.v2.alpha.models.secure_text_app_config_item_type import SecureTextAppConfigItemType
from benchling_api_client.v2.alpha.models.workflow_task_schema_dependency import WorkflowTaskSchemaDependency
from benchling_api_client.v2.beta.models.scalar_config_types import ScalarConfigTypes
from benchling_api_client.v2.stable.extensions import UnknownType

from benchling_sdk.apps.config.scalars import DateTimeScalar
from benchling_sdk.apps.helpers.config_helpers import (
    field_definitions_from_dependency,
    options_from_dependency,
    workflow_task_schema_output_from_dependency,
)

ManifestDependencies = Union[
    DropdownDependency,
    EntitySchemaDependency,
    ManifestScalarConfig,
    ResourceDependency,
    SchemaDependency,
    WorkflowTaskSchemaDependency,
    UnknownType,
]


def mock_app_config_items_from_manifest(manifest: BenchlingAppManifest) -> List[AppConfigItem]:
    """
    Mock Benchling App Config Items.

    This method accepts an app manifest model and creates mocked values for app the app config.

    The concrete mocked out values, such as API Ids and schema names are nonsensical and random,
    but are valid.

    Code should avoid relying on specific values or conventions (such as API prefixes). If
    specific dependency values need to be tested in isolation, the caller can selectively
    override the randomized values with with_dependency().
    """
    root_config_items = [_mock_dependency(dependency) for dependency in manifest.configuration]
    return [config_item for sub_config_items in root_config_items for config_item in sub_config_items]


def replace_mocked_config_item_by_path(
    original_config: List[AppConfigItem], replacement_path: List[str], replacement_item: AppConfigItem
) -> List[AppConfigItem]:
    """Return an updated list of app config items with a specific config item replaced with the provided mock."""
    replaced_config = [config for config in original_config if config.path != replacement_path]
    replaced_config.append(replacement_item)
    return replaced_config


def _mock_dependency(
    dependency: ManifestDependencies,
) -> List[AppConfigItem]:
    """Mock a dependency from its manifest definition."""
    if isinstance(dependency, DropdownDependency):
        config_item = GenericAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=GenericAppConfigItemType.DROPDOWN,
            value=_random_string("val_"),
        )
        sub_items = [
            _mock_subdependency(subdependency, dependency)
            for subdependency in options_from_dependency(dependency)
        ]
        return [config_item] + sub_items
    elif isinstance(dependency, EntitySchemaDependency):
        config_item = GenericAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=GenericAppConfigItemType(dependency.subtype),
            value=_random_string("val_"),
        )
        sub_items = [
            _mock_subdependency(subdependency, dependency)
            for subdependency in field_definitions_from_dependency(dependency)
        ]
        return [config_item] + sub_items
    elif isinstance(dependency, SchemaDependency):
        config_item = GenericAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=GenericAppConfigItemType(dependency.type),
            value=_random_string("val_"),
        )
        sub_items = [
            _mock_subdependency(subdependency, dependency)
            for subdependency in field_definitions_from_dependency(dependency)
        ]
        return [config_item] + sub_items
    elif isinstance(dependency, WorkflowTaskSchemaDependency):
        config_item = GenericAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=GenericAppConfigItemType.WORKFLOW_TASK_SCHEMA,
            value=_random_string("val_"),
        )
        sub_items = [
            _mock_subdependency(subdependency, dependency)
            for subdependency in field_definitions_from_dependency(dependency)
        ]
        workflow_task_output = workflow_task_schema_output_from_dependency(dependency)
        if workflow_task_output:
            output_fields = field_definitions_from_dependency(workflow_task_output)
            output_items = [
                _mock_workflow_output_subdependency(subdependency, dependency)
                for subdependency in output_fields
            ]
            sub_items += output_items
        return [config_item] + sub_items
    elif isinstance(dependency, ManifestScalarConfig):
        return [_mock_scalar_dependency(dependency)]
    elif isinstance(dependency, UnknownType):
        return UnknownType(value="Unknown")
    else:
        return [
            GenericAppConfigItem(
                id=_random_string("aci_"),
                path=[dependency.name],
                type=GenericAppConfigItemType(dependency.type),
                value=_random_string("val_"),
            )
        ]


def _mock_scalar_dependency(dependency: ManifestScalarConfig) -> AppConfigItem:
    if dependency.type == ScalarConfigTypes.BOOLEAN:
        return BooleanAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=BooleanAppConfigItemType.BOOLEAN,
            value=_mock_scalar_value(dependency.type),
        )
    elif dependency.type == ScalarConfigTypes.DATE:
        app_config = DateAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=DateAppConfigItemType.DATE,
            value=_mock_scalar_value(dependency.type),
        )
        return app_config
    elif dependency.type == ScalarConfigTypes.DATETIME:
        app_config = DatetimeAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=DatetimeAppConfigItemType.DATETIME,
            value=_mock_scalar_value(dependency.type),
        )
        return app_config
    elif dependency.type == ScalarConfigTypes.FLOAT:
        app_config = FloatAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=FloatAppConfigItemType.FLOAT,
            value=_mock_scalar_value(dependency.type),
        )
        return app_config
    elif dependency.type == ScalarConfigTypes.INTEGER:
        app_config = IntegerAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=IntegerAppConfigItemType.INTEGER,
            value=_mock_scalar_value(dependency.type),
        )
        return app_config
    elif dependency.type == ScalarConfigTypes.JSON:
        app_config = JsonAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=JsonAppConfigItemType.JSON,
            value=_mock_scalar_value(dependency.type),
        )
        return app_config
    elif dependency.type == ScalarConfigTypes.SECURE_TEXT:
        app_config = SecureTextAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=SecureTextAppConfigItemType.SECURE_TEXT,
            value=_mock_scalar_value(dependency.type),
        )
        return app_config
    else:
        return GenericAppConfigItem(
            id=_random_string("aci_"),
            path=[dependency.name],
            type=GenericAppConfigItemType.TEXT,
            value=_mock_scalar_value(dependency.type),
        )


def _mock_subdependency(subdependency: BaseManifestConfig, parent_config) -> AppConfigItem:
    if isinstance(parent_config, DropdownDependency):
        return GenericAppConfigItem(
            id=_random_string("aci_"),
            path=[parent_config.name, subdependency.name],
            type=GenericAppConfigItemType.DROPDOWN_OPTION,
            value=_random_string("opt_"),
        )
    elif isinstance(parent_config, (EntitySchemaDependency, SchemaDependency, WorkflowTaskSchemaDependency)):
        path = [parent_config.name, subdependency.name]
        app_config = FieldAppConfigItem(
            id=_random_string("aci_"),
            path=path,
            type=FieldAppConfigItemType.FIELD,
            value=_random_string("tsf_"),
        )
        return app_config


def _mock_workflow_output_subdependency(subdependency: BaseManifestConfig, parent_config) -> AppConfigItem:
    app_config = FieldAppConfigItem(
        id=_random_string("aci_"),
        path=[parent_config.name, "output", subdependency.name],
        type=FieldAppConfigItemType.FIELD,
        value=_random_string("tsf_"),
    )
    return app_config


def _mock_scalar_value(scalar_type: ScalarConfigTypes) -> Optional[str]:
    """Mock a scalar config value from its manifest definition."""
    if scalar_type == scalar_type.BOOLEAN:
        return "true"
    elif scalar_type == scalar_type.DATE:
        return date.today().strftime("%Y-%m-%d")
    elif scalar_type == scalar_type.DATETIME:
        return datetime.now().strftime(DateTimeScalar.expected_format())
    elif scalar_type == scalar_type.FLOAT:
        return str(random.random())
    elif scalar_type == scalar_type.INTEGER:
        return str(random.randint(-1000, 1000))
    elif scalar_type == scalar_type.JSON:
        return json.dumps(
            {_random_string(): [_random_string(), _random_string()], _random_string(): random.random()}
        )
    return _random_string()


def _random_string(prefix: str = "", random_length: int = 20) -> str:
    """Generate a randomized string up to a specified length with an optional prefix."""
    delimited_prefix = f"{prefix}-" if prefix else ""
    return f"{delimited_prefix}{''.join(random.choice(string.ascii_letters) for i in range(random_length))}"
