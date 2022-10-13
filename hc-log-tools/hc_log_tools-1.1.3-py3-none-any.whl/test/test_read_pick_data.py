import unittest
import os
from unittest.mock import patch
import json
from src.v_t_chart import *
from datetime import datetime
from dateutil.parser import parse


class TestReadPickData(unittest.TestCase):

    def test_walk_folder(self):
        files = get_file_in_time_range_pick("474E50", os.path.relpath("./test/test_data/pick"), 1, parse("2022-09-03 14:23:59"))
        file_list = list(files)
        self.assertEqual(len(file_list), 1)
        self.assertIn(os.path.abspath("./test/test_data/pick/474E50/load-2022-09-03.log.gz"), file_list)


if __name__ == "main":
    unittest.main()
