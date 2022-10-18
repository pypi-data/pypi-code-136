"""_1259.py

InteriorPermanentMagnetMachine
"""


from mastapy.electric_machines import _1258, _1267
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_MACHINE = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetMachine')


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetMachine',)


class InteriorPermanentMagnetMachine(_1267.NonCADElectricMachineDetail):
    """InteriorPermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_MACHINE

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetMachine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(self) -> '_1258.InteriorPermanentMagnetAndSynchronousReluctanceRotor':
        """InteriorPermanentMagnetAndSynchronousReluctanceRotor: 'Rotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
