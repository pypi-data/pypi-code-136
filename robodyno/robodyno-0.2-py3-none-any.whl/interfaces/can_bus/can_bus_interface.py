#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""can_bus_interface.py
Time    :   2022/10/08
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Can Bus Interface Abstract Class
"""

from abc import abstractmethod
import threading
from enum import Enum
from collections import defaultdict
from ..interface import Interface
from .motor_node import CanSpeed, CanBusMotorNode

class CanBusInterface(Interface):
    """Can bus interface manage can id, rx thread and subscribers."""
    
    MAX_DEVICE_NUM = 0x40
    DEVICE_ID_ALL = MAX_DEVICE_NUM

    MAX_COMMAND_NUM = 0x20
    COMMAND_ID_ALL = MAX_COMMAND_NUM

    def __init__(self, auto_connect = True, *args, **kwargs):
        """Init can driver interface.
        
        Args:
            auto_connect: if set to False, you need to call connect() manually
        """
        self._subscribers = defaultdict(lambda: defaultdict(list))
        self._send_lock = threading.Lock()
        self._thread_running = False
        self._rx_thread = threading.Thread(
            target = self._rx_thread_method,
            name = 'candle.rx'
        )
        self._rx_thread.daemon = True
        if auto_connect:
            self.connect()

    def pack_can_id(self, device_id, command_id):
        """calculate can frame id from device id and command id
        
        Args:
            device_id: robodyno device id
            command_id: device command id
        
        Returns:
            can frame id
        """
        return device_id << 5 | command_id
    
    def unpack_can_id(self, can_id):
        """split can frame id into device id and command id
        
        Args:
            can_id: can frame id
        
        Returns:
            (device_id, command_id)
        """
        return ((can_id & 0x7ff) >> 5, can_id & 0x1f)
    
    def get_motor_node(self, motor):
        """Return new can bus motor node."""
        return CanBusMotorNode(motor = motor, iface = self)
    
    @abstractmethod
    def _enable(self):
        """Enable can bus interface."""

    @abstractmethod
    def _disable(self):
        """Disable can bus interface."""
        
        
    def connect(self):
        """Connect to can bus."""
        try:
            self._enable()
            self._thread_running = True
            self._rx_thread.start()
        except:
            raise IOError('Failed to connect can bus.')
    
    def disconnect(self):
        """Disconnect to can bus."""
        self._thread_running = False
        self._rx_thread.join(1)
        try:
            self._disable()
        except:
            raise IOError('Failed to disconnect can bus.')
    
    @abstractmethod
    def _send(self, can_frame_id, data, remote):
        """Send can frame with id, data and remote bit.
        
        Args:
            can_frame_id: standard can frame id(11bit)
            data: can frame payload byte array, up to 8 bytes
            remote: can frame RTR bit
        """

    @abstractmethod
    def _read(self, timeout = 0):
        """Read can frame with timeout.
        
        Args:
            timeout: blocking read timeout(s)
        
        Returns:
            can_frame_id, data, timestamp
        """

    def send_can_msg(self, device_id, command_id, data = b'', remote = False):
        """Send message from can bus.
        
        Args:
            device_id: robodyno device id, upper 6 bits of can frame id
            command_id: device command id, lower 5 bits of can frame id
            data: bytes of can frame payload
            remotr: can frame rtr bit
        """
        with self._send_lock:
            can_frame_id = self.pack_can_id(device_id, command_id)
            self._send(can_frame_id, data, remote)

    def subscribe(self, device_id, command_id, callback):
        """Subscribe specific device id and command id from can bus.
        
        Args:
            device_id: robodyno device id or Interface.DEVICE_ID_ALL
            command_id: device command id or Interface.COMMAND_ID_ALL
            callback: func(device_id, command_id, data, timestamp)
        """
        if callback not in self._subscribers[device_id][command_id]:
            self._subscribers[device_id][command_id].append(callback)
        
    def unsubscribe(self, device_id, command_id, callback = None):
        """Unsubscribe specific device id and command id from can bus.
        
        Args:
            device_id: robodyno device id or Interface.DEVICE_ID_ALL
            command_id: device command id or Interface.COMMAND_ID_ALL
            callback: callback to unsubscribe or leave None to unsubscribe all callbacks
        """
        if callback:
            try:
                self._subscribers[device_id][command_id].remove(callback)
            except:
                raise ValueError('Failed to find callback to unsubscribe.')
        else:
            self._subscribers[device_id][command_id] = []
    
    def _notify(self, frame_id, data, timestamp):
        """Protected method, notify subscribers when can frame received.
        
        Args:
            frame_id: can frame id
            data: can frame payload
            timestamp: can frame timestamp
        """
        device_id, command_id = self.unpack_can_id(frame_id)
        for subscriber in self._subscribers[device_id][command_id]:
            subscriber(device_id, command_id, data, timestamp)
        for subscriber in self._subscribers[device_id][self.COMMAND_ID_ALL]:
            subscriber(device_id, command_id, data, timestamp)
        for subscriber in self._subscribers[self.DEVICE_ID_ALL][command_id]:
            subscriber(device_id, command_id, data, timestamp)
        for subscriber in self._subscribers[self.DEVICE_ID_ALL][self.COMMAND_ID_ALL]:
            subscriber(device_id, command_id, data, timestamp)
        
    def _rx_thread_method(self):
        """read can bus thread method"""
        while self._thread_running:
            try:
                can_frame_id, data, timestamp = self._read(0.1)
                self._notify(can_frame_id, data, timestamp)
            except:
                pass
