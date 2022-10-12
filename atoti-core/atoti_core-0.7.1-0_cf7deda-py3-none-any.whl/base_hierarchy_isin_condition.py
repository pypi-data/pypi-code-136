from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple

from .base_single_condition import BaseSingleCondition
from .constant import Constant
from .hierarchy_coordinates import HierarchyCoordinates
from .keyword_only_dataclass import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class BaseHierarchyIsinCondition(BaseSingleCondition):
    operator: str = field(default="hi", init=False)
    hierarchy_coordinates: HierarchyCoordinates
    level_names: Tuple[str, ...]
    member_paths: Tuple[Tuple[Constant, ...], ...]

    def __post_init__(self) -> None:
        for member_path in self.member_paths:
            if len(member_path) > len(self.level_names):
                raise ValueError(
                    f"Member path {member_path} contains more than {len(self.level_names)} elements which is the number of levels of the {self.hierarchy_coordinates} hierarchy."
                )
