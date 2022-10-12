from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock

from yw_etl_target_clickhouse.ReceiveStream import ReceiveStream
from yw_etl_target_clickhouse.ReceiveStreamManager import ReceiveStreamManager, StreamIsNotDeclared, \
    receive_stream_manager

stream_table_lookup = {
    'stream 1': "table_1",
    "stream 2": "table_2"
}

mock_db = Mock()
working_dir = Path(__file__).parent.parent / 'test'


class TestReceiveStreamManager(TestCase):
    def test_get_stream(self):
        manager = ReceiveStreamManager(stream_table_lookup, mock_db, working_dir, False)

        rstream = manager.get_stream(list(stream_table_lookup.keys())[0])
        self.assertIsInstance(rstream, ReceiveStream)

        try:
            manager.get_stream("not_existed_stream")
            self.fail("should throw when encounter unknown stream name")
        except Exception as e:
            self.assertIsInstance(e, StreamIsNotDeclared)

        manager.close_all()

    def test_context_management(self):
        with receive_stream_manager(stream_table_lookup, mock_db, working_dir, False) as manager:
            # no csv file is create until a stream is requested from the manager
            exp_csv_1 = working_dir / 'stream 1.csv'
            self.assertTrue(not exp_csv_1.exists())
            exp_csv_2 = working_dir / 'stream 2.csv'
            self.assertTrue(not exp_csv_2.exists())

            # request one stream
            rs1: ReceiveStream = manager.get_stream('stream 1')
            # csv file should be created
            self.assertTrue(exp_csv_1.exists())
            # insert record
            data = [{'a': 1}]
            for d in data:
                rs1.write_record(d)

        # after manage context
        # database.load_csv() should be called
        mock_db.load_csv.assert_called_with(exp_csv_1, stream_table_lookup['stream 1'])
        # csv_file should be dropped since retain_csv is False
        self.assertTrue(not exp_csv_1.exists())
