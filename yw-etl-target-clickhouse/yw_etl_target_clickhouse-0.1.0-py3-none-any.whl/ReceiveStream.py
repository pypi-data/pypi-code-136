import csv
from pathlib import Path

from yw_etl_target_clickhouse.Database import Database
from yw_etl_target_clickhouse.utils import targetlog


class ReceiveStreamIsClosed(Exception):
    def __init__(self, r: 'ReceiveStream'):
        super().__init__(f"{r} is closed")


class ReceiveStream:
    @staticmethod
    def ensure_open(fn):
        def method(self: 'ReceiveStream', *args):
            if self._is_closed:
                raise ReceiveStreamIsClosed(self)
            return fn(self, *args)

        return method

    def __init__(self, stream_name: str, table_name: str, database: Database, working_dir: Path, retain_csv: bool):
        self.database = database
        self.retain_csv = retain_csv
        self.stream_name = stream_name
        self.table_name = table_name
        self.working_dir = working_dir

        self._csv_path = self.working_dir / (self.stream_name + '.csv')
        self._file = open(self._csv_path, 'w')
        self._csv_writer = csv.writer(self._file)

        self._is_closed = False

    @ensure_open
    def write_record(self, record: dict):
        row = record.values()
        self._csv_writer.writerow(row)

    @ensure_open
    def sink(self):
        # ensure data is flushed
        self._file.flush()
        self.database.load_csv(self._csv_path, self.table_name)

    def close(self):
        try:
            targetlog.debug(f"close {self}")
            if self._is_closed:
                return

            self._file.close()
            if not self.retain_csv:
                targetlog.debug(f"drop {self._csv_path}")
                self._csv_path.unlink()
        finally:
            self._file = None
            self._csv_writer = None
            self._is_closed = True

    def __str__(self) -> str:
        return f"ReceiveStream[name={self.stream_name}, table={self.table_name}]"
