"""_2285.py

CycloidalDiscAxialLeftSocket
"""


from mastapy.system_model.connections_and_sockets import _2232
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal', 'CycloidalDiscAxialLeftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscAxialLeftSocket',)


class CycloidalDiscAxialLeftSocket(_2232.InnerShaftSocketBase):
    """CycloidalDiscAxialLeftSocket

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET

    def __init__(self, instance_to_wrap: 'CycloidalDiscAxialLeftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
