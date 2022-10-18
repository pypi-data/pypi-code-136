"""_1238.py

CADStator
"""


from mastapy._internal import constructor
from mastapy.electric_machines import _1239, _1233
from mastapy._internal.python_net import python_net_import

_CAD_STATOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADStator')


__docformat__ = 'restructuredtext en'
__all__ = ('CADStator',)


class CADStator(_1233.AbstractStator):
    """CADStator

    This is a mastapy class.
    """

    TYPE = _CAD_STATOR

    def __init__(self, instance_to_wrap: 'CADStator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_slots_for_imported_sector(self) -> 'int':
        """int: 'NumberOfSlotsForImportedSector' is the original name of this property."""

        temp = self.wrapped.NumberOfSlotsForImportedSector

        if temp is None:
            return 0

        return temp

    @number_of_slots_for_imported_sector.setter
    def number_of_slots_for_imported_sector(self, value: 'int'):
        self.wrapped.NumberOfSlotsForImportedSector = int(value) if value else 0

    @property
    def tooth_and_slot(self) -> '_1239.CADToothAndSlot':
        """CADToothAndSlot: 'ToothAndSlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
