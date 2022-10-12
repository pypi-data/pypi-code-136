from __future__ import annotations

from abc import abstractmethod
from typing import Optional

from atoti_core import BaseCondition

from .measure_description import MeasureConvertible


class Condition(BaseCondition, MeasureConvertible):
    """ABC for conditions which will be used to filter measures."""

    def __and__(self, other: BaseCondition) -> Condition:
        if not isinstance(other, Condition):
            raise TypeError("Cannot combine condition with base condition.")

        return self._and(other)

    @abstractmethod
    def _and(self, other: Condition) -> Condition:
        ...

    def __invert__(self) -> Condition:
        """Override the ~ bitwise operator.

        This allows the user to write more complicated conditions when filtering.

        Since Python's built-in ``not`` cannot be overridden to return anything other than a boolean value, the ``~`` bitwise operator is used to reverse the value of a condition.
        """
        from ._measures.boolean_measure import (  # pylint: disable=nested-import
            BooleanMeasure,
        )

        return BooleanMeasure("invert", (self._measure_description,))

    def __or__(self, other: Condition) -> Condition:
        """Override the | bitwise operator to allow users to combine conditions."""
        from ._measures.boolean_measure import (  # pylint: disable=nested-import
            BooleanMeasure,
        )

        return BooleanMeasure(
            "or",
            (self._measure_description, other._measure_description),
        )

    @property
    def _bool_alternative_message(self) -> Optional[str]:  # pylint: disable=no-self-use
        return "To combine conditions, use the bitwise operators `&` or `|` instead of the keywords `and` or `or`."
