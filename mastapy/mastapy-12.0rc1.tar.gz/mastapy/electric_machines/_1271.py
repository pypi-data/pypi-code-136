"""_1271.py

PermanentMagnetRotor
"""


from mastapy.electric_machines import _1274
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'PermanentMagnetRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('PermanentMagnetRotor',)


class PermanentMagnetRotor(_1274.Rotor):
    """PermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ROTOR

    def __init__(self, instance_to_wrap: 'PermanentMagnetRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
