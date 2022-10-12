from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Optional

from atoti_core import keyword_only_dataclass
from atoti_query import QueryMeasure

from ..._local_measures import LocalMeasures


@keyword_only_dataclass
@dataclass
class DistributedMeasures(LocalMeasures[QueryMeasure]):
    """Manage the measures."""

    _cube_name: str

    def _get_underlying(self) -> Dict[str, QueryMeasure]:
        """Fetch the measures from the JVM each time they are needed."""
        cube_measures = self._java_api.get_measures(self._cube_name)
        return {
            name: QueryMeasure(
                _name=name,
                _visible=cube_measures[name].visible,
                _folder=cube_measures[name].folder,
                _formatter=cube_measures[name].formatter,
                _description=cube_measures[name].description,
            )
            for name in cube_measures
        }

    def __getitem__(self, key: str) -> QueryMeasure:
        measure = self._java_api.get_measure(key, cube_name=self._cube_name)
        return QueryMeasure(
            _name=key,
            _visible=measure.visible,
            _folder=measure.folder,
            _formatter=measure.formatter,
            _description=measure.description,
        )

    def _update(self, other: Mapping[str, QueryMeasure]) -> None:
        raise NotImplementedError("Distributed cube measures cannot be changed")

    def _delete_keys(self, keys: Optional[Iterable[str]] = None, /) -> None:
        raise NotImplementedError("Distributed cube measures cannot be changed")
