from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription


def tan(measure: MeasureDescription, /) -> MeasureDescription:
    """Return a measure equal to the tangent of the passed measure in radians.

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
        >>> m["tan(D)"] = tt.math.tan(m["D.SUM"])
        >>> cube.query(m["D.SUM"], m["tan(D)"], levels=[l["City"]])
                  D.SUM tan(D)
        City
        Berlin     1.00   1.56
        London     3.14   -.00
        New York  10.00    .65
        Paris       .00    .00

    """
    return CalculatedMeasure(Operator("tan", [measure]))
