"""Java function implementation for array functions."""

from ..._operation import JavaFunctionOperation, Operation
from ...type import DOUBLE, DOUBLE_ARRAY
from ..java_function import CustomJavaFunction

_SUM_FUNCTION = CustomJavaFunction(
    [("vector", DOUBLE_ARRAY)],
    method_name="array_sum",
    method_body="return vector.sumDouble();\n",
    output_type=DOUBLE,
)


def array_sum(operation: Operation) -> JavaFunctionOperation:
    return _SUM_FUNCTION(operation)


_MEAN_FUNCTION = CustomJavaFunction(
    [("vector", DOUBLE_ARRAY)],
    method_name="array_mean",
    method_body="return vector.average();",
    output_type=DOUBLE,
)


def array_mean(operation: Operation) -> JavaFunctionOperation:
    return _MEAN_FUNCTION(operation)
