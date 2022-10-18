"""_2256.py

BevelGearTeethSocket
"""


from mastapy.system_model.connections_and_sockets.gears import _2252
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearTeethSocket',)


class BevelGearTeethSocket(_2252.AGMAGleasonConicalGearTeethSocket):
    """BevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_TEETH_SOCKET

    def __init__(self, instance_to_wrap: 'BevelGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
