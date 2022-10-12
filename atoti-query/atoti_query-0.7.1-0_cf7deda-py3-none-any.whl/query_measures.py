from atoti_core import BaseMeasures, ImmutableMapping

from .query_measure import QueryMeasure


class QueryMeasures(ImmutableMapping[str, QueryMeasure], BaseMeasures[QueryMeasure]):
    """Manage the query measures."""
