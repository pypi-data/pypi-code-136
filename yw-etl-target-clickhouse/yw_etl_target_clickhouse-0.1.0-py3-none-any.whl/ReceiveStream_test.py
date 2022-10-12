from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock

from yw_etl_target_clickhouse.ReceiveStream import ReceiveStream, ReceiveStreamIsClosed

mock_db = Mock()
working_dir = Path(__file__).parent.parent / 'test'


class TestReceiveStream(TestCase):

    def test_sink(self):
        sname = "stream_name_3"
        tname = "table_name"

        rstream = ReceiveStream(sname, tname, mock_db, working_dir, False)
        data = [{'a': 1}, {'a': 2}, {'a': 3}]
        for d in data:
            rstream.write_record(d)

        rstream.sink()
        mock_db.load_csv.assert_called_with(rstream._csv_path, tname)

        rstream.close()

    def test_write_record(self):
        sname = "stream_name_2"
        tname = "table_name"

        rstream = ReceiveStream(sname, tname, mock_db, working_dir, True)

        data = [{'a': 1}, {'a': 2}, {'a': 3}]
        for d in data:
            rstream.write_record(d)
        # cause flush
        rstream.close()

        rtn = rstream._csv_path.read_text(encoding='utf8')
        exp = "1\n2\n3\n"
        self.assertEqual(rtn, exp)

        # clean test
        rstream._csv_path.unlink()

    def test_open_close(self):
        sname = "stream_name"
        tname = "table_name"

        rstream = ReceiveStream(sname, tname, mock_db, working_dir, False)

        # csv file should be created on ReceiveStream initialization
        csv_created = working_dir / (sname + '.csv')
        self.assertTrue(csv_created.is_file())

        # with retain_csv = False, close ReceiveStream should also remove csv file
        rstream.close()
        self.assertFalse(csv_created.exists())

        # operation after close should raise error
        try:
            rstream.write_record({"a": 1})
            self.fail("should reject operation after receive stream is closed")
        except Exception as e:
            self.assertIsInstance(e, ReceiveStreamIsClosed)
