import configparser
from iot_gh.GHService import GHService
from iot_gh.GHConf import GHConf

class IoTGreenhouseService(GHService):
    """A container class for IoT Greenhouse services implemented on the 
    Raspberry Pi.
    """

    def __init__(self):
        import os
        import pigpio
        import spidev
        import configparser

        pi = pigpio.pi()
        spi = spidev.SpiDev()
        conf = GHConf()
        super().__init__(pi, spi, conf)

