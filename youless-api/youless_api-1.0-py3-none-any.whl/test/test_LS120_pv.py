import unittest

from unittest.mock import patch

from youless_api.device.LS120_pv import LS120PVOutput
from youless_api.test import MockResponse, URI_ELOGIC, URI_GENERIC


def mock_ls120_pvoutput(*args, **kwargs) -> MockResponse:
    response = MockResponse()

    def raise_ex(e):
        raise Exception(e)

    if args[0] == URI_ELOGIC:
        response.setup(
            True,
            lambda: raise_ex("Unsupported operation"),
            'd=20210903&t=14:58&v1=3024759&v2=370&c1=1&v3=19623222&v4=300',
            {'Content-Type': 'text/html'})

    if args[0] == URI_GENERIC:
        response.setup(
            True,
            lambda: {
                "cnt": " 16600,536",
                "pwr": -930,
                "lvl": 0,
                "dev": "",
                "det": "",
                "con": "OK",
                "sts": "(245)",
                "cs0": " 3021,525",
                "ps0": 1288,
                "raw": 0},
            '',
            {'Content-Type': 'application/json'})

    return response


class LS120Tests(unittest.TestCase):

    @patch('youless_api.device.LS110.requests.get', side_effect=mock_ls120_pvoutput)
    def test_ls120_pvoutput_firmware(self, mock_get):
        api = LS120PVOutput('', {})
        api.update()

        self.assertEqual(api.current_power_usage.value, -930)
        self.assertEqual(api.power_meter.total.value, 16600.536)
        self.assertEqual(api.extra_meter.usage.value, 1288)
        self.assertEqual(api.extra_meter.total.value, 3021.525)
        self.assertEqual(api.extra_meter.usage.value, 1288)

