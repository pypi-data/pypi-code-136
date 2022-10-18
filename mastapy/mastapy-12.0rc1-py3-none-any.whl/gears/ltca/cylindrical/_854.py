"""_854.py

CylindricalMeshLoadDistributionAtRotation
"""


from typing import List

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111
from mastapy._internal import constructor, conversion
from mastapy.gears.ltca.cylindrical import _851
from mastapy.gears.ltca import _835
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalMeshLoadDistributionAtRotation')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshLoadDistributionAtRotation',)


class CylindricalMeshLoadDistributionAtRotation(_835.GearMeshLoadDistributionAtRotation):
    """CylindricalMeshLoadDistributionAtRotation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LOAD_DISTRIBUTION_AT_ROTATION

    def __init__(self, instance_to_wrap: 'CylindricalMeshLoadDistributionAtRotation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_alignment(self) -> '_1111.MeshAlignment':
        """MeshAlignment: 'MeshAlignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loaded_contact_lines(self) -> 'List[_851.CylindricalGearMeshLoadedContactLine]':
        """List[CylindricalGearMeshLoadedContactLine]: 'LoadedContactLines' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedContactLines

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
