# -*- coding: utf8 -*-
# 文件:  ip.py
# 日期:  2021/10/7 13:41
import platform
import socket

__version__ = "1.1"
__all__ = ['get_ip', 'is_windows_os', 'get_hostname']


def get_ip():
    if is_windows_os():
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    else:
        ip = '0.0.0.0'
    return ip


def get_hostname():
    hostname = socket.gethostname()
    return hostname


def is_windows_os():
    return 'Windows' in platform.system()
