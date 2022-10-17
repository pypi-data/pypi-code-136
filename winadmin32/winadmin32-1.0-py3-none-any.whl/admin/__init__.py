"""
This simple ctypes wrapper that provides an easy
way to require elevated privileges on Windows.

Usage:

import admin

# Request administrator privileges
admin.request_elevated()

"""

import sys
import ctypes

_perform = True

# Perform basic runtime checks
if __name__ == '__main__':
    sys.stderr.write("The admin module is not meant to be run standalone. Please import the module!\n")
    sys.exit(1)

if sys.platform != 'win32':
    sys.stderr.write("The admin module is only available on Win32 platforms.\n")
    sys.exit(1)

if ctypes.windll.shell32.IsUserAnAdmin():
    _perform = False

def _construct_argv():
    return ' '.join(sys.argv)

"""
request_elevated():

This function is intended to be run before any program logic,
as it does not maintain the previous program state
"""

def request_elevated():
    if not _perform:
        return
    
    ctypes.windll.shell32.ShellExecuteW(
        None             ,
        'runas'          ,
        sys.executable   ,
        _construct_argv(),
        None             ,
        None
    )