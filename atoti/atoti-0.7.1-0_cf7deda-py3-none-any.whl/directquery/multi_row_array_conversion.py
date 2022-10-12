from dataclasses import dataclass
from typing import Sequence

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class MultiRowArrayConversion:
    """Convert an external table where the arrays are stored with one value per row to a table with arrays.

    To use this option the external table must have a column index and at least one "value" column representing the array elements.

    For instance:

    +-----------+-------+----------+
    | PRODUCT   | INDEX | QUANTITY |
    +===========+=======+==========+
    | product_1 |     0 |       10 |
    +-----------+-------+----------+
    | product_1 |     1 |       20 |
    +-----------+-------+----------+
    | product_1 |     2 |       15 |
    +-----------+-------+----------+
    | product_1 |     3 |       25 |
    +-----------+-------+----------+
    | product_1 |     4 |       10 |
    +-----------+-------+----------+
    | product_2 |     0 |       50 |
    +-----------+-------+----------+
    | product_2 |     1 |       65 |
    +-----------+-------+----------+
    | product_2 |     2 |       55 |
    +-----------+-------+----------+
    | product_2 |     3 |       30 |
    +-----------+-------+----------+
    | product_2 |     4 |       80 |
    +-----------+-------+----------+

    When using ``index_column="INDEX"`` and ``array_columns=["QUANTITY"]``, this external table will be equivalent to:

    +-----------+------------------+
    |  PRODUCT  |     QUANTITY     |
    +===========+==================+
    | product_1 | [10,20,15,25,10] |
    +-----------+------------------+
    | product_2 | [50,65,55,30,80] |
    +-----------+------------------+

    If several array columns are passed, a distinct array column will be created for each of them.

    All the table columns which do not correspond to the index column or one of the array columns must be key columns.
    """

    index_column: str
    """Name of the column used as an index for the arrays."""

    array_columns: Sequence[str]
    """Names of the columns that contain array values."""
