from dataclasses import dataclass
from datetime import timedelta
from functools import cached_property
from math import ceil
from pathlib import Path
from ssl import SSLContext, create_default_context
from typing import Any, Dict, Iterable, Literal, Mapping, Optional, Union, cast
from urllib.error import HTTPError
from urllib.parse import urljoin

import pandas as pd
from atoti_core import (
    EMPTY_MAPPING,
    BaseCondition,
    BaseLevel,
    BaseMeasure,
    BaseSession,
    BaseSessionBound,
    Context,
    ServerVersions,
    decombine_condition,
    doc,
    get_active_plugins,
    keyword_only_dataclass,
    local_to_absolute_path,
)

from ._cellset import Cellset
from ._cellset_to_query_result import cellset_to_query_result
from ._create_query_cubes_from_discovery import create_query_cubes_from_discovery
from ._discovery import Discovery
from ._execute_arrow_query import execute_arrow_query
from ._fetch_json import fetch_json
from ._get_level_data_types import GetLevelDataTypes
from ._widget_conversion_details import WidgetConversionDetails
from .auth import Auth
from .client_certificate import ClientCertificate
from .query_cubes import QueryCubes

_VERSIONS_WITHOUT_RAW_MODE = ("4", "5")


def _create_ssl_context(
    *,
    certificate_authority: Optional[Union[str, Path]] = None,
    client_certificate: Optional[ClientCertificate] = None,
) -> Optional[SSLContext]:
    if client_certificate is None and certificate_authority is None:
        return None
    context = create_default_context()
    if certificate_authority is not None:
        context.load_verify_locations(
            cafile=local_to_absolute_path(certificate_authority)
        )
    if client_certificate:
        context.load_cert_chain(
            certfile=local_to_absolute_path(client_certificate.certificate),
            keyfile=local_to_absolute_path(client_certificate.keyfile)
            if client_certificate.keyfile
            else None,
            password=client_certificate.password,
        )
    return context


def _handle_error(error: HTTPError, body: Any) -> None:
    stack_trace = _get_stack_trace(body)
    if stack_trace is not None:
        raise RuntimeError(stack_trace) from error

    raise RuntimeError("Could not handle malformed error.") from error


def _get_stack_trace(body: Any) -> Any:
    if isinstance(body, dict):
        if body.get("status") == "error":
            # ActivePivot < 6.0.0-M1.
            return body.get("error", {}).get("stackTrace")

        return body.get("stackTrace")
    return None


def _serialize_condition(condition: BaseCondition) -> Dict[str, Any]:
    (
        level_conditions,
        level_isin_conditions,
        hierarchy_isin_conditions,
    ) = decombine_condition(condition)

    # Ensure there is no hierarchy conditions
    if hierarchy_isin_conditions:
        raise ValueError("Unsupported hierarchy isin condition in raw query mode.")

    # Ensure all condition are == or isin on strings
    for level_condition in level_conditions:
        if level_condition.operator != "eq":
            raise ValueError(
                f"'{level_condition.operator}' not supported in query condition: level conditions can only be based on equality (==) or isin."
            )
        if not isinstance(level_condition.value, str):
            raise TypeError(
                f"Type {type(level_condition.value)} not supported in query condition: level conditions can only be based on equality with strings."
            )
    for level_isin_condition in level_isin_conditions:
        not_string = [
            value.value
            for value in level_isin_condition.members
            if not isinstance(value.value, str)
        ]
        if not_string:
            raise TypeError(
                f"Only strings are supported in query condition but the following values are not strings: {str(not_string)}."
            )

    # Serialize the conditions
    equal_conditions = {
        level_condition.level_coordinates.java_description: level_condition.value
        for level_condition in level_conditions
    }
    isin_conditions = {
        level_condition.level_coordinates.java_description: [
            member.value for member in level_condition.members
        ]
        for level_condition in level_isin_conditions
    }
    return {
        "equalConditions": equal_conditions,
        "isinConditions": isin_conditions,
    }


def _enrich_context(
    context: Context,
    *,
    timeout: timedelta,
) -> Context:
    return {
        "queriesTimeLimit": ceil(timeout.total_seconds()),
        **context,
    }


@keyword_only_dataclass
@dataclass(frozen=True)
class _QuerySessionPrivateParameters:
    server_versions: Optional[ServerVersions] = None


@keyword_only_dataclass
@dataclass(frozen=True)
class _QueryMdxPrivateParameters:
    session: Optional[BaseSessionBound] = None
    get_level_data_types: Optional[GetLevelDataTypes] = None


class QuerySession(BaseSession[QueryCubes]):
    """Used to query a remote atoti session (or a classic ActivePivot >= 5.7 server).

    Note:
        Query sessions are immutable: the structure of their underlying cubes is not expected to change.
    """

    __cubes: Optional[QueryCubes] = None

    @doc(url="{url}")
    def __init__(
        self,
        url: str,
        *,
        auth: Optional[Auth] = None,
        certificate_authority: Optional[Union[str, Path]] = None,
        client_certificate: Optional[ClientCertificate] = None,
        **kwargs: Any,
    ):
        """Create a QuerySession.

        Args:
            url: The base URL of the session.
                The endpoint ``f"{url}/versions/rest"`` is expected to exist.
            auth: The authentication to use to access the session.
            certificate_authority: Path to the custom certificate authority file to use to verify the HTTPS connection.
                Required when the session has been configured with a certificate that is not signed by some trusted public certificate authority.
            client_certificate: The client certificate to authenticate against the session.
        """

        super().__init__()
        self._url = url
        self._auth = auth or (lambda _: None)
        self._ssl_context = _create_ssl_context(
            client_certificate=client_certificate,
            certificate_authority=certificate_authority,
        )
        private_parameters = _QuerySessionPrivateParameters(**kwargs)
        self.__server_versions = private_parameters.server_versions
        plugins = get_active_plugins().values()
        for plugin in plugins:
            plugin.init_session(self)

    @property
    def cubes(self) -> QueryCubes:
        """Cubes of the session."""
        if self.__cubes is None:
            self.__cubes = create_query_cubes_from_discovery(
                self._discovery,
                execute_gaq=self._execute_gaq if self._gaq_supported else None,
                query_mdx=self.query_mdx,
            )

        return self.__cubes

    @property
    def url(self) -> str:
        """URL of the session."""
        return self._url

    @property
    def _location(self) -> Mapping[str, Any]:
        return {"url": self.url}

    @property
    def _local_url(self) -> str:
        return self.url

    @property
    def _raw_query_mode_supported(self) -> bool:
        return any(
            version["id"] not in _VERSIONS_WITHOUT_RAW_MODE
            for version in self._server_versions["apis"][self._pivot_namespace][
                "versions"
            ]
        )

    @property
    def _gaq_supported(self) -> bool:
        return "atoti" in self._server_versions["apis"]

    def _execute_gaq(
        self,
        *,
        cube_name: str,
        measures: Iterable[BaseMeasure],
        levels: Iterable[BaseLevel],
        filter: Optional[BaseCondition] = None,  # pylint: disable=redefined-builtin
        include_totals: bool,
        scenario: str,
        timeout: timedelta,
    ) -> pd.DataFrame:
        if include_totals:
            raise ValueError("Totals cannot be included with this query mode.")

        url = self._get_endpoint_url(namespace="atoti", route="arrow/query")
        data = {
            "cubeName": cube_name,
            "branch": scenario,
            "measures": [m.name for m in measures],
            "levelCoordinates": [
                level._coordinates.java_description for level in levels
            ],
            **(
                {"equalConditions": {}, "isinConditions": {}}
                if filter is None
                else _serialize_condition(filter)
            ),
            "timeout": ceil(timeout.total_seconds()),
        }
        return execute_arrow_query(url, data=data, headers=self._auth(url) or {})

    def _generate_auth_headers(self) -> Mapping[str, str]:
        return self._auth(self.url) or {}

    def _fetch_json(self, url: str, *, body: Optional[Any] = None) -> Any:
        data = fetch_json(
            url,
            body=body,
            headers=self._auth(url),
            on_error=_handle_error,
            ssl_context=self._ssl_context,
        )

        if (
            isinstance(data, dict)
            and "data" in data
            and data.get("status") == "success"
        ):
            # ActivePivot < 6.0.0-M1.
            data = data["data"]

        return data

    @property
    def _server_versions(self) -> ServerVersions:
        if self.__server_versions is None:
            url = urljoin(f"{self.url}/", "versions/rest")
            self.__server_versions = cast(
                ServerVersions,
                self._fetch_json(url),
            )

        return self.__server_versions

    @property
    def _pivot_namespace(self) -> str:
        return next(
            namespace
            for namespace in [
                "activeviam/pivot",
                "pivot",  # ActivePivot < 6.0.0-M1.
            ]
            if namespace in self._server_versions["apis"]
        )

    @cached_property
    def _discovery(self) -> Discovery:
        url = self._get_endpoint_url(
            namespace=self._pivot_namespace, route="cube/discovery"
        )
        body = self._fetch_json(url)
        return cast(Discovery, body)

    def _query_mdx_to_cellset(self, mdx: str, *, context: Context) -> Cellset:
        url = self._get_endpoint_url(
            namespace=self._pivot_namespace, route="cube/query/mdx"
        )
        body: Mapping[str, Union[str, Context]] = {
            "context": context,
            "mdx": mdx,
        }
        response = self._fetch_json(url, body=body)
        return cast(Cellset, response)

    def query_mdx(
        self,
        mdx: str,
        *,
        keep_totals: bool = False,
        timeout: timedelta = timedelta(seconds=30),
        mode: Literal["pretty", "raw"] = "pretty",
        context: Context = EMPTY_MAPPING,
        **kwargs: Any,
    ) -> pd.DataFrame:
        private_parameters = _QueryMdxPrivateParameters(**kwargs)

        context = _enrich_context(context, timeout=timeout)

        if mode == "raw":
            if not self._raw_query_mode_supported:
                raise ValueError(
                    "`raw` mode not supported by this ActivePivot version."
                )

            url = self._get_endpoint_url(
                namespace=self._pivot_namespace, route="cube/dataexport/download"
            )
            return execute_arrow_query(
                url,
                data={
                    "jsonMdxQuery": {"mdx": mdx, "context": context},
                    "outputConfiguration": {"format": "arrow"},
                },
                headers=self._auth(url) or {},
            )

        cellset = self._query_mdx_to_cellset(mdx, context=context)
        query_result = cellset_to_query_result(
            cellset,
            context=context,
            discovery=self._discovery,
            get_level_data_types=private_parameters.get_level_data_types,
            keep_totals=keep_totals,
        )
        # Let local sessions pass their reference to have the correct name and widget creation code.
        session = private_parameters.session or self

        widget_creation_code = session._get_widget_creation_code()
        if widget_creation_code is not None:
            query_result._atoti_widget_conversion_details = WidgetConversionDetails(
                mdx=mdx,
                session_id=session._id,
                widget_creation_code=widget_creation_code,
            )

        return query_result
