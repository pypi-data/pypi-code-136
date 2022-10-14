from typing import Optional

from youless_api.youless_sensor import YoulessSensor, PowerMeter, DeliveryMeter, ExtraMeter, Phase


class YouLessDevice:
    """The base class for the Youless devices"""

    def __init__(self):
        """Initialize the state"""

    @property
    def state(self) -> Optional[str]:
        """The current state of the connection"""
        return None

    @property
    def error(self) -> Optional[str]:
        """Returns the last known error, only if state == 'FAILED'"""
        return None

    @property
    def mac_address(self) -> Optional[str]:
        """Returns the MAC address"""
        return None

    @property
    def firmware(self) -> Optional[str]:
        """Returns the current firmware on the device."""
        return None

    @property
    def model(self) -> Optional[str]:
        """Returns the model number of the device"""
        return None

    @property
    def gas_meter(self) -> Optional[YoulessSensor]:
        """"Get the gas data available."""
        return None

    @property
    def current_power_usage(self) -> Optional[YoulessSensor]:
        """Get the current power usage."""
        return None

    @property
    def power_meter(self) -> Optional[PowerMeter]:
        """Get the power meter values."""
        return None

    @property
    def delivery_meter(self) -> Optional[DeliveryMeter]:
        """Get the power delivered values."""
        return None

    @property
    def extra_meter(self) -> Optional[ExtraMeter]:
        """Get the meter values of an attached meter."""
        return None

    @property
    def phase1(self) -> Optional[Phase]:
        """Get the phase 1 information"""
        return None

    @property
    def phase2(self) -> Optional[Phase]:
        """Get the phase 1 information"""
        return None

    @property
    def phase3(self) -> Optional[Phase]:
        """Get the phase 1 information"""
        return None

    def update(self) -> None:
        """Placeholder to update values from device"""
