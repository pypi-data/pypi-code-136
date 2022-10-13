import unittest
from unittest.mock import patch
from src.v_t_chart import *
from datetime import datetime


class TestTimeRange(unittest.TestCase):

    def test_is_file_in_time_range(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 23, 14, 16, 27)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            res = is_file_in_time_range("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.gz", 1, mock_date_time.now())
            self.assertEqual(res, True)

    def test_load_json_data_all_zip_files(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 23, 14, 16, 27)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            res = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 10, mock_date_time.now()))
            self.assertIsInstance(res, set)
            self.assertIn(os.path.abspath("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.gz"), res)
            self.assertIn(os.path.abspath("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.1.gz"), res)
            self.assertNotIn(os.path.abspath("test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.2"), res)

    def test_load_json_data_general_files(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 23, 15, 45, 47)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            res = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 10, mock_date_time.now()))
            self.assertIsInstance(res, set)
            self.assertEqual(len(res), 2)
            self.assertNotIn("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.gz", res)

    def test_load_json_data_one_file(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 23, 17, 45, 47)
            mock_date_time.side_effect = lambda *args, **kw: datetime(*args, **kw)

            # 测试取前后60分钟的数据
            res = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 60, mock_date_time.now()))
            self.assertIsInstance(res, set)
            self.assertEqual(len(res), 1)
            self.assertIn(os.path.abspath("./test/test_data/sort/shuttle-debug-G27A25S/shuttle-debug-G27A25S-2022-08-23.log.2"), res)

    def test_should_get_no_data(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 24, 15, 25, 50)
            # 2022-08-24T15:35:50 ~ 2022-08-24T15:55:50
            res = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 5, mock_date_time.now()))

            input_data = collection_data_for_plot(res, mock_date_time.now(), 1)

            self.assertEqual(input_data, ([], [], []))

    def test_collection_data(self):
        with patch("src.v_t_chart.datetime") as mock_date_time:
            mock_date_time.now.return_value = datetime(2022, 8, 24, 15, 25, 50)
            # 2022-08-24T15:35:50 ~ 2022-08-24T15:55:50
            res = set(get_file_in_time_range_sort("G27A25S", "./test/test_data/sort", 30, mock_date_time.now()))

            input_data = collection_data_for_plot(res, mock_date_time.now(), 30)

            self.assertNotEqual(input_data[0], [])


# run: python3 -m test.test_can_io_config.sort_excel_test
if __name__ == '__main__':
    unittest.main()
