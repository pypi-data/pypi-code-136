"""_448.py

CylindricalGearDesignAndRatingSettingsItem
"""


from mastapy.gears import _338, _309, _328
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.rating.cylindrical import (
    _480, _466, _476, _467,
    _470, _473, _474, _475,
    _479
)
from mastapy.gears.gear_designs.cylindrical import _1019
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials import _245
from mastapy.utility.units_and_measurements import _1572
from mastapy.utility.databases import _1792
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearDesignAndRatingSettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignAndRatingSettingsItem',)


class CylindricalGearDesignAndRatingSettingsItem(_1792.NamedDatabaseItem):
    """CylindricalGearDesignAndRatingSettingsItem

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_ITEM

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignAndRatingSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma_quality_grade_type(self) -> '_338.QualityGradeTypes':
        """QualityGradeTypes: 'AGMAQualityGradeType' is the original name of this property."""

        temp = self.wrapped.AGMAQualityGradeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_338.QualityGradeTypes)(value) if value is not None else None

    @agma_quality_grade_type.setter
    def agma_quality_grade_type(self, value: '_338.QualityGradeTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AGMAQualityGradeType = value

    @property
    def agma_stress_cycle_factor_influence_factor(self) -> 'float':
        """float: 'AGMAStressCycleFactorInfluenceFactor' is the original name of this property."""

        temp = self.wrapped.AGMAStressCycleFactorInfluenceFactor

        if temp is None:
            return 0.0

        return temp

    @agma_stress_cycle_factor_influence_factor.setter
    def agma_stress_cycle_factor_influence_factor(self, value: 'float'):
        self.wrapped.AGMAStressCycleFactorInfluenceFactor = float(value) if value else 0.0

    @property
    def agma_tolerances_standard(self) -> '_309.AGMAToleranceStandard':
        """AGMAToleranceStandard: 'AGMATolerancesStandard' is the original name of this property."""

        temp = self.wrapped.AGMATolerancesStandard

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_309.AGMAToleranceStandard)(value) if value is not None else None

    @agma_tolerances_standard.setter
    def agma_tolerances_standard(self, value: '_309.AGMAToleranceStandard'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AGMATolerancesStandard = value

    @property
    def allow_transverse_contact_ratio_less_than_one(self) -> 'bool':
        """bool: 'AllowTransverseContactRatioLessThanOne' is the original name of this property."""

        temp = self.wrapped.AllowTransverseContactRatioLessThanOne

        if temp is None:
            return False

        return temp

    @allow_transverse_contact_ratio_less_than_one.setter
    def allow_transverse_contact_ratio_less_than_one(self, value: 'bool'):
        self.wrapped.AllowTransverseContactRatioLessThanOne = bool(value) if value else False

    @property
    def always_use_chosen_tooth_thickness_for_bending_strength(self) -> 'bool':
        """bool: 'AlwaysUseChosenToothThicknessForBendingStrength' is the original name of this property."""

        temp = self.wrapped.AlwaysUseChosenToothThicknessForBendingStrength

        if temp is None:
            return False

        return temp

    @always_use_chosen_tooth_thickness_for_bending_strength.setter
    def always_use_chosen_tooth_thickness_for_bending_strength(self, value: 'bool'):
        self.wrapped.AlwaysUseChosenToothThicknessForBendingStrength = bool(value) if value else False

    @property
    def apply_application_and_dynamic_factor_by_default(self) -> 'bool':
        """bool: 'ApplyApplicationAndDynamicFactorByDefault' is the original name of this property."""

        temp = self.wrapped.ApplyApplicationAndDynamicFactorByDefault

        if temp is None:
            return False

        return temp

    @apply_application_and_dynamic_factor_by_default.setter
    def apply_application_and_dynamic_factor_by_default(self, value: 'bool'):
        self.wrapped.ApplyApplicationAndDynamicFactorByDefault = bool(value) if value else False

    @property
    def apply_work_hardening_factor_for_wrought_normalised_low_carbon_steel_and_cast_steel(self) -> 'bool':
        """bool: 'ApplyWorkHardeningFactorForWroughtNormalisedLowCarbonSteelAndCastSteel' is the original name of this property."""

        temp = self.wrapped.ApplyWorkHardeningFactorForWroughtNormalisedLowCarbonSteelAndCastSteel

        if temp is None:
            return False

        return temp

    @apply_work_hardening_factor_for_wrought_normalised_low_carbon_steel_and_cast_steel.setter
    def apply_work_hardening_factor_for_wrought_normalised_low_carbon_steel_and_cast_steel(self, value: 'bool'):
        self.wrapped.ApplyWorkHardeningFactorForWroughtNormalisedLowCarbonSteelAndCastSteel = bool(value) if value else False

    @property
    def chosen_tooth_thickness_for_bending_strength(self) -> '_480.ToothThicknesses':
        """ToothThicknesses: 'ChosenToothThicknessForBendingStrength' is the original name of this property."""

        temp = self.wrapped.ChosenToothThicknessForBendingStrength

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_480.ToothThicknesses)(value) if value is not None else None

    @chosen_tooth_thickness_for_bending_strength.setter
    def chosen_tooth_thickness_for_bending_strength(self, value: '_480.ToothThicknesses'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ChosenToothThicknessForBendingStrength = value

    @property
    def cylindrical_gear_profile_measurement(self) -> '_1019.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'CylindricalGearProfileMeasurement' is the original name of this property."""

        temp = self.wrapped.CylindricalGearProfileMeasurement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1019.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @cylindrical_gear_profile_measurement.setter
    def cylindrical_gear_profile_measurement(self, value: '_1019.CylindricalGearProfileMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CylindricalGearProfileMeasurement = value

    @property
    def dynamic_factor_method(self) -> '_466.DynamicFactorMethods':
        """DynamicFactorMethods: 'DynamicFactorMethod' is the original name of this property."""

        temp = self.wrapped.DynamicFactorMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_466.DynamicFactorMethods)(value) if value is not None else None

    @dynamic_factor_method.setter
    def dynamic_factor_method(self, value: '_466.DynamicFactorMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DynamicFactorMethod = value

    @property
    def enable_proportion_system_for_tip_alteration_coefficient(self) -> 'bool':
        """bool: 'EnableProportionSystemForTipAlterationCoefficient' is the original name of this property."""

        temp = self.wrapped.EnableProportionSystemForTipAlterationCoefficient

        if temp is None:
            return False

        return temp

    @enable_proportion_system_for_tip_alteration_coefficient.setter
    def enable_proportion_system_for_tip_alteration_coefficient(self, value: 'bool'):
        self.wrapped.EnableProportionSystemForTipAlterationCoefficient = bool(value) if value else False

    @property
    def film_thickness_equation_for_scuffing(self) -> '_476.ScuffingMethods':
        """ScuffingMethods: 'FilmThicknessEquationForScuffing' is the original name of this property."""

        temp = self.wrapped.FilmThicknessEquationForScuffing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_476.ScuffingMethods)(value) if value is not None else None

    @film_thickness_equation_for_scuffing.setter
    def film_thickness_equation_for_scuffing(self, value: '_476.ScuffingMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FilmThicknessEquationForScuffing = value

    @property
    def gear_blank_factor_calculation_option(self) -> '_467.GearBlankFactorCalculationOptions':
        """GearBlankFactorCalculationOptions: 'GearBlankFactorCalculationOption' is the original name of this property."""

        temp = self.wrapped.GearBlankFactorCalculationOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_467.GearBlankFactorCalculationOptions)(value) if value is not None else None

    @gear_blank_factor_calculation_option.setter
    def gear_blank_factor_calculation_option(self, value: '_467.GearBlankFactorCalculationOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.GearBlankFactorCalculationOption = value

    @property
    def iso_tolerances_standard(self) -> 'overridable.Overridable_ISOToleranceStandard':
        """overridable.Overridable_ISOToleranceStandard: 'ISOTolerancesStandard' is the original name of this property."""

        temp = self.wrapped.ISOTolerancesStandard

        if temp is None:
            return None

        value = overridable.Overridable_ISOToleranceStandard.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @iso_tolerances_standard.setter
    def iso_tolerances_standard(self, value: 'overridable.Overridable_ISOToleranceStandard.implicit_type()'):
        wrapper_type = overridable.Overridable_ISOToleranceStandard.wrapper_type()
        enclosed_type = overridable.Overridable_ISOToleranceStandard.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.ISOTolerancesStandard = value

    @property
    def include_rim_thickness_factor(self) -> 'bool':
        """bool: 'IncludeRimThicknessFactor' is the original name of this property."""

        temp = self.wrapped.IncludeRimThicknessFactor

        if temp is None:
            return False

        return temp

    @include_rim_thickness_factor.setter
    def include_rim_thickness_factor(self, value: 'bool'):
        self.wrapped.IncludeRimThicknessFactor = bool(value) if value else False

    @property
    def internal_gear_root_fillet_radius_is_always_equal_to_basic_rack_root_fillet_radius(self) -> 'bool':
        """bool: 'InternalGearRootFilletRadiusIsAlwaysEqualToBasicRackRootFilletRadius' is the original name of this property."""

        temp = self.wrapped.InternalGearRootFilletRadiusIsAlwaysEqualToBasicRackRootFilletRadius

        if temp is None:
            return False

        return temp

    @internal_gear_root_fillet_radius_is_always_equal_to_basic_rack_root_fillet_radius.setter
    def internal_gear_root_fillet_radius_is_always_equal_to_basic_rack_root_fillet_radius(self, value: 'bool'):
        self.wrapped.InternalGearRootFilletRadiusIsAlwaysEqualToBasicRackRootFilletRadius = bool(value) if value else False

    @property
    def is_scuffing_licensed_for_current_rating_method(self) -> 'bool':
        """bool: 'IsScuffingLicensedForCurrentRatingMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsScuffingLicensedForCurrentRatingMethod

        if temp is None:
            return False

        return temp

    @property
    def limit_dynamic_factor_if_not_in_main_resonance_range_by_default(self) -> 'bool':
        """bool: 'LimitDynamicFactorIfNotInMainResonanceRangeByDefault' is the original name of this property."""

        temp = self.wrapped.LimitDynamicFactorIfNotInMainResonanceRangeByDefault

        if temp is None:
            return False

        return temp

    @limit_dynamic_factor_if_not_in_main_resonance_range_by_default.setter
    def limit_dynamic_factor_if_not_in_main_resonance_range_by_default(self, value: 'bool'):
        self.wrapped.LimitDynamicFactorIfNotInMainResonanceRangeByDefault = bool(value) if value else False

    @property
    def limit_micro_geometry_factor_for_the_dynamic_load_by_default(self) -> 'bool':
        """bool: 'LimitMicroGeometryFactorForTheDynamicLoadByDefault' is the original name of this property."""

        temp = self.wrapped.LimitMicroGeometryFactorForTheDynamicLoadByDefault

        if temp is None:
            return False

        return temp

    @limit_micro_geometry_factor_for_the_dynamic_load_by_default.setter
    def limit_micro_geometry_factor_for_the_dynamic_load_by_default(self, value: 'bool'):
        self.wrapped.LimitMicroGeometryFactorForTheDynamicLoadByDefault = bool(value) if value else False

    @property
    def mean_coefficient_of_friction_flash_temperature_method(self) -> 'float':
        """float: 'MeanCoefficientOfFrictionFlashTemperatureMethod' is the original name of this property."""

        temp = self.wrapped.MeanCoefficientOfFrictionFlashTemperatureMethod

        if temp is None:
            return 0.0

        return temp

    @mean_coefficient_of_friction_flash_temperature_method.setter
    def mean_coefficient_of_friction_flash_temperature_method(self, value: 'float'):
        self.wrapped.MeanCoefficientOfFrictionFlashTemperatureMethod = float(value) if value else 0.0

    @property
    def micropitting_rating_method(self) -> '_470.MicropittingRatingMethod':
        """MicropittingRatingMethod: 'MicropittingRatingMethod' is the original name of this property."""

        temp = self.wrapped.MicropittingRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_470.MicropittingRatingMethod)(value) if value is not None else None

    @micropitting_rating_method.setter
    def micropitting_rating_method(self, value: '_470.MicropittingRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MicropittingRatingMethod = value

    @property
    def number_of_load_strips_for_basic_ltca(self) -> 'int':
        """int: 'NumberOfLoadStripsForBasicLTCA' is the original name of this property."""

        temp = self.wrapped.NumberOfLoadStripsForBasicLTCA

        if temp is None:
            return 0

        return temp

    @number_of_load_strips_for_basic_ltca.setter
    def number_of_load_strips_for_basic_ltca(self, value: 'int'):
        self.wrapped.NumberOfLoadStripsForBasicLTCA = int(value) if value else 0

    @property
    def number_of_points_along_profile_for_micropitting_calculation(self) -> 'int':
        """int: 'NumberOfPointsAlongProfileForMicropittingCalculation' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsAlongProfileForMicropittingCalculation

        if temp is None:
            return 0

        return temp

    @number_of_points_along_profile_for_micropitting_calculation.setter
    def number_of_points_along_profile_for_micropitting_calculation(self, value: 'int'):
        self.wrapped.NumberOfPointsAlongProfileForMicropittingCalculation = int(value) if value else 0

    @property
    def number_of_points_along_profile_for_scuffing_calculation(self) -> 'int':
        """int: 'NumberOfPointsAlongProfileForScuffingCalculation' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsAlongProfileForScuffingCalculation

        if temp is None:
            return 0

        return temp

    @number_of_points_along_profile_for_scuffing_calculation.setter
    def number_of_points_along_profile_for_scuffing_calculation(self, value: 'int'):
        self.wrapped.NumberOfPointsAlongProfileForScuffingCalculation = int(value) if value else 0

    @property
    def number_of_points_along_profile_for_tooth_flank_fracture_calculation(self) -> 'int':
        """int: 'NumberOfPointsAlongProfileForToothFlankFractureCalculation' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsAlongProfileForToothFlankFractureCalculation

        if temp is None:
            return 0

        return temp

    @number_of_points_along_profile_for_tooth_flank_fracture_calculation.setter
    def number_of_points_along_profile_for_tooth_flank_fracture_calculation(self, value: 'int'):
        self.wrapped.NumberOfPointsAlongProfileForToothFlankFractureCalculation = int(value) if value else 0

    @property
    def number_of_rotations_for_basic_ltca(self) -> 'int':
        """int: 'NumberOfRotationsForBasicLTCA' is the original name of this property."""

        temp = self.wrapped.NumberOfRotationsForBasicLTCA

        if temp is None:
            return 0

        return temp

    @number_of_rotations_for_basic_ltca.setter
    def number_of_rotations_for_basic_ltca(self, value: 'int'):
        self.wrapped.NumberOfRotationsForBasicLTCA = int(value) if value else 0

    @property
    def permissible_bending_stress_method(self) -> '_473.RatingMethod':
        """RatingMethod: 'PermissibleBendingStressMethod' is the original name of this property."""

        temp = self.wrapped.PermissibleBendingStressMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_473.RatingMethod)(value) if value is not None else None

    @permissible_bending_stress_method.setter
    def permissible_bending_stress_method(self, value: '_473.RatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PermissibleBendingStressMethod = value

    @property
    def rating_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods':
        """enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods: 'RatingMethod' is the original name of this property."""

        temp = self.wrapped.RatingMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @rating_method.setter
    def rating_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalGearRatingMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RatingMethod = value

    @property
    def scuffing_rating_method_flash_temperature_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod':
        """enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod: 'ScuffingRatingMethodFlashTemperatureMethod' is the original name of this property."""

        temp = self.wrapped.ScuffingRatingMethodFlashTemperatureMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @scuffing_rating_method_flash_temperature_method.setter
    def scuffing_rating_method_flash_temperature_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ScuffingRatingMethodFlashTemperatureMethod = value

    @property
    def scuffing_rating_method_integral_temperature_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod':
        """enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod: 'ScuffingRatingMethodIntegralTemperatureMethod' is the original name of this property."""

        temp = self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @scuffing_rating_method_integral_temperature_method.setter
    def scuffing_rating_method_integral_temperature_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod = value

    @property
    def show_rating_settings_in_report(self) -> 'bool':
        """bool: 'ShowRatingSettingsInReport' is the original name of this property."""

        temp = self.wrapped.ShowRatingSettingsInReport

        if temp is None:
            return False

        return temp

    @show_rating_settings_in_report.setter
    def show_rating_settings_in_report(self, value: 'bool'):
        self.wrapped.ShowRatingSettingsInReport = bool(value) if value else False

    @property
    def show_vdi_rating_when_available(self) -> 'bool':
        """bool: 'ShowVDIRatingWhenAvailable' is the original name of this property."""

        temp = self.wrapped.ShowVDIRatingWhenAvailable

        if temp is None:
            return False

        return temp

    @show_vdi_rating_when_available.setter
    def show_vdi_rating_when_available(self, value: 'bool'):
        self.wrapped.ShowVDIRatingWhenAvailable = bool(value) if value else False

    @property
    def tip_relief_in_scuffing_calculation(self) -> '_479.TipReliefScuffingOptions':
        """TipReliefScuffingOptions: 'TipReliefInScuffingCalculation' is the original name of this property."""

        temp = self.wrapped.TipReliefInScuffingCalculation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_479.TipReliefScuffingOptions)(value) if value is not None else None

    @tip_relief_in_scuffing_calculation.setter
    def tip_relief_in_scuffing_calculation(self, value: '_479.TipReliefScuffingOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.TipReliefInScuffingCalculation = value

    @property
    def tolerance_rounding_system(self) -> '_1572.MeasurementSystem':
        """MeasurementSystem: 'ToleranceRoundingSystem' is the original name of this property."""

        temp = self.wrapped.ToleranceRoundingSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1572.MeasurementSystem)(value) if value is not None else None

    @tolerance_rounding_system.setter
    def tolerance_rounding_system(self, value: '_1572.MeasurementSystem'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ToleranceRoundingSystem = value

    @property
    def use_10_for_contact_ratio_factor_contact_for_spur_gears_with_contact_ratio_less_than_20(self) -> 'bool':
        """bool: 'Use10ForContactRatioFactorContactForSpurGearsWithContactRatioLessThan20' is the original name of this property."""

        temp = self.wrapped.Use10ForContactRatioFactorContactForSpurGearsWithContactRatioLessThan20

        if temp is None:
            return False

        return temp

    @use_10_for_contact_ratio_factor_contact_for_spur_gears_with_contact_ratio_less_than_20.setter
    def use_10_for_contact_ratio_factor_contact_for_spur_gears_with_contact_ratio_less_than_20(self, value: 'bool'):
        self.wrapped.Use10ForContactRatioFactorContactForSpurGearsWithContactRatioLessThan20 = bool(value) if value else False

    @property
    def use_diametral_pitch(self) -> 'bool':
        """bool: 'UseDiametralPitch' is the original name of this property."""

        temp = self.wrapped.UseDiametralPitch

        if temp is None:
            return False

        return temp

    @use_diametral_pitch.setter
    def use_diametral_pitch(self, value: 'bool'):
        self.wrapped.UseDiametralPitch = bool(value) if value else False

    @property
    def use_interpolated_single_pair_tooth_contact_factor_for_hcr_helical_gears(self) -> 'bool':
        """bool: 'UseInterpolatedSinglePairToothContactFactorForHCRHelicalGears' is the original name of this property."""

        temp = self.wrapped.UseInterpolatedSinglePairToothContactFactorForHCRHelicalGears

        if temp is None:
            return False

        return temp

    @use_interpolated_single_pair_tooth_contact_factor_for_hcr_helical_gears.setter
    def use_interpolated_single_pair_tooth_contact_factor_for_hcr_helical_gears(self, value: 'bool'):
        self.wrapped.UseInterpolatedSinglePairToothContactFactorForHCRHelicalGears = bool(value) if value else False

    @property
    def use_ltca_stresses_in_gear_rating(self) -> 'bool':
        """bool: 'UseLTCAStressesInGearRating' is the original name of this property."""

        temp = self.wrapped.UseLTCAStressesInGearRating

        if temp is None:
            return False

        return temp

    @use_ltca_stresses_in_gear_rating.setter
    def use_ltca_stresses_in_gear_rating(self, value: 'bool'):
        self.wrapped.UseLTCAStressesInGearRating = bool(value) if value else False

    @property
    def use_point_of_highest_stress_to_calculate_face_load_factor(self) -> 'bool':
        """bool: 'UsePointOfHighestStressToCalculateFaceLoadFactor' is the original name of this property."""

        temp = self.wrapped.UsePointOfHighestStressToCalculateFaceLoadFactor

        if temp is None:
            return False

        return temp

    @use_point_of_highest_stress_to_calculate_face_load_factor.setter
    def use_point_of_highest_stress_to_calculate_face_load_factor(self, value: 'bool'):
        self.wrapped.UsePointOfHighestStressToCalculateFaceLoadFactor = bool(value) if value else False

    @property
    def vdi_rating_geometry_calculation_method(self) -> 'overridable.Overridable_CylindricalGearRatingMethods':
        """overridable.Overridable_CylindricalGearRatingMethods: 'VDIRatingGeometryCalculationMethod' is the original name of this property."""

        temp = self.wrapped.VDIRatingGeometryCalculationMethod

        if temp is None:
            return None

        value = overridable.Overridable_CylindricalGearRatingMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @vdi_rating_geometry_calculation_method.setter
    def vdi_rating_geometry_calculation_method(self, value: 'overridable.Overridable_CylindricalGearRatingMethods.implicit_type()'):
        wrapper_type = overridable.Overridable_CylindricalGearRatingMethods.wrapper_type()
        enclosed_type = overridable.Overridable_CylindricalGearRatingMethods.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.VDIRatingGeometryCalculationMethod = value
