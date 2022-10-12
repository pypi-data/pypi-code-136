from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Tuple, TypeVar

from .base_condition import BaseCondition
from .keyword_only_dataclass import keyword_only_dataclass

_Condition = TypeVar("_Condition", bound=BaseCondition, covariant=True)


@keyword_only_dataclass
@dataclass(frozen=True)
class BaseMultiCondition(Generic[_Condition], BaseCondition):
    conditions: Tuple[_Condition, ...]

    def __and__(self, other: _Condition) -> BaseMultiCondition[_Condition]:  # type: ignore
        if isinstance(other, BaseMultiCondition):
            return BaseMultiCondition(conditions=(*self.conditions, *other.conditions))

        return BaseMultiCondition(conditions=(*self.conditions, other))
