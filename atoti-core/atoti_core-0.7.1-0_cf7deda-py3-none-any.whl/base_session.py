import random
import string
from abc import abstractmethod
from datetime import timedelta
from time import time
from typing import Any, Generic, Literal, Mapping, Optional, TypeVar, cast

import pandas as pd

from .base_cubes import BaseCubesBound
from .context import Context
from .doc import doc
from .empty_mapping import EMPTY_MAPPING
from .find_corresponding_top_level_variable_name import (
    find_corresponding_top_level_variable_name,
)
from .get_endpoint_url import get_endpoint_url
from .missing_plugin_error import MissingPluginError
from .query_doc import QUERY_ARGS_DOC
from .repr_json import ReprJson, ReprJsonable
from .server_versions import ServerVersions

CubesT = TypeVar("CubesT", bound=BaseCubesBound, covariant=True)


def _generate_session_id() -> str:
    random_string = "".join(
        # No need for cryptographic security.
        random.choices(string.ascii_uppercase + string.digits, k=6)  # nosec
    )
    return f"{str(int(time()))}_{random_string}"


class BaseSession(Generic[CubesT], ReprJsonable):
    """Base class for session."""

    def __init__(self) -> None:
        self.__id = _generate_session_id()

    @property
    @abstractmethod
    def _location(self) -> Mapping[str, Any]:
        """Location data used to create a link to this session."""

    def link(self, *, path: str = "") -> Any:  # pylint: disable=no-self-use
        raise MissingPluginError("jupyterlab")

    @property
    @abstractmethod
    def cubes(self) -> CubesT:
        """Cubes of the session."""

    @property
    @abstractmethod
    def _server_versions(self) -> ServerVersions:
        ...

    @property
    @abstractmethod
    def _local_url(self) -> str:
        """URL that can be used to access the session on the host machine's network."""

    def _get_endpoint_url(
        self,
        *,
        namespace: str,
        route: str,
        attribute_name: Literal["restPath", "wsPath"] = "restPath",
    ) -> str:
        return get_endpoint_url(
            session_url=self._local_url,
            namespace=namespace,
            route=route,
            server_versions=self._server_versions,
            attribute_name=attribute_name,
        )

    def visualize(  # pylint: disable=no-self-use
        self, name: Optional[str] = None
    ) -> Any:
        raise MissingPluginError("jupyterlab")

    @property
    def _id(self) -> str:
        return self.__id

    @doc(
        f"""Execute an MDX query and return its result as a pandas DataFrame.

        Args:

            mdx: The MDX ``SELECT`` query to execute.

                Regardless of the axes on which levels and measures appear in the MDX, the returned DataFrame will have all levels on rows and measures on columns.

                Example:

                    .. doctest:: query_mdx

                        >>> from datetime import date
                        >>> df = pd.DataFrame(
                        ...     columns=["Country", "Date", "Price"],
                        ...     data=[
                        ...         ("China", date(2020, 3, 3), 410.0),
                        ...         ("France", date(2020, 1, 1), 480.0),
                        ...         ("France", date(2020, 2, 2), 500.0),
                        ...         ("France", date(2020, 3, 3), 400.0),
                        ...         ("India", date(2020, 1, 1), 360.0),
                        ...         ("India", date(2020, 2, 2), 400.0),
                        ...         ("UK", date(2020, 2, 2), 960.0),
                        ...     ],
                        ... )
                        >>> table = session.read_pandas(
                        ...     df, keys=["Country", "Date"], table_name="Prices"
                        ... )
                        >>> cube = session.create_cube(table)

                    This MDX:

                    .. doctest:: query_mdx

                        >>> mdx = (
                        ...     "SELECT"
                        ...     "  NON EMPTY Hierarchize("
                        ...     "    DrilldownLevel("
                        ...     "      [Prices].[Country].[ALL].[AllMember]"
                        ...     "    )"
                        ...     "  ) ON ROWS,"
                        ...     "  NON EMPTY Crossjoin("
                        ...     "    [Measures].[Price.SUM],"
                        ...     "    Hierarchize("
                        ...     "      DrilldownLevel("
                        ...     "        [Prices].[Date].[ALL].[AllMember]"
                        ...     "      )"
                        ...     "    )"
                        ...     "  ) ON COLUMNS"
                        ...     "  FROM [Prices]"
                        ... )

                    Returns this DataFrame:

                    .. doctest:: query_mdx

                        >>> session.query_mdx(mdx).sort_index()
                                            Price.SUM
                        Date       Country
                        2020-01-01 France       480.0
                                   India        360.0
                        2020-02-02 France       500.0
                                   India        400.0
                                   UK           960.0
                        2020-03-03 China        410.0
                                   France       400.0

                    But, if it was displayed into a pivot table, would look like this:

                    +---------+-------------------------------------------------+
                    | Country | Price.sum                                       |
                    |         +----------+------------+------------+------------+
                    |         | Total    | 2020-01-01 | 2020-02-02 | 2020-03-03 |
                    +---------+----------+------------+------------+------------+
                    | Total   | 2,280.00 | 840.00     | 1,860.00   | 810.00     |
                    +---------+----------+------------+------------+------------+
                    | China   | 760.00   |            |            | 410.00     |
                    +---------+----------+------------+------------+------------+
                    | France  | 1,800.00 | 480.00     | 500.00     | 400.00     |
                    +---------+----------+------------+------------+------------+
                    | India   | 760.00   | 360.00     | 400.00     |            |
                    +---------+----------+------------+------------+------------+
                    | UK      | 960.00   |            | 960.00     |            |
                    +---------+----------+------------+------------+------------+

                    .. doctest:: query_mdx
                        :hide:

                        Clear the session to isolate the multiple methods sharing this docstring.
                        >>> session._clear()

            keep_totals: Whether the resulting DataFrame should contain, if they are present in the query result, the grand total and subtotals.
                {QUERY_ARGS_DOC["totals"]}

            {QUERY_ARGS_DOC["timeout"]}

            {QUERY_ARGS_DOC["mode"]}

              {QUERY_ARGS_DOC["pretty"]}

              {QUERY_ARGS_DOC["raw"]}

            {QUERY_ARGS_DOC["context"]}
        """
    )
    @abstractmethod
    def query_mdx(
        self,
        mdx: str,
        *,
        keep_totals: bool = False,
        timeout: timedelta = timedelta(seconds=30),
        mode: Literal["pretty", "raw"] = "pretty",
        context: Context = EMPTY_MAPPING,
    ) -> pd.DataFrame:
        ...

    @abstractmethod
    def _generate_auth_headers(self) -> Mapping[str, str]:
        """Generate authentication headers that can be used to authenticate against this session."""

    def _get_widget_creation_code(self) -> Optional[str]:
        session_variable_name = find_corresponding_top_level_variable_name(self)

        return f"{session_variable_name}.visualize()" if session_variable_name else None

    def _block_until_widget_loaded(  # pylint: disable=unused-argument, no-self-use
        self, widget_id: str
    ) -> None:
        # Nothing to do by default.
        ...

    def _repr_json_(self) -> ReprJson:
        cubes = self.cubes._repr_json_()[0]
        data = (
            {"Tables": cast(Any, self).tables._repr_json_()[0], "Cubes": cubes}
            if hasattr(self, "tables")
            else {"Cubes": cubes}
        )
        return (
            data,
            {"expanded": False, "root": type(self).__name__},
        )


BaseSessionBound = BaseSession[BaseCubesBound]
