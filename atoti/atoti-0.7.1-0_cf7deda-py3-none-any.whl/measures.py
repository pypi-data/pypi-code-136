from __future__ import annotations

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Iterable,
    Mapping,
    Optional,
    Tuple,
    Union,
    overload,
)

from typeguard import typeguard_ignore

from ._java_api import JavaApi
from ._local_measures import LocalMeasures
from .measure import Measure
from .measure_description import (
    MeasureDescription,
    MeasureLike,
    _convert_to_measure_description,
)

if TYPE_CHECKING:
    from _typeshed import SupportsKeysAndGetItem  # pylint: disable=nested-import


def _validate_name(name: str) -> None:
    """Validate the measure name.

    Args:
        name: The name to check.
    """
    if "," in name:
        raise ValueError(f'Invalid measure name "{name}". "," are not allowed.')
    if name != name.strip():
        raise ValueError(
            f'Invalid measure name "{name}". Leading or trailing whitespaces are not allowed.'
        )
    if name.startswith("__hidden_"):
        raise ValueError(
            f'Invalid measure name "{name}". Name cannot start with "__hidden_".'
        )


@dataclass(init=False)
class Measures(LocalMeasures[Measure]):
    """Manage the measures."""

    @typeguard_ignore
    def __init__(self, *, java_api: JavaApi, cube_name: str):
        super().__init__(_java_api=java_api)
        self._cube_name = cube_name

    @typeguard_ignore
    def _build_measure(
        self, name: str, description: JavaApi.JavaMeasureDescription
    ) -> Measure:
        return Measure(
            _name=name,
            _data_type=description.underlying_type,
            _cube_name=self._cube_name,
            _java_api=self._java_api,
            _folder=description.folder,
            _formatter=description.formatter,
            _visible=description.visible,
            _description=description.description,
        )

    def _get_underlying(self) -> Dict[str, Measure]:
        """Fetch the measures from the JVM each time they are needed."""
        cube_measures = self._java_api.get_measures(self._cube_name)
        return {
            name: self._build_measure(name, cube_measures[name])
            for name in cube_measures
        }

    def __getitem__(self, key: str) -> Measure:
        cube_measure = self._java_api.get_measure(key, cube_name=self._cube_name)
        return self._build_measure(key, cube_measure)

    # Custom override with same value type as the one used in `update()`.
    def __setitem__(
        self,
        key: str,
        value: MeasureLike,
    ) -> None:
        self.update({key: value})

    @overload
    def update(
        self,
        __m: SupportsKeysAndGetItem[str, MeasureLike],
        **kwargs: MeasureLike,
    ) -> None:
        ...

    @overload
    def update(
        self,
        __m: Iterable[Tuple[str, MeasureLike]],
        **kwargs: MeasureLike,
    ) -> None:
        ...

    @overload
    def update(self, **kwargs: MeasureLike) -> None:
        ...

    # Custom override types on purpose so that measure-like objects can be inserted.
    def update(  # type: ignore
        self,
        __m: Optional[
            Union[Mapping[str, MeasureLike], Iterable[Tuple[str, MeasureLike]]]
        ] = None,
        **kwargs: MeasureLike,
    ) -> None:
        other: Dict[str, MeasureLike] = {}
        if __m is not None:
            other.update(__m)
        other.update(**kwargs)
        self._update(other)

    # Custom override types on purpose so that measure-like objects can be inserted.
    def _update(self, other: Mapping[str, MeasureLike]) -> None:
        for measure_name, measure in other.items():
            _validate_name(measure_name)
            if not isinstance(measure, MeasureDescription):
                measure = _convert_to_measure_description(measure)

            try:
                measure._distil(
                    java_api=self._java_api,
                    cube_name=self._cube_name,
                    measure_name=measure_name,
                )
            except AttributeError as err:
                raise ValueError(f"Cannot create a measure from {measure}") from err

            self._java_api.publish_measures(self._cube_name)

    def _delete_keys(self, keys: Optional[Iterable[str]] = None, /) -> None:
        keys = self._default_to_all_keys(keys)
        for key in keys:
            self._java_api.delete_measure(key, cube_name=self._cube_name)
