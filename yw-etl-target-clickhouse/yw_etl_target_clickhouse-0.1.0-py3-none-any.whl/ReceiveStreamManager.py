import contextlib
from pathlib import Path
from typing import ContextManager

from yw_etl_target_clickhouse.Database import Database
from yw_etl_target_clickhouse.ReceiveStream import ReceiveStream
from yw_etl_target_clickhouse.utils import targetlog


@contextlib.contextmanager
def receive_stream_manager(stream_table_lookup: dict, database: Database, working_dir: Path,
                           retain_csv: bool) -> ContextManager['ReceiveStreamManager']:
    manager = ReceiveStreamManager(stream_table_lookup, database, working_dir, retain_csv)
    try:
        yield manager
        manager.sink_all()
    except Exception as e:
        targetlog.error(e)
        raise e
    finally:
        manager.close_all()


class StreamIsNotDeclared(Exception):
    def __init__(self, stream_name: str):
        super().__init__(f"stream {stream_name} is not declared in stream-table mapping")


class ReceiveStreamManager:
    """Do not instantiate ReceiveStreamManager directly, use

        with receive_stream_manager(...) as manager:
            ...

    """

    def __init__(self, stream_table_lookup: dict, database: Database, working_dir: Path, retain_csv: bool):
        self.retain_csv = retain_csv
        self.working_dir = working_dir
        self.database = database
        self.stream_table_lookup = stream_table_lookup

        self.opened_streams: dict[str, ReceiveStream] = {}

    def get_stream(self, stream_name: str) -> 'ReceiveStream':
        table_name = self.stream_table_lookup.get(stream_name, None)
        if table_name is None:
            raise StreamIsNotDeclared(stream_name)

        if stream_name in self.opened_streams:
            return self.opened_streams[stream_name]
        else:
            self.opened_streams[stream_name] = ReceiveStream(stream_name, table_name, self.database, self.working_dir,
                                                             self.retain_csv)
            return self.get_stream(stream_name)

    def sink_all(self):
        for s in self.opened_streams.values():
            targetlog.debug(f"sinking {s}")
            s.sink()

    def close_all(self):
        for k, s in self.opened_streams.items():
            targetlog.debug(f"closing {s}")
            s.close()

        self.opened_streams = []
