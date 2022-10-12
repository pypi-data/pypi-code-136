from __future__ import annotations

import math
from abc import abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Optional, Tuple, Union

from atoti_core import (
    BitwiseOperatorsOnly,
    ComparisonOperator,
    Constant,
    ConstantValue,
    deprecated,
    keyword_only_dataclass,
)
from typeguard import check_argument_types, typechecked, typeguard_ignore

from ._java_api import JavaApi
from ._py4j_utils import as_java_object

if TYPE_CHECKING:
    from ._measures.boolean_measure import (  # pylint: disable=nested-import
        BooleanMeasure,
    )
    from ._measures.calculated_measure import (  # pylint: disable=nested-import
        CalculatedMeasure,
    )


class MeasureConvertible(BitwiseOperatorsOnly):
    """Instances of this class can be converted to measures."""

    @property
    @abstractmethod
    def _measure_description(self) -> MeasureDescription:
        ...


@keyword_only_dataclass
@typeguard_ignore
@dataclass(eq=False)
class MeasureDescription(MeasureConvertible):
    """The description of a :class:`~atoti.Measure` that has not been added to the cube yet."""

    def _distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        """Return the name of the measure, creating it in the cube if it does not exist yet."""
        if not hasattr(self, "_name"):
            self._name: str = (  # pylint: disable=attribute-defined-outside-init
                self._do_distil(
                    java_api=java_api, cube_name=cube_name, measure_name=measure_name
                )
            )
        elif measure_name is not None:
            # This measure has already been distilled, this is a copy.
            java_api.copy_measure(
                self._name,
                measure_name,
                cube_name=cube_name,
            )
        return self._name

    @abstractmethod
    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        """Create the measure in the cube and return its name."""

    def isnull(self) -> BooleanMeasure:
        """Return a measure evaluating to ``True`` if the measure is ``None`` and ``False`` otherwise.

        Use `~measure.isnull()` for the opposite behavior.

        Example:

            >>> df = pd.DataFrame(
            ...     columns=["Country", "City", "Price"],
            ...     data=[
            ...         ("France", "Paris", 200.0),
            ...         ("Germany", "Berlin", None),
            ...     ],
            ... )
            >>> table = session.read_pandas(df, table_name="isnull example")
            >>> cube = session.create_cube(table)
            >>> l, m = cube.levels, cube.measures
            >>> m["Price.isnull"] = m["Price.SUM"].isnull()
            >>> m["Price.notnull"] = ~m["Price.SUM"].isnull()
            >>> cube.query(
            ...     m["Price.isnull"],
            ...     m["Price.notnull"],
            ...     levels=[l["Country"]],
            ... )
                    Price.isnull Price.notnull
            Country
            France         False          True
            Germany         True         False
        """
        from ._measures.boolean_measure import (  # pylint: disable=nested-import
            BooleanMeasure,
        )

        return BooleanMeasure(_operator="isNull", _operands=(self,))

    def __mul__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("mul", [self, other_measure]))

    def __rmul__(self, other: Any) -> CalculatedMeasure:
        other_measure = _convert_to_measure_description(other)
        return other_measure * self

    def __truediv__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("truediv", [self, other_measure]))

    def __rtruediv__(self, other: Any) -> CalculatedMeasure:
        other_measure = _convert_to_measure_description(other)
        return other_measure / self

    def __floordiv__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("floordiv", [self, other_measure]))

    def __rfloordiv__(self, other: Any) -> CalculatedMeasure:
        other_measure = _convert_to_measure_description(other)
        return other_measure // self

    def __add__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("add", [self, other_measure]))

    def __radd__(self, other: Any) -> CalculatedMeasure:
        other_measure = _convert_to_measure_description(other)
        return other_measure + self

    def __sub__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("sub", [self, other_measure]))

    def __rsub__(self, other: Any) -> CalculatedMeasure:
        other_measure = _convert_to_measure_description(other)
        return other_measure - self

    def __pow__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("pow", [self, other_measure]))

    def __neg__(self) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        return CalculatedMeasure(Operator("neg", [self]))

    def __mod__(self, other: Any) -> CalculatedMeasure:
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        other_measure = _convert_to_measure_description(other)
        return CalculatedMeasure(Operator("mod", [self, other_measure]))

    def _compare(
        self, other: Any, /, *, operator: ComparisonOperator
    ) -> BooleanMeasure:
        from ._measures.boolean_measure import (  # pylint: disable=nested-import
            BooleanMeasure,
        )

        other_measure = _convert_to_measure_description(other)
        return BooleanMeasure(operator, (self, other_measure))

    def __lt__(self, other: Any) -> BooleanMeasure:
        return self._compare(other, operator="lt")

    def __le__(self, other: Any) -> BooleanMeasure:
        return self._compare(other, operator="le")

    def __gt__(self, other: Any) -> BooleanMeasure:
        return self._compare(other, operator="gt")

    def __ge__(self, other: Any) -> BooleanMeasure:
        return self._compare(other, operator="ge")

    def __eq__(  # type: ignore[override]
        self,
        other: Any,
    ) -> BooleanMeasure:
        from ._measures.boolean_measure import (  # pylint: disable=nested-import
            BooleanMeasure,
        )

        if other is None:
            deprecated(
                "Comparing with `None` is deprecated, use `measure.isnull()` instead."
            )
            return BooleanMeasure("isNull", (self,))
        return self._compare(other, operator="eq")

    def __ne__(  # type: ignore[override]
        self,
        other: Any,
    ) -> BooleanMeasure:
        from ._measures.boolean_measure import (  # pylint: disable=nested-import
            BooleanMeasure,
        )

        if other is None:
            deprecated(
                "Comparing with `None` is deprecated, use `~measure.isnull()` instead."
            )
            return BooleanMeasure("notNull", (self,))
        return self._compare(other, operator="ne")

    @typechecked
    def __getitem__(
        self, key: Union[slice, int, Tuple[int, ...], MeasureLike]
    ) -> MeasureDescription:
        """Return a measure equal to the element(s) of this array measure at the passed index(es) or slice."""
        from ._measures.calculated_measure import (  # pylint: disable=nested-import
            CalculatedMeasure,
            Operator,
        )

        # Return a sub-vector if the key is a slice.
        # Because MeasureLike is unbound, pyright throws an error here
        if isinstance(key, slice):
            if key.step:
                raise ValueError("step cannot be used to slice an array measure.")
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else math.inf
            return CalculatedMeasure(
                Operator(
                    "vector_sub",
                    [
                        self,
                        _convert_to_measure_description(start),
                        _convert_to_measure_description(stop),
                    ],
                )
            )

        # Return a single element.
        if isinstance(key, (int, tuple, MeasureConvertible)):
            return CalculatedMeasure(
                Operator("vector_element", [self, _convert_to_measure_description(key)])
            )

        # Crappy input
        raise TypeError("The index must be a slice, a measure or an integer")

    @property
    def _bool_alternative_message(self) -> Optional[str]:  # pylint: disable=no-self-use
        return "For conditions on measure values use `where` or `filter` method."

    # This is needed otherwise errors like "TypeError: unhashable type: 'BooleanMeasure'" are thrown.
    # This is a "eq=False" dataclass so hash method is generated "according to how eq" is set but
    # the desired behavior is to use BitwiseOperatorsOnly.__hash__().
    def __hash__(self) -> int:  # pylint: disable=useless-super-delegation, no-self-use
        return super().__hash__()

    @property
    def _measure_description(self) -> MeasureDescription:
        return self


MeasureLike = Union[ConstantValue, MeasureConvertible]


@keyword_only_dataclass
@dataclass(eq=False)
class _ConstantMeasure(MeasureDescription):
    """A measure equal to a constant."""

    _value: Constant

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        value = as_java_object(self._value.value, gateway=java_api.gateway)
        distilled_name = java_api.create_measure(
            cube_name, measure_name, "CONSTANT", value
        )
        return distilled_name


def _convert_to_measure_description(arg: MeasureLike) -> MeasureDescription:
    check_argument_types()

    if isinstance(arg, MeasureDescription):
        return arg
    if isinstance(arg, MeasureConvertible):
        return arg._measure_description
    return _ConstantMeasure(
        _value=Constant(
            # Tuples are not valid constants, lists are.
            # See comment explaining why in `atoti_core.constant`.
            list(arg)
            if isinstance(arg, tuple)
            else arg
        )
    )
