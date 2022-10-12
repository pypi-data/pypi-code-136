"""Top-level package for Light Controller."""

__author__ = """Tristan Cotte"""
__email__ = 'tristan.cotte@sgs.com'
__version__ = '0.1.0'

from typing import List

import serial

from .utils_uart import split, compute_checksum, compute_command
from .transformations import declist_to_binlist, bin_to_hex


class LightManager(serial.Serial):
    def __init__(self, port: str, baudrate: int, list_channels: List[int]):
        """
        Class which enables to handle the 8 lights channels thanks to the "FG-PDV400W-24-8T" controller
        :param port: communication port used by the computer to reach the controller. Ex : "COM1"
        :param baudrate: communication frequency used to communicate with the controller
        :param list_channels: list of channels used by the controller to handle lights
        """
        super().__init__(port, baudrate, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
        self.port = port
        self.baudrate = baudrate
        self.list_channels = list_channels

        self.initialization()

    def initialization(self) -> None:
        """
        Steady mode on all the channels -> command Hx.1 for all channels named x
        8 is the parameter of the mode
        """
        for i in range(1, 9):
            chain = "$8" + str(i) + "000"
            chain_list = split(chain)
            list_bin = declist_to_binlist(chain_list)

            checksum = compute_checksum(list_bin)
            checksum_hex = bin_to_hex(checksum)
            command = chain + checksum_hex
            self.write(command.encode())

    def switch_off(self) -> None:
        """
        Switch off the five lights in the platform
        """
        for c in self.list_channels:
            command = compute_command(intensity=0, channel=c)
            self.write(command.encode())

    def switch_on(self, list_intensity) -> None:
        """
        Switch on the lights sending 5 commands of intensity for the five lights
        :param list_intensity: list of the light's intensity with index respective to the channel list
        """
        for c, i in zip(self.list_channels, list_intensity):
            command = compute_command(intensity=i, channel=c)
            self.write(command.encode())


