from dataclasses import dataclass
from datetime import timedelta
from typing import Any, Iterable, Literal, Optional

import pandas as pd
from atoti_core import (
    BASE_SCENARIO_NAME,
    EMPTY_MAPPING,
    QUERY_DOC,
    BaseCondition,
    BaseCube,
    BaseLevel,
    BaseMeasure,
    Context,
    QueryPrivateParameters,
    doc,
    generate_mdx,
    get_query_args_doc,
    keyword_only_dataclass,
)
from typeguard import typechecked, typeguard_ignore

from ._execute_gaq import _ExecuteGaq
from ._query_mdx import _QueryMdx
from ._widget_conversion_details import WidgetConversionDetails
from .query_hierarchies import QueryHierarchies
from .query_levels import QueryLevels
from .query_measures import QueryMeasures


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class QueryCube(BaseCube[QueryHierarchies, QueryLevels, QueryMeasures]):
    """Query cube."""

    _hierarchies: QueryHierarchies
    _measures: QueryMeasures
    _execute_gaq: Optional[_ExecuteGaq]
    _query_mdx: _QueryMdx

    @property
    def levels(self) -> QueryLevels:
        """Levels of the cube."""
        return QueryLevels(self.hierarchies)

    @doc(QUERY_DOC, args=get_query_args_doc(is_query_session=True))
    @typechecked
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
        if mode == "raw" and self._execute_gaq and not context:
            return self._execute_gaq(
                cube_name=self.name,
                measures=measures,
                levels=levels,
                filter=filter,
                include_totals=include_totals,
                scenario=scenario,
                timeout=timeout,
            )

        mdx = generate_mdx(
            cube_name=self.name,
            filter=filter,
            hierarchies=self.hierarchies,
            include_totals=include_totals,
            levels=levels,
            measures=measures,
            scenario=scenario,
        )

        query_result = self._query_mdx(
            mdx, keep_totals=include_totals, mode=mode, timeout=timeout, context=context
        )

        # Always use an MDX including totals because ActiveUI 5 then relies on context values to show/hide totals.
        if not include_totals and query_result._atoti_widget_conversion_details:
            query_result._atoti_widget_conversion_details = WidgetConversionDetails(
                mdx=generate_mdx(
                    cube_name=self.name,
                    filter=filter,
                    hierarchies=self.hierarchies,
                    include_totals=True,
                    levels=levels,
                    measures=measures,
                    scenario=scenario,
                ),
                session_id=query_result._atoti_widget_conversion_details.session_id,
                widget_creation_code=query_result._atoti_widget_conversion_details.widget_creation_code,
            )

        return query_result
