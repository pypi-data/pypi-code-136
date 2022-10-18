#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""socketcan_interface.py
Time    :   2022/10/12
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Socket Can Bus Interface(Windows)

  Typical usage example:

  can = SocketCanInterface(channel = 'can0', auto_connect = True)
  can.disconnect()

  or 

  can = SocketCanInterface(auto_connect = False)
  can.connect()
  can.disconnect()
"""

import can
from .can_bus_interface import CanBusInterface

class SocketCanInterface(CanBusInterface):
    """Socket can driver interface, only available on Linux."""

    def __init__(self, channel = 'can0', auto_connect = True, *args, **kwargs):
        """Init candle driver interface
        
        Args:
            channel: socket can channel name
            auto_connect: if set to False, you need to call connect() manually
        """
        self._channel = channel
        self._bus = None
        super().__init__(auto_connect)
    
    def _enable(self):
        """Connect to socket can bus."""
        try:
            self._bus = can.interface.Bus(channel=self._channel, bustype='socketcan')
        except:
            raise IOError('Failed to open can bus.')
    
    def _disable(self):
        """Disconnect to socket can bus."""
        if self._bus is not None:
            self._bus.shutdown()
        del self._bus
    
    def _send(self, can_frame_id, data, remote):
        """Send can frame from candle interface."""
        msg = can.Message(arbitration_id=can_frame_id, data=data, is_extended_id=False, is_remote_frame=remote)
        try:
            self._bus.send(msg)
        except:
            raise IOError('Failed to send to can bus.')

    def _read(self, timeout):
        """Read can frame from candle interface."""
        try:
            msg = self._bus.recv(timeout)
            return msg.arbitration_id, msg.data, msg.timestamp
        except Exception as e:
            raise IOError('Failed to read from candle can bus.')
