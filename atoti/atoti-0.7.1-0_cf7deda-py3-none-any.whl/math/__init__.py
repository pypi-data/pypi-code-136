"""Measures can be combined with mathematical operators.

Several native Python operators are supported:

    * The classic ``+``, ``-`` and ``*`` operators

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
        >>> m["Sum"] = m["A.SUM"] + m["B.SUM"]
        >>> m["Subtract"] = m["A.SUM"] - m["B.SUM"]
        >>> m["Multiply"] = m["A.SUM"] * m["B.SUM"]
        >>> cube.query(
        ...     m["A.SUM"],
        ...     m["B.SUM"],
        ...     m["Sum"],
        ...     m["Subtract"],
        ...     m["Multiply"],
        ...     levels=[l["City"]],
        ... )
                   A.SUM  B.SUM     Sum Subtract Multiply
        City
        Berlin     15.00  10.00   25.00     5.00   150.00
        London     24.00  16.00   40.00     8.00   384.00
        New York  -27.00  15.00  -12.00   -42.00  -405.00
        Paris        .00    .00     .00      .00      .00

    * The float division ``/`` and integer division ``//``

        >>> m["Float division"] = m["A.SUM"] / m["B.SUM"]
        >>> m["Int division"] = m["A.SUM"] // m["B.SUM"]
        >>> cube.query(
        ...     m["A.SUM"],
        ...     m["B.SUM"],
        ...     m["Float division"],
        ...     m["Int division"],
        ...     levels=[l["City"]],
        ... )
                   A.SUM  B.SUM Float division Int division
        City
        Berlin     15.00  10.00           1.50         1.00
        London     24.00  16.00           1.50         1.00
        New York  -27.00  15.00          -1.80        -2.00
        Paris        .00    .00            NaN          NaN

    * The exponentiation ``**``

        >>> m["a²"] = m["A.SUM"] ** 2
        >>> cube.query(m["A.SUM"], m["a²"], levels=[l["City"]])
                   A.SUM      a²
        City
        Berlin     15.00  225.00
        London     24.00  576.00
        New York  -27.00  729.00
        Paris        .00     .00

    * The modulo ``%``

        >>> m["Modulo"] = m["A.SUM"] % m["B.SUM"]
        >>> cube.query(m["A.SUM"], m["B.SUM"], m["Modulo"], levels=[l["City"]])
                   A.SUM  B.SUM Modulo
        City
        Berlin     15.00  10.00   5.00
        London     24.00  16.00   8.00
        New York  -27.00  15.00   3.00
        Paris        .00    .00    NaN

"""

from .abs import *  # pylint: disable=redefined-builtin
from .ceil import *
from .cos import *
from .erf import *
from .erfc import *
from .exp import *
from .floor import *
from .isnan import *
from .log import *
from .log10 import *
from .max import *  # pylint: disable=redefined-builtin
from .min import *  # pylint: disable=redefined-builtin
from .round import *  # pylint: disable=redefined-builtin
from .sin import *
from .sqrt import *
from .tan import *
