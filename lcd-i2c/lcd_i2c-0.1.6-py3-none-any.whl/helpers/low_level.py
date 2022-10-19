from smbus2 import SMBus
from ..constants import EN_BIT
from .delay import delay_us


# /************ low level data pushing commands **********/
class LowLevel():
    def __init__(self, bus: SMBus, address: int, backlight: int) -> None:
        self._bus = bus
        self._address = address
        self._backlight = backlight
    
    # write either command or data
    def send(self, value: int, mode: int):
        high_nibble: int = value & 0xf0 #0xf0 is 11110000
        low_nibble: int = (value<<4) & 0xf0
        self.write4bits(high_nibble|mode)
        self.write4bits(low_nibble|mode)


    def write4bits(self, value: int):
        self.expanderWrite(value)
        self.pulseEnable(value)


    def expanderWrite(self, _data: int):                                        
        # Wire.beginTransmission(_Addr)
        # printIIC((int)(_data) | _backlightval)
        # Wire.endTransmission()
        self._bus.write_byte_data(self._address, 0, _data | self._backlight)


    def pulseEnable(self, _data: int):
        self.expanderWrite(_data | EN_BIT)  # ENABLE_BIT high
        delay_us(1) # enable pulse must be >450ns

        self.expanderWrite(_data & ~EN_BIT) # ENABLE_BIT low
        delay_us(50) # commands need > 37us to settle

