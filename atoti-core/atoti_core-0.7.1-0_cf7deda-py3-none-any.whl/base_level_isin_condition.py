from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple

from .base_single_condition import BaseSingleCondition
from .constant import Constant
from .keyword_only_dataclass import keyword_only_dataclass
from .level_coordinates import LevelCoordinates


@keyword_only_dataclass
@dataclass(frozen=True)
class BaseLevelIsinCondition(BaseSingleCondition):
    operator: str = field(default="li", init=False)
    level_coordinates: LevelCoordinates
    members: Tuple[Constant, ...]
