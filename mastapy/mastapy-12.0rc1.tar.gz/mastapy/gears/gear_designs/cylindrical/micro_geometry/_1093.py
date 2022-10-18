"""_1093.py

CylindricalGearMicroGeometryBase
"""


from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1751
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1086, _1101
from mastapy.gears.gear_designs.cylindrical import _1005, _1034, _1018
from mastapy._internal.cast_exception import CastException
from mastapy.gears.analysis import _1211
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometryBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometryBase',)


class CylindricalGearMicroGeometryBase(_1211.GearImplementationDetail):
    """CylindricalGearMicroGeometryBase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometryBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors' is the original name of this property."""

        temp = self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors

        if temp is None:
            return False

        return constructor.new_from_mastapy_type(overridable.Overridable_bool)(temp) if temp is not None else False

    @adjust_micro_geometry_for_analysis_when_including_pitch_errors.setter
    def adjust_micro_geometry_for_analysis_when_including_pitch_errors(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.AdjustMicroGeometryForAnalysisWhenIncludingPitchErrors = value

    @property
    def lead_form_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadFormChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_slope_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadSlopeChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadSlopeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_total_nominal_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadTotalNominalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_total_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'LeadTotalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_control_point_is_user_specified(self) -> 'bool':
        """bool: 'ProfileControlPointIsUserSpecified' is the original name of this property."""

        temp = self.wrapped.ProfileControlPointIsUserSpecified

        if temp is None:
            return False

        return temp

    @profile_control_point_is_user_specified.setter
    def profile_control_point_is_user_specified(self, value: 'bool'):
        self.wrapped.ProfileControlPointIsUserSpecified = bool(value) if value else False

    @property
    def profile_form_10_percent_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileForm10PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm10PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_50_percent_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileForm50PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm50PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_90_percent_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileForm90PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm90PercentChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileFormChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_total_nominal_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileTotalNominalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTotalNominalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_total_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'ProfileTotalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTotalChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def use_same_micro_geometry_on_both_flanks(self) -> 'bool':
        """bool: 'UseSameMicroGeometryOnBothFlanks' is the original name of this property."""

        temp = self.wrapped.UseSameMicroGeometryOnBothFlanks

        if temp is None:
            return False

        return temp

    @use_same_micro_geometry_on_both_flanks.setter
    def use_same_micro_geometry_on_both_flanks(self, value: 'bool'):
        self.wrapped.UseSameMicroGeometryOnBothFlanks = bool(value) if value else False

    @property
    def common_micro_geometry_of_left_flank(self) -> '_1086.CylindricalGearCommonFlankMicroGeometry':
        """CylindricalGearCommonFlankMicroGeometry: 'CommonMicroGeometryOfLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometryOfLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def common_micro_geometry_of_right_flank(self) -> '_1086.CylindricalGearCommonFlankMicroGeometry':
        """CylindricalGearCommonFlankMicroGeometry: 'CommonMicroGeometryOfRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometryOfRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear(self) -> '_1005.CylindricalGearDesign':
        """CylindricalGearDesign: 'CylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGear

        if temp is None:
            return None

        if _1005.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def common_micro_geometries_of_flanks(self) -> 'List[_1086.CylindricalGearCommonFlankMicroGeometry]':
        """List[CylindricalGearCommonFlankMicroGeometry]: 'CommonMicroGeometriesOfFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometriesOfFlanks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tooth_micro_geometries(self) -> 'List[_1101.CylindricalGearToothMicroGeometry]':
        """List[CylindricalGearToothMicroGeometry]: 'ToothMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothMicroGeometries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
