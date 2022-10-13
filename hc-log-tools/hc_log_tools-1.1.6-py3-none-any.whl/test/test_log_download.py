import unittest
from unittest import mock
from unittest.mock import patch
from src.log_utility import *
from datetime import datetime
import os


class TestDownload(unittest.TestCase):

    def test_get_file_in_time_range(self):
        # python3 src/pack_log.py --prd_type=sort --time_range=1  --timestamp="2022-09-13 20:05:00" --log_root_dir /home/deployer/Projects/hc_sort/current/logs
        mocked_input_args = mock.MagicMock()
        mocked_input_args.prd_type = "sort"
        mocked_input_args.log_root_dir =  "./test/test_data/pick/all"
        mocked_input_args.time_range = 1
        mocked_input_args.timestamp = "2022-09-14 17:20:00"

        res = set(get_file_in_time_range(mocked_input_args, download_log=True))
        self.assertIn(os.path.abspath('./test/test_data/pick/all/all-logs-2022-09-14-17.log'), res)

    def test_file_should_not_in_range(self):
        # python3 src/pack_log.py --prd_type=sort --time_range=1  --timestamp="2022-09-13 20:05:00" --log_root_dir /home/deployer/Projects/hc_sort/current/logs
        mocked_input_args = mock.MagicMock()
        mocked_input_args.prd_type = "sort"
        mocked_input_args.log_root_dir =  "./test/test_data/pick/all"
        mocked_input_args.time_range = 1
        mocked_input_args.timestamp = "2022-09-14 16:20:00"

        res = set(get_file_in_time_range(mocked_input_args, download_log=True))
        self.assertNotIn(os.path.abspath('./test/test_data/pick/all/all-logs-2022-09-14-17.log'), res)

        mocked_input_args.timestamp = "2022-09-14 18:20:00"
        res = set(get_file_in_time_range(mocked_input_args, download_log=True))
        self.assertNotIn(os.path.abspath('./test/test_data/pick/all/all-logs-2022-09-14-17.log'), res)

    def test_log_duriation_file_in_range(self):
        # python3 src/pack_log.py --prd_type=sort --time_range=1  --timestamp="2022-09-13 20:05:00" --log_root_dir /home/deployer/Projects/hc_sort/current/logs
        mocked_input_args = mock.MagicMock()
        mocked_input_args.prd_type = "sort"
        mocked_input_args.log_root_dir =  "./test/test_data/pick/all"
        mocked_input_args.time_range = 1
        mocked_input_args.timestamp = "2022-09-13 15:20:00"
        mocked_input_args.recursive = True

        res = set(get_file_in_time_range(mocked_input_args, download_log=True, recursive=mocked_input_args.recursive))
        self.assertIn(os.path.abspath('./test/test_data/pick/all/all-logs-2022-09-13-18.log'), res)
        self.assertIn(os.path.abspath('./test/test_data/pick/all/sub_dir/all-logs-2022-09-13-18_sub.log'), res)

    def test_log_duriation_file_in_range_not_recursive(self):
        # python3 src/pack_log.py --prd_type=sort --time_range=1  --timestamp="2022-09-13 20:05:00" --log_root_dir /home/deployer/Projects/hc_sort/current/logs
        mocked_input_args = mock.MagicMock()
        mocked_input_args.prd_type = "sort"
        mocked_input_args.log_root_dir =  "./test/test_data/pick/all"
        mocked_input_args.time_range = 1
        mocked_input_args.timestamp = "2022-09-13 15:20:00"
        mocked_input_args.recursive = False

        res = set(get_file_in_time_range(mocked_input_args, download_log=True, recursive=mocked_input_args.recursive))
        self.assertIn(os.path.abspath('./test/test_data/pick/all/all-logs-2022-09-13-18.log'), res)
        self.assertNotIn(os.path.abspath('./test/test_data/pick/all/sub_dir/all-logs-2022-09-13-18_sub.log'), res)


# run: python3 -m test.test_can_io_config.sort_excel_test
if __name__ == '__main__':
    unittest.main()
