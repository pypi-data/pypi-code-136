from __future__ import annotations

from dataclasses import dataclass

from atoti_core import BaseMultiCondition, keyword_only_dataclass

from ._condition import Condition
from .measure_description import MeasureDescription


@keyword_only_dataclass
@dataclass(frozen=True)
class MultiCondition(Condition, BaseMultiCondition[Condition]):  # type: ignore[misc]
    def _and(self, other: Condition) -> Condition:
        if isinstance(other, MultiCondition):
            return MultiCondition(conditions=(*self.conditions, *other.conditions))

        return MultiCondition(
            conditions=(
                *self.conditions,
                other,
            )
        )

    @property
    def _measure_description(self) -> MeasureDescription:
        from .function._conjunction import conjunction  # pylint:disable=nested-import

        return conjunction(
            *(condition._measure_description for condition in self.conditions)
        )
