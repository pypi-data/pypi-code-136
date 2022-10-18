"""_2392.py

Bearing
"""


from typing import List, Optional

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.tolerances import (
    _1864, _1865, _1874, _1868,
    _1881, _1867, _1878, _1873,
    _1883, _1885
)
from mastapy.bearings import (
    _1834, _1847, _1838, _1830
)
from mastapy.materials.efficiency import _286
from mastapy.utility.report import _1751
from mastapy._internal.python_net import python_net_import
from mastapy.bearings.bearing_results import _1920, _1903, _1921
from mastapy.system_model.part_model import (
    _2391, _2425, _2393, _2397,
    _2399
)
from mastapy.bearings.bearing_designs import (
    _2085, _2086, _2087, _2088,
    _2089
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs.rolling import (
    _2090, _2091, _2092, _2093,
    _2094, _2095, _2097, _2103,
    _2104, _2105, _2109, _2114,
    _2115, _2116, _2117, _2120,
    _2121, _2124, _2125, _2126,
    _2127, _2128, _2129
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _2142, _2144, _2146, _2148,
    _2149, _2150
)
from mastapy.bearings.bearing_designs.concept import _2152, _2153, _2154
from mastapy.math_utility.measured_vectors import _1528
from mastapy.bearings.bearing_results.rolling import _2026
from mastapy.materials import _261
from mastapy.system_model.part_model.shaft_model import _2434

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ARRAY = python_net_import('System', 'Array')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')


__docformat__ = 'restructuredtext en'
__all__ = ('Bearing',)


class Bearing(_2399.Connector):
    """Bearing

    This is a mastapy class.
    """

    TYPE = _BEARING

    def __init__(self, instance_to_wrap: 'Bearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_displacement_preload(self) -> 'float':
        """float: 'AxialDisplacementPreload' is the original name of this property."""

        temp = self.wrapped.AxialDisplacementPreload

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    def axial_displacement_preload(self, value: 'float'):
        self.wrapped.AxialDisplacementPreload = float(value) if value else 0.0

    @property
    def axial_force_preload(self) -> 'float':
        """float: 'AxialForcePreload' is the original name of this property."""

        temp = self.wrapped.AxialForcePreload

        if temp is None:
            return 0.0

        return temp

    @axial_force_preload.setter
    def axial_force_preload(self, value: 'float'):
        self.wrapped.AxialForcePreload = float(value) if value else 0.0

    @property
    def axial_internal_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AxialInternalClearance' is the original name of this property."""

        temp = self.wrapped.AxialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @axial_internal_clearance.setter
    def axial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AxialInternalClearance = value

    @property
    def axial_stiffness_at_mounting_points(self) -> 'float':
        """float: 'AxialStiffnessAtMountingPoints' is the original name of this property."""

        temp = self.wrapped.AxialStiffnessAtMountingPoints

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness_at_mounting_points.setter
    def axial_stiffness_at_mounting_points(self, value: 'float'):
        self.wrapped.AxialStiffnessAtMountingPoints = float(value) if value else 0.0

    @property
    def bearing_life_adjustment_factor_for_operating_conditions(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BearingLifeAdjustmentFactorForOperatingConditions' is the original name of this property."""

        temp = self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @bearing_life_adjustment_factor_for_operating_conditions.setter
    def bearing_life_adjustment_factor_for_operating_conditions(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions = value

    @property
    def bearing_life_adjustment_factor_for_special_bearing_properties(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BearingLifeAdjustmentFactorForSpecialBearingProperties' is the original name of this property."""

        temp = self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @bearing_life_adjustment_factor_for_special_bearing_properties.setter
    def bearing_life_adjustment_factor_for_special_bearing_properties(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties = value

    @property
    def bearing_life_modification_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BearingLifeModificationFactor' is the original name of this property."""

        temp = self.wrapped.BearingLifeModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @bearing_life_modification_factor.setter
    def bearing_life_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BearingLifeModificationFactor = value

    @property
    def bearing_tolerance_class(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass':
        """enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass: 'BearingToleranceClass' is the original name of this property."""

        temp = self.wrapped.BearingToleranceClass

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @bearing_tolerance_class.setter
    def bearing_tolerance_class(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingToleranceClass = value

    @property
    def bearing_tolerance_definition(self) -> '_1865.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'BearingToleranceDefinition' is the original name of this property."""

        temp = self.wrapped.BearingToleranceDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1865.BearingToleranceDefinitionOptions)(value) if value is not None else None

    @bearing_tolerance_definition.setter
    def bearing_tolerance_definition(self, value: '_1865.BearingToleranceDefinitionOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BearingToleranceDefinition = value

    @property
    def coefficient_of_friction(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CoefficientOfFriction' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CoefficientOfFriction = value

    @property
    def damping_options(self) -> '_1834.BearingDampingMatrixOption':
        """BearingDampingMatrixOption: 'DampingOptions' is the original name of this property."""

        temp = self.wrapped.DampingOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1834.BearingDampingMatrixOption)(value) if value is not None else None

    @damping_options.setter
    def damping_options(self, value: '_1834.BearingDampingMatrixOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DampingOptions = value

    @property
    def diameter_of_contact_on_inner_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'DiameterOfContactOnInnerRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnInnerRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_of_contact_on_left_race(self) -> 'float':
        """float: 'DiameterOfContactOnLeftRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnLeftRace

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_of_contact_on_outer_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'DiameterOfContactOnOuterRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnOuterRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def diameter_of_contact_on_right_race(self) -> 'float':
        """float: 'DiameterOfContactOnRightRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnRightRace

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(self) -> 'float':
        """float: 'DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection

        if temp is None:
            return 0.0

        return temp

    @property
    def difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(self) -> 'float':
        """float: 'DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency_rating_method(self) -> 'overridable.Overridable_BearingEfficiencyRatingMethod':
        """overridable.Overridable_BearingEfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = overridable.Overridable_BearingEfficiencyRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: 'overridable.Overridable_BearingEfficiencyRatingMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_BearingEfficiencyRatingMethod.wrapper_type()
        enclosed_type = overridable.Overridable_BearingEfficiencyRatingMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def first_element_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FirstElementAngle' is the original name of this property."""

        temp = self.wrapped.FirstElementAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @first_element_angle.setter
    def first_element_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FirstElementAngle = value

    @property
    def has_radial_mounting_clearance(self) -> 'bool':
        """bool: 'HasRadialMountingClearance' is the original name of this property."""

        temp = self.wrapped.HasRadialMountingClearance

        if temp is None:
            return False

        return temp

    @has_radial_mounting_clearance.setter
    def has_radial_mounting_clearance(self, value: 'bool'):
        self.wrapped.HasRadialMountingClearance = bool(value) if value else False

    @property
    def inner_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @inner_diameter.setter
    def inner_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerDiameter = value

    @property
    def inner_fitting_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'InnerFittingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerFittingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_node_position_from_centre(self) -> 'float':
        """float: 'InnerNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def is_internal_clearance_adjusted_after_fitting(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'IsInternalClearanceAdjustedAfterFitting' is the original name of this property."""

        temp = self.wrapped.IsInternalClearanceAdjustedAfterFitting

        if temp is None:
            return False

        return constructor.new_from_mastapy_type(overridable.Overridable_bool)(temp) if temp is not None else False

    @is_internal_clearance_adjusted_after_fitting.setter
    def is_internal_clearance_adjusted_after_fitting(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.IsInternalClearanceAdjustedAfterFitting = value

    @property
    def journal_bearing_type(self) -> '_1847.JournalBearingType':
        """JournalBearingType: 'JournalBearingType' is the original name of this property."""

        temp = self.wrapped.JournalBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1847.JournalBearingType)(value) if value is not None else None

    @journal_bearing_type.setter
    def journal_bearing_type(self, value: '_1847.JournalBearingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.JournalBearingType = value

    @property
    def left_node_position_from_centre(self) -> 'float':
        """float: 'LeftNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def lubrication_detail(self) -> 'str':
        """str: 'LubricationDetail' is the original name of this property."""

        temp = self.wrapped.LubricationDetail.SelectedItemName

        if temp is None:
            return ''

        return temp

    @lubrication_detail.setter
    def lubrication_detail(self, value: 'str'):
        self.wrapped.LubricationDetail.SetSelectedItem(str(value) if value else '')

    @property
    def maximum_bearing_life_modification_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumBearingLifeModificationFactor' is the original name of this property."""

        temp = self.wrapped.MaximumBearingLifeModificationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_bearing_life_modification_factor.setter
    def maximum_bearing_life_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumBearingLifeModificationFactor = value

    @property
    def model(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingModel':
        """enum_with_selected_value.EnumWithSelectedValue_BearingModel: 'Model' is the original name of this property."""

        temp = self.wrapped.Model

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BearingModel.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @model.setter
    def model(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Model = value

    @property
    def offset_of_contact_on_inner_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'OffsetOfContactOnInnerRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnInnerRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_of_contact_on_left_race(self) -> 'float':
        """float: 'OffsetOfContactOnLeftRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnLeftRace

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_of_contact_on_outer_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'OffsetOfContactOnOuterRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnOuterRaceAtNominalContactAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def offset_of_contact_on_right_race(self) -> 'float':
        """float: 'OffsetOfContactOnRightRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnRightRace

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self) -> '_1920.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1920.Orientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1920.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def outer_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @outer_diameter.setter
    def outer_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterDiameter = value

    @property
    def outer_fitting_chart(self) -> '_1751.SimpleChartDefinition':
        """SimpleChartDefinition: 'OuterFittingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterFittingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_node_position_from_centre(self) -> 'float':
        """float: 'OuterNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def override_design_lubrication_detail(self) -> 'bool':
        """bool: 'OverrideDesignLubricationDetail' is the original name of this property."""

        temp = self.wrapped.OverrideDesignLubricationDetail

        if temp is None:
            return False

        return temp

    @override_design_lubrication_detail.setter
    def override_design_lubrication_detail(self, value: 'bool'):
        self.wrapped.OverrideDesignLubricationDetail = bool(value) if value else False

    @property
    def percentage_difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(self) -> 'float':
        """float: 'PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection

        if temp is None:
            return 0.0

        return temp

    @property
    def percentage_difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(self) -> 'float':
        """float: 'PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_load_calculation_method(self) -> 'overridable.Overridable_CylindricalRollerMaxAxialLoadMethod':
        """overridable.Overridable_CylindricalRollerMaxAxialLoadMethod: 'PermissibleAxialLoadCalculationMethod' is the original name of this property."""

        temp = self.wrapped.PermissibleAxialLoadCalculationMethod

        if temp is None:
            return None

        value = overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @permissible_axial_load_calculation_method.setter
    def permissible_axial_load_calculation_method(self, value: 'overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapper_type()
        enclosed_type = overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.PermissibleAxialLoadCalculationMethod = value

    @property
    def permissible_track_truncation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PermissibleTrackTruncation' is the original name of this property."""

        temp = self.wrapped.PermissibleTrackTruncation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @permissible_track_truncation.setter
    def permissible_track_truncation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PermissibleTrackTruncation = value

    @property
    def preload(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PreloadType':
        """enum_with_selected_value.EnumWithSelectedValue_PreloadType: 'Preload' is the original name of this property."""

        temp = self.wrapped.Preload

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_PreloadType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @preload.setter
    def preload(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Preload = value

    @property
    def preload_spring_initial_compression(self) -> 'float':
        """float: 'PreloadSpringInitialCompression' is the original name of this property."""

        temp = self.wrapped.PreloadSpringInitialCompression

        if temp is None:
            return 0.0

        return temp

    @preload_spring_initial_compression.setter
    def preload_spring_initial_compression(self, value: 'float'):
        self.wrapped.PreloadSpringInitialCompression = float(value) if value else 0.0

    @property
    def preload_spring_max_travel(self) -> 'float':
        """float: 'PreloadSpringMaxTravel' is the original name of this property."""

        temp = self.wrapped.PreloadSpringMaxTravel

        if temp is None:
            return 0.0

        return temp

    @preload_spring_max_travel.setter
    def preload_spring_max_travel(self, value: 'float'):
        self.wrapped.PreloadSpringMaxTravel = float(value) if value else 0.0

    @property
    def preload_spring_stiffness(self) -> 'float':
        """float: 'PreloadSpringStiffness' is the original name of this property."""

        temp = self.wrapped.PreloadSpringStiffness

        if temp is None:
            return 0.0

        return temp

    @preload_spring_stiffness.setter
    def preload_spring_stiffness(self, value: 'float'):
        self.wrapped.PreloadSpringStiffness = float(value) if value else 0.0

    @property
    def preload_spring_on_outer(self) -> 'bool':
        """bool: 'PreloadSpringOnOuter' is the original name of this property."""

        temp = self.wrapped.PreloadSpringOnOuter

        if temp is None:
            return False

        return temp

    @preload_spring_on_outer.setter
    def preload_spring_on_outer(self, value: 'bool'):
        self.wrapped.PreloadSpringOnOuter = bool(value) if value else False

    @property
    def preload_is_from_left(self) -> 'bool':
        """bool: 'PreloadIsFromLeft' is the original name of this property."""

        temp = self.wrapped.PreloadIsFromLeft

        if temp is None:
            return False

        return temp

    @preload_is_from_left.setter
    def preload_is_from_left(self, value: 'bool'):
        self.wrapped.PreloadIsFromLeft = bool(value) if value else False

    @property
    def radial_internal_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialInternalClearance' is the original name of this property."""

        temp = self.wrapped.RadialInternalClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @radial_internal_clearance.setter
    def radial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialInternalClearance = value

    @property
    def right_node_position_from_centre(self) -> 'float':
        """float: 'RightNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightNodePositionFromCentre

        if temp is None:
            return 0.0

        return temp

    @property
    def use_design_iso14179_settings(self) -> 'bool':
        """bool: 'UseDesignISO14179Settings' is the original name of this property."""

        temp = self.wrapped.UseDesignISO14179Settings

        if temp is None:
            return False

        return temp

    @use_design_iso14179_settings.setter
    def use_design_iso14179_settings(self, value: 'bool'):
        self.wrapped.UseDesignISO14179Settings = bool(value) if value else False

    @property
    def axial_internal_clearance_tolerance(self) -> '_2391.AxialInternalClearanceTolerance':
        """AxialInternalClearanceTolerance: 'AxialInternalClearanceTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialInternalClearanceTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail(self) -> '_2085.BearingDesign':
        """BearingDesign: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2085.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_detailed_bearing(self) -> '_2086.DetailedBearing':
        """DetailedBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2086.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_dummy_rolling_bearing(self) -> '_2087.DummyRollingBearing':
        """DummyRollingBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2087.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_linear_bearing(self) -> '_2088.LinearBearing':
        """LinearBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2088.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_non_linear_bearing(self) -> '_2089.NonLinearBearing':
        """NonLinearBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2089.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_angular_contact_ball_bearing(self) -> '_2090.AngularContactBallBearing':
        """AngularContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2090.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_angular_contact_thrust_ball_bearing(self) -> '_2091.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2091.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_asymmetric_spherical_roller_bearing(self) -> '_2092.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2092.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2093.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2093.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_axial_thrust_needle_roller_bearing(self) -> '_2094.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2094.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_ball_bearing(self) -> '_2095.BallBearing':
        """BallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2095.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_barrel_roller_bearing(self) -> '_2097.BarrelRollerBearing':
        """BarrelRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2097.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_crossed_roller_bearing(self) -> '_2103.CrossedRollerBearing':
        """CrossedRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2103.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_cylindrical_roller_bearing(self) -> '_2104.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2104.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_deep_groove_ball_bearing(self) -> '_2105.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2105.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_four_point_contact_ball_bearing(self) -> '_2109.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2109.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_multi_point_contact_ball_bearing(self) -> '_2114.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2114.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_needle_roller_bearing(self) -> '_2115.NeedleRollerBearing':
        """NeedleRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2115.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_non_barrel_roller_bearing(self) -> '_2116.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2116.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_roller_bearing(self) -> '_2117.RollerBearing':
        """RollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2117.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_rolling_bearing(self) -> '_2120.RollingBearing':
        """RollingBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2120.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_self_aligning_ball_bearing(self) -> '_2121.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2121.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_spherical_roller_bearing(self) -> '_2124.SphericalRollerBearing':
        """SphericalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2124.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_spherical_roller_thrust_bearing(self) -> '_2125.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2125.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_taper_roller_bearing(self) -> '_2126.TaperRollerBearing':
        """TaperRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2126.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_three_point_contact_ball_bearing(self) -> '_2127.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2127.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_thrust_ball_bearing(self) -> '_2128.ThrustBallBearing':
        """ThrustBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2128.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_toroidal_roller_bearing(self) -> '_2129.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2129.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_pad_fluid_film_bearing(self) -> '_2142.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2142.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_plain_grease_filled_journal_bearing(self) -> '_2144.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2144.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_plain_journal_bearing(self) -> '_2146.PlainJournalBearing':
        """PlainJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2146.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_plain_oil_fed_journal_bearing(self) -> '_2148.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2148.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_tilting_pad_journal_bearing(self) -> '_2149.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2149.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_tilting_pad_thrust_bearing(self) -> '_2150.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2150.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_concept_axial_clearance_bearing(self) -> '_2152.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2152.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_concept_clearance_bearing(self) -> '_2153.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2153.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_concept_radial_clearance_bearing(self) -> '_2154.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail

        if temp is None:
            return None

        if _2154.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_at_zero_displacement(self) -> '_1528.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceAtZeroDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceAtZeroDisplacement

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def friction_coefficients(self) -> '_2026.RollingBearingFrictionCoefficients':
        """RollingBearingFrictionCoefficients: 'FrictionCoefficients' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionCoefficients

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_mounting_sleeve_bore_tolerance(self) -> '_1874.OuterSupportTolerance':
        """OuterSupportTolerance: 'InnerMountingSleeveBoreTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerMountingSleeveBoreTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_mounting_sleeve_outer_diameter_tolerance(self) -> '_1868.InnerSupportTolerance':
        """InnerSupportTolerance: 'InnerMountingSleeveOuterDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerMountingSleeveOuterDiameterTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_support_detail(self) -> '_1881.SupportDetail':
        """SupportDetail: 'InnerSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_support_detail(self) -> '_1881.SupportDetail':
        """SupportDetail: 'LeftSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_mounting_sleeve_bore_tolerance(self) -> '_1874.OuterSupportTolerance':
        """OuterSupportTolerance: 'OuterMountingSleeveBoreTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterMountingSleeveBoreTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_mounting_sleeve_outer_diameter_tolerance(self) -> '_1868.InnerSupportTolerance':
        """InnerSupportTolerance: 'OuterMountingSleeveOuterDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterMountingSleeveOuterDiameterTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_support_detail(self) -> '_1881.SupportDetail':
        """SupportDetail: 'OuterSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_lubrication_detail(self) -> '_261.LubricationDetail':
        """LubricationDetail: 'OverriddenLubricationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenLubricationDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_internal_clearance_tolerance(self) -> '_2425.RadialInternalClearanceTolerance':
        """RadialInternalClearanceTolerance: 'RadialInternalClearanceTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialInternalClearanceTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_support_detail(self) -> '_1881.SupportDetail':
        """SupportDetail: 'RightSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightSupportDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_inner(self) -> '_1867.InnerRingTolerance':
        """InnerRingTolerance: 'RingToleranceInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_left(self) -> '_1878.RingTolerance':
        """RingTolerance: 'RingToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceLeft

        if temp is None:
            return None

        if _1878.RingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_left to RingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_left_of_type_inner_ring_tolerance(self) -> '_1867.InnerRingTolerance':
        """InnerRingTolerance: 'RingToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceLeft

        if temp is None:
            return None

        if _1867.InnerRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_left to InnerRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_left_of_type_outer_ring_tolerance(self) -> '_1873.OuterRingTolerance':
        """OuterRingTolerance: 'RingToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceLeft

        if temp is None:
            return None

        if _1873.OuterRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_left to OuterRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_outer(self) -> '_1873.OuterRingTolerance':
        """OuterRingTolerance: 'RingToleranceOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_right(self) -> '_1878.RingTolerance':
        """RingTolerance: 'RingToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceRight

        if temp is None:
            return None

        if _1878.RingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_right to RingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_right_of_type_inner_ring_tolerance(self) -> '_1867.InnerRingTolerance':
        """InnerRingTolerance: 'RingToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceRight

        if temp is None:
            return None

        if _1867.InnerRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_right to InnerRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_right_of_type_outer_ring_tolerance(self) -> '_1873.OuterRingTolerance':
        """OuterRingTolerance: 'RingToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceRight

        if temp is None:
            return None

        if _1873.OuterRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_right to OuterRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property(self) -> '_2085.BearingDesign':
        """BearingDesign: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2085.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_detailed_bearing(self) -> '_2086.DetailedBearing':
        """DetailedBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2086.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_dummy_rolling_bearing(self) -> '_2087.DummyRollingBearing':
        """DummyRollingBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2087.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_linear_bearing(self) -> '_2088.LinearBearing':
        """LinearBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2088.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_non_linear_bearing(self) -> '_2089.NonLinearBearing':
        """NonLinearBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2089.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_angular_contact_ball_bearing(self) -> '_2090.AngularContactBallBearing':
        """AngularContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2090.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_angular_contact_thrust_ball_bearing(self) -> '_2091.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2091.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_asymmetric_spherical_roller_bearing(self) -> '_2092.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2092.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2093.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2093.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_axial_thrust_needle_roller_bearing(self) -> '_2094.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2094.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_ball_bearing(self) -> '_2095.BallBearing':
        """BallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2095.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_barrel_roller_bearing(self) -> '_2097.BarrelRollerBearing':
        """BarrelRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2097.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_crossed_roller_bearing(self) -> '_2103.CrossedRollerBearing':
        """CrossedRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2103.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_cylindrical_roller_bearing(self) -> '_2104.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2104.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_deep_groove_ball_bearing(self) -> '_2105.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2105.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_four_point_contact_ball_bearing(self) -> '_2109.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2109.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_multi_point_contact_ball_bearing(self) -> '_2114.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2114.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_needle_roller_bearing(self) -> '_2115.NeedleRollerBearing':
        """NeedleRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2115.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_non_barrel_roller_bearing(self) -> '_2116.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2116.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_roller_bearing(self) -> '_2117.RollerBearing':
        """RollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2117.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_rolling_bearing(self) -> '_2120.RollingBearing':
        """RollingBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2120.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_self_aligning_ball_bearing(self) -> '_2121.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2121.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_spherical_roller_bearing(self) -> '_2124.SphericalRollerBearing':
        """SphericalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2124.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_spherical_roller_thrust_bearing(self) -> '_2125.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2125.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_taper_roller_bearing(self) -> '_2126.TaperRollerBearing':
        """TaperRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2126.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_three_point_contact_ball_bearing(self) -> '_2127.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2127.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_thrust_ball_bearing(self) -> '_2128.ThrustBallBearing':
        """ThrustBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2128.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_toroidal_roller_bearing(self) -> '_2129.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2129.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_pad_fluid_film_bearing(self) -> '_2142.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2142.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_plain_grease_filled_journal_bearing(self) -> '_2144.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2144.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_plain_journal_bearing(self) -> '_2146.PlainJournalBearing':
        """PlainJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2146.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_plain_oil_fed_journal_bearing(self) -> '_2148.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2148.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_tilting_pad_journal_bearing(self) -> '_2149.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2149.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_tilting_pad_thrust_bearing(self) -> '_2150.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2150.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_concept_axial_clearance_bearing(self) -> '_2152.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2152.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_concept_clearance_bearing(self) -> '_2153.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2153.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_concept_radial_clearance_bearing(self) -> '_2154.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty

        if temp is None:
            return None

        if _2154.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_inner(self) -> '_1868.InnerSupportTolerance':
        """InnerSupportTolerance: 'SupportToleranceInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_left(self) -> '_1883.SupportTolerance':
        """SupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceLeft

        if temp is None:
            return None

        if _1883.SupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to SupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_left_of_type_inner_support_tolerance(self) -> '_1868.InnerSupportTolerance':
        """InnerSupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceLeft

        if temp is None:
            return None

        if _1868.InnerSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to InnerSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_left_of_type_outer_support_tolerance(self) -> '_1874.OuterSupportTolerance':
        """OuterSupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceLeft

        if temp is None:
            return None

        if _1874.OuterSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to OuterSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_outer(self) -> '_1874.OuterSupportTolerance':
        """OuterSupportTolerance: 'SupportToleranceOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_right(self) -> '_1883.SupportTolerance':
        """SupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceRight

        if temp is None:
            return None

        if _1883.SupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to SupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_right_of_type_inner_support_tolerance(self) -> '_1868.InnerSupportTolerance':
        """InnerSupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceRight

        if temp is None:
            return None

        if _1868.InnerSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to InnerSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_right_of_type_outer_support_tolerance(self) -> '_1874.OuterSupportTolerance':
        """OuterSupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceRight

        if temp is None:
            return None

        if _1874.OuterSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to OuterSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mounting(self) -> 'List[_2393.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'Mounting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mounting

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tolerance_combinations(self) -> 'List[_1885.ToleranceCombination]':
        """List[ToleranceCombination]: 'ToleranceCombinations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToleranceCombinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def is_radial_bearing(self) -> 'bool':
        """bool: 'IsRadialBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsRadialBearing

        if temp is None:
            return False

        return temp

    @property
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(self) -> 'List[List[float]]':
        """List[List[float]]: 'SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem' is the original name of this property."""

        temp = self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)
        return value

    @specified_stiffness_for_linear_bearing_in_local_coordinate_system.setter
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(self, value: 'List[List[float]]'):
        value = value if value else None
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem = value

    def set_detail_from_catalogue(self, catalogue: '_1830.BearingCatalog', designation: 'str'):
        """ 'SetDetailFromCatalogue' is the original name of this method.

        Args:
            catalogue (mastapy.bearings.BearingCatalog)
            designation (str)
        """

        catalogue = conversion.mp_to_pn_enum(catalogue)
        designation = str(designation)
        self.wrapped.SetDetailFromCatalogue(catalogue, designation if designation else '')

    def try_attach_left_side_to(self, shaft: '_2434.Shaft', offset: Optional['float'] = float('nan')) -> '_2397.ComponentsConnectedResult':
        """ 'TryAttachLeftSideTo' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryAttachLeftSideTo(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_attach_right_side_to(self, shaft: '_2434.Shaft', offset: Optional['float'] = float('nan')) -> '_2397.ComponentsConnectedResult':
        """ 'TryAttachRightSideTo' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryAttachRightSideTo(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
