# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from datetime import datetime
import re
from src.log_utility import *


class TestLogFileNameMatch(unittest.TestCase):

    def test_pick_load_file_match(self):
        res1 = pick_load_file_match_res("load-2022-08-18.log")
        self.assertEqual(res1.group("log_serial_number"), None)

        res2 = pick_load_file_match_res("load-2022-08-18.log.1")

        res3 = pick_load_file_match_res("load-2022-08-18.log.gz")
        self.assertEqual(res3.group("log_zip_suffix"), ".gz")
        self.assertEqual(res3.group("log_serial_number"), None)

        res4 = pick_load_file_match_res("load-2022-08-18.log.1.gz")
        self.assertEqual(bool(res1), True)
        self.assertEqual(bool(res2), True)
        self.assertEqual(bool(res3), True)
        self.assertEqual(bool(res4), True)
        self.assertEqual(res4.group("log_zip_suffix"), ".gz")
        self.assertEqual(res4.group("log_serial_number"), ".1")

# run: python3 -m test.test_can_io_config.sort_excel_test
if __name__ == '__main__':
    unittest.main()
