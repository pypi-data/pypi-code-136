from typing import Tuple, Union

TableName = str
SchemaName = str
DatabaseName = str

ExternalTableKey = Union[
    TableName, Tuple[SchemaName, TableName], Tuple[DatabaseName, SchemaName, TableName]
]
