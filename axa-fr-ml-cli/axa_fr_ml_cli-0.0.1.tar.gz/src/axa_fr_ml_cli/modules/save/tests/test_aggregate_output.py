import json
import logging
import unittest
from pathlib import Path

from aggregate_output import build_agregation

BASE_PATH = Path(__file__).resolve().parent

raw_dir = BASE_PATH / 'raw'

class TestFiltserData(unittest.TestCase):
    # Set log level to info
    logging.getLogger().setLevel(logging.INFO)

    def test_aggregate_output(self):
        result = build_agregation(str(raw_dir))
        expected_result = {'total': 3, 'number200_OK': 3, 'number200_KO': 0, 'number200': 0,
                           'number500': 0, 'number600': 0, 'number400': 3,
                           'http600': [], 'http500': [],
                           'http400': ['2_pdf', '3_pdf', '1_pdf'],
                           'http200': []}
        print(result)
        self.assertEqual(
            json.dumps(expected_result, sort_keys=True, indent=4),
            json.dumps(result, sort_keys=True, indent=4)
        )
