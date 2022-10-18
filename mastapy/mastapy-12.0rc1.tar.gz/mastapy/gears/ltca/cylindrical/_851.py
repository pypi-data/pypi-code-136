"""_851.py

CylindricalGearMeshLoadedContactLine
"""


from typing import List

from mastapy.gears.ltca.cylindrical import _852
from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _836
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_LINE = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearMeshLoadedContactLine')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshLoadedContactLine',)


class CylindricalGearMeshLoadedContactLine(_836.GearMeshLoadedContactLine):
    """CylindricalGearMeshLoadedContactLine

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_LINE

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshLoadedContactLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_contact_strip_end_points(self) -> 'List[_852.CylindricalGearMeshLoadedContactPoint]':
        """List[CylindricalGearMeshLoadedContactPoint]: 'LoadedContactStripEndPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedContactStripEndPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
