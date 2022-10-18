"""_1092.py

CylindricalGearMicroGeometry
"""


from typing import List

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1087, _1113, _1093
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometry',)


class CylindricalGearMicroGeometry(_1093.CylindricalGearMicroGeometryBase):
    """CylindricalGearMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank(self) -> '_1087.CylindricalGearFlankMicroGeometry':
        """CylindricalGearFlankMicroGeometry: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank(self) -> '_1087.CylindricalGearFlankMicroGeometry':
        """CylindricalGearFlankMicroGeometry: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def flanks(self) -> 'List[_1087.CylindricalGearFlankMicroGeometry]':
        """List[CylindricalGearFlankMicroGeometry]: 'Flanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Flanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gears(self) -> 'List[_1113.MeshedCylindricalGearMicroGeometry]':
        """List[MeshedCylindricalGearMicroGeometry]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def both_flanks(self) -> '_1087.CylindricalGearFlankMicroGeometry':
        """CylindricalGearFlankMicroGeometry: 'BothFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BothFlanks

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
