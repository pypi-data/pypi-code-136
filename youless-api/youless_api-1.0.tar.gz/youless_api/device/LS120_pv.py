from typing import Optional

from youless_api.device.LS110 import LS110


class LS120PVOutput(LS110):

    def __init__(self, host, device_information):
        super(LS120PVOutput, self).__init__(host)
        self._info = device_information

    @property
    def model(self) -> Optional[str]:
        return "LS120 - PVOutput"

    @property
    def mac_address(self) -> Optional[str]:
        """Return the MAC address"""
        if self._info is not None:
            return self._info['mac']

        return None
