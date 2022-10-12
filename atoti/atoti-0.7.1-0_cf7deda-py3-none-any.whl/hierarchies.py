from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Optional, Tuple, Union, overload

from atoti_core import ColumnCoordinates, HierarchyKey, keyword_only_dataclass
from typeguard import typechecked, typeguard_ignore

from ._exceptions import AtotiJavaException
from ._local_hierarchies import LocalHierarchies
from .column import Column
from .hierarchy import Hierarchy
from .level import Level

LevelOrColumn = Union[Level, Column]

_HierarchyDescription = Union[Iterable[LevelOrColumn], Mapping[str, LevelOrColumn]]


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class Hierarchies(LocalHierarchies[Hierarchy]):
    """Manage the hierarchies.

    Example:
        >>> prices_df = pd.DataFrame(
        ...     columns=["Nation", "City", "Color", "Price"],
        ...     data=[
        ...         ("France", "Paris", "red", 20.0),
        ...         ("France", "Lyon", "blue", 15.0),
        ...         ("France", "Toulouse", "green", 10.0),
        ...         ("UK", "London", "red", 20.0),
        ...         ("UK", "Manchester", "blue", 15.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(prices_df, table_name="Prices")
        >>> cube = session.create_cube(table, mode="manual")
        >>> h = cube.hierarchies
        >>> h["Nation"] = {"Nation": table["Nation"]}
        >>> list(h)
        [('Prices', 'Nation')]

    A hierarchy can be renamed by creating a new one with the same levels and then removing the old one.

        >>> h["Country"] = h["Nation"].levels
        >>> del h["Nation"]
        >>> list(h)
        [('Prices', 'Country')]

    The :meth:`~dict.update` method is overridden to batch hierarchy creation operations for improved performance:

        >>> h.update(
        ...     {
        ...         ("Geography", "Geography"): [table["Nation"], table["City"]],
        ...         "Color": {"Color": table["Color"]},
        ...     }
        ... )
        >>> list(h)
        [('Prices', 'Color'), ('Geography', 'Geography'), ('Prices', 'Country')]
    """

    _cube_name: str

    def _get_underlying(self) -> Dict[Tuple[str, str], Hierarchy]:
        return {
            coordinates.key: self._create_hierarchy_from_arguments(description)
            for coordinates, description in self._java_api.get_hierarchies(
                cube_name=self._cube_name,
            ).items()
        }

    @typechecked
    def __getitem__(self, key: HierarchyKey) -> Hierarchy:
        (dimension_name, hierarchy_name) = self._convert_key(key)
        try:
            hierarchy_argument = self._java_api.get_hierarchy(
                hierarchy_name,
                cube_name=self._cube_name,
                dimension_name=dimension_name,
            )
        except AtotiJavaException as exception:
            raise KeyError(str(exception)) from None
        return self._create_hierarchy_from_arguments(hierarchy_argument)

    def _delete_keys(self, keys: Optional[Iterable[Tuple[str, str]]] = None, /) -> None:
        keys = self._default_to_all_keys(keys)
        for key in keys:
            self._java_api.delete_hierarchy(
                self[key]._coordinates, cube_name=self._cube_name
            )

    def __delitem__(self, key: HierarchyKey, /) -> None:
        if isinstance(key, str):
            key = self[key]._coordinates.key
        return super().__delitem__(key)

    # Custom override with same value type as the one used in `update()`.
    @typechecked
    def __setitem__(  # type: ignore
        self,
        key: HierarchyKey,
        value: _HierarchyDescription,
    ) -> None:
        self.update({key: value})

    # Custom override types on purpose so that hierarchies can be described either as an iterable or a mapping.
    def _update(  # type: ignore[override]
        self,
        other: Mapping[HierarchyKey, Mapping[str, LevelOrColumn]],
    ) -> None:
        structure: Dict[str, Dict[str, Mapping[str, ColumnCoordinates]]] = {}
        for hierarchy_key, levels_or_columns in other.items():
            dimension_name, hierarchy_name = self._convert_key(hierarchy_key)
            if dimension_name is None:
                self._check_no_hierarchy_name_conflict(hierarchy_name)
                dimension_name = _infer_dimension_name_from_level_or_column(
                    next(iter(levels_or_columns.values()))
                )
            if dimension_name not in structure:
                structure[dimension_name] = {}
            structure[dimension_name].update(
                {
                    hierarchy_name: {
                        name: level_or_column._column_coordinates
                        for name, level_or_column in levels_or_columns.items()
                    }
                }
            )
        self._java_api.update_hierarchies_for_cube(self._cube_name, structure=structure)
        self._java_api.refresh()

    # Custom override types on purpose so that hierarchies can be described either as an iterable or a mapping.
    @overload  # type: ignore[override]
    def update(
        self,
        __m: Mapping[HierarchyKey, _HierarchyDescription],
        **kwargs: _HierarchyDescription,
    ) -> None:
        ...

    @overload
    def update(
        self,
        __m: Iterable[Tuple[HierarchyKey, _HierarchyDescription]],
        **kwargs: _HierarchyDescription,
    ) -> None:
        ...

    @overload
    def update(self, **kwargs: _HierarchyDescription) -> None:
        ...

    # Custom override types on purpose so that hierarchies can be described either as an iterable or a mapping.
    def update(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        __m: Optional[
            Union[
                Mapping[HierarchyKey, _HierarchyDescription],
                Iterable[Tuple[HierarchyKey, _HierarchyDescription]],
            ]
        ] = None,
        **kwargs: _HierarchyDescription,
    ) -> None:
        """This method batches the updates for improved performance."""
        other: Dict[HierarchyKey, _HierarchyDescription] = {}
        if __m is not None:
            other.update(__m)
        other.update(**kwargs)
        final_hierarchies: Mapping[HierarchyKey, Mapping[str, LevelOrColumn]] = {
            hierarchy_key: _normalize_levels(levels_or_columns)
            for hierarchy_key, levels_or_columns in other.items()
        }
        self._update(final_hierarchies)

    def _check_no_hierarchy_name_conflict(self, hierarchy_name: str) -> None:
        try:
            self._java_api.get_hierarchy(
                hierarchy_name,
                dimension_name=None,
                cube_name=self._cube_name,
            )
        except KeyError:
            # Hierarchy does not exists but no conflict
            return
        except AtotiJavaException as exception:
            # Two hierarchies with same name in different dimensions
            raise KeyError(str(exception)) from None


def _infer_dimension_name_from_level_or_column(
    levels_or_column: LevelOrColumn,
) -> str:
    if isinstance(levels_or_column, Level):
        return levels_or_column.dimension
    return levels_or_column._table_name


def _normalize_levels(
    levels_or_columns: Union[Iterable[LevelOrColumn], Mapping[str, LevelOrColumn]]
) -> Mapping[str, LevelOrColumn]:
    return (
        levels_or_columns  # pyright: ignore[reportGeneralTypeIssues]
        if isinstance(levels_or_columns, Mapping)
        else {
            level_or_column.name: level_or_column
            for level_or_column in levels_or_columns
        }
    )
