from typing import List

from ..utils import match_regexps
from .base import (
    CHECKSUM_HEXDIGITS,
    MD5_HEXDIGITS,
    TIMESTAMP_PRECISION_POS,
    ConnectError,
    DbPath,
    ColType,
    ColType_UUID,
    ThreadedDatabase,
    import_helper,
)
from .database_types import Decimal, Float, FractionalType, Integer, TemporalType, Text, Timestamp, TimestampTZ


@import_helper("vertica")
def import_vertica():
    import vertica_python

    return vertica_python


class Vertica(ThreadedDatabase):
    default_schema = "public"

    TYPE_CLASSES = {
        # Timestamps
        "timestamp": Timestamp,
        "timestamptz": TimestampTZ,
        # Numbers
        "numeric": Decimal,
        "int": Integer,
        "float": Float,
        # Text
        "char": Text,
        "varchar": Text,
    }

    ROUNDS_ON_PREC_LOSS = True

    def __init__(self, *, thread_count, **kw):
        self._args = kw
        self._args["AUTOCOMMIT"] = False

        super().__init__(thread_count=thread_count)

    def create_connection(self):
        vertica = import_vertica()
        try:
            c = vertica.connect(**self._args)
            return c
        except vertica.errors.ConnectionError as e:
            raise ConnectError(*e.args) from e

    def _parse_type(
        self,
        table_path: DbPath,
        col_name: str,
        type_repr: str,
        datetime_precision: int = None,
        numeric_precision: int = None,
        numeric_scale: int = None,
    ) -> ColType:
        timestamp_regexps = {
            r"timestamp\(?(\d?)\)?": Timestamp,
            r"timestamptz\(?(\d?)\)?": TimestampTZ,
        }
        for m, t_cls in match_regexps(timestamp_regexps, type_repr):
            precision = int(m.group(1)) if m.group(1) else 6
            return t_cls(precision=precision, rounds=self.ROUNDS_ON_PREC_LOSS)

        number_regexps = {
            r"numeric\((\d+),(\d+)\)": Decimal,
        }
        for m, n_cls in match_regexps(number_regexps, type_repr):
            _prec, scale = map(int, m.groups())
            return n_cls(scale)

        string_regexps = {
            r"varchar\((\d+)\)": Text,
            r"char\((\d+)\)": Text,
        }
        for m, n_cls in match_regexps(string_regexps, type_repr):
            return n_cls()

        return super()._parse_type(table_path, col_name, type_repr, datetime_precision, numeric_precision)

    def select_table_schema(self, path: DbPath) -> str:
        schema, table = self._normalize_table_path(path)

        return (
            "SELECT column_name, data_type, datetime_precision, numeric_precision, numeric_scale "
            "FROM V_CATALOG.COLUMNS "
            f"WHERE table_name = '{table}' AND table_schema = '{schema}'"
        )

    def quote(self, s: str):
        return f'"{s}"'

    def concat(self, l: List[str]) -> str:
        return " || ".join(l)

    def md5_to_int(self, s: str) -> str:
        return f"CAST(HEX_TO_INTEGER(SUBSTRING(MD5({s}), {1 + MD5_HEXDIGITS - CHECKSUM_HEXDIGITS})) AS NUMERIC(38, 0))"

    def to_string(self, s: str) -> str:
        return f"CAST({s} AS VARCHAR)"

    def normalize_timestamp(self, value: str, coltype: TemporalType) -> str:
        if coltype.rounds:
            return f"TO_CHAR({value}::TIMESTAMP({coltype.precision}), 'YYYY-MM-DD HH24:MI:SS.US')"

        timestamp6 = f"TO_CHAR({value}::TIMESTAMP(6), 'YYYY-MM-DD HH24:MI:SS.US')"
        return (
            f"RPAD(LEFT({timestamp6}, {TIMESTAMP_PRECISION_POS+coltype.precision}), {TIMESTAMP_PRECISION_POS+6}, '0')"
        )

    def normalize_number(self, value: str, coltype: FractionalType) -> str:
        return self.to_string(f"CAST({value} AS NUMERIC(38, {coltype.precision}))")

    def normalize_uuid(self, value: str, coltype: ColType_UUID) -> str:
        # Trim doesn't work on CHAR type
        return f"TRIM(CAST({value} AS VARCHAR))"
