#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""motor.py
Time    :   2022/09/30
Author  :   song 
Version :   1.0
Contact :   zhaosongy@126.com
License :   (C)Copyright 2022, robottime / robodyno

Robodyno Motor Python Driver

  Typical usage example:

  from robodyno.interfaces import CanBus, Webots
  from robodyno.components import Motor

  can = CanBus()
  webots = Webots()
  
  motor_can = Motor(iface = can, id = 0x10, type = 'ROBODYNO_PRO_44')
  motor_webots = Motor(iface = webots, id = 0x11, type = 'ROBODYNO_PRO_12')

  can.disconnect()
"""

from enum import Enum
from abc import ABC, abstractmethod
from re import L

class MotorApiRuntimeError(RuntimeError):
    def __init__(self):
        super().__init__('Failed to invoke motor api from interface.')

class MotorType(Enum):
    ROBODYNO_PRO_44 = 0x00
    ROBODYNO_PRO_12 = 0x01
    ROBODYNO_PLUS_50  = 0x10
    ROBODYNO_PLUS_100 = 0x11

class MotorState(Enum):
    UNKNOWN = -1
    IDLE = 1
    CALIBRATE = 3
    MOTOR_CALIBRATING = 4
    OFFSET_CALIBRATING = 7
    CLOSED_LOOP = 8

class MotorError(Enum):
    NONE = 0
    # INVALID_STATE = 0 TODO: 修复固件发送错误值可能为0的bug
    UNDER_VOLTAGE = 1
    OVER_VOLTAGE = 2
    CURRENT_MEASUREMENT_TIMEOUT = 3
    BRAKE_RESISTOR_DISARMED = 4
    MOTOR_DISARMED = 5
    MOTOR_FAILED = 6
    SENSORLESS_ESTIMATOR_FAILED = 7
    ENCODER_FAILED = 8
    CONTROLLER_FAILED = 9
    POS_CTRL_DURING_SENSORLESS = 10
    WATCHDOG_TIMER_EXPIRED = 11
    MIN_ENDSTOP_PRESSED = 12
    MAX_ENDSTOP_PRESSED = 13
    ESTOP_REQUESTED = 14
    HOMING_WITHOUT_ENDSTOP = 17
    OVER_TEMP = 18

class MotorMotorError(Enum):
    NONE = 0
    # PHASE_RESISTANCE_OUT_OF_RANGE = 0
    PHASE_INDUCTANCE_OUT_OF_RANGE = 1
    ADC_FAILED = 2
    DRV_FAULT = 3
    CONTROL_DEADLINE_MISSED = 4
    NOT_IMPLEMENTED_MOTOR_TYPE = 5
    BRAKE_CURRENT_OUT_OF_RANGE = 6
    MODULATION_MAGNITUDE = 7
    BRAKE_DEADTIME_VIOLATION = 8
    UNEXPECTED_TIMER_CALLBACK = 9
    CURRENT_SENSE_SATURATION = 10
    CURRENT_LIMIT_VIOLATION = 12
    BRAKE_DUTY_CYCLE_NAN = 13
    DC_BUS_OVER_REGEN_CURRENT = 14
    DC_BUS_OVER_CURRENT = 15

class MotorEncoderError(Enum):
    NONE = 0
    # UNSTABLE_GAIN = 0
    CPR_POLEPAIRS_MISMATCH = 1
    NO_RESPONSE = 2
    UNSUPPORTED_ENCODER_MODE = 3
    ILLEGAL_HALL_STATE = 4
    INDEX_NOT_FOUND_YET = 5
    ABS_SPI_TIMEOUT = 6
    ABS_SPI_COM_FAIL = 7
    ABS_SPI_NOT_READY = 8
    
class MotorControllerError(Enum):
    NONE = 0
    # OVERSPEED = 0
    INVALID_INPUT_MODE = 1
    UNSTABLE_GAIN = 2
    INVALID_MIRROR_AXIS = 3
    INVALID_LOAD_ENCODER = 4
    INVALID_ESTIMATE = 5

class MotorControlMode(Enum):
    UNKNOWN = -1
    POSITION_MODE = 0
    POSITION_FILTER_MODE = 1
    POSITION_TRACK_MODE = 2
    VELOCITY_MODE = 3
    VELOCITY_RAMP_MODE = 4
    TORQUE_MODE = 5

class MotorNode(ABC):
    """Robodyno motor node abstract class."""
    
    def __init__(self, motor, iface):
        """Init node with motor object and robodyno interface.
        
        Args:
            motor: motor object
            iface: robodyno interface
        """
        self._motor = motor
        self._iface = iface
    
    def get_version(self, timeout):
        """Get motor firmware / simulation version.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            dictionary of motor version
            None if timeout
        """
        return None
    
    def estop(self):
        """Emergency stop motor."""
        pass
    
    def reboot(self):
        """Reboot motor."""
        pass

    def clear_errors(self):
        """Try to clear motor errors."""
        pass
        
    def save_configuration(self):
        """Save configurations to hardware."""
        pass

    def config_can_bus(self, new_id, heartbeat, bitrate):
        """Configure motor can bus settings.
        
        Args:
            new_id: motor device id(0x01-0x3f)
            heartbeat: heartbeat period(ms)
            bitrate: motor can bus bitrate(save and reboot to take effect)
        """
        pass

    def set_state(self, state):
        """Cange motor state.
        
        Args:
            state: motor state(MotorState)
        """
        pass

    def get_voltage(self, timeout):
        """Get motor vbus voltage.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            voltage(V)
            None if timeout
        """
        return None
    
    def get_temperature(self, timeout):
        """Get motor temperature.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            temperature(°C)
            None if timeout
        """
        return None
    
    def get_feedback(self, timeout):
        """Get motor position, velocity and torque feedback.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            position(rad), velocity(rad/s), torque(Nm)
            None if timeout
        """
        return None
    
    def get_mode(self, timeout):
        """Get motor control mode and params.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            control mode(MotorControlMode), control params dict
            None if timeout
        """
        return None
        
    def position_mode(self):
        """Enter position pid mode."""
        pass

    def position_filter_mode(self, bandwidth):
        """Enter position filter mode.
        
        Args:
            bandwidth: filter bandwith, equals to control frequency(Hz)
        """
        pass

    def position_track_mode(self, vel, acc, dec):
        """Enter position track mode.
        
        Args:
            vel: motion max vel(rad/s)
            acc: motion acceleration(rad/s^2)
            dec: motion deceleration(rad/s^2)
        """
        pass

    def velocity_mode(self):
        """Enter velocity mode."""
        pass

    def velocity_ramp_mode(self, ramp):
        """Enter velocity ramp mode.
        
        Args:
            ramp: motion acceleration(rad/s^2)
        """
        pass

    def torque_mode(self):
        """Enter torque mode"""
        pass

    def get_pid(self, timeout):
        """Get motor pid params.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            pos_kp, vel_kp, vel_ki
            None if timeout
        """
        return None
    
    def set_pid(self, pos_kp, vel_kp, vel_ki):
        """Set motor pid params.
        
        Args:
            pos_kp: kp of position control
            vel_kp: kp of velocity control
            vel_ki: ki of velocity control
        """
        pass

    def get_vel_limit(self, timeout):
        """Get motor volocity limit.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            velocity limit(rad/s)
            None if timeout
        """
        return None
        
    def get_current_limit(self, timeout):
        """Get motor current limit.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            current limit(A)
            None if timeout
        """
        return None

    def set_vel_limit(self, vel_lim):
        """Set motor velocity limit.
        
        Args:
            vel_lim: velocity limit(rad/s)
        """
        pass

    def set_current_limit(self, current_lim):
        """Set motor current limit.
        
        Args:
            current_lim: current limit(A)
        """
        pass

    def set_pos(self, pos, vel_ff, torque_ff):
        """Set motor target position.
        
        Args:
            pos: target position(rad)
            vel_ff: velocity feed forward(rad/s)
            torque_ff:torque feed forward(Nm)
        """
        pass

    def set_vel(self, vel, torque_ff):
        """Set motor velocity.
        
        Args:
            vel: target velocity(rad)
            torque_ff: torque feed forward(Nm)
        """
        pass

    def set_torque(self, torque):
        """Set motor torque.
        
        Args:
            torque: target torque(Nm)
        """
        pass

    def reset(self):
        """Reset motor with factory configurations."""
        pass

    def unlock(self):
        """Unlock motor brake if motor has one."""
        pass

class Motor(object):
    """Robodyno Motor
    
    Attributes:
        id: correspond with motor id in real world or simulation.
        type: motor type enum
        reduction: motor reduction
        available_volocity: theoretical max volocity(rad/s)
        available_torque: theoretical max torque(Nm)
        available_current: theoretical max phase current(A)
        torque_constant: theoretical torque provided by unit current(Nm/A)
        with_brake: is motor has a brake(bool)
        state: motor state read from heartbeat pack
        error: motor error read from heartbeat pack
        mode: motor mode read from heartbeat pack
        sync_time: last timestamp when receive heartbeat pack
    """

    def __init__(self, iface, id = 0x10, type = 'ROBODYNO_PRO_44'):
        """Init motor from interface, id and type.
        
        Args:
            iface: robodyno interface object
            id: range from 0x01 to 0x40
            type: Motor type string
        """
        try:
            self.id = id
            if id < 0x01 or id >= 0x40:
                raise ValueError
        except:
            raise ValueError('Motor id is not available.')

        try:
            self.type = MotorType[type]
            self.__dict__.update(self.__get_spec())
        except:
            raise ValueError('Motor type not recognized.')

        try:
            self._node = iface.get_motor_node(self)
        except:
            raise RuntimeError('Failed to init motor from interface.')

        
        # TODO: 添加同步心跳包的功能
        self.state = MotorState.UNKNOWN
        self.error = {
            'error': MotorError.NONE,
            'motor_err': MotorMotorError.NONE,
            'encoder_err': MotorEncoderError.NONE,
            'controller_err': MotorControllerError.NONE,
        }
        self.mode = MotorControlMode.UNKNOWN
        self.sync_time = 0

    def __get_spec(self):
        """get motor factory specifications"""
        robodyno_motor_specs = {
            MotorType.ROBODYNO_PRO_44: {
                'reduction': -44,
                'available_velocity': 27,
                'available_torque': 13,
                'available_current': 15,
                'torque_constant': 0.7742,
                'with_brake': False,
            },
            MotorType.ROBODYNO_PRO_12: {
                'reduction': -12.45,
                'available_velocity': 95,
                'available_torque': 4,
                'available_current': 15,
                'torque_constant': 0.2191,
                'with_brake': False,
            },
            MotorType.ROBODYNO_PLUS_50: {
                'reduction': 50,
                'available_velocity': 24,
                'available_torque': 48,
                'available_current': 25,
                'torque_constant': 1.7229,
                'with_brake': True,
            },
            MotorType.ROBODYNO_PLUS_100: {
                'reduction': 100,
                'available_velocity': 12,
                'available_torque': 96,
                'available_current': 25,
                'torque_constant': 3.4458,
                'with_brake': True,
            },
        }
        return robodyno_motor_specs.get(self.type, None)

    def get_version(self, timeout = 0):
        """Blocking function to get motor firmware / simulation version.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            dictionary of motor version
            None if timeout
        """
        try:
            return self._node.get_version(timeout)
        except:
            raise MotorApiRuntimeError
    
    def estop(self):
        """Stop motor by set an error bit, reboot motor to recover."""
        try:
            self._node.estop()
        except:
            raise MotorApiRuntimeError
    
    def reboot(self):
        """Reboot motor."""
        try:
            self._node.reboot()
        except:
            raise MotorApiRuntimeError
    
    def clear_errors(self):
        """Try to clear motor errors."""
        try:
            self._node.clear_errors()
        except:
            raise MotorApiRuntimeError
    
    def save_configuration(self):
        """Save motor configurations."""
        try:
            self._node.save_configuration()
        except:
            raise MotorApiRuntimeError
    
    def config_can_bus(self, new_id, heartbeat = 1, bitrate = 'CAN_1M'):
        """Configure motor can bus settings.
        
        Args:
            new_id: motor device id(0x01-0x3f)
            heartbeat: heartbeat period(s)
            bitrate: choose from 'CAN_1000K', 'CAN_500K', 'CAN_250K',
                     (save and reboot to take effect)
        """
        if new_id < 0x01 or new_id > 0x3f:
            raise ValueError('Unavailable can id. Choose from 0x01-0x3f')
        try:
            self._node.config_can_bus(new_id, heartbeat, bitrate)
        except:
            raise MotorApiRuntimeError

    def enable(self):
        """Enable motor. Set motor state to CLOSED_LOOP."""
        try:
            self._node.set_state(MotorState.CLOSED_LOOP)
        except:
            raise MotorApiRuntimeError
    
    def calibrate(self):
        """Calibrate motor. Set motor state to CALIBRATE."""
        try:
            self._node.set_state(MotorState.CALIBRATE)
        except:
            raise MotorApiRuntimeError
    
    def disable(self):
        """Disable motor. Set motor state to IDLE."""
        try:
            self._node.set_state(MotorState.IDLE)
        except:
            raise MotorApiRuntimeError
        
    def get_voltage(self, timeout = 0):
        """Get motor vbus voltage.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            voltage(V)
            None if timeout
        """
        try:
            return self._node.get_voltage(timeout)
        except:
            raise MotorApiRuntimeError
        
    def get_temperature(self, timeout = 0):
        """Get motor temperature.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            temperature(°C)
            None if timeout
        """
        try:
            return self._node.get_temperature(timeout)
        except:
            raise MotorApiRuntimeError
    
    def get_feedback(self, timeout = 0):
        """Get motor position, velocity and torque feedback.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            position(rad), velocity(rad/s), torque(Nm)
            None if timeout
        """
        try:
            return self._node.get_feedback(timeout)
        except:
            raise MotorApiRuntimeError
    
    def get_pos(self, timeout = 0):
        """Get motor position.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            position(rad)
            None if timeout
        """
        try:
            return self._node.get_feedback(timeout)[0]
        except:
            raise MotorApiRuntimeError
    
    def get_vel(self, timeout = 0):
        """Get motor velocity.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            velocity(rad/s)
            None if timeout
        """
        try:
            return self._node.get_feedback(timeout)[1]
        except:
            raise MotorApiRuntimeError
    
    def get_torque(self, timeout = 0):
        """Get motor torque.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            torque(Nm)
            None if timeout
        """
        try:
            return self._node.get_feedback(timeout)[2]
        except:
            raise MotorApiRuntimeError
    
    def get_mode(self, timeout = 0):
        """Get motor control mode and params.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            control mode(MotorControlMode), control params dict
            None if timeout
        """
        try:
            return self._node.get_mode(timeout)
        except:
            raise MotorApiRuntimeError
        
    def position_mode(self):
        """Enter position pid mode."""
        try:
            self._node.position_mode()
        except:
            raise MotorApiRuntimeError

    def position_filter_mode(self, bandwidth):
        """Enter position filter mode.
        
        Args:
            bandwidth: filter bandwith, equals to control frequency(Hz)
        """
        try:
            self._node.position_filter_mode(bandwidth)
        except:
            raise MotorApiRuntimeError

    def position_track_mode(self, vel, acc, dec):
        """Enter position track mode.
        
        Args:
            vel: motion max vel(rad/s)
            acc: motion acceleration(rad/s^2)
            dec: motion deceleration(rad/s^2)
        """
        try:
            self._node.position_track_mode(vel, acc, dec)
        except:
            raise MotorApiRuntimeError

    def velocity_mode(self):
        """Enter velocity mode."""
        try:
            self._node.velocity_mode()
        except:
            raise MotorApiRuntimeError

    def velocity_ramp_mode(self, ramp):
        """Enter velocity ramp mode.
        
        Args:
            ramp: motion acceleration(rad/s^2)
        """
        try:
            self._node.velocity_ramp_mode(ramp)
        except:
            raise MotorApiRuntimeError

    def torque_mode(self):
        """Enter torque mode"""
        try:
            self._node.torque_mode()
        except:
            raise MotorApiRuntimeError

    def get_pid(self, timeout = 0):
        """Get motor pid params.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            pos_kp, vel_kp, vel_ki
            None if timeout
        """
        try:
            return self._node.get_pid(timeout)
        except:
            raise MotorApiRuntimeError
    
    def set_pid(self, pos_kp, vel_kp, vel_ki):
        """Set motor pid params.
        
        Args:
            pos_kp: kp of position control
            vel_kp: kp of velocity control
            vel_ki: ki of velocity control
        """
        try:
            self._node.set_pid(pos_kp, vel_kp, vel_ki)
        except:
            raise MotorApiRuntimeError

    def get_vel_limit(self, timeout = 0):
        """Get motor volocity limit.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            velocity limit(rad/s)
            None if timeout
        """
        try:
            return self._node.get_vel_limit(timeout)
        except:
            raise MotorApiRuntimeError
        
    def get_current_limit(self, timeout = 0):
        """Get motor current limit.
        
        Args:
            timeout: 0 indicates unlimited timeout(s)
        
        Returns:
            current limit(A)
            None if timeout
        """
        try:
            return self._node.get_current_limit(timeout)
        except:
            raise MotorApiRuntimeError

    def set_vel_limit(self, vel_lim):
        """Set motor velocity limit.
        
        Args:
            vel_lim: velocity limit(rad/s)
        """
        try:
            self._node.set_vel_limit(vel_lim)
        except:
            raise MotorApiRuntimeError

    def set_current_limit(self, current_lim):
        """Set motor current limit.
        
        Args:
            current_lim: current limit(A)
        """
        try:
            self._node.set_current_limit(current_lim)
        except:
            raise MotorApiRuntimeError

    def set_pos(self, pos, vel_ff = 0, torque_ff = 0):
        """Set motor target position.
        
        Args:
            pos: target position(rad)
            vel_ff: velocity feed forward(rad/s)
            torque_ff:torque feed forward(Nm)
        """
        try:
            self._node.set_pos(pos, vel_ff, torque_ff)
        except:
            raise MotorApiRuntimeError

    def set_vel(self, vel, torque_ff = 0):
        """Set motor velocity.
        
        Args:
            vel: target velocity(rad)
            torque_ff: torque feed forward(Nm)
        """
        try:
            self._node.set_vel(vel, torque_ff)
        except:
            raise MotorApiRuntimeError

    def set_torque(self, torque):
        """Set motor torque.
        
        Args:
            torque: target torque(Nm)
        """
        try:
            self._node.set_torque(torque)
        except:
            raise MotorApiRuntimeError

    def reset(self):
        """Reset motor with factory configurations."""
        try:
            self._node.reset()
        except:
            raise MotorApiRuntimeError

    def unlock(self):
        """Unlock motor brake if motor has one."""
        if not self.with_brake:
            raise RuntimeError('Motor do not have a brake.')
        try:
            self._node.reset()
        except:
            raise MotorApiRuntimeError
