#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""utils.py
Time    :   2022/10/17
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Can Bus Interface Utilities
"""

import time
from enum import Enum
import struct

class CanSpeed(Enum):
    CAN_1M    = 1000000
    CAN_1000K = 1000000
    CAN_500K  = 500000
    CAN_250K  = 250000

def get_from_bus(command_id, format):
    """Decorator for getting data from can bus.
    
    Args:
        command_id: command id
        format: python struct format to unpack msg bytes
    
    Returns:
        decorated function
    """
    def wrapper(func):
        def innerwrapper(self, timeout = 0):
            try:
                def callback(device_id, command_id, data, timestamp):
                    callback.data = data
                    callback.updated = True
                callback.updated = False

                self._iface().subscribe(
                    device_id = self.id, 
                    command_id = command_id, 
                    callback = callback
                )
                self._iface().send_can_msg(self.id, command_id, b'', True)

                start = time.time()
                while timeout == 0 or time.time() - start < timeout:
                    if callback.updated:
                        try:
                            return func(self, *struct.unpack(format, callback.data))
                        except:
                            raise ValueError()
                self._iface().unsubscribe(
                    device_id = self.id,
                    command_id = command_id,
                    callback = callback
                )
            except:
                raise RuntimeError('Failed to get data from can bus.')
        return innerwrapper
    return wrapper

def send_to_bus(command_id, format = '', remote = False):
    """Decorator for sending data from can bus.
    
    Args:
        command_id: command id
        format: python struct format to pack msg bytes
        remote: can frame rtr bit
    
    Returns:
        decorated function
    """
    def wrapper(func):
        def inner_wrapper(self, *args, **kwargs):
            try:
                data = b''
                if len(format) > 0:
                    data = struct.pack(format, *func(self, *args, **kwargs))
                self._iface().send_can_msg(self.id, command_id, data, remote)
            except:
                raise RuntimeError('Failed to send data from can bus.')
        return inner_wrapper
    return wrapper