from __future__ import annotations

import operator
from abc import abstractmethod
from dataclasses import dataclass, field
from itertools import chain
from typing import Dict, Generic, Iterator, Mapping, Optional, Tuple, TypeVar, cast

from .base_hierarchies import BaseHierarchiesBound
from .base_hierarchy import LevelT
from .base_level import BaseLevel
from .ipython_key_completions import (
    IPythonKeyCompletions,
    get_ipython_key_completions_for_mapping,
)
from .level_key import LevelKey
from .repr_json import ReprJson, ReprJsonable

HierarchiesT = TypeVar("HierarchiesT", bound=BaseHierarchiesBound, covariant=True)


@dataclass(frozen=True)
class BaseLevels(
    Generic[HierarchiesT, LevelT], Mapping[LevelKey, LevelT], ReprJsonable
):  # pylint: disable=keyword-only-dataclass
    """Base class to manipulate flattened levels."""

    _hierarchies: HierarchiesT = field(repr=False)

    def _flatten(self) -> Dict[str, Optional[LevelT]]:
        flat_levels: Dict[str, Optional[LevelT]] = {}
        for hierarchy in self._hierarchies.values():
            for level in hierarchy.levels.values():
                if level.name in flat_levels:
                    # None is used as a flag to mark levels appearing in multiple hierarchies.
                    # When it happens, the user must use a tuple to retrieve the level.
                    # Like that: (hierarchy name, level name).
                    flat_levels[level.name] = None
                else:
                    flat_levels[level.name] = level  # type: ignore
        return flat_levels

    def __getitem__(self, key: LevelKey) -> LevelT:
        """Return the level with the given key."""
        if isinstance(key, str):
            return self._find_level(key)

        if len(key) == 2:
            return self._find_level(key[1], hierarchy_name=key[0])

        key = cast(Tuple[str, str, str], key)
        return self._find_level(key[2], dimension_name=key[0], hierarchy_name=key[1])

    @abstractmethod
    def _find_level(
        self,
        level_name: str,
        *,
        dimension_name: Optional[str] = None,
        hierarchy_name: Optional[str] = None,
    ) -> LevelT:
        """Get a level from the hierarchy name and level name."""

    def __iter__(
        self,
    ) -> Iterator[LevelKey]:
        """Return the iterator on all the levels."""
        return chain(
            *[
                iter(
                    {
                        (hierarchy.dimension, hierarchy.name, level_name): level
                        for level_name, level in hierarchy.levels.items()
                    }
                )
                for hierarchy in self._hierarchies.values()
            ]
        )

    def __len__(self) -> int:
        """Return the number of levels."""
        return sum([len(hierarchy.levels) for hierarchy in self._hierarchies.values()])

    def _ipython_key_completions_(self) -> IPythonKeyCompletions:
        return get_ipython_key_completions_for_mapping(self._flatten())

    def _repr_json_(self) -> ReprJson:
        # Use the dimension/hierarchy/level in the map key to make it unique.
        data = {
            f"{level.name} ({level.dimension}/{level.hierarchy}/{level.name})": level._repr_json_()[
                0
            ]
            for hierarchy in self._hierarchies.values()
            for level in hierarchy.levels.values()
        }
        sorted_data = dict(sorted(data.items(), key=operator.itemgetter(0)))
        return (
            sorted_data,
            {
                "expanded": True,
                "root": "Levels",
            },
        )


BaseLevelsBound = BaseLevels[BaseHierarchiesBound, BaseLevel]
