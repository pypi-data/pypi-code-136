from __future__ import annotations

from abc import abstractmethod
from dataclasses import replace
from datetime import timedelta
from pathlib import Path
from subprocess import STDOUT, CalledProcessError, check_output  # nosec
from types import TracebackType
from typing import (
    Any,
    Callable,
    Generic,
    Iterable,
    List,
    Literal,
    Mapping,
    Optional,
    Type,
    TypeVar,
)

# Importing the whole module to be able to monkey patch its `get_active_plugins()` in tests.
import atoti_core
import pandas as pd
from atoti_core import (
    EMPTY_MAPPING,
    BaseSession,
    Context,
    DataType,
    LevelCoordinates,
    MissingPluginError,
    PathLike,
    ServerVersions,
    doc,
)
from atoti_query import Auth as QueryAuth, QuerySession
from py4j.java_gateway import DEFAULT_PORT as _PY4J_DEFAULT_PORT

from ._docs_utils import EXPLAIN_QUERY_DOC
from ._endpoint import EndpointHandler
from ._exceptions import AtotiException, AtotiJavaException
from ._get_java_executable_path import get_java_executable_path
from ._java_api import JavaApi
from ._local_cube import LocalCube
from ._local_cubes import LocalCubes
from ._path_utils import to_absolute_path
from ._query_plan import QueryAnalysis
from ._runtime_type_checking_utils import typecheck
from ._server_subprocess import ServerSubprocess
from .config._session_config import SessionConfig

_LocalCubes = TypeVar("_LocalCubes", bound=LocalCubes[LocalCube[Any, Any, Any]])


def _add_plugin_app_extensions_to_config(config: SessionConfig) -> SessionConfig:
    config_app_extensions = {**(config.app_extensions or {})}
    app_extensions = config_app_extensions.copy()

    for plugin_name, plugin in atoti_core.get_active_plugins().items():
        for extension_name, extension_path in plugin.app_extensions.items():
            if extension_name in config_app_extensions:
                raise ValueError(
                    f"App extension {extension_name} is declared both in the session's configuration and in the plugin {plugin_name}."
                )
            if extension_name in app_extensions:
                raise ValueError(
                    f"App extension {extension_name} is declared in multiple plugins."
                )
            app_extensions[extension_name] = extension_path

    return replace(config, app_extensions=app_extensions)


@typecheck
class LocalSession(Generic[_LocalCubes], BaseSession[_LocalCubes]):
    """Local session class."""

    __server_versions: Optional[ServerVersions] = None

    def __init__(
        self,
        *,
        config: SessionConfig,
        distributed: bool = False,
        name: Optional[str] = None,
    ):
        super().__init__()
        self._name = name
        self._config = _add_plugin_app_extensions_to_config(config)

        self._create_subprocess_and_java_api(distributed=distributed)

        for plugin in atoti_core.get_active_plugins().values():
            plugin.init_session(self)

        try:
            self._start_application()
        except AtotiJavaException as ave:
            raise AtotiException(
                f"{ave.java_traceback}\n"
                f"An error occurred while configuring the session.\n"
                f"The logs are available at {self.logs_path}"
            ) from None

        self._closed = False

    def _create_subprocess_and_java_api(
        self,
        *,
        distributed: bool,
    ) -> None:
        try:
            # Attempt to connect to an existing detached process (useful for debugging).
            # Failed attempts are very fast (usually less than 2ms): users won't notice them.
            self._java_api = JavaApi(
                py4j_java_port=_PY4J_DEFAULT_PORT,
                distributed=distributed,
            )
            self._server_subprocess = None
        except ConnectionRefusedError:
            # No available unauthenticated detached process: creating subprocess.
            process = ServerSubprocess(config=self._config, session_id=self._id)
            self._java_api = JavaApi(
                auth_token=process.auth_token,
                py4j_java_port=process.py4j_java_port,
                distributed=distributed,
            )
            self._server_subprocess = process

    @property
    def name(self) -> Optional[str]:
        """Name of the session."""
        return self._name

    @property
    @abstractmethod
    def cubes(self) -> _LocalCubes:
        """Cubes of the session."""

    @property
    def closed(self) -> bool:
        """Return whether the session is closed or not."""
        return self._closed

    @property
    def port(self) -> int:
        """Port on which the session is exposed.

        Can be configured with :func:`atoti.Session`'s *port*  parameter.

        """
        return self._java_api.get_session_port()

    @property
    def logs_path(self) -> Path:
        """Path to the session logs file."""
        if not self._server_subprocess:
            raise NotImplementedError(
                "The logs path is not available when using a detached server process"
            )
        return self._server_subprocess.logs_path

    @property
    def security(self) -> Any:
        raise MissingPluginError("plus")

    def _start_application(self) -> None:
        self._java_api.start_application(self._config)

    def __exit__(  # pylint: disable=too-many-positional-parameters
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.close()

    def _clear(self) -> None:
        """Clear this session and free all the associated resources."""
        self._java_api.clear_session()

    def close(self) -> None:
        """Close this session and free all the associated resources."""
        self._java_api.shutdown()
        if self._server_subprocess:
            self.wait()
        self._closed = True

    def wait(self) -> None:
        """Wait for the underlying server subprocess to terminate.

        This will prevent the Python process to exit.
        """
        if self._server_subprocess is None:
            raise NotImplementedError("Server subprocess is not defined")
        self._server_subprocess.wait()

    @property
    def _location(self) -> Mapping[str, Any]:
        return {
            "https": self._config.https is not None,
            "port": self.port,
        }

    @property
    def _local_url(self) -> str:
        return (
            f"https://{self._config.https.domain}:{self.port}"
            if self._config.https is not None
            else f"http://localhost:{self.port}"
        )

    @property
    def _server_versions(self) -> ServerVersions:
        if self.__server_versions is None:
            self.__server_versions = QuerySession(
                self._local_url,
                certificate_authority=self._config.https.certificate_authority
                if self._config.https
                else None,
            )._server_versions

        return self.__server_versions

    def _generate_token(self) -> str:
        """Return a token that can be used to authenticate against the server."""
        return self._java_api.generate_jwt()

    def _block_until_widget_loaded(self, widget_id: str) -> None:
        self._java_api.block_until_widget_loaded(widget_id)

    def _create_query_session(self) -> QuerySession:
        headers = self._generate_auth_headers()
        auth: Optional[QueryAuth] = (lambda _url: headers) if headers else None
        return QuerySession(
            self._local_url,
            auth=auth,
            # Pass the versions to avoid refetching them.
            server_versions=self._server_versions,
            certificate_authority=self._config.https.certificate_authority
            if self._config.https
            else None,
        )

    def query_mdx(
        self,
        mdx: str,
        *,
        keep_totals: bool = False,
        timeout: timedelta = timedelta(seconds=30),
        mode: Literal["pretty", "raw"] = "pretty",
        context: Context = EMPTY_MAPPING,
    ) -> pd.DataFrame:
        def get_level_data_types(
            levels_coordinates: Iterable[LevelCoordinates], *, cube_name: str
        ) -> Mapping[LevelCoordinates, DataType]:
            return self.cubes[cube_name]._get_level_data_types(levels_coordinates)

        return self._create_query_session().query_mdx(
            mdx,
            get_level_data_types=get_level_data_types,
            keep_totals=keep_totals,
            timeout=timeout,
            session=self,
            mode=mode,
            context=context,
        )

    @doc(EXPLAIN_QUERY_DOC, corresponding_method="query_mdx")
    def explain_mdx_query(
        self, mdx: str, *, timeout: timedelta = timedelta(seconds=30)
    ) -> QueryAnalysis:
        return self._java_api.analyze_mdx(mdx, timeout=timeout)

    def _generate_auth_headers(self) -> Mapping[str, str]:
        return {"Authorization": f"Jwt {self._java_api.generate_jwt()}"}

    def endpoint(
        self, route: str, *, method: Literal["POST", "GET", "PUT", "DELETE"] = "GET"
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Create a custom endpoint at ``/atoti/pyapi/{route}"``.

        This is useful to reuse atoti's built-in server instead of adding a `FastAPI <https://fastapi.tiangolo.com/>`__ or `Flask <https://flask.palletsprojects.com/>`__ server to the project.
        This way, when deploying the project in a container or a VM, only one port (the one of the atoti server) can be exposed instead of two.
        Since custom endpoints are exposed by atoti's server, they automatically inherit from the configured :func:`atoti.Session`'s *authentication* and *https* parameter.

        The decorated function must take three parameters with types :class:`atoti.pyapi.User`, :class:`atoti.pyapi.HttpRequest`, and :class:`atoti.Session` and return a response body as a Python data structure that can be converted to JSON.

        Args:
            route: The path suffix after ``/atoti/pyapi/``.
                For instance, if ``custom/search`` is passed, a request to ``/atoti/pyapi/custom/search?query=test#results`` will match.
                The route should not contain the query (``?``) or fragment (``#``).

                Path parameters can be configured by wrapping their name in curly braces in the route.
            method: The HTTP method the request must be using to trigger this endpoint.
                ``DELETE``, ``POST``, and ``PUT`` requests can have a body but it must be JSON.

        Example:
            .. doctest:: Session.endpoint
                :skipif: True

                >>> import requests
                >>> df = pd.DataFrame(
                ...     columns=["Year", "Month", "Day", "Quantity"],
                ...     data=[
                ...         (2019, 7, 1, 15),
                ...         (2019, 7, 2, 20),
                ...     ],
                ... )
                >>> table = session.read_pandas(df, table_name="Quantity")
                >>> table.head()
                Year  Month  Day  Quantity
                0  2019      7    1        15
                1  2019      7    2        20
                >>> endpoints_base_url = f"http://localhost:{session.port}/atoti/pyapi"
                >>> @session.endpoint("tables/{table_name}/size", method="GET")
                ... def get_table_size(request, user, session):
                ...     table_name = request.path_parameters["table_name"]
                ...     return len(session.tables[table_name])
                >>> requests.get(f"{endpoints_base_url}/tables/Quantity/size").json()
                2
                >>> @session.endpoint("tables/{table_name}/rows", method="POST")
                ... def append_rows_to_table(request, user, session):
                ...     rows = request.body
                ...     table_name = request.path_parameters["table_name"]
                ...     session.tables[table_name].append(*rows)
                >>> requests.post(
                ...     f"{endpoints_base_url}/tables/Quantity/rows",
                ...     json=[
                ...         {"Year": 2021, "Month": 5, "Day": 19, "Quantity": 50},
                ...         {"Year": 2021, "Month": 5, "Day": 20, "Quantity": 6},
                ...     ],
                ... ).status_code
                200
                >>> requests.get(f"{endpoints_base_url}/tables/Quantity/size").json()
                4
                >>> table.head()
                Year  Month  Day  Quantity
                0  2019      7    1        15
                1  2019      7    2        20
                2  2021      5   19        50
                3  2021      5   20         6

        """
        if route[0] == "/" or "?" in route or "#" in route:
            raise ValueError(
                f"Invalid route '{route}'. It should not start with '/' and not contain '?' or '#'."
            )

        def endpoint_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self._java_api.create_endpoint(
                http_method=method,
                route=route,
                handler=EndpointHandler(callback=func, session=self),
            )
            return func

        return endpoint_decorator

    def export_translations_template(self, path: PathLike) -> None:
        """Export a template containing all translatable values in the session's cubes.

        Args:
            path: The path at which to write the template.
        """
        self._java_api.export_i18n_template(path)

    def _get_jfr_command(self, jfr_action: str, *args: str) -> List[str]:
        if not self._server_subprocess:
            raise RuntimeError("Cannot create flight recording with detached process.")

        return [
            str(get_java_executable_path(executable_name="jcmd")),
            str(self._server_subprocess.pid),
            f"JFR.{jfr_action}",
            *args,
        ]

    def _create_flight_recording(self, path: PathLike, *, duration: timedelta) -> None:
        """Create a recording file using Java Flight Recorder (JFR).

        This call is non-blocking: ``jcmd`` will continue writing to the file at the specified *path* for the given *duration* after this function returns.
        Call :func:`time.sleep` with ``duration.total_seconds()`` to block the current thread until the end of the recording.

        Args:
            path: The path (with a :guilabel:`.jfr` extension) at which the recording file should be written to.
            duration: The duration of the recording.
        """
        command = self._get_jfr_command(
            "start",
            f"duration={int(duration.total_seconds())}s",
            f"filename={to_absolute_path(path)}",
        )

        try:
            check_output(  # nosec
                command,
                stderr=STDOUT,
                text=True,
            )
        except CalledProcessError as error:
            raise RuntimeError(
                f"Failed to create flight recording:\n{error.output}"
            ) from error
