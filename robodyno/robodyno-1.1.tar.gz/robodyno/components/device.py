#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""device.py
Time    :   2022/10/17
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Robodyno common device object

  Typical usage example:

  from robodyno.interfaces import CanBus
  from robodyno.components import Device

  can = CanBus()
  device = Device(iface = can, id = 0x10)
  device.get_version()
"""

from enum import Enum
from abc import ABC
import weakref

class DeviceType(Enum):
    ROBODYNO_PRO_44 = 0x00
    ROBODYNO_PRO_12 = 0x01
    ROBODYNO_PLUS_50  = 0x10
    ROBODYNO_PLUS_100 = 0x11
    ROBODYNO_EXB_FCTY = 0x80

class DeviceNode(ABC):
    """Robodyno common device node abstract class"""

    def __init__(self, device, iface):
        """Init node with device object and interface.
        
        Args:
            device: robodyno device object
            iface: robodyno interface
        """
        self._device = weakref.ref(device)
        self._iface = weakref.ref(iface)
    
    def _delete(self):
        """Collect node from memory."""
        pass

    def get_version(self, timeout):
        """Get device firmware / simulation version.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            dictionary of motor version
            None if timeout
        """
        return None

class Device(object):
    """Robodyno common device
    
    Attributes:
        id: correspond with device id in real world or simulation.
    """
    
    def __init__(self, iface, id = 0x10):
        """Init device with interface and id
        
        Args:
            iface: robodyno interface
            id: device id
        """
        try:
            self.id = id
            if id < 0x01 or id >= 0x40:
                raise ValueError
        except:
            raise ValueError('Device id is not available.')
        
        try:
            self._node = iface.get_device_node(self)
        except:
            raise RuntimeError('Failed to init motor from interface.')
    
    def get_version(self, timeout = 0):
        """Blocking function to get device firmware / simulation version.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            dictionary of device version
            None if timeout
        """
        try:
            return self._node.get_version(timeout)
        except:
            raise RuntimeError('Failed to invoke device api from interface.')
