import wx
from user_interface import MainFrame
from configparser import ConfigParser
import os
import sys
import argparse

file_path = os.path.dirname(os.path.abspath(__file__))
niraapad_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(niraapad_path)

import niraapad.backends
from niraapad.lab_computer.niraapad_client import NiraapadClient



## ENTER THE HOST AND PORT
host = 'localhost'
port = '1337'
NiraapadClient.connect_to_middlebox(host, port)


if __name__ == '__main__':

    """Running the user interface."""

    app = wx.App()
    states_frame = MainFrame()
    app.MainLoop()





