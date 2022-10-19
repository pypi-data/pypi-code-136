import base64
import re
from typing import NamedTuple, Dict, List, Set, Iterable
from sqlalchemy.engine import Connection, Dialect

from bach.expression import Expression, ColumnReferenceToken
from bach.sql_model import BachSqlModel
from sql_models.util import is_postgres, DatabaseNotSupportedException, is_bigquery, is_athena


class SortColumn(NamedTuple):
    expression: Expression
    asc: bool


class FeatureRange(NamedTuple):
    min: int
    max: int


class ResultSeries(NamedTuple):
    name: str
    expression: 'Expression'
    dtype: str


def get_result_series_dtype_mapping(result_series: List[ResultSeries]) -> Dict[str, str]:
    return {
        rs.name: rs.dtype
        for rs in result_series
    }


def get_merged_series_dtype(dtypes: Set[str]) -> str:
    """
    returns a final dtype when trying to combine series with different dtypes
    """
    from bach import get_series_type_from_dtype, SeriesAbstractNumeric
    if len(dtypes) == 1:
        return dtypes.pop()
    elif all(
        issubclass(get_series_type_from_dtype(dtype), SeriesAbstractNumeric)
        for dtype in dtypes
    ):
        return 'float64'

    # default casting will be as text, this way we avoid any SQL errors
    # when merging different db types into a column
    return 'string'


def escape_parameter_characters(conn: Connection, raw_sql: str) -> str:
    """
    Return a modified copy of the given sql with the query-parameter special characters escaped.
    e.g. if the connection uses '%' to mark a parameter, then all occurrences of '%' will be replaced by '%%'
    """
    # for now we'll just assume Postgres and assume the pyformat parameter style is used.
    # When we support more databases we'll need to do something smarter, see
    # https://www.python.org/dev/peps/pep-0249/#paramstyle
    return raw_sql.replace('%', '%%')


def is_valid_column_name(dialect: Dialect, name: str) -> bool:
    """
    Check that the given name is a valid column name in the SQL dialect.
    """
    if is_postgres(dialect):
        # Identifiers longer than 63 characters are not necessarily wrong, but they will be truncated which
        # could lead to identifier collisions, so we just disallow it.
        # source: https://www.postgresql.org/docs/14/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS
        return 0 < len(name) < 64
    if is_athena(dialect):
        # Source: https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html

        # Only allow lower-case a-z, to make sure we don't have duplicate case-insensitive column names
        regex = '^[a-z0-9_]*$'
        len_ok = 0 < len(name) <= 255
        pattern_ok = bool(re.match(pattern=regex, string=name))
        return len_ok and pattern_ok
    if is_bigquery(dialect):
        # Sources:
        #  https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#column_names
        #  https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#case_sensitivity
        #  https://cloud.google.com/bigquery/docs/schemas#column_names

        # Only allow lower-case a-z, to make sure we don't have duplicate case-insensitive column names
        regex = '^[a-z_][a-z0-9_]*$'
        reserved_prefixes = [
            '_TABLE_',
            '_FILE_',
            '_PARTITION',
            '_ROW_TIMESTAMP',
            '__ROOT__',
            '_COLIDENTIFIER'
        ]
        len_ok = 0 < len(name) <= 300
        pattern_ok = bool(re.match(pattern=regex, string=name))
        prefix_ok = not any(name.startswith(prefix.lower()) for prefix in reserved_prefixes)
        return len_ok and pattern_ok and prefix_ok
    raise DatabaseNotSupportedException(dialect)


def get_sql_column_name(dialect: Dialect, name: str) -> str:
    """
    Given the name of a series and dialect, return the sql column name.

    If the name contains no characters that require escaping, for the given dialect, then the same string is
    returned. Otherwise, a column name is that can be safely used with the given dialect. The generated name
    will be based on the given name, and can be reverted again with :meth:`get_name_from_sql_column_name()`

    **Background**
    Each Bach Series is mapped to a column in queries. Unfortunately, some databases only supported a limited
    set of characters in column names. To work around this limitation we distinguish the Series name from the
    sql-column name. The former is the name a Bach user will see and use, the latter is the name that will
    appear in SQL queries.

    The algorithm we use to map series names to column names is deterministic and reversible.

    :raises ValueError: if name cannot be appropriately escaped or is too long for the given dialect
    :return: column name for the given series name.
    """
    if is_valid_column_name(dialect, name):
        return name
    escaped = base64.b32encode(name.encode('utf-8')).decode('utf-8').lower().replace('=', '')
    escaped = f'__esc_{escaped}'
    if not is_valid_column_name(dialect, escaped):
        raise ValueError(f'Column name "{name}" is not valid for SQL dialect {dialect.name}, and cannot be '
                         f'escaped. Try making the series name shorter and/or using characters [a-z] only.')
    return escaped


def get_name_to_column_mapping(dialect: Dialect, names: Iterable[str]) -> Dict[str, str]:
    """ Give a mapping of series names to sql column names. """
    return {
        name: get_sql_column_name(dialect=dialect, name=name) for name in names
    }


def get_name_from_sql_column_name(sql_column_name: str) -> str:
    """
    Given a sql column name, give the Series name.

    This is the reverese operation of :meth:`get_sql_column_name()`.
    """
    escape_indicator = '__esc_'
    if not sql_column_name.startswith(escape_indicator):
        return sql_column_name
    rest = sql_column_name[len(escape_indicator):]
    # In get_sql_column_name() we removed the padding, but b32decode() requires the padding, so add it again.
    # Padding should make each string a multiple of 8 characters [1].
    # [1]: https://datatracker.ietf.org/doc/html/rfc4648.html#section-6
    padding = '=' * (8 - (len(rest) % 8))
    b32_encoded = (rest + padding).upper()
    original = base64.b32decode(b32_encoded.encode('utf-8')).decode('utf-8')
    return original


def validate_node_column_references_in_sorting_expressions(
    dialect: Dialect, node: BachSqlModel, order_by: List[SortColumn],
) -> None:
    """
    Validate that all ColumnReferenceTokens in order_by expressions refer columns that exist in node.
    """
    sql_column_names = set(get_sql_column_name(dialect=dialect, name=column) for column in node.series_names)
    for ob in order_by:
        invalid_column_references = [
            token.column_name
            for token in ob.expression.get_all_tokens()
            if isinstance(token, ColumnReferenceToken) and token.column_name not in sql_column_names
        ]
        if invalid_column_references:
            raise ValueError(
                (
                    'Sorting contains expressions referencing '
                    f'non-existent columns in current base node. {invalid_column_references}.'
                    ' Please call DataFrame.sort_values([]) or DataFrame.sort_index() for removing'
                    ' sorting and try again.'
                )
            )


def merge_sql_statements(dialect: Dialect, sql_statements: List[str]) -> List[str]:
    """
    Merge multiple sql statements into one statement with separating semicolons, if the dialect supports
    executing multiple statements in once call to conn.execute(). Otherwise return the original list.
    """
    if is_athena(dialect) or not sql_statements:
        return sql_statements
    combined = '; '.join(sql_statements)
    return [combined]
