"""_2264.py

FaceGearTeethSocket
"""


from mastapy.system_model.connections_and_sockets.gears import _2266
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'FaceGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearTeethSocket',)


class FaceGearTeethSocket(_2266.GearTeethSocket):
    """FaceGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_TEETH_SOCKET

    def __init__(self, instance_to_wrap: 'FaceGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
