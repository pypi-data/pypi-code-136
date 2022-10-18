"""_1283.py

SurfacePermanentMagnetMachine
"""


from mastapy.electric_machines import _1284, _1267
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_SURFACE_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'SurfacePermanentMagnetMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('SurfacePermanentMagnetMachine',)


class SurfacePermanentMagnetMachine(_1267.NonCADElectricMachineDetail):
    """SurfacePermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _SURFACE_PERMANENT_MAGNET_MACHINE

    def __init__(self, instance_to_wrap: 'SurfacePermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(self) -> '_1284.SurfacePermanentMagnetRotor':
        """SurfacePermanentMagnetRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
