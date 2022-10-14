import datetime
from unittest import TestCase
from unittest.mock import patch, Mock

from youless_api.const import STATE_FAILED, STATE_OK
from youless_api.device.LS120 import LS120
from youless_api.test import MockResponse, URI_ELOGIC, URI_PHASES

default_ok_response = [{
    "tm": 1611929119,
    "net": 9194.164,
    "pwr": 2382,
    "ts0": 1608654000,
    "cs0": 0.000,
    "ps0": 0,
    "p1": 4703.562,
    "p2": 4490.631,
    "n1": 0.029,
    "n2": 0.000,
    "gas": 1624.264,
    "gts": int(datetime.datetime.now().strftime("%y%m%d%H00"))
}]
default_phases_response = {
    "ver": 50,
    "tr": 2,
    "i1": 0.000,
    "i2": 0.000,
    "i3": 2.000,
    "v1": 231.600,
    "v2": 230.400,
    "v3": 233.100,
    "l1": 64,
    "l2": 103,
    "l3": 312
}


def mock_ls120_ok(*args, **kwargs) -> MockResponse:
    response = MockResponse()
    if args[0] == URI_ELOGIC:
        response.setup(
            True,
            lambda: default_ok_response,
            '',
            {'Content-Type': 'application/json'}
        )

    return response


def mock_ls120_phase_output(*args, **kwargs) -> MockResponse:
    response = mock_ls120_ok(*args, *kwargs)

    if args[0] == URI_PHASES:
        response.setup(
            True,
            lambda: default_phases_response,
            '',
            {'Content-Type': 'application/json'}
        )

    return response


class LS120Tests(TestCase):

    def test_ls120_failed(self):
        """Check what happens if the remote device is not ok"""
        with patch('youless_api.device.LS120.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=False)

            api = LS120('', {})
            api.update()

        self.assertEqual(api.state, STATE_FAILED)

    @patch('youless_api.device.LS120.requests.get', side_effect=mock_ls120_ok)
    def test_ls120_ok(self, mock_get):
        """Test the update functionality."""
        api = LS120('', {})
        api.update()

        self.assertEqual(api.state, STATE_OK)
        self.assertEqual(api.firmware, None)

        self.assertEqual(api.power_meter.total.value, 9194.164)
        self.assertEqual(api.power_meter.high.value, 4490.631)
        self.assertEqual(api.power_meter.low.value, 4703.562)
        self.assertEqual(api.current_power_usage.value, 2382)
        self.assertEqual(api.gas_meter.value, 1624.264)
        self.assertEqual(api.delivery_meter.high.value, 0.000)
        self.assertEqual(api.delivery_meter.low.value, 0.029)
        self.assertEqual(api.phase1, None)
        self.assertEqual(api.phase2, None)
        self.assertEqual(api.phase3, None)

    def test_ls120_gas_stale(self):
        """Test case for incident with stale data from the API"""
        with patch('youless_api.device.LS120.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = [{
                "tm": 1611929119,
                "net": 9194.164,
                "pwr": 2382,
                "ts0": 1608654000,
                "cs0": 0.000,
                "ps0": 0,
                "p1": 4703.562,
                "p2": 4490.631,
                "n1": 0.029,
                "n2": 0.000,
                "gas": 1624.264,
                "gts": 3894900
            }]

            api = LS120('', {})
            api.update()

        self.assertEqual(api.state, STATE_OK)
        self.assertIsNone(api.gas_meter.value)

    def test_ls120_missing_p_and_n(self):
        """Test case for incident with missing sensors from the API"""
        with patch('youless_api.device.LS120.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = [{
                "tm": 1611929119,
                "net": 9194.164,
                "pwr": 2382,
                "ts0": 1608654000,
                "cs0": 0.000,
                "ps0": 0,
                "gas": 1624.264,
                "gts": int(datetime.datetime.now().strftime("%y%m%d%H00"))
            }]

            api = LS120('', {})
            api.update()

        self.assertEqual(api.state, STATE_OK)
        self.assertEqual(api.power_meter.high.value, None)
        self.assertEqual(api.power_meter.low.value, None)

    @patch('youless_api.device.LS120.requests.get', side_effect=mock_ls120_phase_output)
    def test_ls120_with_phases(self, mock_get):
        """Test case for the new 1.5.x firmware with phases"""
        api = LS120('', {
            "model": "LS120",
            "mac": "xxxx",
            "fw": "1.5.3-EL"
        })
        api.update()

        self.assertEqual(api.state, STATE_OK)
        self.assertEqual(api.firmware, '1.5.3-EL')
        self.assertEqual(api.phase1.current.value, 0.000)
        self.assertEqual(api.phase1.voltage.value, 231.600)
        self.assertEqual(api.phase1.power.value, 64)
        self.assertEqual(api.phase2.current.value, 0.000)
        self.assertEqual(api.phase2.voltage.value, 230.400)
        self.assertEqual(api.phase2.power.value, 103)
        self.assertEqual(api.phase3.current.value, 2.000)
        self.assertEqual(api.phase3.voltage.value, 233.100)
        self.assertEqual(api.phase3.power.value, 312)
