from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import (
    MeasureDescription,
    MeasureLike,
    _convert_to_measure_description,
)


def min(  # pylint: disable=redefined-builtin
    *measures: MeasureLike,
) -> MeasureDescription:
    """Return a measure equal to the minimum of the passed arguments.

    Example:

        >>> df = pd.DataFrame(
        ...     columns=["City", "A", "B", "C", "D"],
        ...     data=[
        ...         ("Berlin", 15.0, 10.0, 10.1, 1.0),
        ...         ("London", 24.0, 16.0, 20.5, 3.14),
        ...         ("New York", -27.0, 15.0, 30.7, 10.0),
        ...         ("Paris", 0.0, 0.0, 0.0, 0.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(df, keys=["City"], table_name="Math")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> m["min"] = tt.math.min(m["A.SUM"], m["B.SUM"])
        >>> cube.query(m["A.SUM"], m["B.SUM"], m["min"], levels=[l["City"]])
                   A.SUM  B.SUM     min
        City
        Berlin     15.00  10.00   10.00
        London     24.00  16.00   16.00
        New York  -27.00  15.00  -27.00
        Paris        .00    .00     .00

    """
    if len(measures) < 2:
        raise ValueError(
            "You can not calculate the min of a single measure using this function. "
            "If you want to find the minimum value of this measure on the levels it is defined on, use atoti.agg.min"
        )
    return CalculatedMeasure(
        Operator(
            "min", [_convert_to_measure_description(measure) for measure in measures]
        )
    )
