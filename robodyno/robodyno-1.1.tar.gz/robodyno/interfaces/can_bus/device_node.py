#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""device_node.py
Time    :   2022/10/17
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno
"""

from ...components.device import *
from .utils import get_from_bus, send_to_bus

class CanBusDeviceNode(DeviceNode):
    """Can Bus Robodyno Common Device Node"""

    CMD_GET_VERSION = 0x01

    def __init__(self, device, iface):
        """Init node from robodyno common device and can bus interface
        
        Args:
            device: robodyno common device object
            iface: can bus interface
        """
        super().__init__(device, iface)
        self.id = device.id
    
    @get_from_bus(CMD_GET_VERSION, '<HHI')
    def get_version(self, main_ver, sub_ver, type):
        """Get device firmware / simulation version.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            dictionary of device version
            None if timeout
        """
        return {
            'main_version': main_ver,
            'sub_version': sub_ver,
            'type': DeviceType(type)
        }
    