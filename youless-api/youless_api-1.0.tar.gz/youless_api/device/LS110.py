import requests
from typing import Optional

from youless_api.device import YouLessDevice
from youless_api.const import STATE_OK, STATE_FAILED
from youless_api.youless_sensor import YoulessSensor, PowerMeter, ExtraMeter


def validate_basic_response(raw_data: dict) -> dict:
    """Validate the response from the old /a interface and adjust the dict if needed."""

    corrected = {**{'cs0': None, 'ps0': None}, **raw_data}
    parse_float_values_for = ['cnt', 'cs0']

    for correct_value in parse_float_values_for:
        if correct_value in corrected and corrected[correct_value] is not None:
            corrected[correct_value] = float(corrected[correct_value].replace(",", "."))

    return corrected


class LS110(YouLessDevice):
    """The device integration for the Youless LS110"""

    def __init__(self, host):
        """Initialize the integration"""
        super().__init__()
        self._host = host
        self._cache = None
        self._state = STATE_OK


    @property
    def state(self) -> Optional[str]:
        """Get the current device connectivity state"""
        return self._state

    @property
    def model(self) -> Optional[str]:
        """Return the device model"""
        return "LS110"

    @property
    def power_meter(self) -> Optional[PowerMeter]:
        """Fetch the power meter values from the internal cache"""
        if self._cache is not None:
            return PowerMeter(
                YoulessSensor(None, None),
                YoulessSensor(None, None),
                YoulessSensor(self._cache['cnt'], 'kWh')
            )

        return None

    @property
    def current_power_usage(self) -> Optional[YoulessSensor]:
        """Fetch the current power usage from the internal cache"""
        if self._cache is not None:
            return YoulessSensor(self._cache['pwr'], 'W')

        return None

    @property
    def extra_meter(self):
        """Get the meter values of an attached meter."""
        if self._cache is not None:
            return ExtraMeter(
                YoulessSensor(self._cache['cs0'], 'kWh'),
                YoulessSensor(self._cache['ps0'], 'W')
            )

        return None

    def update(self) -> None:
        """Update the sensor values from the device"""
        response = requests.get(f"{self._host}/a?f=j", timeout=2)
        if response.ok:
            validated_response = validate_basic_response(response.json())
            self._state = STATE_OK
            self._cache = validated_response
        else:
            self._state = STATE_FAILED
