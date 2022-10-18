"""_1015.py

CylindricalGearMicroGeometrySettingsItem
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.micro_geometry import (
    _564, _566, _567, _568,
    _569, _570, _571, _573,
    _574
)
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114
from mastapy.gears.gear_designs.cylindrical import (
    _1037, _1061, _1053, _1054
)
from mastapy.utility.databases import _1792
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearMicroGeometrySettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometrySettingsItem',)


class CylindricalGearMicroGeometrySettingsItem(_1792.NamedDatabaseItem):
    """CylindricalGearMicroGeometrySettingsItem

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_ITEM

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometrySettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def add_flank_side_labels_to_micro_geometry_lead_tolerance_charts(self) -> 'bool':
        """bool: 'AddFlankSideLabelsToMicroGeometryLeadToleranceCharts' is the original name of this property."""

        temp = self.wrapped.AddFlankSideLabelsToMicroGeometryLeadToleranceCharts

        if temp is None:
            return False

        return temp

    @add_flank_side_labels_to_micro_geometry_lead_tolerance_charts.setter
    def add_flank_side_labels_to_micro_geometry_lead_tolerance_charts(self, value: 'bool'):
        self.wrapped.AddFlankSideLabelsToMicroGeometryLeadToleranceCharts = bool(value) if value else False

    @property
    def adjust_micro_geometry_for_analysis_by_default_when_including_pitch_errors(self) -> 'bool':
        """bool: 'AdjustMicroGeometryForAnalysisByDefaultWhenIncludingPitchErrors' is the original name of this property."""

        temp = self.wrapped.AdjustMicroGeometryForAnalysisByDefaultWhenIncludingPitchErrors

        if temp is None:
            return False

        return temp

    @adjust_micro_geometry_for_analysis_by_default_when_including_pitch_errors.setter
    def adjust_micro_geometry_for_analysis_by_default_when_including_pitch_errors(self, value: 'bool'):
        self.wrapped.AdjustMicroGeometryForAnalysisByDefaultWhenIncludingPitchErrors = bool(value) if value else False

    @property
    def centre_tolerance_charts_at_maximum_fullness(self) -> 'bool':
        """bool: 'CentreToleranceChartsAtMaximumFullness' is the original name of this property."""

        temp = self.wrapped.CentreToleranceChartsAtMaximumFullness

        if temp is None:
            return False

        return temp

    @centre_tolerance_charts_at_maximum_fullness.setter
    def centre_tolerance_charts_at_maximum_fullness(self, value: 'bool'):
        self.wrapped.CentreToleranceChartsAtMaximumFullness = bool(value) if value else False

    @property
    def crop_face_width_axis_of_micro_geometry_lead_tolerance_charts(self) -> 'bool':
        """bool: 'CropFaceWidthAxisOfMicroGeometryLeadToleranceCharts' is the original name of this property."""

        temp = self.wrapped.CropFaceWidthAxisOfMicroGeometryLeadToleranceCharts

        if temp is None:
            return False

        return temp

    @crop_face_width_axis_of_micro_geometry_lead_tolerance_charts.setter
    def crop_face_width_axis_of_micro_geometry_lead_tolerance_charts(self, value: 'bool'):
        self.wrapped.CropFaceWidthAxisOfMicroGeometryLeadToleranceCharts = bool(value) if value else False

    @property
    def crop_profile_measurement_axis_of_micro_geometry_profile_tolerance_charts(self) -> 'bool':
        """bool: 'CropProfileMeasurementAxisOfMicroGeometryProfileToleranceCharts' is the original name of this property."""

        temp = self.wrapped.CropProfileMeasurementAxisOfMicroGeometryProfileToleranceCharts

        if temp is None:
            return False

        return temp

    @crop_profile_measurement_axis_of_micro_geometry_profile_tolerance_charts.setter
    def crop_profile_measurement_axis_of_micro_geometry_profile_tolerance_charts(self, value: 'bool'):
        self.wrapped.CropProfileMeasurementAxisOfMicroGeometryProfileToleranceCharts = bool(value) if value else False

    @property
    def default_flank_side_with_zero_face_width(self) -> '_564.FlankSide':
        """FlankSide: 'DefaultFlankSideWithZeroFaceWidth' is the original name of this property."""

        temp = self.wrapped.DefaultFlankSideWithZeroFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_564.FlankSide)(value) if value is not None else None

    @default_flank_side_with_zero_face_width.setter
    def default_flank_side_with_zero_face_width(self, value: '_564.FlankSide'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DefaultFlankSideWithZeroFaceWidth = value

    @property
    def default_location_of_evaluation_lower_limit(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit':
        """enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit: 'DefaultLocationOfEvaluationLowerLimit' is the original name of this property."""

        temp = self.wrapped.DefaultLocationOfEvaluationLowerLimit

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @default_location_of_evaluation_lower_limit.setter
    def default_location_of_evaluation_lower_limit(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfEvaluationLowerLimit = value

    @property
    def default_location_of_evaluation_upper_limit(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit':
        """enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit: 'DefaultLocationOfEvaluationUpperLimit' is the original name of this property."""

        temp = self.wrapped.DefaultLocationOfEvaluationUpperLimit

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @default_location_of_evaluation_upper_limit.setter
    def default_location_of_evaluation_upper_limit(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfEvaluationUpperLimit = value

    @property
    def default_location_of_root_relief_evaluation(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation':
        """enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation: 'DefaultLocationOfRootReliefEvaluation' is the original name of this property."""

        temp = self.wrapped.DefaultLocationOfRootReliefEvaluation

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @default_location_of_root_relief_evaluation.setter
    def default_location_of_root_relief_evaluation(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfRootReliefEvaluation = value

    @property
    def default_location_of_root_relief_start(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation':
        """enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation: 'DefaultLocationOfRootReliefStart' is the original name of this property."""

        temp = self.wrapped.DefaultLocationOfRootReliefStart

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @default_location_of_root_relief_start.setter
    def default_location_of_root_relief_start(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfRootReliefStart = value

    @property
    def default_location_of_tip_relief_evaluation(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation':
        """enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation: 'DefaultLocationOfTipReliefEvaluation' is the original name of this property."""

        temp = self.wrapped.DefaultLocationOfTipReliefEvaluation

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @default_location_of_tip_relief_evaluation.setter
    def default_location_of_tip_relief_evaluation(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfTipReliefEvaluation = value

    @property
    def default_location_of_tip_relief_start(self) -> 'enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation':
        """enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation: 'DefaultLocationOfTipReliefStart' is the original name of this property."""

        temp = self.wrapped.DefaultLocationOfTipReliefStart

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @default_location_of_tip_relief_start.setter
    def default_location_of_tip_relief_start(self, value: 'enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DefaultLocationOfTipReliefStart = value

    @property
    def default_micro_geometry_lead_tolerance_chart_view(self) -> '_1114.MicroGeometryLeadToleranceChartView':
        """MicroGeometryLeadToleranceChartView: 'DefaultMicroGeometryLeadToleranceChartView' is the original name of this property."""

        temp = self.wrapped.DefaultMicroGeometryLeadToleranceChartView

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1114.MicroGeometryLeadToleranceChartView)(value) if value is not None else None

    @default_micro_geometry_lead_tolerance_chart_view.setter
    def default_micro_geometry_lead_tolerance_chart_view(self, value: '_1114.MicroGeometryLeadToleranceChartView'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DefaultMicroGeometryLeadToleranceChartView = value

    @property
    def default_scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(self) -> '_1037.DoubleAxisScaleAndRange':
        """DoubleAxisScaleAndRange: 'DefaultScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts' is the original name of this property."""

        temp = self.wrapped.DefaultScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1037.DoubleAxisScaleAndRange)(value) if value is not None else None

    @default_scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts.setter
    def default_scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(self, value: '_1037.DoubleAxisScaleAndRange'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DefaultScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts = value

    @property
    def draw_micro_geometry_charts_with_face_width_axis_oriented_to_view_through_air(self) -> 'bool':
        """bool: 'DrawMicroGeometryChartsWithFaceWidthAxisOrientedToViewThroughAir' is the original name of this property."""

        temp = self.wrapped.DrawMicroGeometryChartsWithFaceWidthAxisOrientedToViewThroughAir

        if temp is None:
            return False

        return temp

    @draw_micro_geometry_charts_with_face_width_axis_oriented_to_view_through_air.setter
    def draw_micro_geometry_charts_with_face_width_axis_oriented_to_view_through_air(self, value: 'bool'):
        self.wrapped.DrawMicroGeometryChartsWithFaceWidthAxisOrientedToViewThroughAir = bool(value) if value else False

    @property
    def draw_micro_geometry_profile_chart_with_relief_on_horizontal_axis(self) -> 'bool':
        """bool: 'DrawMicroGeometryProfileChartWithReliefOnHorizontalAxis' is the original name of this property."""

        temp = self.wrapped.DrawMicroGeometryProfileChartWithReliefOnHorizontalAxis

        if temp is None:
            return False

        return temp

    @draw_micro_geometry_profile_chart_with_relief_on_horizontal_axis.setter
    def draw_micro_geometry_profile_chart_with_relief_on_horizontal_axis(self, value: 'bool'):
        self.wrapped.DrawMicroGeometryProfileChartWithReliefOnHorizontalAxis = bool(value) if value else False

    @property
    def ltca_root_stress_surface_chart_option(self) -> '_1061.RootStressSurfaceChartOption':
        """RootStressSurfaceChartOption: 'LTCARootStressSurfaceChartOption' is the original name of this property."""

        temp = self.wrapped.LTCARootStressSurfaceChartOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1061.RootStressSurfaceChartOption)(value) if value is not None else None

    @ltca_root_stress_surface_chart_option.setter
    def ltca_root_stress_surface_chart_option(self, value: '_1061.RootStressSurfaceChartOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.LTCARootStressSurfaceChartOption = value

    @property
    def main_profile_modification_ends_at_the_start_of_root_relief_by_default(self) -> '_570.MainProfileReliefEndsAtTheStartOfRootReliefOption':
        """MainProfileReliefEndsAtTheStartOfRootReliefOption: 'MainProfileModificationEndsAtTheStartOfRootReliefByDefault' is the original name of this property."""

        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfRootReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_570.MainProfileReliefEndsAtTheStartOfRootReliefOption)(value) if value is not None else None

    @main_profile_modification_ends_at_the_start_of_root_relief_by_default.setter
    def main_profile_modification_ends_at_the_start_of_root_relief_by_default(self, value: '_570.MainProfileReliefEndsAtTheStartOfRootReliefOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MainProfileModificationEndsAtTheStartOfRootReliefByDefault = value

    @property
    def main_profile_modification_ends_at_the_start_of_tip_relief_by_default(self) -> '_571.MainProfileReliefEndsAtTheStartOfTipReliefOption':
        """MainProfileReliefEndsAtTheStartOfTipReliefOption: 'MainProfileModificationEndsAtTheStartOfTipReliefByDefault' is the original name of this property."""

        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfTipReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_571.MainProfileReliefEndsAtTheStartOfTipReliefOption)(value) if value is not None else None

    @main_profile_modification_ends_at_the_start_of_tip_relief_by_default.setter
    def main_profile_modification_ends_at_the_start_of_tip_relief_by_default(self, value: '_571.MainProfileReliefEndsAtTheStartOfTipReliefOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MainProfileModificationEndsAtTheStartOfTipReliefByDefault = value

    @property
    def measure_root_reliefs_from_extrapolated_linear_relief_by_default(self) -> 'bool':
        """bool: 'MeasureRootReliefsFromExtrapolatedLinearReliefByDefault' is the original name of this property."""

        temp = self.wrapped.MeasureRootReliefsFromExtrapolatedLinearReliefByDefault

        if temp is None:
            return False

        return temp

    @measure_root_reliefs_from_extrapolated_linear_relief_by_default.setter
    def measure_root_reliefs_from_extrapolated_linear_relief_by_default(self, value: 'bool'):
        self.wrapped.MeasureRootReliefsFromExtrapolatedLinearReliefByDefault = bool(value) if value else False

    @property
    def measure_tip_reliefs_from_extrapolated_linear_relief_by_default(self) -> 'bool':
        """bool: 'MeasureTipReliefsFromExtrapolatedLinearReliefByDefault' is the original name of this property."""

        temp = self.wrapped.MeasureTipReliefsFromExtrapolatedLinearReliefByDefault

        if temp is None:
            return False

        return temp

    @measure_tip_reliefs_from_extrapolated_linear_relief_by_default.setter
    def measure_tip_reliefs_from_extrapolated_linear_relief_by_default(self, value: 'bool'):
        self.wrapped.MeasureTipReliefsFromExtrapolatedLinearReliefByDefault = bool(value) if value else False

    @property
    def micro_geometry_lead_relief_definition(self) -> '_1053.MicroGeometryConvention':
        """MicroGeometryConvention: 'MicroGeometryLeadReliefDefinition' is the original name of this property."""

        temp = self.wrapped.MicroGeometryLeadReliefDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1053.MicroGeometryConvention)(value) if value is not None else None

    @micro_geometry_lead_relief_definition.setter
    def micro_geometry_lead_relief_definition(self, value: '_1053.MicroGeometryConvention'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MicroGeometryLeadReliefDefinition = value

    @property
    def micro_geometry_profile_relief_definition(self) -> '_1054.MicroGeometryProfileConvention':
        """MicroGeometryProfileConvention: 'MicroGeometryProfileReliefDefinition' is the original name of this property."""

        temp = self.wrapped.MicroGeometryProfileReliefDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1054.MicroGeometryProfileConvention)(value) if value is not None else None

    @micro_geometry_profile_relief_definition.setter
    def micro_geometry_profile_relief_definition(self, value: '_1054.MicroGeometryProfileConvention'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MicroGeometryProfileReliefDefinition = value

    @property
    def number_of_points_for_2d_micro_geometry_plots(self) -> 'int':
        """int: 'NumberOfPointsFor2DMicroGeometryPlots' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsFor2DMicroGeometryPlots

        if temp is None:
            return 0

        return temp

    @number_of_points_for_2d_micro_geometry_plots.setter
    def number_of_points_for_2d_micro_geometry_plots(self, value: 'int'):
        self.wrapped.NumberOfPointsFor2DMicroGeometryPlots = int(value) if value else 0

    @property
    def number_of_steps_for_ltca_contact_surface(self) -> 'int':
        """int: 'NumberOfStepsForLTCAContactSurface' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsForLTCAContactSurface

        if temp is None:
            return 0

        return temp

    @number_of_steps_for_ltca_contact_surface.setter
    def number_of_steps_for_ltca_contact_surface(self, value: 'int'):
        self.wrapped.NumberOfStepsForLTCAContactSurface = int(value) if value else 0

    @property
    def parabolic_root_relief_starts_tangent_to_main_profile_relief_by_default(self) -> '_573.ParabolicRootReliefStartsTangentToMainProfileRelief':
        """ParabolicRootReliefStartsTangentToMainProfileRelief: 'ParabolicRootReliefStartsTangentToMainProfileReliefByDefault' is the original name of this property."""

        temp = self.wrapped.ParabolicRootReliefStartsTangentToMainProfileReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_573.ParabolicRootReliefStartsTangentToMainProfileRelief)(value) if value is not None else None

    @parabolic_root_relief_starts_tangent_to_main_profile_relief_by_default.setter
    def parabolic_root_relief_starts_tangent_to_main_profile_relief_by_default(self, value: '_573.ParabolicRootReliefStartsTangentToMainProfileRelief'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ParabolicRootReliefStartsTangentToMainProfileReliefByDefault = value

    @property
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief_by_default(self) -> '_574.ParabolicTipReliefStartsTangentToMainProfileRelief':
        """ParabolicTipReliefStartsTangentToMainProfileRelief: 'ParabolicTipReliefStartsTangentToMainProfileReliefByDefault' is the original name of this property."""

        temp = self.wrapped.ParabolicTipReliefStartsTangentToMainProfileReliefByDefault

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_574.ParabolicTipReliefStartsTangentToMainProfileRelief)(value) if value is not None else None

    @parabolic_tip_relief_starts_tangent_to_main_profile_relief_by_default.setter
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief_by_default(self, value: '_574.ParabolicTipReliefStartsTangentToMainProfileRelief'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ParabolicTipReliefStartsTangentToMainProfileReliefByDefault = value

    @property
    def shift_micro_geometry_lead_and_profile_modification_to_have_zero_maximum(self) -> 'bool':
        """bool: 'ShiftMicroGeometryLeadAndProfileModificationToHaveZeroMaximum' is the original name of this property."""

        temp = self.wrapped.ShiftMicroGeometryLeadAndProfileModificationToHaveZeroMaximum

        if temp is None:
            return False

        return temp

    @shift_micro_geometry_lead_and_profile_modification_to_have_zero_maximum.setter
    def shift_micro_geometry_lead_and_profile_modification_to_have_zero_maximum(self, value: 'bool'):
        self.wrapped.ShiftMicroGeometryLeadAndProfileModificationToHaveZeroMaximum = bool(value) if value else False

    @property
    def use_same_micro_geometry_on_both_flanks_by_default(self) -> 'bool':
        """bool: 'UseSameMicroGeometryOnBothFlanksByDefault' is the original name of this property."""

        temp = self.wrapped.UseSameMicroGeometryOnBothFlanksByDefault

        if temp is None:
            return False

        return temp

    @use_same_micro_geometry_on_both_flanks_by_default.setter
    def use_same_micro_geometry_on_both_flanks_by_default(self, value: 'bool'):
        self.wrapped.UseSameMicroGeometryOnBothFlanksByDefault = bool(value) if value else False
