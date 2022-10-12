from __future__ import annotations

from ._condition import Condition
from ._multi_condition import MultiCondition


class SingleCondition(Condition):
    def _and(self, other: Condition) -> Condition:
        if isinstance(other, MultiCondition):
            return other & self

        return MultiCondition(conditions=(self, other))
