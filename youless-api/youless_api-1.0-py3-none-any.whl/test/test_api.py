import unittest
from unittest.mock import patch, Mock, MagicMock

from requests import Response

from youless_api import YoulessAPI


def mock_ls120_pvoutput(*args, **kwargs) -> Response:
    response: Response = Mock()

    if args[0] == 'http://192.1.1.1/d':
        response.ok = True
        response.json = lambda: {'mac': '293:23fd:23'}

    if args[0] == 'http://192.1.1.1/e':
        response.ok = True
        response.headers = {'Content-Type': 'text/html'}

    return response


def mock_ls120(*args, **kwargs) -> Response:
    response: Response = Mock()

    if args[0] == 'http://192.1.1.1/d':
        response.ok = True
        response.json = lambda: {'mac': '293:23fd:23'}

    if args[0] == 'http://192.1.1.1/e':
        response.ok = True
        response.headers = {'Content-Type': 'application/json'}

    return response


def mock_ls110_device(*args, **kwargs):
    if args[0] == 'http://192.1.1.1/d':
        return Mock(ok=False)
    if args[0] == 'http://192.1.1.1':
        return Mock(ok=True)

    return Mock(ok=False)


class YoulessAPITest(unittest.TestCase):

    @patch('youless_api.device.LS120.requests.get', side_effect=mock_ls120)
    def test_device_ls120(self, mock_get: MagicMock):
        api = YoulessAPI('192.1.1.1')
        api.initialize()

        self.assertEqual(api.model, 'LS120')
        self.assertEqual(api.mac_address, '293:23fd:23')
        mock_get.assert_any_call('http://192.1.1.1/d', auth=None, timeout=2)
        mock_get.assert_any_call('http://192.1.1.1/e', auth=None, timeout=2)

    @patch('youless_api.device.LS120.requests.get', side_effect=mock_ls120)
    def test_device_ls120_authenticated(self, mock_get: MagicMock):
        api = YoulessAPI('192.1.1.1', 'admin', 'password')
        api.initialize()

        self.assertEqual(api.model, 'LS120')
        mock_get.assert_any_call('http://192.1.1.1/d', auth=('admin', 'password'), timeout=2)
        mock_get.assert_any_call('http://192.1.1.1/e', auth=('admin', 'password'), timeout=2)

    @patch('youless_api.device.LS110.requests.get', side_effect=mock_ls120_pvoutput)
    def test_ls120_firmare_pvoutput(self, mock_get: MagicMock):
        api = YoulessAPI('192.1.1.1')
        api.initialize()

        self.assertEqual(api.model, 'LS120 - PVOutput')
        self.assertEqual(api.mac_address, '293:23fd:23')
        mock_get.assert_any_call('http://192.1.1.1/d', auth=None, timeout=2)
        mock_get.assert_any_call('http://192.1.1.1/e', auth=None, timeout=2)

    @patch('youless_api.device.LS110.requests.get', side_effect=mock_ls120_pvoutput)
    def test_ls120_firmare_pvoutput_authenticated(self, mock_get: MagicMock):
        api = YoulessAPI('192.1.1.1', 'admin', 'password')
        api.initialize()

        self.assertEqual(api.model, 'LS120 - PVOutput')
        self.assertEqual(api.mac_address, '293:23fd:23')
        mock_get.assert_any_call('http://192.1.1.1/d', auth=('admin', 'password'), timeout=2)
        mock_get.assert_any_call('http://192.1.1.1/e', auth=('admin', 'password'), timeout=2)

    @patch('youless_api.requests.get', side_effect=mock_ls110_device)
    def test_device_ls110(self, mock_get: MagicMock):
        api = YoulessAPI('192.1.1.1')
        api.initialize()

        self.assertEqual(api.model, 'LS110')
        self.assertIsNone(api.mac_address)

        mock_get.assert_called_with('http://192.1.1.1', auth=None, timeout=2)

    @patch('youless_api.requests.get', side_effect=mock_ls110_device)
    def test_device_ls110_authenticated(self, mock_get: MagicMock):
        api = YoulessAPI('192.1.1.1', 'admin', 'password')
        api.initialize()

        self.assertEqual(api.model, 'LS110')
        self.assertIsNone(api.mac_address)

        mock_get.assert_called_with('http://192.1.1.1', auth=('admin', 'password'), timeout=2)
