"""_2266.py

GearTeethSocket
"""


from mastapy.system_model.connections_and_sockets import _2248
from mastapy._internal.python_net import python_net_import

_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('GearTeethSocket',)


class GearTeethSocket(_2248.Socket):
    """GearTeethSocket

    This is a mastapy class.
    """

    TYPE = _GEAR_TEETH_SOCKET

    def __init__(self, instance_to_wrap: 'GearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
