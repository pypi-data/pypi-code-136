"""
This file contains a helper class to easily obtain data from the YouLess sensor.
"""
from typing import Optional

import requests

from youless_api.device import YouLessDevice
from youless_api.device.LS110 import LS110
from youless_api.device.LS120 import LS120
from youless_api.device.LS120_pv import LS120PVOutput
from youless_api.youless_sensor import YoulessSensor, PowerMeter, ExtraMeter, DeliveryMeter

name = "youless_api"


class YoulessAPI:
    """A helper class to obtain data from the YouLess Sensor."""

    _device: Optional[YouLessDevice]

    def __init__(self, host, username=None, password=None):
        """Initialize the data bridge."""
        self._url = 'http://' + host
        if username is None:
            self._authentication = None
        else:
            self._authentication = (username, password)
        self._device = None

    def initialize(self):
        """Establish a connection to the remote device"""
        response = requests.get(f"{self._url}/d", auth=self._authentication, timeout=2)
        if response.ok:
            firmware_check = requests.get(f"{self._url}/e", auth=self._authentication, timeout=2)
            if firmware_check.ok and firmware_check.headers['Content-Type'] == 'application/json':
                self._device = LS120(self._url, response.json())
            else:
                self._device = LS120PVOutput(self._url, response.json())
        else:
            alive = requests.get(self._url, auth=self._authentication, timeout=2)
            if alive.ok:
                self._device = LS110(self._url)

    def update(self):
        """Fetch the latest settings from the Youless Sensor."""
        if self._device:
            self._device.update()

    @property
    def mac_address(self) -> Optional[str]:
        """Get the MAC address of the connected device."""
        if self._device is not None:
            return self._device.mac_address

        return None

    @property
    def model(self) -> Optional[str]:
        """Return the model of the connected device."""
        if self._device is not None:
            return self._device.model

        return None

    @property
    def gas_meter(self) -> Optional[YoulessSensor]:
        """"Get the gas data available."""
        if self._device is not None:
            return self._device.gas_meter

        return None

    @property
    def current_power_usage(self) -> Optional[YoulessSensor]:
        """Get the current power usage."""
        if self._device is not None:
            return self._device.current_power_usage

        return None

    @property
    def power_meter(self) -> Optional[PowerMeter]:
        """Get the power meter values."""
        if self._device is not None:
            return self._device.power_meter

        return None

    @property
    def delivery_meter(self) -> Optional[DeliveryMeter]:
        """Get the power delivered values."""
        if self._device is not None:
            return self._device.delivery_meter

        return None

    @property
    def extra_meter(self) -> Optional[ExtraMeter]:
        """Get the meter values of an attached meter."""
        if self._device is not None:
            return self._device.extra_meter

        return None

    @property
    def secured(self) -> bool:
        """Flag indicating if the API has authentication or not."""
        return self._authentication is not None
