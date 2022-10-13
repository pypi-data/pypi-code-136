import unittest
import os
from unittest.mock import patch
import json
from src.v_t_chart import *
from datetime import datetime


class TestReadSortData(unittest.TestCase):

    def test_load_json_data_all_zip_files(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 23, 14, 13, 27)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            data_files = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 1, mock_date_time.now()))

            self.assertIsInstance(data_files, set)

            self.assertIn(os.path.abspath("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.gz"), data_files)
            self.assertEqual(len(data_files), 1)

            # diagram_input_data = collection_data(data_files, parse("2022-08-29 14:45:20"), 1)


    def test_read_data_lines_called_once(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 23, 14, 16, 27)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            with patch("src.v_t_chart.read_data_lines") as mock_read_data_lines:

                data_files = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 1, mock_date_time.now()))

                self.assertIsInstance(data_files, set)

                self.assertIn(os.path.abspath("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.gz"), data_files)

                self.assertEqual(len(data_files), 2)

                # collection_data(data_files, parse("2022-08-29 14:45:20"), 1)
                collection_data_for_plot(data_files, parse("2022-08-29 14:45:20"), 1)

                # self.assertEqual(mock_read_data_lines(),None)
                self.assertEqual(mock_read_data_lines.call_count, 2)


    def test_load_right_data(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 24, 15, 56, 00)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            data_files = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 1, mock_date_time.now()))

            self.assertIsInstance(data_files, set)

            self.assertEqual(len(data_files), 2)
            input_data = collection_data_for_plot(data_files, mock_date_time.now(), 1)
            print(input_data)



if __name__ == "main":
    unittest.main()
