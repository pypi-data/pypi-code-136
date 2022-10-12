from dataclasses import dataclass
from typing import Protocol

from atoti_core import keyword_only_dataclass
from typeguard import typeguard_ignore


class _GetCapacity(Protocol):
    def __call__(self, *, cube_name: str) -> int:
        ...


class _SetCapacity(Protocol):
    def __call__(self, capacity: int, *, cube_name: str) -> None:
        ...


@keyword_only_dataclass
@typeguard_ignore
@dataclass
class AggregatesCache:
    """The aggregates cache associated with a :class:`~atoti.Cube`."""

    _cube_name: str
    _set_capacity: _SetCapacity
    _get_capacity: _GetCapacity

    @property
    def capacity(self) -> int:
        """Capacity of the cache.

        If:

        * ``> 0``: corresponds to the maximum amount of ``{location: measure}`` pairs that the cache can hold.
        * ``0``: Sharing is enabled but caching is disabled.
          Queries will share their computations if they are executed at the same time, but the aggregated values will not be stored to be retrieved later.
        * ``< 0``: Caching and sharing are disabled.

        Example:

            >>> table = session.create_table("example", types={"id": tt.INT})
            >>> cube = session.create_cube(table)
            >>> cube.aggregates_cache.capacity
            100
            >>> cube.aggregates_cache.capacity = -1
            >>> cube.aggregates_cache.capacity
            -1
        """
        return self._get_capacity(cube_name=self._cube_name)

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        self._set_capacity(cube_name=self._cube_name, capacity=capacity)
