from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Dict, TypeVar

from atoti_core import BaseMeasures, keyword_only_dataclass
from atoti_query import QueryMeasure
from typeguard import typechecked, typeguard_ignore

from ._delegate_mutable_mapping import DelegateMutableMapping
from ._java_api import JavaApi
from .measure import Measure

_Measure = TypeVar("_Measure", Measure, QueryMeasure)


@keyword_only_dataclass
@typeguard_ignore
@dataclass
class LocalMeasures(DelegateMutableMapping[str, _Measure], BaseMeasures[_Measure]):
    """Local measures class."""

    _java_api: JavaApi = field(repr=False)

    @abstractmethod
    def _get_underlying(self) -> Dict[str, _Measure]:
        """Fetch the measures from the JVM each time they are needed."""

    @typechecked
    @abstractmethod
    def __getitem__(self, key: str, /) -> _Measure:
        """Return the measure with the given name."""
