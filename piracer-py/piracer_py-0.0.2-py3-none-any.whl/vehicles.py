import math
import time

import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685


class PiRacerBase:
    PWM_RESOLUTION = 16
    PWM_MAX_RAW_VALUE = math.pow(2, PWM_RESOLUTION) - 1

    PWM_FREQ_50HZ = 50.0
    PWM_WAVELENGTH_50HZ = 1.0 / PWM_FREQ_50HZ
    PWM_FREQ_500HZ = 500.0
    PWM_WAVELENGTH_500HZ = 1.0 / PWM_FREQ_500HZ

    def __init__(self):
        self.i2c_bus = busio.I2C(SCL, SDA)

    def warmup(self):
        self.set_steering_percent(0.0)
        self.set_throttle_percent(0.0)
        time.sleep(2.0)

    @classmethod
    def set_channel_active_time(self, time: float, pwm_controller: PCA9685, channel: int):
        raw_value = int(self.PWM_MAX_RAW_VALUE * (time / self.PWM_WAVELENGTH_50HZ))
        pwm_controller.channels[channel].duty_cycle = raw_value


class PiRacerPro(PiRacerBase):
    PWM_STEERING_CHANNEL = 0
    PWM_THROTTLE_CHANNEL = 1

    def __init__(self):
        super().__init__()
        self.pwm_controller = PCA9685(self.i2c_bus, address=0x40)
        self.pwm_controller.frequency = self.PWM_FREQ_50HZ
        self.warmup()

    def set_steering_percent(self, value: float):
        self.set_channel_active_time(0.0015 + (value * 0.0005), self.pwm_controller, self.PWM_STEERING_CHANNEL)

    def set_throttle_percent(self, value: float):
        self.set_channel_active_time(0.0015 + (value * 0.0005), self.pwm_controller, self.PWM_THROTTLE_CHANNEL)


class PiRacerStandard(PiRacerBase):
    PWM_STEERING_CHANNEL = 0
    PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN1 = 5
    PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN2 = 6
    PWM_THROTTLE_CHANNEL_LEFT_MOTOR_PWM = 7
    PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN1 = 1
    PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN2 = 2
    PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_PWM = 0

    def __init__(self):
        super().__init__()
        self.steering_pwm_controller = PCA9685(self.i2c_bus, address=0x40)
        self.steering_pwm_controller.frequency = self.PWM_FREQ_50HZ

        self.throttle_pwm_controller = PCA9685(self.i2c_bus, address=0x60)
        self.throttle_pwm_controller.frequency = self.PWM_FREQ_50HZ

        self.warmup()

    def set_steering_percent(self, value: float):
        self.set_channel_active_time(0.0015 + (value * 0.0005), self.steering_pwm_controller, self.PWM_STEERING_CHANNEL)
        pass

    def set_throttle_percent(self, value: float):
        if value > 0:
            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN1].duty_cycle = self.PWM_MAX_RAW_VALUE
            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN2].duty_cycle = 0

            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN1].duty_cycle = 0
            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN2].duty_cycle = self.PWM_MAX_RAW_VALUE
        else:
            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN1].duty_cycle = 0
            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN2].duty_cycle = self.PWM_MAX_RAW_VALUE

            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN1].duty_cycle = self.PWM_MAX_RAW_VALUE
            self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN2].duty_cycle = 0

        pwm_raw_value = int(self.PWM_MAX_RAW_VALUE * abs(value))
        print(pwm_raw_value)
        self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_PWM].duty_cycle = pwm_raw_value
        self.throttle_pwm_controller.channels[self.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_PWM].duty_cycle = pwm_raw_value
