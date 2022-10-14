import sys

if sys.platform == 'win32':
    from .can_bus.candle_interface import CandleInterface as CanBus
elif sys.platform.startswith('linux'):
    from .can_bus.socketcan_interface import SocketCanInterface as CanBus

