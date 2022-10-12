from dataclasses import dataclass
from typing import Any, Optional, Sequence

from atoti_core import keyword_only_dataclass

from .._aggregate_provider_description import (
    AggregateProviderDescription,
    AggregateProviderKey,
)
from .._condition import Condition
from ..level import Level
from ..measure import Measure
from ._filters import to_java_filters


@keyword_only_dataclass
@dataclass(frozen=True)
class AggregateProvider:
    """
    An aggregate provider pre-aggregates some table columns up to certain levels.
    If a step of a query uses a subset of the aggregate provider's levels and measures, the provider will speed up the query.

    An aggregate provider uses additional memory to store the intermediate aggregates.
    The more levels and measures are added, the more memory it requires.

    Example:
        >>> df = pd.DataFrame(
        ...     {
        ...         "Seller": ["Seller_1", "Seller_1", "Seller_2", "Seller_2"],
        ...         "ProductId": ["aBk3", "ceJ4", "aBk3", "ceJ4"],
        ...         "Price": [2.5, 49.99, 3.0, 54.99],
        ...     }
        ... )
        >>> table = session.read_pandas(df, table_name="Seller")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> cube.aggregate_providers.update(
        ...     {
        ...         "Seller provider": tt.AggregateProvider(
        ...             key="bitmap",
        ...             levels=[l["Seller"], l["ProductId"]],
        ...             measures=[m["Price.SUM"]],
        ...             filter=l["ProductId"] == "cdJ4",
        ...             partitioning="hash4(Seller)",
        ...         )
        ...     }
        ... )
    """

    key: AggregateProviderKey = "leaf"
    """The key of the provider.

    The bitmap is generally faster but also takes more memory."""

    levels: Sequence[Level] = ()
    """The levels to build the provider on."""

    measures: Sequence[Measure] = ()
    """The measures to build in the provider on."""

    filter: Optional[Condition] = None
    """Only compute and provide aggregates matching this condition.

    The passed condition must be an equality test on a level (handled by the provider or not) or a combination of that kind of condition."""

    partitioning: Optional[str] = None
    """The partitioning of the provider.

    Default to the partitioning of the cube's base table."""

    @property
    def _description(self) -> AggregateProviderDescription:
        return AggregateProviderDescription(
            key=self.key,
            levels_coordinates=[level._coordinates for level in self.levels],
            measures_names=[measure.name for measure in self.measures],
            partitioning=self.partitioning,
            filters={} if self.filter is None else to_java_filters(self.filter),
        )

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AggregateProvider):
            return False
        return self._description == other._description
