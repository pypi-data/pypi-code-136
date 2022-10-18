"""_1087.py

CylindricalGearFlankMicroGeometry
"""


from typing import List

from mastapy.math_utility.measured_data import _1530
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
    _1085, _1088, _1089, _1095,
    _1097, _1098, _1102, _1106,
    _1108, _1117, _1119, _1122,
    _1123
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _1018, _1005, _1034
from mastapy.gears.micro_geometry import _563
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearFlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFlankMicroGeometry',)


class CylindricalGearFlankMicroGeometry(_563.FlankMicroGeometry):
    """CylindricalGearFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_MICRO_GEOMETRY

    def __init__(self, instance_to_wrap: 'CylindricalGearFlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_matrix(self) -> '_1530.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'MicroGeometryMatrix' is the original name of this property."""

        temp = self.wrapped.MicroGeometryMatrix

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @micro_geometry_matrix.setter
    def micro_geometry_matrix(self, value: '_1530.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.MicroGeometryMatrix = value

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_assuming_unmodified_normal_module_and_pressure_angle_modification(self) -> 'float':
        """float: 'ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModuleAndPressureAngleModification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModuleAndPressureAngleModification

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def use_measured_map_data(self) -> 'bool':
        """bool: 'UseMeasuredMapData' is the original name of this property."""

        temp = self.wrapped.UseMeasuredMapData

        if temp is None:
            return False

        return temp

    @use_measured_map_data.setter
    def use_measured_map_data(self, value: 'bool'):
        self.wrapped.UseMeasuredMapData = bool(value) if value else False

    @property
    def bias(self) -> '_1085.CylindricalGearBiasModification':
        """CylindricalGearBiasModification: 'Bias' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bias

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_relief(self) -> '_1088.CylindricalGearLeadModification':
        """CylindricalGearLeadModification: 'LeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadRelief

        if temp is None:
            return None

        if _1088.CylindricalGearLeadModification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast lead_relief to CylindricalGearLeadModification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_map(self) -> '_1095.CylindricalGearMicroGeometryMap':
        """CylindricalGearMicroGeometryMap: 'MicroGeometryMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_control_point(self) -> '_1018.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ProfileControlPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileControlPoint

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_relief(self) -> '_1097.CylindricalGearProfileModification':
        """CylindricalGearProfileModification: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileRelief

        if temp is None:
            return None

        if _1097.CylindricalGearProfileModification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast profile_relief to CylindricalGearProfileModification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def triangular_end_relief(self) -> '_1102.CylindricalGearTriangularEndModification':
        """CylindricalGearTriangularEndModification: 'TriangularEndRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TriangularEndRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_form_deviation_points(self) -> 'List[_1106.LeadFormReliefWithDeviation]':
        """List[LeadFormReliefWithDeviation]: 'LeadFormDeviationPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadFormDeviationPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def lead_slope_deviation_points(self) -> 'List[_1108.LeadSlopeReliefWithDeviation]':
        """List[LeadSlopeReliefWithDeviation]: 'LeadSlopeDeviationPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadSlopeDeviationPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_form_deviation_points(self) -> 'List[_1117.ProfileFormReliefWithDeviation]':
        """List[ProfileFormReliefWithDeviation]: 'ProfileFormDeviationPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviationPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_slope_deviation_at_10_percent_face_width(self) -> 'List[_1119.ProfileSlopeReliefWithDeviation]':
        """List[ProfileSlopeReliefWithDeviation]: 'ProfileSlopeDeviationAt10PercentFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAt10PercentFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_slope_deviation_at_50_percent_face_width(self) -> 'List[_1119.ProfileSlopeReliefWithDeviation]':
        """List[ProfileSlopeReliefWithDeviation]: 'ProfileSlopeDeviationAt50PercentFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAt50PercentFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_slope_deviation_at_90_percent_face_width(self) -> 'List[_1119.ProfileSlopeReliefWithDeviation]':
        """List[ProfileSlopeReliefWithDeviation]: 'ProfileSlopeDeviationAt90PercentFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAt90PercentFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def total_lead_relief_points(self) -> 'List[_1122.TotalLeadReliefWithDeviation]':
        """List[TotalLeadReliefWithDeviation]: 'TotalLeadReliefPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalLeadReliefPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def total_profile_relief_points(self) -> 'List[_1123.TotalProfileReliefWithDeviation]':
        """List[TotalProfileReliefWithDeviation]: 'TotalProfileReliefPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileReliefPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_design(self) -> '_1005.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign

        if temp is None:
            return None

        if _1005.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def total_relief(self, face_width: 'float', roll_distance: 'float') -> 'float':
        """ 'TotalRelief' is the original name of this method.

        Args:
            face_width (float)
            roll_distance (float)

        Returns:
            float
        """

        face_width = float(face_width)
        roll_distance = float(roll_distance)
        method_result = self.wrapped.TotalRelief(face_width if face_width else 0.0, roll_distance if roll_distance else 0.0)
        return method_result
