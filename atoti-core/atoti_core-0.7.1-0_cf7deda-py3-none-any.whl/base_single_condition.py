from __future__ import annotations

from .base_condition import BaseCondition
from .base_multi_condition import BaseMultiCondition


class BaseSingleCondition(BaseCondition):
    def __and__(self, other: BaseCondition) -> BaseCondition:
        if isinstance(other, BaseMultiCondition):
            return other & self

        return BaseMultiCondition(conditions=(self, other))
