from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timedelta
from functools import cached_property, wraps
from math import ceil
from pathlib import Path
from types import FunctionType
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

import pandas as pd
from atoti_core import (
    BASE_SCENARIO_NAME,
    ColumnCoordinates,
    ComparisonOperator,
    Constant,
    DataType,
    HierarchyCoordinates,
    LevelCoordinates,
    MissingPluginError,
    convert_to_pandas,
    get_env_flag,
    is_array_type,
    is_numeric_array_type,
    is_numeric_type,
    keyword_only_dataclass,
    parse_data_type,
    running_in_ipython,
)
from py4j.clientserver import ClientServer, JavaParameters, PythonParameters
from py4j.java_collections import JavaMap
from py4j.java_gateway import JavaObject
from py4j.protocol import Py4JJavaError

from ._aggregate_provider_description import AggregateProviderDescription
from ._base_column_condition import ColumnConditionCoordinates
from ._endpoint import EndpointHandler
from ._exceptions import AtotiJavaException
from ._external_table_coordinates import ExternalTableCoordinates
from ._hierarchy_arguments import HierarchyArguments
from ._level_arguments import LevelArguments
from ._py4j_utils import (
    as_java_object,
    to_java_map,
    to_java_object_array,
    to_java_object_list,
    to_java_object_map,
    to_java_string_array,
    to_python_dict,
    to_python_list,
    to_python_object,
    to_store_field,
)
from ._query_plan import ExternalRetrieval, PivotRetrieval, QueryAnalysis, QueryPlan
from ._report import LoadingReport, _warn_new_errors
from ._sources.csv import CsvFileFormat
from ._transaction import Transaction, is_inside_transaction
from .config._session_config import SessionConfig, serialize_config_to_json
from .order import CustomOrder, NaturalOrder
from .order._order import Order
from .type import DataType

_VERBOSE_JAVA_EXCEPTIONS_ENV_VAR = "ATOTI_VERBOSE_JAVA_EXCEPTIONS"


def _parse_measure_data_type(value: str, /) -> DataType:
    parts = value.split("nullable ")
    return parse_data_type(parts[-1])


def _to_data_type(java_type: Any, /) -> DataType:
    return parse_data_type(java_type.getJavaType())


def _convert_java_levels_to_level_arguments(
    java_levels: JavaMap,  # pyright: ignore[reportUnknownParameterType]
) -> Dict[str, LevelArguments]:
    java_levels_dict = to_python_dict(java_levels)
    levels = {}
    for name, java_level in java_levels_dict.items():
        comparator_key = java_level.comparatorPluginKey()
        first_elements = (
            list(java_level.firstMembers())
            if java_level.firstMembers() is not None
            else None
        )
        order = _java_comparator_to_python_order(
            comparator_key=comparator_key,
            first_elements=first_elements,
        )
        levels[name] = (
            name,
            ColumnCoordinates(
                table_name=java_level.getTableName(),
                column_name=java_level.getFieldName(),
            ),
            _to_data_type(java_level.type()),
            order,
        )
    return levels


def _java_comparator_to_python_order(
    *, comparator_key: str, first_elements: Optional[Sequence[Any]] = None
) -> Order:
    if comparator_key == CustomOrder(first_elements=())._key:
        return CustomOrder(first_elements=first_elements or [])

    return NaturalOrder(ascending="reverse" not in comparator_key.lower())


def _convert_java_description_to_level_coordinates(
    java_description: str,
) -> LevelCoordinates:
    level, hierarchy, dimension = java_description.split("@")
    return LevelCoordinates(dimension, hierarchy, level)


def _convert_java_hierarchy_to_python_hierarchy_arguments(
    java_hierarchy: Any,
) -> HierarchyArguments:
    return HierarchyArguments(
        name=java_hierarchy.name(),
        levels_arguments=_convert_java_levels_to_level_arguments(
            java_hierarchy.levels()
        ),
        dimension=java_hierarchy.dimensionName(),
        slicing=java_hierarchy.slicing(),
        visible=java_hierarchy.visible(),
        virtual=java_hierarchy.virtual(),
    )


def _enhance_py4j_errors(function: Callable[[Any], Any]) -> Callable[[Any], Any]:
    @wraps(function)
    def wrapped_method(self: JavaApi, *args: Any, **kwargs: Any) -> Any:
        try:
            return function(self, *args, **kwargs)
        except Py4JJavaError as java_exception:
            cause = (
                str(java_exception)
                if get_env_flag(_VERBOSE_JAVA_EXCEPTIONS_ENV_VAR)
                else self.get_throwable_root_cause(java_exception.java_exception)
            )
            raise AtotiJavaException(
                cause,
                java_traceback=str(java_exception),
                java_exception=java_exception,
            ) from None

    return wrapped_method


def _convert_java_column_types(schema: Any, /) -> Mapping[str, DataType]:
    field_names = list(schema.fieldNames())
    field_types = list(schema.types())
    return {
        field_names[i]: _to_data_type(field_types[i])
        for i in range(0, len(field_names))
    }


def _convert_java_table_list(
    java_list: Any,
) -> Dict[str, Dict[str, List[ExternalTableCoordinates]]]:
    return {
        database_name: {
            schema_name: [
                ExternalTableCoordinates(
                    database_name=database_name,
                    schema_name=schema_name,
                    table_name=t,
                )
                for t in to_python_list(tables)
            ]
            for schema_name, tables in to_python_dict(schemas).items()
        }
        for database_name, schemas in to_python_dict(java_list).items()
    }


class ApiMetaClass(type):
    """Meta class for the API calls."""

    def __new__(  # pylint: disable=too-many-positional-parameters
        cls, classname: str, bases: Tuple[type, ...], class_dict: Mapping[str, Any]
    ) -> ApiMetaClass:
        """Automatically wrap all of the classes methods.

        This class applies the api_call_wrapper to all of a particular classes methods.
        This allows for cleaner handling of Py4J related exceptions.
        """
        new_class_dict = {}
        for attribute_name, attribute in class_dict.items():
            if isinstance(attribute, FunctionType):
                attribute = _enhance_py4j_errors(attribute)
            new_class_dict[attribute_name] = attribute
        return type.__new__(cls, classname, bases, new_class_dict)


_REALTIME_SOURCE_KEYS = ["KAFKA"]

# pylint: disable=too-many-lines
class JavaApi(metaclass=ApiMetaClass):
    """API for communicating with the JVM."""

    def __init__(
        self,
        *,
        auth_token: Optional[str] = None,
        py4j_java_port: Optional[int] = None,
        distributed: bool = False,
    ):
        """Create the Java gateway."""
        self.gateway: ClientServer = JavaApi._create_py4j_gateway(
            auth_token=auth_token, py4j_java_port=py4j_java_port
        )
        self.java_session: JavaObject = self.gateway.entry_point
        self.java_session.api(distributed)

    @property
    def java_api(self) -> Any:
        return self.java_session.api()

    @staticmethod
    def _create_py4j_gateway(
        *, auth_token: Optional[str] = None, py4j_java_port: Optional[int] = None
    ) -> ClientServer:
        # Connect to the Java side using the provided Java port and start the Python callback server with a dynamic port.
        gateway = ClientServer(
            java_parameters=JavaParameters(auth_token=auth_token, port=py4j_java_port),
            python_parameters=PythonParameters(daemonize=True, port=0),
        )

        # Retrieve the port on which the python callback server was bound to.
        cb_server = gateway.get_callback_server()
        if cb_server is None:
            raise ValueError("Null callback server from py4j gateway")
        python_port = cb_server.get_listening_port()

        # Tell the Java side to connect to the Python callback server with the new Python port.
        gateway_server = gateway.java_gateway_server
        if gateway_server is None:
            raise ValueError("Null gateway server from py4j gateway")
        # ignore type next line because we do some Java calls
        gateway_server.resetCallbackClient(
            gateway_server.getCallbackClient().getAddress(),
            python_port,
        )

        return gateway

    def shutdown(self) -> None:
        """Shutdown the connection to the Java gateway."""
        self.gateway.shutdown()

    def refresh(self) -> None:
        """Refresh the Java session."""
        self.java_api.refresh()
        _warn_new_errors(self.get_new_load_errors())

    @cached_property
    def license_end_date(self) -> datetime:
        return datetime.fromtimestamp(self.java_session.getLicenseEndDate() / 1000)

    @cached_property
    def is_community_license(self) -> bool:
        return cast(bool, self.java_session.isCommunityLicense())

    def publish_measures(self, cube_name: str) -> None:
        """Publish the new measures."""
        self._outside_transaction_api().publishMeasures(cube_name)

    def clear_session(self) -> None:
        """Refresh the pivot."""
        self.java_api.clearSession()

    def get_session_port(self) -> int:
        """Return the port of the session."""
        return cast(int, self.java_session.getPort())

    def get_throwable_root_cause(self, throwable: Any) -> str:
        """Get the root cause of a java exception."""
        return cast(str, self.java_api.getRootCause(throwable))

    def generate_jwt(self) -> str:
        """Return the JWT required to authenticate against to this session."""
        return cast(str, self.java_session.generateJwt())

    def create_endpoint(
        self,
        *,
        http_method: Literal["POST", "GET", "PUT", "DELETE"],
        route: str,
        handler: EndpointHandler,
    ) -> None:
        """Create a new custom endpoint."""
        self._outside_transaction_api().createEndpoint(
            http_method,
            route,
            handler,
        )

    def delete_role(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def upsert_role(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_role_mapping(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def upsert_role_mapping(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def remove_role_from_role_mapping(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def set_locale(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> None:
        """Set the locale to use for the session."""
        raise MissingPluginError("plus")

    def export_i18n_template(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        """Generate a template translations file at the desired location."""
        raise MissingPluginError("plus")

    def start_application(self, config: SessionConfig) -> None:
        """Start the application."""
        json_config = serialize_config_to_json(config)
        self.java_session.startServer(json_config)

    def _create_java_types(
        self,
        types: Mapping[str, DataType],
        /,
        *,
        default_values: Mapping[str, Any],
        keys: Collection[str],
    ) -> JavaMap:
        """Convert the Python types to Java types."""
        # pylint: disable=invalid-name
        TypeImpl: Any = self.gateway.jvm.io.atoti.loading.impl.TypeImpl
        # pylint: enable=invalid-name

        java_types: Dict[str, Any] = {}

        for column_name, data_type in types.items():
            if column_name in default_values:
                if default_values[column_name] is None:
                    java_types[column_name] = TypeImpl(data_type, True)
                else:
                    java_types[column_name] = TypeImpl(
                        data_type,
                        False,
                        as_java_object(
                            default_values[column_name], gateway=self.gateway
                        ),
                    )
            else:
                is_numeric_column = is_numeric_type(data_type) or is_numeric_array_type(
                    data_type
                )
                java_types[column_name] = TypeImpl(
                    data_type,
                    is_numeric_column and column_name not in keys,
                )

        return to_java_map(java_types, gateway=self.gateway)

    def _get_java_type_from_data_type(self, data_type: DataType, /) -> JavaObject:
        return self.gateway.jvm.io.atoti.loading.impl.TypeImpl(data_type, True)

    def _outside_transaction_api(self) -> Any:
        return self.java_api.outsideTransactionApi(is_inside_transaction())

    def _enterprise_api(self) -> Any:
        return self.java_api.enterpriseApi(is_inside_transaction())

    def get_table_names(self) -> List[str]:
        return to_python_list(self.java_api.getStoreNames())

    def create_table_parameters(
        self,
        *,
        keys: Iterable[str],
        partitioning: Optional[str],
        types: Mapping[str, DataType],
        default_values: Mapping[str, Any],
        is_parameter_table: bool,
    ) -> JavaObject:
        return self.gateway.jvm.io.atoti.loading.impl.StoreParams(
            to_java_object_list(keys, gateway=self.gateway),
            partitioning,
            self._create_java_types(
                types, default_values=default_values, keys=list(keys)
            ),
            is_parameter_table,
        )

    def create_loading_parameters(
        self,
        *,
        scenario_name: str,
    ) -> JavaObject:
        return self.gateway.jvm.io.atoti.loading.impl.LoadingParams().setBranch(
            scenario_name
        )

    def create_table(
        self,
        name: str,
        *,
        types: Mapping[str, DataType],
        keys: Iterable[str],
        partitioning: Optional[str],
        default_values: Mapping[str, Any],
        is_parameter_table: bool,
    ) -> None:
        """Create a java store from its schema."""
        table_params = self.create_table_parameters(
            keys=keys,
            partitioning=partitioning,
            types=types,
            default_values=default_values,
            is_parameter_table=is_parameter_table,
        )
        self._outside_transaction_api().createStore(name, table_params)
        self.refresh()

    def delete_table(self, table_name: str) -> None:
        self._outside_transaction_api().deleteStore(table_name)

    def convert_source_params(self, params: Mapping[str, Any]) -> JavaMap:
        """Convert the params to Java Objects."""
        java_params = {}
        for param in params:
            value = params[param]
            if isinstance(value, Mapping):
                value = to_java_map(value, gateway=self.gateway)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                value = to_java_object_list(value, gateway=self.gateway)
            java_params[param] = value
        return to_java_map(java_params, gateway=self.gateway)

    def discover_csv_file_format(
        self,
        *,
        keys: Iterable[str],
        default_values: Mapping[str, Any],
        source_params: Mapping[str, Any],
    ) -> CsvFileFormat:
        source_params = self.convert_source_params(source_params)
        java_csv_format = self._outside_transaction_api().discoverCsvFileFormat(
            to_java_object_list(keys, gateway=self.gateway),
            to_java_object_map(default_values, gateway=self.gateway),
            source_params,
        )
        types: Mapping[str, DataType] = {
            column_name: _to_data_type(java_type)
            for column_name, java_type in to_python_dict(
                java_csv_format.getTypes()
            ).items()
        }
        file_format = CsvFileFormat(
            process_quotes=java_csv_format.shouldProcessQuotes(),
            separator=java_csv_format.separator(),
            types=types,
        )
        return file_format

    def infer_table_types_from_source(
        self,
        *,
        source_key: str,
        keys: Iterable[str],
        default_values: Mapping[str, Any],
        source_params: Mapping[str, Any],
    ) -> Dict[str, DataType]:
        """Infer Table types from a data source."""
        source_params = self.convert_source_params(source_params)
        java_column_types = to_python_dict(
            self._outside_transaction_api().inferTypesFromDataSource(
                source_key,
                to_java_object_list(keys, gateway=self.gateway),
                to_java_object_map(default_values, gateway=self.gateway),
                source_params,
            )
        )
        return {
            column_name: _to_data_type(java_type)
            for column_name, java_type in java_column_types.items()
        }

    def load_data_into_table(
        self,
        table_name: str,
        *,
        source_key: str,
        scenario_name: str,
        source_params: Mapping[str, Any],
    ) -> None:
        """Load the data into an existing table with a given source."""
        source_params = self.convert_source_params(source_params)
        load_params = self.create_loading_parameters(scenario_name=scenario_name)
        if scenario_name == BASE_SCENARIO_NAME and self.java_api.isParameterStore(
            table_name
        ):
            for scenario in self.get_scenarios():
                self._inside_transaction(
                    lambda: cast(
                        None,
                        self.java_api.loadDataSourceIntoStore(
                            table_name,
                            source_key,
                            load_params,
                            source_params,
                        ),
                    ),
                    scenario_name=scenario,
                    source_key=source_key,
                )
        else:
            self._inside_transaction(
                lambda: cast(
                    None,
                    self.java_api.loadDataSourceIntoStore(
                        table_name,
                        source_key,
                        load_params,
                        source_params,
                    ),
                ),
                scenario_name=scenario_name,
                source_key=source_key,
            )

        # Check if errors happened during the loading
        _warn_new_errors(self.get_new_load_errors())

    def create_scenario(self, scenario_name: str, parent_scenario: str) -> None:
        self._outside_transaction_api().createBranch(scenario_name, parent_scenario)

    def get_scenarios(self) -> List[str]:
        return to_python_list(self.java_api.getBranches())

    def delete_scenario(self, scenario: str) -> None:
        self._outside_transaction_api().deleteBranch(scenario)

    def start_transaction(self, *, scenario_name: str, is_user_initiated: bool) -> int:
        """Start a multi operation transaction on the datastore."""
        return cast(
            int, self.java_api.startTransaction(scenario_name, is_user_initiated)
        )

    def end_transaction(
        self, *, has_succeeded: bool, transaction_id: Optional[int]
    ) -> None:
        """End a multi operation transaction on the datastore."""
        self.java_api.endTransaction(has_succeeded, transaction_id)

    def get_aggregates_cache_capacity(self, *, cube_name: str) -> int:
        java_cache_description = (
            self._outside_transaction_api().getAggregatesCacheDescription(cube_name)
        )
        return cast(int, java_cache_description.getSize())

    def set_aggregates_cache_capacity(self, capacity: int, *, cube_name: str) -> None:
        self._outside_transaction_api().setAggregatesCache(cube_name, capacity)

    def _convert_aggregate_provider(
        self,
        description: AggregateProviderDescription,
        /,
    ) -> JavaObject:
        plugin_key = description.key.upper()
        levels = to_java_object_list(
            [
                level_coordinates.java_description
                for level_coordinates in description.levels_coordinates
            ],
            gateway=self.gateway,
        )
        measures = to_java_object_list(
            description.measures_names,
            gateway=self.gateway,
        )
        filters = to_java_map(
            {
                level_coordinates.java_description: to_java_object_list(
                    [
                        as_java_object(value.value, gateway=self.gateway)
                        for value in values
                    ],
                    gateway=self.gateway,
                )
                for level_coordinates, values in description.filters.items()
            },
            gateway=self.gateway,
        )
        return (
            self.gateway.jvm.io.atoti.api.impl.AggregateProviderDescription.builder()
            .pluginKey(plugin_key)
            .levelDescriptions(levels)
            .measures(measures)
            .partitioning(description.partitioning)
            .filters(filters)
            .build()
        )

    def _convert_provider_description_mapping(
        self, providers: Mapping[str, AggregateProviderDescription]
    ) -> JavaMap:
        return to_java_map(
            {
                name: self._convert_aggregate_provider(provider_description)
                for name, provider_description in providers.items()
            },
            gateway=self.gateway,
        )

    def get_aggregate_providers_attributes(
        self,
        cube_name: str,
        /,
    ) -> Mapping[str, AggregateProviderDescription]:
        java_providers = self._outside_transaction_api().getAggregateProviders(
            cube_name
        )
        return {
            name: AggregateProviderDescription(
                key=description.pluginKey().lower(),
                levels_coordinates=[
                    _convert_java_description_to_level_coordinates(level)
                    for level in to_python_list(description.levelDescriptions())
                ],
                measures_names=to_python_list(description.measures()),
                partitioning=description.partitioning(),
                filters={
                    _convert_java_description_to_level_coordinates(level): [
                        Constant(member) for member in to_python_list(members)
                    ]
                    for level, members in (
                        {}
                        if description.filters() is None
                        else to_python_dict(description.filters())
                    ).items()
                },
            )
            for name, description in to_python_dict(java_providers).items()
        }

    def add_aggregate_providers(
        self,
        descriptions: Mapping[str, AggregateProviderDescription],
        /,
        *,
        cube_name: str,
    ) -> None:
        self._outside_transaction_api().addAggregateProviders(
            self._convert_provider_description_mapping(descriptions), cube_name
        )

    def remove_aggregate_providers(
        self,
        names: Optional[Iterable[str]] = None,
        /,
        *,
        cube_name: str,
    ) -> None:
        if names is None:
            self._outside_transaction_api().clearAggregateProviders(cube_name)
            return

        if not self._outside_transaction_api().removeAggregateProviders(
            to_java_object_list(
                names,
                gateway=self.gateway,
            ),
            cube_name,
        ):
            raise KeyError(names)

    def join_distributed_cluster(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        """Join the distributed cluster at the given address for the given distributed cube."""
        raise MissingPluginError("plus")

    def get_table_column_names(self, table_name: str, /) -> List[str]:
        return cast(List[str], self.java_api.getTableFieldNames(table_name))

    def get_table_partitioning(self, table_name: str) -> str:
        """Return the table's partitioning."""
        return cast(
            str, self._outside_transaction_api().getStorePartitioning(table_name)
        )

    def get_column_data_type(self, column_name: str, /, *, table_name: str) -> DataType:
        return _to_data_type(self.java_api.getFieldType(column_name, table_name))

    @staticmethod
    def _convert_reports(reports: Iterable[Any]) -> List[LoadingReport]:
        """Convert the Java report to Python ones."""
        return [
            LoadingReport(
                name=r.getName(),
                source=r.getType(),
                loaded=r.getLoadedCount(),
                errors=r.getErrorCount(),
                duration=r.getDuration(),
                error_messages=to_python_list(r.getFailureMessages()),
            )
            for r in reports
        ]

    def clear_loading_report(self, table_name: str, /) -> None:
        self.java_api.clearLoadingReports(table_name)

    def get_loading_report(self, table_name: str, /) -> List[LoadingReport]:
        return self._convert_reports(
            to_python_list(self.java_api.getLoadingReports(table_name))
        )

    def get_new_load_errors(self) -> Dict[str, int]:
        """Return the new loading errors per table."""
        errors = self.java_api.getNewLoadingErrors()
        return to_python_dict(errors)

    def get_key_columns(self, table_name: str) -> List[str]:
        return to_python_list(self.java_api.getStoreKeyFieldNames(table_name))

    def get_selection_fields(self, cube_name: str) -> List[ColumnCoordinates]:
        """Return the list of fields that are part of the cube's datastore selection."""
        java_fields = self._outside_transaction_api().getSelectionFields(cube_name)
        return [
            ColumnCoordinates(
                table_name=java_field.getStore(), column_name=java_field.getName()
            )
            for java_field in to_python_list(java_fields)
        ]

    def create_cube_from_table(
        self,
        *,
        table_name: str,
        cube_name: str,
        creation_mode: str,
    ) -> None:
        self._outside_transaction_api().createCubeFromStore(
            table_name, cube_name, creation_mode
        )

    def create_distributed_cube(self, cube_name: str) -> None:
        self.java_api.createDistributedCube(cube_name)

    def generate_schema_graph(self, *, cube_name: Optional[str] = None) -> Any:
        """Generate the schema graph of the given cube (or the whole datastore if *cube_name* is ``None``)."""
        path: str

        try:
            path = cast(
                str, self._outside_transaction_api().generateSchemaGraph(cube_name)
            )
        except Py4JJavaError as error:
            logging.getLogger("atoti").warning(error)
            return

        if running_in_ipython():
            from IPython.display import (  # pylint: disable=undeclared-dependency, nested-import
                SVG,
            )

            return SVG(filename=path)

        return Path(path)

    def delete_cube(self, cube_name: str) -> None:
        if not self._outside_transaction_api().deleteCube(cube_name):
            raise KeyError(cube_name)

    def create_join(
        self,
        table_name: str,
        other_table_name: str,
        *,
        mapping: Optional[Mapping[str, str]],
    ) -> None:
        """Define a join between two tables."""
        java_mapping = (
            to_java_map(mapping, gateway=self.gateway) if mapping is not None else None
        )

        self._outside_transaction_api().createJoin(
            table_name, other_table_name, java_mapping
        )

        self.refresh()

    def get_table_size(self, table_name: str, *, table_scenario: str) -> int:
        """Get the size of the table on its current scenario."""
        return cast(
            int,
            self._outside_transaction_api().getStoreSize(table_name, table_scenario),
        )

    def _build_java_column_condition(
        self,
        column_name: str,
        *,
        value: Any,
        comparison_operator: Literal[ComparisonOperator, "isin"],
        column_data_type: DataType,
    ) -> JavaObject:
        # pylint: disable=invalid-name
        ColumnCondition = self.gateway.jvm.io.atoti.api.impl.ColumnCondition
        # pylint: enable=invalid-name
        comparison_operator_to_java_enum = {
            "eq": ColumnCondition.ComparisonOperator.EQ,
            "ne": ColumnCondition.ComparisonOperator.NE,
            "lt": ColumnCondition.ComparisonOperator.LT,
            "le": ColumnCondition.ComparisonOperator.LE,
            "gt": ColumnCondition.ComparisonOperator.GT,
            "ge": ColumnCondition.ComparisonOperator.GE,
            "isin": ColumnCondition.ComparisonOperator.ISIN,
        }
        return (
            ColumnCondition.builder()
            .fieldName(column_name)
            .value(
                as_java_object(value, gateway=self.gateway, data_type=column_data_type)
                if comparison_operator != "isin"
                else to_java_object_array(
                    [
                        as_java_object(
                            item,
                            gateway=self.gateway,
                            data_type=column_data_type,
                        )
                        for item in value
                    ],
                    gateway=self.gateway,
                )
            )
            .comparisonOperator(comparison_operator_to_java_enum[comparison_operator])
            .fieldType(self._get_java_type_from_data_type(column_data_type))
            .build()
        )

    def delete_rows_from_table(
        self,
        *,
        table_name: str,
        scenario_name: str,
        coordinates: Iterable[Iterable[ColumnConditionCoordinates]],
    ) -> None:
        """Delete rows from the table matching the provided coordinates."""
        java_column_conditions = None
        if coordinates:
            java_column_conditions = to_java_object_list(
                [
                    to_java_object_list(
                        [
                            self._build_java_column_condition(
                                condition[0],
                                value=condition[1],
                                comparison_operator=condition[2],
                                column_data_type=condition[3],
                            )
                            for condition in and_conditions
                        ],
                        gateway=self.gateway,
                    )
                    for and_conditions in coordinates
                ],
                gateway=self.gateway,
            )
        self._inside_transaction(
            lambda: cast(
                None,
                self.java_api.deleteOnStoreBranch(
                    table_name, scenario_name, java_column_conditions
                ),
            ),
            scenario_name=scenario_name,
        )

    def get_table_dataframe(
        self,
        table_name: str,
        n: int,
        *,
        types: Mapping[str, DataType],
        keys: Iterable[str],
        scenario_name: str,
    ) -> pd.DataFrame:
        """Return the first given rows of the table as a pandas DataFrame."""
        dataframe_view = self._outside_transaction_api().dataFrameRowsAndHeaders(
            table_name, scenario_name, n
        )

        headers = to_python_list(dataframe_view.contentHeader())
        rows = to_python_list(dataframe_view.contentRows())

        data_types = list(types.values())
        data = [
            [
                cell.toString()
                if isinstance(cell, JavaObject)
                and not is_array_type(data_types[column_index])
                else cell
                for column_index, cell in enumerate(row)
            ]
            for row in rows
        ]

        dataframe = pd.DataFrame(
            data=data,
            columns=headers,
        )

        for name, data_type in types.items():
            dataframe[name] = convert_to_pandas(
                dataframe[name].apply(
                    lambda cell: None if cell is None else to_python_list(cell)
                )
                if is_array_type(data_type)
                else dataframe[name],
                data_type=data_type,
            )

        if keys:
            dataframe.set_index(keys, inplace=True)

        return dataframe

    def update_hierarchies_for_cube(
        self,
        cube_name: str,
        *,
        structure: Mapping[str, Mapping[str, Mapping[str, ColumnCoordinates]]],
    ) -> None:
        java_structure = to_java_map(
            {
                dimension_name: to_java_map(
                    {
                        hierarchy_name: to_java_map(
                            {
                                name: to_store_field(column, gateway=self.gateway)
                                for name, column in levels.items()
                            },
                            gateway=self.gateway,
                        )
                        for hierarchy_name, levels in hierarchy.items()
                    },
                    gateway=self.gateway,
                )
                for dimension_name, hierarchy in structure.items()
            },
            gateway=self.gateway,
        )
        self._outside_transaction_api().updateHierarchiesForCube(
            cube_name, java_structure
        )

    def create_analysis_hierarchy(
        self, name: str, *, cube_name: str, table_name: str, column_name: str
    ) -> None:
        """Create an analysis hierarchy from an existing table column."""
        self._outside_transaction_api().createAnalysisHierarchy(
            cube_name,
            name,
            table_name,
            column_name,
        )

    def create_date_hierarchy(
        self,
        *,
        cube_name: str,
        table_name: str,
        field: str,
        hierarchy_name: str,
        levels: Mapping[str, str],
    ) -> None:
        self._outside_transaction_api().createDateHierarchy(
            cube_name,
            table_name,
            field,
            hierarchy_name,
            to_java_map(levels, gateway=self.gateway),
        )

    def update_hierarchy_coordinate(
        self,
        *,
        cube_name: str,
        hierarchy_coordinates: HierarchyCoordinates,
        new_dim: str,
        new_hierarchy: str,
    ) -> None:
        self._outside_transaction_api().updateHierarchyCoordinate(
            cube_name,
            hierarchy_coordinates.java_description,
            HierarchyCoordinates(new_dim, new_hierarchy).java_description,
        )

    def update_hierarchy_slicing(
        self,
        *,
        cube_name: str,
        hierarchy_coordinates: HierarchyCoordinates,
        slicing: bool,
    ) -> None:
        """Update whether the hierarchy is slicing or not."""
        self._outside_transaction_api().setHierarchySlicing(
            cube_name,
            hierarchy_coordinates.java_description,
            slicing,
        )

    def update_hierarchy_virtual(
        self,
        *,
        cube_name: str,
        hierarchy_coordinates: HierarchyCoordinates,
        virtual: bool,
    ) -> None:
        self._outside_transaction_api().setHierarchyVirtual(
            cube_name,
            hierarchy_coordinates.java_description,
            virtual,
        )

    def update_level_order(
        self,
        order: Order,
        *,
        cube_name: str,
        level_coordinates: LevelCoordinates,
    ) -> None:
        comparator_key = order._key if order is not None else None
        first_elements = (
            to_java_object_array(order.first_elements, gateway=self.gateway)
            if isinstance(order, CustomOrder)
            else None
        )

        self._outside_transaction_api().updateLevelComparator(
            cube_name,
            level_coordinates.java_description,
            comparator_key,
            first_elements,
        )

    def delete_level(
        self, level_coordinates: LevelCoordinates, /, *, cube_name: str
    ) -> None:
        if (
            self._outside_transaction_api()
            .removeLevel(level_coordinates.java_description, cube_name)
            .isEmpty()
        ):
            raise KeyError(level_coordinates.level_name)

    def delete_hierarchy(
        self, hierarchy_coordinates: HierarchyCoordinates, /, *, cube_name: str
    ) -> None:
        if (
            self._outside_transaction_api()
            .removeHierarchy(hierarchy_coordinates.java_description, cube_name)
            .isEmpty()
        ):
            raise KeyError(hierarchy_coordinates.hierarchy_name)

    def get_cubes(self) -> List[JavaObject]:
        return to_python_list(self._outside_transaction_api().getCubes())

    def get_cube(self, cube_name: str) -> JavaObject:
        cube = self._outside_transaction_api().getCube(cube_name)
        if cube.isEmpty():
            raise KeyError(cube_name)
        return cube.orElseThrow()

    def get_hierarchies(
        self,
        *,
        cube_name: str,
    ) -> Dict[HierarchyCoordinates, HierarchyArguments]:
        java_hierarchies = self._outside_transaction_api().getHierarchies(cube_name)
        return {
            HierarchyCoordinates(hierarchy.dimension, hierarchy.name): hierarchy
            for hierarchy in [
                _convert_java_hierarchy_to_python_hierarchy_arguments(java_hierarchy)
                for java_hierarchy in to_python_dict(java_hierarchies).values()
            ]
        }

    def get_hierarchy(
        self,
        name: str,
        /,
        *,
        cube_name: str,
        dimension_name: Optional[str],
    ) -> HierarchyArguments:
        java_hierarchy = self._outside_transaction_api().getHierarchy(
            cube_name, dimension_name, name
        )
        if java_hierarchy.isEmpty():
            raise KeyError(name)
        return _convert_java_hierarchy_to_python_hierarchy_arguments(
            java_hierarchy.orElseThrow()
        )

    def find_level_hierarchy(
        self,
        level_name: str,
        /,
        *,
        cube_name: str,
        dimension_name: Optional[str],
        hierarchy_name: Optional[str],
    ) -> HierarchyArguments:
        java_hierarchy = self._outside_transaction_api().findLevelHierarchy(
            cube_name, dimension_name, hierarchy_name, level_name
        )
        if java_hierarchy.isEmpty():
            raise KeyError(level_name)
        return _convert_java_hierarchy_to_python_hierarchy_arguments(
            java_hierarchy.orElseThrow()
        )

    def set_hierarchy_visibility(
        self,
        *,
        cube_name: str,
        dimension: Optional[str],
        name: str,
        visible: bool,
    ) -> None:
        self._outside_transaction_api().setHierarchyVisibility(
            visible, name, dimension, cube_name
        )

    def set_measure_folder(
        self, *, cube_name: str, measure_name: str, folder: Optional[str]
    ) -> None:
        self._outside_transaction_api().setMeasureFolder(
            folder, measure_name, cube_name
        )

    def set_measure_formatter(
        self, *, cube_name: str, measure_name: str, formatter: Optional[str]
    ) -> None:
        self._outside_transaction_api().setMeasureFormatter(
            formatter, measure_name, cube_name
        )

    def set_measure_visibility(
        self, *, cube_name: str, measure_name: str, visible: Optional[bool]
    ) -> None:
        self._outside_transaction_api().setMeasureVisibility(
            visible, measure_name, cube_name
        )

    def set_measure_description(
        self, *, cube_name: str, measure_name: str, description: Optional[str]
    ) -> None:
        self._outside_transaction_api().setMeasureDescription(
            description, measure_name, cube_name
        )

    @keyword_only_dataclass
    @dataclass(frozen=True)
    class JavaMeasureDescription:
        """Description of a measure to build."""

        folder: str
        formatter: str
        visible: bool
        underlying_type: DataType
        description: Optional[str]

    def get_measures(self, cube_name: str) -> Dict[str, JavaApi.JavaMeasureDescription]:
        """Retrieve the list of the cube's measures, including their required levels."""
        java_measures = self._outside_transaction_api().getMeasures(cube_name)
        measures = to_python_list(java_measures)
        final_measures: Dict[str, JavaApi.JavaMeasureDescription] = {}
        for measure in measures:
            final_measures[measure.name()] = JavaApi.JavaMeasureDescription(
                folder=measure.folder(),
                formatter=measure.formatter(),
                visible=measure.visible(),
                underlying_type=_parse_measure_data_type(measure.type()),
                description=measure.description(),
            )
        return final_measures

    def get_measure(
        self, measure_name: str, /, *, cube_name: str
    ) -> JavaApi.JavaMeasureDescription:
        measure = self._outside_transaction_api().getMeasure(measure_name, cube_name)
        if measure.isEmpty():
            raise KeyError(measure_name)
        measure = measure.orElseThrow()
        return JavaApi.JavaMeasureDescription(
            folder=measure.folder(),
            formatter=measure.formatter(),
            visible=measure.visible(),
            underlying_type=_parse_measure_data_type(measure.type()),
            description=measure.description(),
        )

    @staticmethod
    def create_retrieval(java_retrieval: Any) -> PivotRetrieval:
        """Convert Java retrieval to Python."""
        loc_str = ", ".join(
            [
                str(loc.getDimension())
                + "@"
                + str(loc.getHierarchy())
                + "@"
                + "\\".join(to_python_list(loc.getLevel()))
                + ": "
                + "\\".join(str(x) for x in to_python_list(loc.getPath()))
                for loc in to_python_list(java_retrieval.getLocation())
            ]
        )
        timings = to_python_dict(java_retrieval.getTimingInfo())
        return PivotRetrieval(
            id=java_retrieval.getRetrievalId(),
            retrieval_type=java_retrieval.getType(),
            location=loc_str,
            filter_id=java_retrieval.getFilterId(),
            measures=to_python_list(java_retrieval.getMeasures()),
            start_times=list(timings.get("startTime", [])),
            elapsed_times=list(timings.get("elapsedTime", [])),
            result_sizes=list(java_retrieval.getResultSizes()),
            retrieval_filter=str(java_retrieval.getFilterId()),
            partitioning=java_retrieval.getPartitioning(),
            measures_provider=java_retrieval.getMeasureProvider(),
        )

    @staticmethod
    def create_external_retrieval(java_retrieval: Any) -> ExternalRetrieval:
        timings = to_python_dict(java_retrieval.getTimingInfo())
        return ExternalRetrieval(
            id=java_retrieval.getRetrievalId(),
            retrieval_type="ExternalDatastoreRetrieval",
            start_times=list(timings.get("startTime", [])),
            elapsed_times=list(timings.get("elapsedTime", [])),
            result_sizes=list(java_retrieval.getResultSizes()),
            store=java_retrieval.getStore(),
            joined_measures=list(java_retrieval.getJoinedMeasure()),
            condition=java_retrieval.getCondition(),
            fields=list(java_retrieval.getFields()),
        )

    @staticmethod
    def create_query_plan(java_plan: Any) -> QueryPlan:
        """Create a query plan."""
        java_infos = java_plan.getPlanInfo()
        infos = {
            "ActivePivot": {
                "Type": java_infos.getPivotType(),
                "Id": java_infos.getPivotId(),
                "Branch": java_infos.getBranch(),
                "Epoch": java_infos.getEpoch(),
            },
            "Cube filters": {
                f.getId(): f.getDescription()
                for f in to_python_list(java_plan.getQueryFilters())
            },
            "Continuous": java_infos.isContinuous(),
            "Range sharing": java_infos.getRangeSharing(),
            "Missed prefetches": java_infos.getMissedPrefetchBehavior(),
            "Cache": java_infos.getAggregatesCache(),
            "Global timings (ms)": to_python_dict(java_infos.getGlobalTimings()),
        }
        retrievals = [
            JavaApi.create_retrieval(retrieval)
            for retrieval in to_python_list(java_plan.getAggregateRetrievals())
        ]
        dependencies = {
            key: to_python_list(item)
            for key, item in to_python_dict(java_plan.getDependencies()).items()
        }
        external_retrievals = [
            JavaApi.create_external_retrieval(retrieval)
            for retrieval in to_python_list(java_plan.getExternalRetrievals())
        ]
        external_dependencies = {
            key: to_python_list(item)
            for key, item in to_python_dict(java_plan.getExternalDependencies()).items()
        }
        return QueryPlan(
            infos=infos,
            retrievals=retrievals,
            dependencies=dependencies,
            external_retrievals=external_retrievals,
            external_dependencies=external_dependencies,
        )

    def analyze_mdx(self, mdx: str, *, timeout: timedelta) -> QueryAnalysis:
        java_plans = to_python_list(
            self._outside_transaction_api().analyzeMdx(
                mdx, ceil(timeout.total_seconds())
            )
        )
        plans = [
            JavaApi.create_query_plan(java_plan)
            for java_plan in java_plans
            if java_plan.getPlanInfo().getClass().getSimpleName() == "PlanInfoData"
        ]
        return QueryAnalysis(query_plans=plans)

    def copy_measure(
        self,
        copied_measure_name: str,
        new_name: str,
        *,
        cube_name: str,
    ) -> None:
        self._outside_transaction_api().copyMeasure(
            cube_name, copied_measure_name, new_name
        )

    def create_measure(  # pylint: disable=too-many-positional-parameters
        self,
        cube_name: str,
        measure_name: Optional[str],
        measure_plugin_key: str,
        *args: Any,
    ) -> str:
        """Create a new measure with by giving its constructor arguments."""
        return cast(
            str,
            self._outside_transaction_api().createMeasure(
                cube_name,
                measure_name,
                measure_plugin_key,
                to_java_object_array(
                    [self._levels_to_descriptions(arg) for arg in args],
                    gateway=self.gateway,
                ),
            ),
        )

    def register_aggregation_function(
        self,
        *,
        additional_imports: Iterable[str],
        additional_methods: Iterable[str],
        contribute_source_code: str,
        decontribute_source_code: Optional[str],
        merge_source_code: str,
        terminate_source_code: str,
        buffer_types: Iterable[DataType],
        output_type: DataType,
        plugin_key: str,
    ) -> None:
        """Register a new user defined aggregation function."""
        self._outside_transaction_api().registerUserDefinedAggregateFunction(
            contribute_source_code,
            decontribute_source_code,
            merge_source_code,
            terminate_source_code,
            to_java_string_array(list(buffer_types), gateway=self.gateway),
            output_type,
            plugin_key,
            to_java_string_array(list(additional_imports), gateway=self.gateway),
            to_java_string_array(list(additional_methods), gateway=self.gateway),
        )

    def _levels_to_descriptions(self, arg: Any) -> Any:
        """Recursively convert levels, hierarchies, and columns to their Java descriptions."""
        if isinstance(arg, tuple):
            return to_java_object_array(
                tuple(self._levels_to_descriptions(e) for e in arg),
                gateway=self.gateway,
            )
        if isinstance(arg, Mapping):
            return to_java_map(
                {
                    self._levels_to_descriptions(k): self._levels_to_descriptions(v)
                    for k, v in arg.items()
                },
                gateway=self.gateway,
            )
        if isinstance(arg, (list, set)):
            return to_java_object_list(
                [self._levels_to_descriptions(e) for e in arg],
                gateway=self.gateway,
            )
        if isinstance(arg, ColumnCoordinates):
            return to_store_field(arg, gateway=self.gateway)
        return arg

    def aggregated_measure(
        self,
        *,
        cube_name: str,
        measure_name: Optional[str],
        table_name: str,
        column_name: str,
        agg_function: str,
    ) -> str:
        """Create a new aggregated measure and return its name."""
        return cast(
            str,
            self._outside_transaction_api().createAggregatedMeasure(
                cube_name,
                measure_name,
                table_name,
                column_name,
                agg_function,
            ),
        )

    def delete_measure(self, measure_name: str, /, *, cube_name: str) -> None:
        if (
            self._outside_transaction_api()
            .removeMeasure(measure_name, cube_name)
            .isEmpty()
        ):
            raise KeyError(measure_name)

    def get_column_default_value(self, column_name: str, /, *, table_name: str) -> Any:
        return to_python_object(
            self.java_api.getFieldDefaultValue(column_name, table_name)
        )

    def set_column_default_value(
        self,
        default_value: Any,
        /,
        *,
        column_name: str,
        table_name: str,
        data_type: DataType,
    ) -> None:
        self._outside_transaction_api().setFieldDefaultValue(
            as_java_object(default_value, gateway=self.gateway),
            column_name,
            self._get_java_type_from_data_type(data_type),
            table_name,
        )
        self.refresh()

    def create_parameter_simulation(
        self,
        *,
        cube_name: str,
        simulation_name: str,
        measures: Mapping[
            str, Optional[Union[float, int, Iterable[int], Iterable[float]]]
        ],
        levels_coordinates: Iterable[LevelCoordinates],
        base_scenario_name: str,
    ) -> str:
        """Create a simulation in the cube and return the name of its backing table."""
        java_measures = to_java_map(measures, gateway=self.gateway)
        java_levels = to_java_string_array(
            [
                level_coordinates.java_description
                for level_coordinates in levels_coordinates
            ],
            gateway=self.gateway,
        )
        return cast(
            str,
            self._outside_transaction_api().createParameterSimulation(
                cube_name,
                simulation_name,
                java_levels,
                base_scenario_name,
                java_measures,
            ),
        )

    def _inside_transaction(
        self,
        callback: Callable[[], None],
        *,
        scenario_name: str,
        source_key: Optional[str] = None,
    ) -> None:
        if is_inside_transaction() or source_key in _REALTIME_SOURCE_KEYS:
            callback()
        else:
            with Transaction(
                scenario_name,
                start=self.start_transaction,
                end=self.end_transaction,
                is_user_initiated=False,
            ):
                callback()

    def block_until_widget_loaded(self, widget_id: str) -> None:
        """Block until the widget is loaded."""
        self.java_api.blockUntilWidgetLoaded(widget_id)

    def get_shared_context_values(self, cube_name: str) -> Dict[str, str]:
        return to_python_dict(
            self._outside_transaction_api().getCubeShareContextValues(cube_name)
        )

    def set_shared_context_value(self, *, cube_name: str, key: str, value: str) -> None:
        self._outside_transaction_api().setCubeSharedContextValue(cube_name, key, value)

    def get_user(self, *args: Any, **kwargs: Any) -> Any:  # pylint: disable=no-self-use
        raise MissingPluginError("plus")

    def get_users(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def create_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_individual_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_individual_roles_for_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def upsert_individual_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def delete_individual_roles_for_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def get_default_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def set_default_roles(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def change_user_password(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def delete_user(  # pylint: disable=no-self-use
        self, *args: Any, **kwargs: Any
    ) -> Any:
        raise MissingPluginError("plus")

    def external_api(self, key: str, /) -> Any:
        return self._outside_transaction_api().externalDatabaseApi(key)

    def _to_java_table_id(self, coordinates: ExternalTableCoordinates, /) -> JavaObject:
        return (
            self.gateway.jvm.io.atoti.api.directquery.ExternalTableId.builder()
            .databaseName(coordinates.database_name)
            .schemaName(coordinates.schema_name)
            .tableName(coordinates.table_name)
            .build()
        )

    def connect_to_database(
        self,
        key: str,
        /,
        *,
        url: Optional[str],
        password: Optional[str],
        options: Mapping[str, Optional[str]],
    ) -> None:
        options = to_java_map(options, gateway=self.gateway)
        self.external_api(key).connectToDatabase(url, password, options)

    def get_external_tables(
        self, key: str, /
    ) -> Dict[str, Dict[str, List[ExternalTableCoordinates]]]:
        result = self.external_api(key).getTables()
        return _convert_java_table_list(result)

    def get_external_table_schema(
        self,
        key: str,
        /,
        *,
        coordinates: ExternalTableCoordinates,
    ) -> Mapping[str, DataType]:
        schema = self.external_api(key).getTableSchema(
            self._to_java_table_id(coordinates)
        )
        return _convert_java_column_types(schema)

    def add_external_table(
        self,
        key: str,
        /,
        *,
        clustering_columns: Optional[Sequence[str]],
        columns: Mapping[str, str],
        coordinates: ExternalTableCoordinates,
        keys: Optional[Sequence[str]],
        local_table_name: str,
    ) -> None:
        java_keys = (
            None if keys is None else to_java_object_list(keys, gateway=self.gateway)
        )
        java_clustering_columns = (
            None
            if clustering_columns is None
            else to_java_object_list(clustering_columns, gateway=self.gateway)
        )
        java_columns = to_java_map(columns, gateway=self.gateway)
        self.external_api(key).addTable(
            self._to_java_table_id(coordinates),
            local_table_name,
            java_keys,
            java_columns,
            java_clustering_columns,
        )

    def add_external_table_with_multi_row_arrays(
        self,
        key: str,
        /,
        *,
        array_columns: Sequence[str],
        clustering_columns: Optional[Sequence[str]],
        coordinates: ExternalTableCoordinates,
        columns: Mapping[str, str],
        index_column: str,
        local_table_name: str,
    ) -> None:
        java_clustering_columns = (
            None
            if clustering_columns is None
            else to_java_object_list(clustering_columns, gateway=self.gateway)
        )
        java_columns = to_java_map(columns, gateway=self.gateway)
        self.external_api(key).addTableWithMultiRowArray(
            self._to_java_table_id(coordinates),
            local_table_name,
            java_columns,
            java_clustering_columns,
            index_column,
            to_java_object_list(array_columns, gateway=self.gateway),
        )

    def add_external_multi_column_array_table(
        self,
        key: str,
        /,
        *,
        array_prefixes: Optional[Sequence[str]],
        clustering_columns: Optional[Sequence[str]],
        columns: Mapping[str, str],
        coordinates: ExternalTableCoordinates,
        keys: Optional[Sequence[str]],
        local_table_name: str,
    ) -> None:
        java_keys = (
            None if keys is None else to_java_object_list(keys, gateway=self.gateway)
        )
        java_array_prefixes = (
            None
            if array_prefixes is None
            else to_java_object_list(array_prefixes, gateway=self.gateway)
        )
        java_clustering_columns = (
            None
            if clustering_columns is None
            else to_java_object_list(clustering_columns, gateway=self.gateway)
        )
        java_columns = to_java_map(columns, gateway=self.gateway)
        self.external_api(key).addTableWithMultiColumnArray(
            self._to_java_table_id(coordinates),
            local_table_name,
            java_keys,
            java_columns,
            java_clustering_columns,
            java_array_prefixes,
        )

    def get_external_database_cache(self, key: str, /) -> Optional[bool]:
        return cast(Optional[bool], self.external_api(key).getCache())

    def set_external_database_cache(self, key: str, /, cache: bool) -> None:
        self.external_api(key).setCache(cache)

    def synchronize_with_external_database(self) -> None:
        self.java_api.synchronizeWithDatabase()
