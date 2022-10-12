from dataclasses import dataclass
from typing import Sequence

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class MultiColumnArrayConversion:
    """Convert an external table where the array values are stored with one element per column to a table with arrays.

    When a table has at least 2 columns with names following the pattern ``prefix + delimiter + number`` (numbers being consecutive and starting with 0 or 1), all these columns can be converted into a single array column.

    For instance, given a table where a "Quantity" array is stored with 5 five columns:

    +-----------+------------+------------+------------+------------+------------+
    |  PRODUCT  | QUANTITY_0 | QUANTITY_1 | QUANTITY_2 | QUANTITY_3 | QUANTITY_4 |
    +===========+============+============+============+============+============+
    | product_1 | 10         | 20         | 15         | 25         | 10         |
    +-----------+------------+------------+------------+------------+------------+
    | product_2 | 50         | 65         | 55         | 30         | 80         |
    +-----------+------------+------------+------------+------------+------------+

    These columns can be matched with the ``"QUANTITY"`` prefix and it will be converted to a table with an array column:

    +-----------+------------------+
    |  PRODUCT  |     QUANTITY     |
    +===========+==================+
    | product_1 | [10,20,15,25,10] |
    +-----------+------------------+
    | product_2 | [50,65,55,30,80] |
    +-----------+------------------+

    If several prefixes are passed, a distinct array column will be created for each of them.
    """

    column_prefixes: Sequence[str]
    """
    The prefixes of the array element columns in the external table.

    One array column per prefix will be created.
    """
