import os
import sys
from tkinter import *


def SetWindowPosition(window):
    '''
    Place window to the center of screen
    '''

    window.update()
    window.resizable(0, 0)

    win_width = window.winfo_reqwidth() // 2
    win_height = window.winfo_reqheight() // 2

    screen_width = window.winfo_screenwidth() // 2
    screen_height = window.winfo_screenheight() // 2

    window.geometry(f'+{screen_width - win_width}+{screen_height - win_height}')
    window.deiconify()


def ResourcePath(FileName):
    '''
    Get absolute path to resource from temporary directory

    In development:
        Gets path of files that are used in this script like icons, images or file of any extension from current directory

    After compiling to .exe with pyinstaller and using --add-data flag:
        Gets path of files that are used in this script like icons, images or file of any extension from temporary directory
    '''

    try:
        base_path = sys._MEIPASS  # PyInstaller creates a temporary directory and stores path of that directory in _MEIPASS

    except AttributeError:
        base_path = os.path.dirname(__file__)

    base_path = os.path.dirname(base_path)

    return os.path.join(base_path, 'assets', FileName)
