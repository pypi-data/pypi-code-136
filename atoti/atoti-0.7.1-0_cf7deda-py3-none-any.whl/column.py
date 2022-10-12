from dataclasses import dataclass, field
from typing import Any, Optional, Protocol, Sequence

from atoti_core import (
    BitwiseOperatorsOnly,
    ColumnCoordinates,
    Constant,
    ConstantValue,
    DataType,
    ReprJson,
    ReprJsonable,
    is_json_primitive,
    keyword_only_dataclass,
)
from typeguard import typeguard_ignore

from ._column_condition import ColumnCondition
from ._column_isin_condition import ColumnIsinCondition
from ._operation import ColumnOperation, Operation
from .type import DataType


class _GetColumnDataType(Protocol):
    def __call__(self, column_name: str, /, *, table_name: str) -> DataType:
        ...


class _GetColumnDefaultValue(Protocol):
    def __call__(self, column_name: str, /, *, table_name: str) -> Any:
        ...


class _SetColumnDefaultValue(Protocol):
    def __call__(
        self,
        default_value: Any,
        /,
        *,
        column_name: str,
        table_name: str,
        data_type: DataType,
    ) -> Any:
        ...


@keyword_only_dataclass
@typeguard_ignore
@dataclass(eq=False)
class Column(BitwiseOperatorsOnly, ReprJsonable):
    """Column of a :class:`atoti.Table`."""

    _name: str
    _table_keys: Sequence[str]
    _table_name: str
    _get_column_data_type: _GetColumnDataType
    _get_column_default_value: _GetColumnDefaultValue = field(repr=False)
    _set_column_default_value: _SetColumnDefaultValue = field(repr=False)

    @property
    def name(self) -> str:
        """The name of the column."""
        return self._name

    @property
    def data_type(self) -> DataType:
        """The type of the elements in the column."""
        return self._get_column_data_type(self.name, table_name=self._table_name)

    @property
    def _column_coordinates(self) -> ColumnCoordinates:
        return ColumnCoordinates(table_name=self._table_name, column_name=self.name)

    @property
    def default_value(self) -> Any:
        """Value used to replace ``None`` inserted values.

        Each data type has its own default ``default_value`` value:

        >>> from pprint import pprint
        >>> table = session.create_table(
        ...     "Main data types",
        ...     types={
        ...         "boolean": tt.BOOLEAN,
        ...         "double": tt.DOUBLE,
        ...         "double[]": tt.DOUBLE_ARRAY,
        ...         "float": tt.FLOAT,
        ...         "float[]": tt.FLOAT_ARRAY,
        ...         "int": tt.INT,
        ...         "int[]": tt.INT_ARRAY,
        ...         "LocalDate": tt.LOCAL_DATE,
        ...         "LocalDateTime": tt.LOCAL_DATE_TIME,
        ...         "LocalTime": tt.LOCAL_TIME,
        ...         "long": tt.LONG,
        ...         "long[]": tt.LONG_ARRAY,
        ...         "String": tt.STRING,
        ...         "ZonedDateTime": tt.ZONED_DATE_TIME,
        ...     },
        ... )
        >>> pprint(
        ...     {
        ...         column_name: table[column_name].default_value
        ...         for column_name in table.columns
        ...     },
        ...     sort_dicts=False,
        ... )
        {'boolean': False,
         'double': None,
         'double[]': None,
         'float': None,
         'float[]': None,
         'int': None,
         'int[]': None,
         'LocalDate': datetime.date(1970, 1, 1),
         'LocalDateTime': datetime.datetime(1970, 1, 1, 0, 0),
         'LocalTime': datetime.time(0, 0),
         'long': None,
         'long[]': None,
         'String': 'N/A',
         'ZonedDateTime': datetime.datetime(1970, 1, 1, 0, 0, tzinfo=tzutc())}

        Key columns cannot have ``None`` as their default value so it is forced to something else.
        For numeric scalar columns, this is zero:

        >>> table = session.create_table(
        ...     "Numeric",
        ...     keys=["int", "float"],
        ...     types={
        ...         "int": tt.INT,
        ...         "float": tt.FLOAT,
        ...         "long": tt.LONG,
        ...         "double": tt.DOUBLE,
        ...     },
        ... )
        >>> {
        ...     column_name: table[column_name].default_value
        ...     for column_name in table.columns
        ... }
        {'int': 0, 'float': 0.0, 'long': None, 'double': None}
        >>> table += (None, None, None, None)
        >>> table.head()
                   long  double
        int float
        0   0.0     NaN     NaN

        The default value of array columns is ``None`` and cannot be changed:

        >>> session.create_table(  # doctest: +ELLIPSIS
        ...     "Array",
        ...     types={"long array": tt.LONG_ARRAY},
        ...     default_values={"long array": [0, 0]},
        ... )
        Traceback (most recent call last):
            ...
        atoti._exceptions.AtotiJavaException: Cannot make an array type non nullable. ...

        Changing the default value from ``None`` to something else affects both the previously inserted ``None`` values and the upcoming ones:

        >>> table["long"].default_value = 42
        >>> table["long"].default_value
        42
        >>> table.head()
                   long  double
        int float
        0   0.0      42     NaN
        >>> table += (1, None, None, None)
        >>> table.head()
                   long  double
        int float
        0   0.0      42     NaN
        1   0.0      42     NaN

        Once a column has a default value different than ``None``, it cannot be changed anymore:

        >>> table["long"].default_value = 1337
        Traceback (most recent call last):
            ...
        NotImplementedError: The default value is already not ``None`` and cannot be changed: recreate the table using the `default_values` parameter instead.
        >>> table["long"].default_value
        42
        >>> del session.tables["Numeric"]
        >>> table = session.create_table(
        ...     "Numeric",
        ...     keys=["int", "float"],
        ...     types={
        ...         "int": tt.INT,
        ...         "float": tt.FLOAT,
        ...         "long": tt.LONG,
        ...         "double": tt.DOUBLE,
        ...     },
        ...     default_values={"long": 1337},
        ... )
        >>> table["long"].default_value
        1337

        The default value can also not be changed to ``None``:

        >>> table = session.create_table("Stringly", types={"String": tt.STRING})
        >>> table["String"].default_value = None
        Traceback (most recent call last):
            ...
        NotImplementedError: The default value cannot be changed to `None`: recreate the table using the `default_values` parameter instead.
        >>> table["String"].default_value
        'N/A'
        >>> del session.tables["Stringly"]
        >>> table = session.create_table(
        ...     "Stringly",
        ...     types={"String": tt.STRING},
        ...     default_values={"String": None},
        ... )
        >>> print(table["String"].default_value)
        None
        """
        return self._get_column_default_value(self.name, table_name=self._table_name)

    @default_value.setter
    def default_value(self, default_value: Any) -> None:
        alternative = "recreate the table using the `default_values` parameter instead"
        if default_value is None:
            raise NotImplementedError(
                f"The default value cannot be changed to `None`: {alternative}."
            )
        if self.default_value is not None:
            # See https://support.activeviam.com/jira/browse/PIVOT-5681.
            raise NotImplementedError(
                f"The default value is already not ``None`` and cannot be changed: {alternative}."
            )
        self._set_column_default_value(
            default_value,
            column_name=self.name,
            table_name=self._table_name,
            data_type=self.data_type,
        )

    def isin(self, *members: Optional[ConstantValue]) -> ColumnIsinCondition:
        """Return a condition evaluating to ``True`` if a column element is among the given members and ``False`` otherwise.

        ``table["City"].isin("Paris", "New York")`` is equivalent to ``(table["City"] == "Paris") | (table["City"] == "New York")``.

        Args:
            members: One or more members on which the column should be."""

        return ColumnIsinCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _members=tuple(
                None if member is None else Constant(member) for member in members
            ),
        )

    def isnull(self) -> ColumnCondition:
        """Return a condition evaluating to ``True`` when a column element is ``None`` and ``False`` otherwise.

        Use `~column.isnull()` for the opposite behavior.
        """
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=None,
            _comparison_operator="eq",
        )

    def __mul__(self, other: Any) -> Operation:
        return ColumnOperation(self._column_coordinates, self.data_type) * other  # type: ignore[no-any-return]

    def __rmul__(self, other: Any) -> Operation:
        return other * ColumnOperation(self._column_coordinates, self.data_type)  # type: ignore[no-any-return]

    def __truediv__(self, other: Any) -> Operation:
        return ColumnOperation(self._column_coordinates, self.data_type) / other  # type: ignore[no-any-return]

    def __rtruediv__(self, other: Any) -> Operation:
        return other / ColumnOperation(self._column_coordinates, self.data_type)  # type: ignore[no-any-return]

    def __add__(self, other: Any) -> Operation:
        return ColumnOperation(self._column_coordinates, self.data_type) + other  # type: ignore[no-any-return]

    def __radd__(self, other: Any) -> Operation:
        return other + ColumnOperation(self._column_coordinates, self.data_type)  # type: ignore[no-any-return]

    def __sub__(self, other: Any) -> Operation:
        return ColumnOperation(self._column_coordinates, self.data_type) - other  # type: ignore[no-any-return]

    def __rsub__(self, other: Any) -> Operation:
        return other - ColumnOperation(self._column_coordinates, self.data_type)  # type: ignore[no-any-return]

    def __eq__(  # type: ignore[override]
        self,
        other: Any,
    ) -> ColumnCondition:
        if other is None:
            raise ValueError("To compare with `None`, use `column.isnull()` instead.")
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=other,
            _comparison_operator="eq",
        )

    def __ne__(  # type: ignore[override]
        self,
        other: Any,
    ) -> ColumnCondition:
        if other is None:
            raise ValueError("To compare with `None`, use `~column.isnull()` instead.")
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=other,
            _comparison_operator="ne",
        )

    def __lt__(self, other: Any) -> ColumnCondition:
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=other,
            _comparison_operator="lt",
        )

    def __gt__(self, other: Any) -> ColumnCondition:
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=other,
            _comparison_operator="gt",
        )

    def __le__(self, other: Any) -> ColumnCondition:
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=other,
            _comparison_operator="le",
        )

    def __ge__(self, other: Any) -> ColumnCondition:
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self.data_type,
            _value=other,
            _comparison_operator="ge",
        )

    def _repr_json_(self) -> ReprJson:
        return {
            "key": self.name in self._table_keys,
            "type": self.data_type,
            "default_value": self.default_value
            if is_json_primitive(self.default_value)
            else repr(self.default_value),
        }, {"expanded": True, "root": self.name}
