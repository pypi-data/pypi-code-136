from typing import Dict, Mapping

from atoti.column import Column

from .._base_column_condition import BaseColumnCondition
from .._column_condition import ColumnCondition
from .._column_multi_condition import ColumnMultiCondition
from .._measures.generic_measure import GenericMeasure
from ..measure_description import MeasureDescription, _convert_to_measure_description


def _fill_with_condition(
    column_name_to_measure_description: Dict[str, MeasureDescription],
    /,
    *,
    condition: BaseColumnCondition,
) -> Dict[str, MeasureDescription]:
    if isinstance(condition, ColumnCondition):
        if condition._comparison_operator != "eq":
            raise ValueError(
                "Expected a `==` condition or a combination of `==` conditions."
            )
        column_name_to_measure_description.update(
            {
                condition._column_coordinates.column_name: _convert_to_measure_description(
                    condition._value
                )
            }
        )
        return column_name_to_measure_description
    if isinstance(condition, ColumnMultiCondition):
        if condition.operator == "or":
            raise ValueError("`or` conditions are not supported.")
        for part in condition.conditions:
            column_name_to_measure_description = _fill_with_condition(
                column_name_to_measure_description, condition=part
            )
    return column_name_to_measure_description


def lookup(column: Column, mapping: BaseColumnCondition, /) -> MeasureDescription:
    """Return a measure equal to a get-by-key query on the given table column.

    Args:
        column: The column to get the value from.
        mapping: A condition made of equality checks on all the :attr:`~atoti.Table.keys` of the passed *column*'s :class:`~atoti.Table`.

    Example:
        >>> budget_dataframe = pd.DataFrame(
        ...     {
        ...         "Position": [
        ...             "Sales manager 1",
        ...             "Sales person 1",
        ...             "Sales person 2",
        ...             "Sales manager 2",
        ...             "Sales person 3",
        ...         ],
        ...         "Budget": [20000, 15000, 10000, 40000, 12000],
        ...     }
        ... )
        >>> organization_dataframe = pd.DataFrame(
        ...     {
        ...         "Supervisors 1": [
        ...             "Sales manager 1",
        ...             "Sales manager 2",
        ...         ],
        ...         "Supervisors 2": ["Sales person 1", "Sales person 3"],
        ...         "Supervisors 3": ["Sales person 2", ""],
        ...     }
        ... )
        >>> budget_table = session.read_pandas(
        ...     budget_dataframe, table_name="Budget", keys=["Position"]
        ... )
        >>> organization_table = session.read_pandas(
        ...     organization_dataframe,
        ...     table_name="Company organization",
        ...     keys=["Supervisors 1"],
        ... )
        >>> cube = session.create_cube(organization_table, mode="manual")
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> h["Organization level"] = [
        ...     organization_table["Supervisors 1"],
        ...     organization_table["Supervisors 2"],
        ...     organization_table["Supervisors 3"],
        ... ]
        >>> m["Position"] = tt.where(
        ...     (~l["Supervisors 1"].isnull()) & (l["Supervisors 2"].isnull()),
        ...     l["Supervisors 1"],
        ...     tt.where(
        ...         (~l["Supervisors 2"].isnull()) & (l["Supervisors 3"].isnull()),
        ...         l["Supervisors 2"],
        ...         l["Supervisors 3"],
        ...     ),
        ... )
        >>> cube.query(m["Position"], levels=[l["Supervisors 3"]], include_totals=True)
                                                              Position
        Supervisors 1   Supervisors 2  Supervisors 3
        Sales manager 1                                Sales manager 1
                        Sales person 1                  Sales person 1
                                       Sales person 2   Sales person 2
        Sales manager 2                                Sales manager 2
                        Sales person 3                  Sales person 3
                                       N/A                         N/A
        >>> m["Position budget"] = tt.lookup(
        ...     budget_table["Budget"], budget_table["Position"] == m["Position"]
        ... )
        >>> cube.query(
        ...     m["Position budget"], levels=[l["Supervisors 3"]], include_totals=True
        ... )
                                                      Position budget
        Supervisors 1   Supervisors 2  Supervisors 3
        Sales manager 1                                        20,000
                        Sales person 1                         15,000
                                       Sales person 2          10,000
        Sales manager 2                                        40,000
                        Sales person 3                         12,000
    """
    if mapping._table_name != column._table_name:
        raise ValueError(
            f"Expected column and mapping condition to share the same table but column is from `{column._table_name}` and condition is on `{mapping._table_name}`."
        )
    filled_mapping: Mapping[str, MeasureDescription] = _fill_with_condition(
        {}, condition=mapping
    )
    return GenericMeasure(
        "LOOKUP",
        column._table_name,
        filled_mapping,
        column.name,
    )
