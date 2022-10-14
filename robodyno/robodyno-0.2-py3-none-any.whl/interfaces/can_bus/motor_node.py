#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""motor_node.py
Time    :   2022/09/30
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno
"""

from math import pi, fabs
import time
import struct
from ...components.motor import *

class CanSpeed(Enum):
    CAN_1M    = 1000000
    CAN_1000K = 1000000
    CAN_500K  = 500000
    CAN_250K  = 250000

def can_bus_get_decorator(command_id, format):
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

                self._iface.subscribe(
                    device_id = self._motor.id, 
                    command_id = command_id, 
                    callback = callback
                )
                self._iface.send_can_msg(self._motor.id, command_id, b'', True)

                start = time.time()
                while timeout == 0 or time.time() - start < timeout:
                    if callback.updated:
                        try:
                            return func(self, *struct.unpack(format, callback.data))
                        except:
                            raise ValueError()
            except:
                raise RuntimeError('Failed to get data from can bus.')
        return innerwrapper
    return wrapper

def can_bus_send_decorator(command_id, format = '', remote = False):
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
                self._iface.send_can_msg(self._motor.id, command_id, data, remote)
            except:
                raise RuntimeError('Failed to send data from can bus.')
        return inner_wrapper
    return wrapper

class CanBusMotorNode(MotorNode):
    """Can Bus Motor Node"""

    CMD_GET_VERSION = 0x01
    CMD_HEARTBEAT = 0x02
    CMD_ESTOP = 0x03
    CMD_REBOOT = 0x04
    CMD_CLEAR_ERRORS = 0x05
    CMD_SAVE = 0x06
    CMD_CONFIG_CAN = 0x07
    CMD_SET_STATE = 0x08
    CMD_GET_HARDWARE_STATUS = 0x09
    CMD_GET_MOTOR_FEEDBACK = 0x0A
    CMD_GET_MODE = 0x0B
    CMD_SET_MODE = 0x0C
    CMD_GET_PID = 0x0D
    CMD_SET_PID = 0x0E
    CMD_GET_LIMITS = 0x0F
    CMD_SET_LIMITS = 0x10
    CMD_SET_POS = 0x11
    CMD_SET_VEL = 0x12
    CMD_SET_TORQUE = 0x13
    CMD_RESET = 0x14
    CMD_UNLOCK = 0x15
    
    def __init__(self, motor, iface):
        """Init node from motor object and can bus interface.
        
        Args:
            motor: robodyno motor object
            iface: can bus interface
        """
        super().__init__(motor, iface)
        self._reduction = motor.reduction
        self._rot_factor = motor.reduction / 2 / pi
        self._iface.subscribe(
            device_id = self._motor.id, 
            command_id = self.CMD_HEARTBEAT, 
            callback = self._heartbeat_callback
        )
    
    def __del__(self):
        """Deinit method"""
        self._iface.unsubscribe(
            device_id = self._motor.id, 
            command_id = self.CMD_HEARTBEAT, 
            callback = self._heartbeat_callback
        )

    def _heartbeat_callback(self, device_id, command_id, data, timestamp):
        """Update motor attributes from heartbeat."""
        state, err, merr, eerr, cerr, cm, im, _ = struct.unpack('<BBBBBBBB', data)
        self._motor.state = MotorState(state)
        self._motor.error.update({
            'error': MotorError(err),
            'motor_err': MotorMotorError(merr),
            'encoder_err': MotorEncoderError(eerr),
            'controller_err': MotorControllerError(cerr),
        })
        self._motor.mode = self._ctrl_mode_from_raw(cm, im)
        self._motor.sync_time = timestamp

    def _ctrl_mode_to_raw(self, mode):
        """Translate from control mode enum to control mode raw msg
        
        Args:
            mode: control mode enum
        
        Returns:
            tuple of raw msg: (control mode, input mode)
            None when mode not recognized
        """
        if mode == MotorControlMode.POSITION_MODE:
            return (3, 1)
        elif mode == MotorControlMode.POSITION_FILTER_MODE:
            return (3, 3)
        elif mode == MotorControlMode.POSITION_TRACK_MODE:
            return (3, 5)
        elif mode == MotorControlMode.VELOCITY_MODE:
            return (2, 1)
        elif mode == MotorControlMode.VELOCITY_RAMP_MODE:
            return (2, 2)
        elif mode == MotorControlMode.TORQUE_MODE:
            return (1, 1)
        else:
            return None

    def _ctrl_mode_from_raw(self, cmode, imode):
        """Translate from control mode raw msg to control mode enum
        
        Args:
            cmode: raw control mode
            imode: raw input mode
        
        Returns:
            control mode enum
        """
        if cmode == 3:
            if imode == 1:
                return MotorControlMode.POSITION_MODE
            elif imode == 3:
                return MotorControlMode.POSITION_FILTER_MODE
            elif imode == 5:
                return MotorControlMode.POSITION_TRACK_MODE
        if cmode == 2:
            if imode == 1:
                return MotorControlMode.VELOCITY_MODE
            elif imode == 2:
                return MotorControlMode.VELOCITY_RAMP_MODE
        if cmode == 1 and imode == 1:
            return MotorControlMode.TORQUE_MODE
        return MotorControlMode.UNKNOWN
    
    @can_bus_get_decorator(CMD_GET_VERSION, '<HHI')
    def get_version(self, main_ver, sub_ver, type):
        """Get motor firmware / simulation version.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            dictionary of motor version
            None if timeout
        """
        return {
            'main_version': main_ver,
            'sub_version': sub_ver,
            'type': MotorType(type)
        }
    
    @can_bus_send_decorator(CMD_ESTOP)
    def estop(self):
        """Emergency stop motor."""
        pass

    @can_bus_send_decorator(CMD_REBOOT)
    def reboot(self):
        """Reboot motor."""
        pass

    @can_bus_send_decorator(CMD_CLEAR_ERRORS)
    def clear_errors(self):
        """Try to clear motor errors."""
        pass

    @can_bus_send_decorator(CMD_SAVE)
    def save_configuration(self):
        """Save configurations to hardware."""
        pass

    @can_bus_send_decorator(CMD_CONFIG_CAN, '<HHI')
    def config_can_bus(self, new_id, heartbeat, bitrate):
        """Configure motor can bus settings.
        
        Args:
            new_id: motor device id(0x01-0x3f)
            heartbeat: heartbeat period(ss)
            bitrate: choose from 'CAN_1000K', 'CAN_500K', 'CAN_250K',
                     (save and reboot to take effect)
        """
        bitrate = CanSpeed[bitrate].value
        if bitrate == 250000:
            bitrate_id = 0
        elif bitrate == 500000:
            bitrate_id = 1
        else:
            bitrate_id = 2
        return (new_id, bitrate_id, int(heartbeat*1000))

    @can_bus_send_decorator(CMD_SET_STATE, '<I')
    def set_state(self, state):
        """Cange motor state.
        
        Args:
            state: motor state(MotorState)
        """
        return (state.value,)

    @can_bus_get_decorator(CMD_GET_HARDWARE_STATUS, '<ff')
    def get_voltage(self, vbus, temperature):
        """Get motor vbus voltage.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            voltage(V)
            None if timeout
        """
        return vbus
    
    @can_bus_get_decorator(CMD_GET_HARDWARE_STATUS, '<ff')
    def get_temperature(self, vbus, temperature):
        """Get motor temperature.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            temperature(°C)
            None if timeout
        """
        return temperature
    
    @can_bus_get_decorator(CMD_GET_MOTOR_FEEDBACK, '<fee')
    def get_feedback(self, pos, vel, torque):
        """Get motor position, velocity and torque feedback.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            position(rad), velocity(rad/s), torque(Nm)
            None if timeout
        """
        return pos / self._rot_factor, vel / self._rot_factor, torque * self._reduction
    
    @can_bus_get_decorator(CMD_GET_MODE, '8s')
    def get_mode(self, payload):
        """Get motor control mode and params.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            control mode(MotorControlMode), control params dict
            None if timeout
        """
        control_mode, input_mode = struct.unpack('<BB', payload[:2])
        mode = self._ctrl_mode_from_raw(control_mode, input_mode)
        self._motor.mode = mode
        if mode == MotorControlMode.POSITION_FILTER_MODE:
            bandwidth, = struct.unpack('<f', payload[2:6])
            return (mode, {'bandwidth': bandwidth})
        elif mode == MotorControlMode.POSITION_TRACK_MODE:
            vel, acc, dec = struct.unpack('<eee', payload[2:8])
            return (mode, {
                'vel': fabs(vel / self._rot_factor),
                'acc': fabs(acc / self._rot_factor),
                'dec': fabs(dec / self._rot_factor),
            })
        elif mode == MotorControlMode.VELOCITY_RAMP_MODE:
            ramp, = struct.unpack('<f', payload[2:6])
            return (mode, {'ramp': fabs(ramp / self._rot_factor)})
        else:
            return (mode, )
    
    @can_bus_send_decorator(CMD_SET_MODE, '<BB')
    def position_mode(self):
        """Enter position pid mode."""
        return self._ctrl_mode_to_raw(MotorControlMode.POSITION_MODE)

    @can_bus_send_decorator(CMD_SET_MODE, '<BBf')
    def position_filter_mode(self, bandwidth):
        """Enter position filter mode.
        
        Args:
            bandwidth: filter bandwith, equals to control frequency(Hz)
        """
        cmode, imode = self._ctrl_mode_to_raw(MotorControlMode.POSITION_FILTER_MODE)
        return (cmode, imode, bandwidth)
    
    @can_bus_send_decorator(CMD_SET_MODE, '<BBeee')
    def position_track_mode(self, vel, acc, dec):
        """Enter position track mode.
        
        Args:
            vel: motion max vel(rad/s)
            acc: motion acceleration(rad/s^2)
            dec: motion deceleration(rad/s^2)
        """
        cmode, imode = self._ctrl_mode_to_raw(MotorControlMode.POSITION_TRACK_MODE)
        return (
            cmode, 
            imode, 
            fabs(vel * self._rot_factor), 
            fabs(acc * self._rot_factor), 
            fabs(dec * self._rot_factor)
        )
    
    @can_bus_send_decorator(CMD_SET_MODE, '<BB')
    def velocity_mode(self):
        """Enter velocity mode."""
        return self._ctrl_mode_to_raw(MotorControlMode.VELOCITY_MODE)
    
    @can_bus_send_decorator(CMD_SET_MODE, '<BBf')
    def velocity_ramp_mode(self, ramp):
        """Enter velocity ramp mode.
        
        Args:
            ramp: motion acceleration(rad/s^2)
        """
        cmode, imode = self._ctrl_mode_to_raw(MotorControlMode.VELOCITY_RAMP_MODE)
        return (cmode, imode, fabs(ramp * self._rot_factor))
    
    @can_bus_send_decorator(CMD_SET_MODE, '<BB')
    def torque_mode(self):
        """Enter torque mode"""
        return self._ctrl_mode_to_raw(MotorControlMode.TORQUE_MODE)
    
    @can_bus_get_decorator(CMD_GET_PID, '<fee')
    def get_pid(self, pos_kp, vel_kp, vel_ki):
        """Get motor pid params.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            pos_kp, vel_kp, vel_ki
            None if timeout
        """
        return (pos_kp, vel_kp, vel_ki)
    
    @can_bus_send_decorator(CMD_SET_PID, '<fee')
    def set_pid(self, pos_kp, vel_kp, vel_ki):
        """Set motor pid params.
        
        Args:
            pos_kp: kp of position control
            vel_kp: kp of velocity control
            vel_ki: ki of velocity control
        """
        return (pos_kp, vel_kp, vel_ki)

    @can_bus_get_decorator(CMD_GET_LIMITS, '<ff')
    def get_vel_limit(self, vel_limit, current_limit):
        """Get motor volocity limit.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            velocity limit(rad/s)
            None if timeout
        """
        return vel_limit / fabs(self._rot_factor)
    
    @can_bus_get_decorator(CMD_GET_LIMITS, '<ff')
    def get_current_limit(self, vel_limit, current_limit):
        """Get motor current limit.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            current limit(A)
            None if timeout
        """
        return current_limit

    @can_bus_send_decorator(CMD_SET_LIMITS, '<ff')
    def set_vel_limit(self, vel_lim):
        """Set motor velocity limit.
        
        Args:
            vel_lim: velocity limit(rad/s)
        """
        return (fabs(vel_lim * self._rot_factor), 0)
    
    @can_bus_send_decorator(CMD_SET_LIMITS, '<ff')
    def set_current_limit(self, current_lim):
        """Set motor current limit.
        
        Args:
            current_lim: current limit(A)
        """
        return (0, current_lim)
    
    @can_bus_send_decorator(CMD_SET_POS, '<fee')
    def set_pos(self, pos, vel_ff, torque_ff):
        """Set motor target position.
        
        Args:
            pos: target position(rad)
            vel_ff: velocity feed forward(rad/s)
            torque_ff:torque feed forward(Nm)
        """
        return (pos * self._rot_factor, vel_ff * self._rot_factor, torque_ff / self._reduction)

    @can_bus_send_decorator(CMD_SET_VEL, '<ff')
    def set_vel(self, vel, torque_ff):
        """Set motor velocity.
        
        Args:
            vel: target velocity(rad)
            torque_ff: torque feed forward(Nm)
        """
        return (vel * self._rot_factor, torque_ff / self._reduction)
    
    @can_bus_send_decorator(CMD_SET_TORQUE, '<f')
    def set_torque(self, torque):
        """Set motor torque.
        
        Args:
            torque: target torque(Nm)
        """
        return (torque / self._reduction, )

    @can_bus_send_decorator(CMD_RESET)
    def reset(self):
        """Reset motor with factory configurations."""
        pass

    @can_bus_send_decorator(CMD_UNLOCK)
    def unlock(self):
        """Unlock motor brake if motor has one."""
        pass
