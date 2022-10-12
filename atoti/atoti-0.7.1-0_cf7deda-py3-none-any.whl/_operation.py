from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Iterable, List, Optional, Sequence

from atoti_core import (
    BitwiseOperatorsOnly,
    ColumnCoordinates,
    Constant,
    DataType,
    keyword_only_dataclass,
)

from ._measures.column_measure import ColumnMeasure
from .measure_description import MeasureDescription

if TYPE_CHECKING:
    from ._udaf_utils import (  # pylint: disable=nested-import
        JavaFunction,
        JavaOperationElement,
        OperationVisitor,
    )


def _to_operation(obj: Any, /) -> Operation:
    """Convert an object to an operation if is not already one."""
    if isinstance(obj, Operation):
        return obj

    if isinstance(obj, MeasureDescription):
        raise TypeError("MeasureDescriptions cannot be converted to an operation")

    from .column import Column  # pylint: disable=nested-import

    if isinstance(obj, Column):
        return ColumnOperation(obj._column_coordinates, obj.data_type)

    return ConstantOperation(Constant(obj))


def _get_new_columns(
    operation: Operation, column_names: Iterable[ColumnCoordinates]
) -> List[ColumnCoordinates]:
    columns: List[ColumnCoordinates] = []
    for column in operation.columns:
        if not column in column_names:
            columns.append(column)
    return columns


class Operation(BitwiseOperatorsOnly):
    """An operation between table columns."""

    @abstractmethod
    def accept(self, operation_visitor: OperationVisitor) -> JavaOperationElement:
        """Contribute this operation to the visitor."""

    @property
    @abstractmethod
    def columns(self) -> List[ColumnCoordinates]:
        """Columns involved in this operation."""

    def __mul__(self, other: Any) -> Operation:
        """Override the * operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return MultiplicationOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __rmul__(self, other: Any) -> Operation:
        """Override the * operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return MultiplicationOperation(other_op, self)
        except TypeError:
            return NotImplemented

    def __truediv__(self, other: Any) -> Operation:
        """Override the / operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return DivisionOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __rtruediv__(self, other: Any) -> Operation:
        """Override the / operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return DivisionOperation(other_op, self)
        except TypeError:
            return NotImplemented

    def __add__(self, other: Any) -> Operation:
        """Override the + operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return AdditionOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __radd__(self, other: Any) -> Operation:
        """Override the + operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return AdditionOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __sub__(self, other: Any) -> Operation:
        """Override the - operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return SubtractionOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __rsub__(self, other: Any) -> Operation:
        """Override the - operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return SubtractionOperation(other_op, self)
        except TypeError:
            return NotImplemented

    def __eq__(  # type: ignore[override]
        self,
        other: Any,
    ) -> Operation:
        """Override the == operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return EqualOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __ne__(  # type: ignore[override]
        self,
        other: Any,
    ) -> Operation:
        """Override the != operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return NotEqualOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __lt__(self, other: Any) -> Operation:
        """Override the < operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return LowerThanOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __gt__(self, other: Any) -> Operation:
        """Override the > operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return GreaterThanOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __le__(self, other: Any) -> Operation:
        """Override the <= operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return LowerThanOrEqualOperation(self, other_op)
        except TypeError:
            return NotImplemented

    def __ge__(self, other: Any) -> Operation:
        """Override the >= operator to delay the conversion."""
        try:
            other_op = _to_operation(other)
            return GreaterThanOrEqualOperation(self, other_op)
        except TypeError:
            return NotImplemented


class JavaFunctionOperation(Operation):
    @property
    @abstractmethod
    def underlyings(self) -> Sequence[Operation]:
        ...

    @property
    @abstractmethod
    def java_function(self) -> JavaFunction:
        ...

    def accept(self, operation_visitor: OperationVisitor) -> JavaOperationElement:
        return operation_visitor.visit_java_function_operation(self)

    @property
    def columns(self) -> List[ColumnCoordinates]:
        columns: List[ColumnCoordinates] = []
        for underlying in self.underlyings:
            columns += _get_new_columns(underlying, columns)
        return columns


@dataclass(frozen=True, eq=False)
class ColumnOperation(Operation):  # pylint: disable=keyword-only-dataclass
    """Column of a table in an operation."""

    _column_coordinates: ColumnCoordinates
    _column_data_type: DataType

    @property
    def _measure_description(self) -> MeasureDescription:
        return ColumnMeasure(
            _column_coordinates=self._column_coordinates,
            _plugin_key="SINGLE_VALUE_NULLABLE",
        )

    def accept(self, operation_visitor: OperationVisitor) -> JavaOperationElement:
        return operation_visitor.visit_column_operation(operation=self)

    @property
    def columns(self) -> List[ColumnCoordinates]:
        return [self._column_coordinates]


@dataclass(frozen=True, eq=False)
class ConstantOperation(Operation):  # pylint: disable=keyword-only-dataclass
    """Constant leaf of an operation."""

    _value: Constant

    def accept(self, operation_visitor: OperationVisitor) -> JavaOperationElement:
        return operation_visitor.visit_constant_operation(self)

    @property
    def columns(self) -> List[ColumnCoordinates]:
        return []


@dataclass(eq=False, frozen=True)
class LeftRightOperation(
    JavaFunctionOperation
):  # pylint: disable=keyword-only-dataclass
    """Operation with left and right member."""

    _left: Operation
    _right: Operation

    @property
    def underlyings(self) -> Sequence[Operation]:
        return [self._left, self._right]


class MultiplicationOperation(LeftRightOperation):
    """Multiplication operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import MUL_FUNCTION  # pylint: disable=nested-import

        return MUL_FUNCTION


class AdditionOperation(LeftRightOperation):
    """Addition operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import ADD_FUNCTION  # pylint: disable=nested-import

        return ADD_FUNCTION


class SubtractionOperation(LeftRightOperation):
    """Subtraction operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import SUB_FUNCTION  # pylint: disable=nested-import

        return SUB_FUNCTION


class DivisionOperation(LeftRightOperation):
    """Division operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import TRUEDIV_FUNCTION  # pylint: disable=nested-import

        return TRUEDIV_FUNCTION


@keyword_only_dataclass
@dataclass(frozen=True, eq=False)
class TernaryOperation(Operation):
    condition: ConditionOperation
    true_operation: Operation
    false_operation: Optional[Operation]

    def accept(self, operation_visitor: OperationVisitor) -> JavaOperationElement:
        return operation_visitor.visit_ternary_operation(self)

    @property
    def columns(self) -> List[ColumnCoordinates]:
        columns: List[ColumnCoordinates] = []
        columns += self.condition.columns
        columns += _get_new_columns(self.true_operation, columns)
        if self.false_operation is not None:
            columns += _get_new_columns(self.false_operation, columns)
        return columns


class ConditionOperation(LeftRightOperation):
    """Operations which can be used as conditions."""


class EqualOperation(ConditionOperation):
    """== operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import EQ_FUNCTION  # pylint: disable=nested-import

        return EQ_FUNCTION


class NotEqualOperation(ConditionOperation):
    """!= operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import NEQ_FUNCTION  # pylint: disable=nested-import

        return NEQ_FUNCTION


class GreaterThanOperation(ConditionOperation):
    """> operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import GT_FUNCTION  # pylint: disable=nested-import

        return GT_FUNCTION


class GreaterThanOrEqualOperation(ConditionOperation):
    """>= operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import GTE_FUNCTION  # pylint: disable=nested-import

        return GTE_FUNCTION


class LowerThanOperation(ConditionOperation):
    """< operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import LT_FUNCTION  # pylint: disable=nested-import

        return LT_FUNCTION


class LowerThanOrEqualOperation(ConditionOperation):
    """<= operation."""

    @property
    def java_function(self) -> JavaFunction:
        from ._udaf_utils import LTE_FUNCTION  # pylint: disable=nested-import

        return LTE_FUNCTION
