from abc import abstractmethod
from datetime import timedelta
from typing import Any, Callable, Dict, Iterable, Literal, Optional, TypeVar

import pandas as pd
from atoti_core import (
    BASE_SCENARIO_NAME,
    EMPTY_MAPPING,
    QUERY_DOC,
    BaseCondition,
    BaseCube,
    BaseHierarchyBound,
    BaseLevel,
    BaseMeasure,
    Context,
    DataType,
    LevelCoordinates,
    LevelsT,
    QueryPrivateParameters,
    doc,
    generate_mdx,
    get_query_args_doc,
)
from atoti_query import _ExecuteGaq, _QueryMdx

from ._docs_utils import EXPLAIN_QUERY_DOC
from ._hierarchy_arguments import HierarchyArguments
from ._java_api import JavaApi
from ._local_hierarchies import LocalHierarchies
from ._local_measures import LocalMeasures
from ._query_plan import QueryAnalysis
from ._runtime_type_checking_utils import typecheck
from .aggregates_cache import AggregatesCache

_LocalMeasures = TypeVar("_LocalMeasures", bound=LocalMeasures[Any])
_LocalHierarchies = TypeVar("_LocalHierarchies", bound=LocalHierarchies[Any])


@typecheck
class LocalCube(BaseCube[_LocalHierarchies, LevelsT, _LocalMeasures]):
    """Local cube class."""

    def __init__(
        self,
        name: str,
        *,
        java_api: JavaApi,
        session_name: Optional[str],
        hierarchies: _LocalHierarchies,
        level_function: Callable[[_LocalHierarchies], LevelsT],
        measures: _LocalMeasures,
        agg_cache: AggregatesCache,
        query_mdx: _QueryMdx,
        execute_gaq: _ExecuteGaq,
    ):
        super().__init__(_name=name, _hierarchies=hierarchies, _measures=measures)
        self._session_name = session_name
        self._java_api = java_api
        self._levels: LevelsT = level_function(hierarchies)
        self._agg_cache = agg_cache
        self._query_mdx = query_mdx
        self._execute_gaq = execute_gaq

    @property
    def name(self) -> str:
        """Name of the cube."""
        return self._name

    @property
    def hierarchies(self) -> _LocalHierarchies:
        """Hierarchies of the cube."""
        return self._hierarchies

    @property
    def levels(self) -> LevelsT:
        """Levels of the cube."""
        return self._levels

    @property
    def measures(self) -> _LocalMeasures:
        """Measures of the cube."""
        return self._measures

    @property
    def aggregates_cache(self) -> AggregatesCache:
        """Aggregates cache of the cube."""
        return self._agg_cache

    @abstractmethod
    def _get_level_data_types(
        self, levels_coordinates: Iterable[LevelCoordinates]
    ) -> Dict[LevelCoordinates, DataType]:
        ...

    @doc(QUERY_DOC, args=get_query_args_doc(is_query_session=False))
    def query(
        self,
        *measures: BaseMeasure,
        filter: Optional[BaseCondition] = None,  # pylint: disable=redefined-builtin
        include_totals: bool = False,
        levels: Iterable[BaseLevel] = (),
        mode: Literal["pretty", "raw"] = "pretty",
        scenario: str = BASE_SCENARIO_NAME,
        timeout: timedelta = timedelta(seconds=30),
        context: Context = EMPTY_MAPPING,
        **kwargs: Any,
    ) -> pd.DataFrame:
        query_private_parameters = QueryPrivateParameters(**kwargs)
        filter = query_private_parameters.condition if filter is None else filter
        if mode == "pretty" or context:
            mdx = generate_mdx(
                cube_name=self.name,
                hierarchies=self.hierarchies,
                filter=filter,
                include_totals=include_totals,
                levels=levels,
                measures=measures,
                scenario=scenario,
            )
            query_result = self._query_mdx(
                mdx,
                keep_totals=include_totals,
                mode=mode,
                timeout=timeout,
                context=context,
            )
            return query_result

        # Execute the query without going through `QueryCube.query()` to avoid fetching the discovery.
        return self._execute_gaq(
            cube_name=self.name,
            measures=measures,
            levels=levels,
            filter=filter,
            include_totals=include_totals,
            scenario=scenario,
            timeout=timeout,
        )

    @doc(EXPLAIN_QUERY_DOC, corresponding_method="query")
    def explain_query(
        self,
        *measures: BaseMeasure,
        filter: Optional[BaseCondition] = None,  # pylint: disable=redefined-builtin
        include_totals: bool = False,
        levels: Iterable[BaseLevel] = (),
        scenario: str = BASE_SCENARIO_NAME,
        timeout: timedelta = timedelta(seconds=30),
        **kwargs: Any,
    ) -> QueryAnalysis:
        query_private_parameters = QueryPrivateParameters(**kwargs)
        filter = query_private_parameters.condition if filter is None else filter
        mdx = generate_mdx(
            cube_name=self.name,
            hierarchies=self.hierarchies,
            filter=filter,
            include_totals=include_totals,
            levels=levels,
            measures=measures,
            scenario=scenario,
        )
        return self._java_api.analyze_mdx(mdx, timeout=timeout)

    @abstractmethod
    def _create_hierarchy_from_arguments(
        self, arguments: HierarchyArguments
    ) -> BaseHierarchyBound:
        ...
