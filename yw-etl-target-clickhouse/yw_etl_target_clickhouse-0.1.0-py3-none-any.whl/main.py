import io
import json.decoder
import os
import sys
import traceback

import singer.utils

from yw_etl_target_clickhouse.Database import Database
from yw_etl_target_clickhouse.ReceiveStreamManager import receive_stream_manager
from yw_etl_target_clickhouse.WorkingDirectory import WorkingDirectory
from yw_etl_target_clickhouse.utils import targetlog

REQUIRED_CONFIG_KEYS = ['connection', 'sync.stream_table_map']


def main():
    args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)
    if args.discover:
        raise Exception("Discover mode is not supported")

    config = args.config

    _stream_table_map = config['sync.stream_table_map']

    stream_table_lookup = {k: _stream_table_map[k] for k in _stream_table_map.keys()}
    database = Database.from_config(config)
    working_dir = WorkingDirectory.get_directory(config)
    retain_csv = config.get("sync.retain_csv", False)

    with receive_stream_manager(stream_table_lookup, database, working_dir, retain_csv) as manager:
        input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf8')
        for msg_line in input_stream:
            # ignore lines starts with #
            if msg_line.startswith('#'):
                continue

            try:
                msg = singer.parse_message(msg_line).asdict()
            except json.decoder.JSONDecodeError:
                targetlog.error(f"Unable to parse:\n{msg_line}")
                raise

            msg_type = msg['type']
            match msg_type:
                case 'RECORD':
                    stream_name = msg['stream']
                    rstream = manager.get_stream(stream_name)
                    record = msg['record']
                    rstream.write_record(record)
                case 'SCHEMA' | 'STATE':
                    # SCHEMA and STATE message handling not implemented
                    continue
                case _ as x:
                    targetlog.warning(f'unknown message type {x}')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        targetlog.error(e)
        if os.environ.get('DEBUG', None):
            traceback.print_exception(e)
        sys.exit(1)
