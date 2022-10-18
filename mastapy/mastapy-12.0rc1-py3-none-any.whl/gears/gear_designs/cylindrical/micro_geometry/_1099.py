"""_1099.py

CylindricalGearSetMicroGeometry
"""


from typing import List

from mastapy.gears.gear_designs.cylindrical import _1021, _1033
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093, _1090
from mastapy.gears.analysis import _1221
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearSetMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMicroGeometry',)


class CylindricalGearSetMicroGeometry(_1221.GearSetImplementationDetail):
    """CylindricalGearSetMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MICRO_GEOMETRY

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set_design(self) -> '_1021.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'CylindricalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetDesign

        if temp is None:
            return None

        if _1021.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_set_design to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometries(self) -> 'List[_1093.CylindricalGearMicroGeometryBase]':
        """List[CylindricalGearMicroGeometryBase]: 'CylindricalGearMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_mesh_micro_geometries(self) -> 'List[_1090.CylindricalGearMeshMicroGeometry]':
        """List[CylindricalGearMeshMicroGeometry]: 'CylindricalMeshMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def duplicate(self) -> 'CylindricalGearSetMicroGeometry':
        """ 'Duplicate' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_and_add_to(self, gear_set_design: '_1021.CylindricalGearSetDesign') -> 'CylindricalGearSetMicroGeometry':
        """ 'DuplicateAndAddTo' is the original name of this method.

        Args:
            gear_set_design (mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign)

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        method_result = self.wrapped.DuplicateAndAddTo(gear_set_design.wrapped if gear_set_design else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_planet(self) -> '_1221.GearSetImplementationDetail':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachPlanet' is the original name of this method.

        Returns:
            mastapy.gears.analysis.GearSetImplementationDetail
        """

        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachPlanet()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_planet_and_add_to(self, gear_set_design: '_1033.CylindricalPlanetaryGearSetDesign') -> '_1221.GearSetImplementationDetail':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachPlanetAndAddTo' is the original name of this method.

        Args:
            gear_set_design (mastapy.gears.gear_designs.cylindrical.CylindricalPlanetaryGearSetDesign)

        Returns:
            mastapy.gears.analysis.GearSetImplementationDetail
        """

        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachPlanetAndAddTo(gear_set_design.wrapped if gear_set_design else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_tooth(self) -> 'CylindricalGearSetMicroGeometry':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachTooth' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachTooth()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_specifying_separate_micro_geometry_for_each_tooth_for(self, gears: 'List[_1093.CylindricalGearMicroGeometryBase]') -> 'CylindricalGearSetMicroGeometry':
        """ 'DuplicateSpecifyingSeparateMicroGeometryForEachToothFor' is the original name of this method.

        Args:
            gears (List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMicroGeometryBase])

        Returns:
            mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry
        """

        gears = conversion.mp_to_pn_objects_in_list(gears)
        method_result = self.wrapped.DuplicateSpecifyingSeparateMicroGeometryForEachToothFor(gears)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
