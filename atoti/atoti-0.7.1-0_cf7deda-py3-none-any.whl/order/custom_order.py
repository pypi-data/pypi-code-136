from dataclasses import dataclass
from typing import Any, Sequence

from atoti_core import keyword_only_dataclass

from ._base_order import BaseOrder


@keyword_only_dataclass
@dataclass(frozen=True)
class CustomOrder(BaseOrder):
    """Custom order with the given first elements.

    Example:
        >>> df = pd.DataFrame(
        ...     {
        ...         "Product": ["TV", "Smartphone", "Computer", "Screen"],
        ...         "Quantity": [12, 18, 50, 68],
        ...     }
        ... )
        >>> table = session.read_pandas(df, table_name="Products")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> cube.query(m["Quantity.SUM"], levels=[l["Product"]])
                   Quantity.SUM
        Product
        Computer             50
        Screen               68
        Smartphone           18
        TV                   12
        >>> l["Product"].order = tt.CustomOrder(first_elements=["TV", "Screen"])
        >>> cube.query(m["Quantity.SUM"], levels=[l["Product"]])
                   Quantity.SUM
        Product
        TV                   12
        Screen               68
        Computer             50
        Smartphone           18

    """

    first_elements: Sequence[Any]

    @property
    def _key(self) -> str:
        return "Custom"
