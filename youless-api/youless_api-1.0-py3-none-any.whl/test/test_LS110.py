from unittest import TestCase
from unittest.mock import patch, Mock

from youless_api.const import STATE_OK
from youless_api.device.LS110 import LS110


class LS110Test(TestCase):

    def test_ls110_ok(self):
        with patch('youless_api.device.LS110.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = {
                "cnt": "141950,625",
                "pwr": 750,
                "lvl": 90,
                "dev": "(&plusmn;3%)",
                "det": "",
                "con": "OK",
                "sts": "(33)",
                "raw": 743
            }

            api = LS110('')
            api.update()

        self.assertEqual(api.state, STATE_OK)
        self.assertEqual(api.power_meter.high.value, None)
        self.assertEqual(api.power_meter.low.value, None)
        self.assertEqual(api.power_meter.total.unit_of_measurement, "kWh")
        self.assertEqual(api.power_meter.total.value, 141950.625)
        self.assertEqual(api.current_power_usage.value, 750)
        self.assertEqual(api.firmware, None)
