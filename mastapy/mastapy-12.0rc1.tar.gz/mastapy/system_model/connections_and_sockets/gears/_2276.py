"""_2276.py

SpiralBevelGearTeethSocket
"""


from mastapy.system_model.connections_and_sockets.gears import _2256
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'SpiralBevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearTeethSocket',)


class SpiralBevelGearTeethSocket(_2256.BevelGearTeethSocket):
    """SpiralBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_TEETH_SOCKET

    def __init__(self, instance_to_wrap: 'SpiralBevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
