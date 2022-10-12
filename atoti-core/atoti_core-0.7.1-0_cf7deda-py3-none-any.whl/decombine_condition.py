from typing import List, Tuple

from .base_condition import BaseCondition
from .base_hierarchy_isin_condition import BaseHierarchyIsinCondition
from .base_level_condition import BaseLevelCondition
from .base_level_isin_condition import BaseLevelIsinCondition
from .base_multi_condition import BaseMultiCondition
from .base_single_condition import BaseSingleCondition


def decombine_condition(
    condition: BaseCondition,
) -> Tuple[
    List[BaseLevelCondition],
    List[BaseLevelIsinCondition],
    List[BaseHierarchyIsinCondition],
]:
    if isinstance(condition, BaseLevelCondition):
        return [condition], [], []
    if isinstance(condition, BaseLevelIsinCondition):
        return [], [condition], []
    if isinstance(condition, BaseHierarchyIsinCondition):
        return [], [], [condition]
    if isinstance(condition, BaseMultiCondition):
        level_conditions: List[BaseLevelCondition] = []
        level_isin_conditions: List[BaseLevelIsinCondition] = []
        hierarchy_isin_conditions: List[BaseHierarchyIsinCondition] = []
        for _condition in condition.conditions:
            if not isinstance(_condition, BaseSingleCondition):
                raise NotImplementedError(
                    f"Multi-condition containing condition of type {type(_condition).__name__} are not supported."
                )

            level_conditions += decombine_condition(_condition)[0]
            level_isin_conditions += decombine_condition(_condition)[1]
            hierarchy_isin_conditions += decombine_condition(_condition)[2]

        return level_conditions, level_isin_conditions, hierarchy_isin_conditions

    raise NotImplementedError(
        f"Conditions of type {type(condition).__name__} are not supported."
    )
