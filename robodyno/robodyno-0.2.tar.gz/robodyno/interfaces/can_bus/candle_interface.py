#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""candle_interface.py
Time    :   2022/09/30
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Candle Can Bus Interface(Windows)

  Typical usage example:

  can = CandleInterface(bitrate = 'CAN_1000K', auto_connect = True)
  can.disconnect()

  or 

  can = CandleInterface(bitrate = 'CAN_250K', auto_connect = False)
  can.connect()
  can.disconnect()
"""

import candle_driver as candle
from .can_bus_interface import CanBusInterface, CanSpeed

class CandleInterface(CanBusInterface):
    """Candle driver interface, only available on Windows."""

    def __init__(self, bitrate = 'CAN_1000K', auto_connect = True, *args, **kwargs):
        """Init candle driver interface
        
        Args:
            bitrate: choose from 'CAN_1000K', 'CAN_500K', 'CAN_250K'
            auto_connect: if set to False, you need to call connect() manually
        """
        try:
            self._device = candle.list_devices()[0]
            self._channel = self._device.channel(0)
        except:
            raise IOError('Failed to open can bus.')
        
        try:
            self._bitrate = CanSpeed[bitrate].value
        except:
            raise ValueError('Bitrate is not available.')
        
        super().__init__(auto_connect)
    
    def _enable(self):
        """Connect to candle can bus."""
        if not self._device.open():
            raise IOError
        self._channel.set_bitrate(self._bitrate)
        if not self._channel.start():
            raise IOError
    
    def _disable(self):
        """Disconnect to candle can bus."""
        self._channel.stop()
        self._device.close()
    
    def _send(self, can_frame_id, data, remote):
        """Send can frame from candle interface."""
        if remote:
            can_frame_id |= candle.CANDLE_ID_RTR
        try:
            self._channel.write(can_frame_id, data)
        except:
            raise IOError('Failed to send to candle can bus.')

    def _read(self, timeout):
        """Read can frame from candle interface."""
        try:
            frame_type, frame_id, data, _, timestamp = self._channel.read(int(timeout * 1000))
            if frame_type == candle.CANDLE_FRAMETYPE_RECEIVE:
                return frame_id, data, timestamp
            else:
                return None
        except Exception as e:
            raise IOError('Failed to read from candle can bus.')
