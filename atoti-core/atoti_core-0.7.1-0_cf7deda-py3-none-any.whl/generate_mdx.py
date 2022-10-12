from typing import Collection, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .base_condition import BaseCondition
from .base_hierarchies import BaseHierarchiesBound
from .base_hierarchy import BaseHierarchyBound
from .base_hierarchy_isin_condition import BaseHierarchyIsinCondition
from .base_level import BaseLevel
from .base_level_condition import BaseLevelCondition
from .base_level_isin_condition import BaseLevelIsinCondition
from .base_measure import BaseMeasure
from .constant import Constant
from .decombine_condition import decombine_condition
from .level_coordinates import LevelCoordinates
from .scenario import BASE_SCENARIO_NAME


def _escape(name: str) -> str:
    return name.replace("]", "]]")


def _generate_set(
    members: Collection[str], *, single_element_short_syntax: bool = True
) -> str:
    if single_element_short_syntax and len(members) == 1:
        return next(iter(members))

    return f"""{{{", ".join(members)}}}"""


def _generate_columns_set(measures: Iterable[BaseMeasure]) -> str:
    return _generate_set(
        [f"[Measures].[{_escape(measure.name)}]" for measure in measures],
        # ActiveUI 5 does not support it.
        # See https://support.activeviam.com/jira/browse/UI-5036.
        single_element_short_syntax=False,
    )


def _keep_only_deepest_levels(
    levels: Iterable[BaseLevel],
    *,
    hierarchies: BaseHierarchiesBound,
) -> Dict[BaseLevel, int]:
    hierarchy_to_max_level_depth: Dict[Tuple[str, str], int] = {}

    for level in levels:
        hierarchy_coordinates = (level.dimension, level.hierarchy)
        current_max_level_depth = hierarchy_to_max_level_depth.get(
            hierarchy_coordinates, -1
        )
        level_depth = list(hierarchies[hierarchy_coordinates].levels).index(level.name)

        if level_depth > current_max_level_depth:
            hierarchy_to_max_level_depth[hierarchy_coordinates] = level_depth

    return {
        list(hierarchies[hierarchy_coordinates].levels.values())[depth]: depth
        for hierarchy_coordinates, depth in hierarchy_to_max_level_depth.items()
    }


def _generate_hierarchy_unique_name(dimension: str, hierarchy: str) -> str:
    return f"[{_escape(dimension)}].[{_escape(hierarchy)}]"


def _generate_level_set(
    level: BaseLevel,
    *,
    hierarchies: BaseHierarchiesBound,
    include_totals: bool,
    level_depth: int,
) -> str:
    hierarchy = hierarchies[level.dimension, level.hierarchy]
    hierarchy_unique_name = _generate_hierarchy_unique_name(
        level.dimension, level.hierarchy
    )
    return (
        f"{hierarchy_unique_name}.[{_escape(level.name)}].Members"
        if hierarchy.slicing or not include_totals
        else f"Hierarchize(Descendants({{{hierarchy_unique_name}.[AllMember]}}, {level_depth + 1}, SELF_AND_BEFORE))"
    )


def _generate_rows_set(
    levels: Mapping[BaseLevel, int],
    *,
    hierarchies: BaseHierarchiesBound,
    include_totals: bool,
) -> str:
    if len(levels) == 1:
        level, level_depth = next(iter(levels.items()))
        return _generate_level_set(
            level,
            hierarchies=hierarchies,
            include_totals=include_totals,
            level_depth=level_depth,
        )

    return f"""Crossjoin({", ".join(
        [
            _generate_level_set(level, hierarchies=hierarchies,include_totals=include_totals, level_depth=level_depth)
            for level, level_depth in levels.items()
        ]
    )})"""


def _ensure_condition_on_shallowest_level(
    level_coordinates: LevelCoordinates,
    *,
    hierarchies: BaseHierarchiesBound,
) -> None:
    if (
        next(
            iter(
                hierarchies[
                    level_coordinates.dimension_name, level_coordinates.hierarchy_name
                ].levels
            )
        )
        != level_coordinates.level_name
    ):
        raise (
            ValueError(
                f"Only conditions based on the shallowest level of a hierarchy are supported but level {level_coordinates} was given."
            )
        )


def _generate_hierarchy_coordinates_to_member_paths_from_conditions(
    *,
    hierarchies: BaseHierarchiesBound,
    hierarchy_isin_conditions: Iterable[BaseHierarchyIsinCondition],
    level_conditions: Iterable[BaseLevelCondition],
    level_isin_conditions: Iterable[BaseLevelIsinCondition],
) -> Dict[Tuple[str, str], Sequence[Tuple[Constant, ...]]]:
    hierarchy_coordinates_to_member_paths: Dict[
        Tuple[str, str], Sequence[Tuple[Constant, ...]]
    ] = {}

    for level_condition in level_conditions:
        if level_condition.operator != "eq":
            raise (
                ValueError(
                    f"Only level conditions based on equality (==) are supported but operation {level_condition.operator} was given."
                )
            )

        _ensure_condition_on_shallowest_level(
            level_condition.level_coordinates, hierarchies=hierarchies
        )

        hierarchy_coordinates_to_member_paths[
            level_condition.level_coordinates.dimension_name,
            level_condition.level_coordinates.hierarchy_name,
        ] = [(Constant(level_condition.value),)]

    for level_isin_condition in level_isin_conditions:
        _ensure_condition_on_shallowest_level(
            level_isin_condition.level_coordinates, hierarchies=hierarchies
        )

        hierarchy_coordinates_to_member_paths[
            level_isin_condition.level_coordinates.dimension_name,
            level_isin_condition.level_coordinates.hierarchy_name,
        ] = [(member,) for member in level_isin_condition.members]

    for hierarchy_isin_condition in hierarchy_isin_conditions:
        hierarchy_coordinates_to_member_paths[
            hierarchy_isin_condition.hierarchy_coordinates.dimension_name,
            hierarchy_isin_condition.hierarchy_coordinates.hierarchy_name,
        ] = hierarchy_isin_condition.member_paths

    return hierarchy_coordinates_to_member_paths


def _generate_member_unique_name(
    member_path: Iterable[Constant], *, hierarchy: BaseHierarchyBound
) -> str:
    parts = [_generate_hierarchy_unique_name(hierarchy.dimension, hierarchy.name)]

    if not hierarchy.slicing:
        parts.append("[AllMember]")

    for member in member_path:
        value = member.value
        if not isinstance(value, str):
            raise (
                TypeError(
                    f"Only conditions against strings are supported but ({hierarchy.dimension}, {hierarchy.name}) was compared against {value} of type {type(value)}."
                )
            )

        parts.append(f"[{_escape(value)}]")

    return ".".join(parts)


def _generate_filter(
    *,
    hierarchy: BaseHierarchyBound,
    member_paths: Iterable[Tuple[Constant, ...]],
) -> str:
    return _generate_set(
        [
            _generate_member_unique_name(member_path, hierarchy=hierarchy)
            for member_path in member_paths
        ]
    )


def _generate_filters(
    *,
    hierarchies: BaseHierarchiesBound,
    hierarchy_coordinates_to_member_paths: Mapping[
        Tuple[str, str], Iterable[Tuple[Constant, ...]]
    ],
    scenario_name: str,
) -> List[str]:
    filters = [
        _generate_filter(
            hierarchy=hierarchies[hierarchy_coordinates[0], hierarchy_coordinates[1]],
            member_paths=member_paths,
        )
        for hierarchy_coordinates, member_paths in hierarchy_coordinates_to_member_paths.items()
    ]

    if scenario_name != BASE_SCENARIO_NAME:
        filters.append(f"[Epoch].[Epoch].[{_escape(scenario_name)}]")

    return filters


def _generate_from_clause(
    *,
    cube_name: str,
    hierarchies: BaseHierarchiesBound,
    filters: Sequence[str],
) -> str:
    from_cube = f"FROM [{_escape(cube_name)}]"

    if not filters:
        return from_cube

    return f"FROM (SELECT {filters[-1]} ON COLUMNS {_generate_from_clause(cube_name=cube_name, hierarchies=hierarchies, filters=filters[0:-1])})"


def _generate_mdx_with_decombined_conditions(
    *,
    cube_name: str,
    hierarchies: BaseHierarchiesBound,
    hierarchy_isin_conditions: Iterable[BaseHierarchyIsinCondition] = (),
    include_totals: bool = False,
    levels: Iterable[BaseLevel],
    level_conditions: Iterable[BaseLevelCondition] = (),
    level_isin_conditions: Iterable[BaseLevelIsinCondition] = (),
    measures: Iterable[BaseMeasure],
    scenario_name: str = BASE_SCENARIO_NAME,
) -> str:
    mdx = f"SELECT {_generate_columns_set(measures)} ON COLUMNS"

    deepest_levels = _keep_only_deepest_levels(levels, hierarchies=hierarchies)

    if deepest_levels:
        mdx = f"{mdx}, NON EMPTY {_generate_rows_set(deepest_levels, hierarchies=hierarchies, include_totals=include_totals)} ON ROWS"

    hierarchy_coordinates_to_member_paths = (
        _generate_hierarchy_coordinates_to_member_paths_from_conditions(
            hierarchies=hierarchies,
            hierarchy_isin_conditions=hierarchy_isin_conditions,
            level_conditions=level_conditions,
            level_isin_conditions=level_isin_conditions,
        )
    )

    filters = _generate_filters(
        hierarchies=hierarchies,
        hierarchy_coordinates_to_member_paths=hierarchy_coordinates_to_member_paths,
        scenario_name=scenario_name,
    )

    mdx = f"{mdx} {_generate_from_clause(cube_name=cube_name, hierarchies=hierarchies, filters=filters)}"

    return mdx


def generate_mdx(
    *,
    cube_name: str,
    hierarchies: BaseHierarchiesBound,
    filter: Optional[BaseCondition] = None,  # pylint: disable=redefined-builtin
    include_totals: bool = False,
    levels: Iterable[BaseLevel] = (),
    measures: Iterable[BaseMeasure] = (),
    scenario: str = BASE_SCENARIO_NAME,
) -> str:
    """Return the corresponding MDX query.

    The value of the measures is given on all the members of the given levels.
    If no level is specified then the value at the top level is returned.
    """
    level_conditions, level_isin_conditions, hierarchy_isin_conditions = (
        ([], [], []) if filter is None else decombine_condition(filter)
    )

    return _generate_mdx_with_decombined_conditions(
        cube_name=cube_name,
        hierarchies=hierarchies,
        hierarchy_isin_conditions=hierarchy_isin_conditions,
        include_totals=include_totals,
        levels=levels,
        level_conditions=level_conditions,
        level_isin_conditions=level_isin_conditions,
        measures=measures,
        scenario_name=scenario,
    )
