"""_2155.py

Design
"""


from typing import List, Optional, TypeVar
from os import path

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.class_property import classproperty
from mastapy.system_model_gui import _1808
from mastapy.gears import _316, _322
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials.efficiency import _286
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import (
    _2424, _2427, _2430, _2426,
    _2420, _2386, _2387, _2388,
    _2389, _2392, _2394, _2395,
    _2396, _2399, _2400, _2404,
    _2405, _2406, _2407, _2414,
    _2415, _2416, _2418, _2421,
    _2423, _2428, _2429, _2431
)
from mastapy.system_model import (
    _2178, _2179, _2164, _2161,
    _2177, _2156
)
from mastapy.detailed_rigid_connectors.splines import _1357
from mastapy.system_model.fe import _2313
from mastapy.utility import _1548, _1549, _1547
from mastapy._math.vector_3d import Vector3D
from mastapy.gears.materials import _591
from mastapy.system_model.part_model.gears import (
    _2463, _2484, _2464, _2465,
    _2466, _2467, _2468, _2469,
    _2470, _2471, _2472, _2473,
    _2474, _2475, _2476, _2477,
    _2478, _2479, _2480, _2481,
    _2483, _2485, _2486, _2487,
    _2488, _2489, _2490, _2491,
    _2492, _2493, _2494, _2495,
    _2496, _2497, _2498, _2499,
    _2500, _2501, _2502, _2503,
    _2504, _2505
)
from mastapy.shafts import _35
from mastapy.system_model.part_model.configurations import _2566, _2563, _2565
from mastapy.bearings.bearing_results.rolling import _1936
from mastapy.system_model.database_access import _2216
from mastapy.system_model.analyses_and_results.load_case_groups import _5599, _5600, _5607
from mastapy.system_model.analyses_and_results.static_loads import _6731, _6730
from mastapy.utility.model_validation import _1758
from mastapy.system_model.analyses_and_results.synchroniser_analysis import _2928
from mastapy.system_model.part_model.creation_options import (
    _2522, _2523, _2524, _2525,
    _2526
)
from mastapy.gears.gear_designs.creation_options import _1136, _1138, _1139
from mastapy.nodal_analysis import _78
from mastapy.bearings.bearing_designs.rolling import _2120
from mastapy import _7483, _0
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy.system_model.part_model.cycloidal import _2519, _2520, _2521
from mastapy.system_model.part_model.couplings import (
    _2527, _2529, _2530, _2532,
    _2533, _2534, _2535, _2537,
    _2538, _2539, _2540, _2541,
    _2547, _2548, _2549, _2551,
    _2552, _2553, _2555, _2556,
    _2557, _2558, _2559, _2561
)

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ARRAY = python_net_import('System', 'Array')
_STRING = python_net_import('System', 'String')
_BOOLEAN = python_net_import('System', 'Boolean')
_TASK_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'TaskProgress')
_DESIGN = python_net_import('SMT.MastaAPI.SystemModel', 'Design')


__docformat__ = 'restructuredtext en'
__all__ = ('Design',)


class Design(_0.APIBase):
    """Design

    This is a mastapy class.
    """

    TYPE = _DESIGN

    def __init__(self, instance_to_wrap: 'Design.TYPE' = None):
        super().__init__(instance_to_wrap if instance_to_wrap else Design.TYPE())
        self._freeze()

    @classproperty
    def available_examples(cls) -> 'List[str]':
        """List[str]: 'AvailableExamples' is the original name of this property."""

        temp = Design.TYPE.AvailableExamples

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @property
    def masta_gui(self) -> '_1808.MASTAGUI':
        """MASTAGUI: 'MastaGUI' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MastaGUI

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def axial_contact_ratio_requirement(self) -> '_316.ContactRatioRequirements':
        """ContactRatioRequirements: 'AxialContactRatioRequirement' is the original name of this property."""

        temp = self.wrapped.AxialContactRatioRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_316.ContactRatioRequirements)(value) if value is not None else None

    @axial_contact_ratio_requirement.setter
    def axial_contact_ratio_requirement(self, value: '_316.ContactRatioRequirements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def bearing_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'BearingConfiguration' is the original name of this property."""

        temp = self.wrapped.BearingConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @bearing_configuration.setter
    def bearing_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.BearingConfiguration = value

    @property
    def coefficient_of_friction(self) -> 'float':
        """float: 'CoefficientOfFriction' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'float'):
        self.wrapped.CoefficientOfFriction = float(value) if value else 0.0

    @property
    def comment(self) -> 'str':
        """str: 'Comment' is the original name of this property."""

        temp = self.wrapped.Comment

        if temp is None:
            return ''

        return temp

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else ''

    @property
    def design_name(self) -> 'str':
        """str: 'DesignName' is the original name of this property."""

        temp = self.wrapped.DesignName

        if temp is None:
            return ''

        return temp

    @design_name.setter
    def design_name(self, value: 'str'):
        self.wrapped.DesignName = str(value) if value else ''

    @property
    def efficiency_rating_method_for_bearings(self) -> '_286.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'EfficiencyRatingMethodForBearings' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethodForBearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_286.BearingEfficiencyRatingMethod)(value) if value is not None else None

    @efficiency_rating_method_for_bearings.setter
    def efficiency_rating_method_for_bearings(self, value: '_286.BearingEfficiencyRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EfficiencyRatingMethodForBearings = value

    @property
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod':
        """enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod: 'EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @efficiency_rating_method_if_skf_loss_model_does_not_provide_losses.setter
    def efficiency_rating_method_if_skf_loss_model_does_not_provide_losses(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingEfficiencyRatingMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.EfficiencyRatingMethodIfSKFLossModelDoesNotProvideLosses = value

    @property
    def fe_substructure_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'FESubstructureConfiguration' is the original name of this property."""

        temp = self.wrapped.FESubstructureConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @fe_substructure_configuration.setter
    def fe_substructure_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.FESubstructureConfiguration = value

    @property
    def file_name(self) -> 'str':
        """str: 'FileName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileName

        if temp is None:
            return ''

        return temp

    @property
    def gear_set_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'GearSetConfiguration' is the original name of this property."""

        temp = self.wrapped.GearSetConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @gear_set_configuration.setter
    def gear_set_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.GearSetConfiguration = value

    @property
    def gravity_magnitude(self) -> 'float':
        """float: 'GravityMagnitude' is the original name of this property."""

        temp = self.wrapped.GravityMagnitude

        if temp is None:
            return 0.0

        return temp

    @gravity_magnitude.setter
    def gravity_magnitude(self, value: 'float'):
        self.wrapped.GravityMagnitude = float(value) if value else 0.0

    @property
    def housing_material_for_grounded_connections(self) -> 'str':
        """str: 'HousingMaterialForGroundedConnections' is the original name of this property."""

        temp = self.wrapped.HousingMaterialForGroundedConnections.SelectedItemName

        if temp is None:
            return ''

        return temp

    @housing_material_for_grounded_connections.setter
    def housing_material_for_grounded_connections(self, value: 'str'):
        self.wrapped.HousingMaterialForGroundedConnections.SetSelectedItem(str(value) if value else '')

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self) -> 'str':
        """str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase' is the original name of this property."""

        temp = self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self) -> 'str':
        """str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase' is the original name of this property."""

        temp = self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SelectedItemName

        if temp is None:
            return ''

        return temp

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def input_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'InputPowerLoad' is the original name of this property."""

        temp = self.wrapped.InputPowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_PowerLoad)(temp) if temp is not None else None

    @input_power_load.setter
    def input_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.InputPowerLoad = value

    @property
    def manufacturer(self) -> 'str':
        """str: 'Manufacturer' is the original name of this property."""

        temp = self.wrapped.Manufacturer

        if temp is None:
            return ''

        return temp

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value else ''

    @property
    def maximum_acceptable_axial_contact_ratio(self) -> 'float':
        """float: 'MaximumAcceptableAxialContactRatio' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_axial_contact_ratio.setter
    def maximum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatio = float(value) if value else 0.0

    @property
    def maximum_acceptable_axial_contact_ratio_above_integer(self) -> 'float':
        """float: 'MaximumAcceptableAxialContactRatioAboveInteger' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_axial_contact_ratio_above_integer.setter
    def maximum_acceptable_axial_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger = float(value) if value else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio(self) -> 'float':
        """float: 'MaximumAcceptableTransverseContactRatio' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_transverse_contact_ratio.setter
    def maximum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatio = float(value) if value else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio_above_integer(self) -> 'float':
        """float: 'MaximumAcceptableTransverseContactRatioAboveInteger' is the original name of this property."""

        temp = self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger

        if temp is None:
            return 0.0

        return temp

    @maximum_acceptable_transverse_contact_ratio_above_integer.setter
    def maximum_acceptable_transverse_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger = float(value) if value else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio(self) -> 'float':
        """float: 'MinimumAcceptableAxialContactRatio' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableAxialContactRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_axial_contact_ratio.setter
    def minimum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatio = float(value) if value else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio_below_integer(self) -> 'float':
        """float: 'MinimumAcceptableAxialContactRatioBelowInteger' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_axial_contact_ratio_below_integer.setter
    def minimum_acceptable_axial_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger = float(value) if value else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumAcceptableTransverseContactRatio' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_transverse_contact_ratio.setter
    def minimum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatio = float(value) if value else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio_below_integer(self) -> 'float':
        """float: 'MinimumAcceptableTransverseContactRatioBelowInteger' is the original name of this property."""

        temp = self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger

        if temp is None:
            return 0.0

        return temp

    @minimum_acceptable_transverse_contact_ratio_below_integer.setter
    def minimum_acceptable_transverse_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger = float(value) if value else 0.0

    @property
    def node_size(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NodeSize' is the original name of this property."""

        temp = self.wrapped.NodeSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @node_size.setter
    def node_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NodeSize = value

    @property
    def number_of_gear_set_configurations(self) -> 'int':
        """int: 'NumberOfGearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfGearSetConfigurations

        if temp is None:
            return 0

        return temp

    @property
    def output_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'OutputPowerLoad' is the original name of this property."""

        temp = self.wrapped.OutputPowerLoad

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_PowerLoad)(temp) if temp is not None else None

    @output_power_load.setter
    def output_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.OutputPowerLoad = value

    @property
    def shaft_detail_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ShaftDetailConfiguration' is the original name of this property."""

        temp = self.wrapped.ShaftDetailConfiguration

        if temp is None:
            return ''

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else ''

    @shaft_detail_configuration.setter
    def shaft_detail_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ShaftDetailConfiguration = value

    @property
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing':
        """enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing: 'ShaftDiameterModificationDueToRollingBearingRings' is the original name of this property."""

        temp = self.wrapped.ShaftDiameterModificationDueToRollingBearingRings

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @shaft_diameter_modification_due_to_rolling_bearing_rings.setter
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ShaftDiameterModificationDueToRollingBearingRings = value

    @property
    def thermal_expansion_for_grounded_nodes(self) -> '_2178.ThermalExpansionOptionForGroundedNodes':
        """ThermalExpansionOptionForGroundedNodes: 'ThermalExpansionForGroundedNodes' is the original name of this property."""

        temp = self.wrapped.ThermalExpansionForGroundedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2178.ThermalExpansionOptionForGroundedNodes)(value) if value is not None else None

    @thermal_expansion_for_grounded_nodes.setter
    def thermal_expansion_for_grounded_nodes(self, value: '_2178.ThermalExpansionOptionForGroundedNodes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ThermalExpansionForGroundedNodes = value

    @property
    def transverse_contact_ratio_requirement(self) -> '_316.ContactRatioRequirements':
        """ContactRatioRequirements: 'TransverseContactRatioRequirement' is the original name of this property."""

        temp = self.wrapped.TransverseContactRatioRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_316.ContactRatioRequirements)(value) if value is not None else None

    @transverse_contact_ratio_requirement.setter
    def transverse_contact_ratio_requirement(self, value: '_316.ContactRatioRequirements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def unbalanced_mass_inclusion(self) -> '_2430.UnbalancedMassInclusionOption':
        """UnbalancedMassInclusionOption: 'UnbalancedMassInclusion' is the original name of this property."""

        temp = self.wrapped.UnbalancedMassInclusion

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2430.UnbalancedMassInclusionOption)(value) if value is not None else None

    @unbalanced_mass_inclusion.setter
    def unbalanced_mass_inclusion(self, value: '_2430.UnbalancedMassInclusionOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(self) -> 'bool':
        """bool: 'UseElementContactAnglesForAngularVelocitiesInBallBearings' is the original name of this property."""

        temp = self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings

        if temp is None:
            return False

        return temp

    @use_element_contact_angles_for_angular_velocities_in_ball_bearings.setter
    def use_element_contact_angles_for_angular_velocities_in_ball_bearings(self, value: 'bool'):
        self.wrapped.UseElementContactAnglesForAngularVelocitiesInBallBearings = bool(value) if value else False

    @property
    def use_expanded_2d_projection_mode(self) -> 'bool':
        """bool: 'UseExpanded2DProjectionMode' is the original name of this property."""

        temp = self.wrapped.UseExpanded2DProjectionMode

        if temp is None:
            return False

        return temp

    @use_expanded_2d_projection_mode.setter
    def use_expanded_2d_projection_mode(self, value: 'bool'):
        self.wrapped.UseExpanded2DProjectionMode = bool(value) if value else False

    @property
    def volumetric_oil_air_mixture_ratio(self) -> 'float':
        """float: 'VolumetricOilAirMixtureRatio' is the original name of this property."""

        temp = self.wrapped.VolumetricOilAirMixtureRatio

        if temp is None:
            return 0.0

        return temp

    @volumetric_oil_air_mixture_ratio.setter
    def volumetric_oil_air_mixture_ratio(self, value: 'float'):
        self.wrapped.VolumetricOilAirMixtureRatio = float(value) if value else 0.0

    @property
    def default_system_temperatures(self) -> '_2179.TransmissionTemperatureSet':
        """TransmissionTemperatureSet: 'DefaultSystemTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DefaultSystemTemperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detailed_spline_settings(self) -> '_1357.DetailedSplineJointSettings':
        """DetailedSplineJointSettings: 'DetailedSplineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DetailedSplineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_group(self) -> '_2164.ElectricMachineGroup':
        """ElectricMachineGroup: 'ElectricMachineGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fe_batch_operations(self) -> '_2313.BatchOperations':
        """BatchOperations: 'FEBatchOperations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEBatchOperations

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def file_save_details_all(self) -> '_1548.FileHistory':
        """FileHistory: 'FileSaveDetailsAll' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileSaveDetailsAll

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def file_save_details_most_recent(self) -> '_1549.FileHistoryItem':
        """FileHistoryItem: 'FileSaveDetailsMostRecent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileSaveDetailsMostRecent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_group(self) -> '_322.GearSetDesignGroup':
        """GearSetDesignGroup: 'GearSetDesignGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gravity_orientation(self) -> 'Vector3D':
        """Vector3D: 'GravityOrientation' is the original name of this property."""

        temp = self.wrapped.GravityOrientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @gravity_orientation.setter
    def gravity_orientation(self, value: 'Vector3D'):
        value = value if value else None
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityOrientation = value

    @property
    def gravity_vector_components(self) -> 'Vector3D':
        """Vector3D: 'GravityVectorComponents' is the original name of this property."""

        temp = self.wrapped.GravityVectorComponents

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @gravity_vector_components.setter
    def gravity_vector_components(self, value: 'Vector3D'):
        value = value if value else None
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.GravityVectorComponents = value

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_external_external_meshes(self) -> '_591.ISOTR1417912001CoefficientOfFrictionConstants':
        """ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes(self) -> '_591.ISOTR1417912001CoefficientOfFrictionConstants':
        """ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_gear_set_selection_group(self) -> '_2463.ActiveGearSetDesignSelectionGroup':
        """ActiveGearSetDesignSelectionGroup: 'SelectedGearSetSelectionGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedGearSetSelectionGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def settings(self) -> '_2161.DesignSettings':
        """DesignSettings: 'Settings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shafts(self) -> '_35.ShaftSafetyFactorSettings':
        """ShaftSafetyFactorSettings: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system(self) -> '_2177.SystemReporting':
        """SystemReporting: 'System' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.System

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_detail_configurations(self) -> 'List[_2566.BearingDetailConfiguration]':
        """List[BearingDetailConfiguration]: 'BearingDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDetailConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_substructure_configurations(self) -> 'List[_2563.ActiveFESubstructureSelectionGroup]':
        """List[ActiveFESubstructureSelectionGroup]: 'FESubstructureConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FESubstructureConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_configurations(self) -> 'List[_2463.ActiveGearSetDesignSelectionGroup]':
        """List[ActiveGearSetDesignSelectionGroup]: 'GearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def iso14179_settings_per_bearing_type(self) -> 'List[_1936.ISO14179SettingsPerBearingType]':
        """List[ISO14179SettingsPerBearingType]: 'ISO14179SettingsPerBearingType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179SettingsPerBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_detail_configurations(self) -> 'List[_2565.ActiveShaftDesignSelectionGroup]':
        """List[ActiveShaftDesignSelectionGroup]: 'ShaftDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftDetailConfigurations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def databases(self) -> '_2216.Databases':
        """Databases: 'Databases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Databases

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_states(self) -> 'List[_5599.DesignState]':
        """List[DesignState]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def duty_cycles(self) -> 'List[_5600.DutyCycle]':
        """List[DutyCycle]: 'DutyCycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_config(self) -> '_2484.GearSetConfiguration':
        """GearSetConfiguration: 'GearSetConfig' is the original name of this property."""

        temp = self.wrapped.GearSetConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @gear_set_config.setter
    def gear_set_config(self, value: '_2484.GearSetConfiguration'):
        value = value.wrapped if value else None
        self.wrapped.GearSetConfig = value

    @property
    def masta_settings(self) -> '_2156.MastaSettings':
        """MastaSettings: 'MastaSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MastaSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_assembly(self) -> '_2426.RootAssembly':
        """RootAssembly: 'RootAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssembly

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def static_loads(self) -> 'List[_6731.StaticLoadCase]':
        """List[StaticLoadCase]: 'StaticLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def status(self) -> '_1758.Status':
        """Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Status

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_series_load_case_groups(self) -> 'List[_5607.TimeSeriesLoadCaseGroup]':
        """List[TimeSeriesLoadCaseGroup]: 'TimeSeriesLoadCaseGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeSeriesLoadCaseGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_design_state(self, name: Optional['str'] = 'New Design State') -> '_5599.DesignState':
        """ 'AddDesignState' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        """

        name = str(name)
        method_result = self.wrapped.AddDesignState(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_duty_cycle(self, name: Optional['str'] = 'New Duty Cycle') -> '_5600.DutyCycle':
        """ 'AddDutyCycle' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        """

        name = str(name)
        method_result = self.wrapped.AddDutyCycle(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_synchroniser_shift(self, name: 'str') -> '_2928.SynchroniserShift':
        """ 'AddSynchroniserShift' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        """

        name = str(name)
        method_result = self.wrapped.AddSynchroniserShift.Overloads[_STRING](name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_synchroniser_shift_empty(self) -> '_2928.SynchroniserShift':
        """ 'AddSynchroniserShift' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        """

        method_result = self.wrapped.AddSynchroniserShift()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def clear_design(self):
        """ 'ClearDesign' is the original name of this method."""

        self.wrapped.ClearDesign()

    def __copy__(self) -> 'Design':
        """ 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        """

        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def __deepcopy__(self, memo) -> 'Design':
        """ 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        """

        method_result = self.wrapped.Copy()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def copy_with_results(self) -> 'Design':
        """ 'CopyWithResults' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        """

        method_result = self.wrapped.CopyWithResults()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def design_state_load_case_group_named(self, name: 'str') -> '_5599.DesignState':
        """ 'DesignStateLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        """

        name = str(name)
        method_result = self.wrapped.DesignStateLoadCaseGroupNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def design_state_named(self, name: 'str') -> '_5599.DesignState':
        """ 'DesignStateNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        """

        name = str(name)
        method_result = self.wrapped.DesignStateNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def dispose(self):
        """ 'Dispose' is the original name of this method."""

        self.wrapped.Dispose()

    def duty_cycle_named(self, name: 'str') -> '_5600.DutyCycle':
        """ 'DutyCycleNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        """

        name = str(name)
        method_result = self.wrapped.DutyCycleNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def load_results(self, file_name: 'str'):
        """ 'LoadResults' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.LoadResults(file_name if file_name else '')

    def new_belt_creation_options(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.08, pulley_b_diameter: Optional['float'] = 0.08, name: Optional['str'] = 'Belt Drive') -> '_2522.BeltCreationOptions':
        """ 'NewBeltCreationOptions' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.BeltCreationOptions
        """

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.NewBeltCreationOptions(centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_cycloidal_assembly_creation_options(self, number_of_discs: Optional['int'] = 1, number_of_pins: Optional['int'] = 10, name: Optional['str'] = 'Cycloidal Assembly') -> '_2523.CycloidalAssemblyCreationOptions':
        """ 'NewCycloidalAssemblyCreationOptions' is the original name of this method.

        Args:
            number_of_discs (int, optional)
            number_of_pins (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CycloidalAssemblyCreationOptions
        """

        number_of_discs = int(number_of_discs)
        number_of_pins = int(number_of_pins)
        name = str(name)
        method_result = self.wrapped.NewCycloidalAssemblyCreationOptions(number_of_discs if number_of_discs else 0, number_of_pins if number_of_pins else 0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_cylindrical_gear_linear_train_creation_options(self, number_of_gears: Optional['int'] = 3, name: Optional['str'] = 'Gear Train') -> '_2524.CylindricalGearLinearTrainCreationOptions':
        """ 'NewCylindricalGearLinearTrainCreationOptions' is the original name of this method.

        Args:
            number_of_gears (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions
        """

        number_of_gears = int(number_of_gears)
        name = str(name)
        method_result = self.wrapped.NewCylindricalGearLinearTrainCreationOptions(number_of_gears if number_of_gears else 0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_cylindrical_gear_pair_creation_options(self) -> '_1136.CylindricalGearPairCreationOptions':
        """ 'NewCylindricalGearPairCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions
        """

        method_result = self.wrapped.NewCylindricalGearPairCreationOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_hypoid_gear_set_creation_options(self) -> '_1138.HypoidGearSetCreationOptions':
        """ 'NewHypoidGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.HypoidGearSetCreationOptions
        """

        method_result = self.wrapped.NewHypoidGearSetCreationOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_nodal_matrix(self, dense_matrix: 'List[List[float]]') -> '_78.NodalMatrix':
        """ 'NewNodalMatrix' is the original name of this method.

        Args:
            dense_matrix (List[List[float]])

        Returns:
            mastapy.nodal_analysis.NodalMatrix
        """

        dense_matrix = conversion.mp_to_pn_list_float_2d(dense_matrix)
        method_result = self.wrapped.NewNodalMatrix(dense_matrix)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_planet_carrier_creation_options(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.05) -> '_2525.PlanetCarrierCreationOptions':
        """ 'NewPlanetCarrierCreationOptions' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions
        """

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.NewPlanetCarrierCreationOptions(number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_shaft_creation_options(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.025, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2526.ShaftCreationOptions':
        """ 'NewShaftCreationOptions' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.ShaftCreationOptions
        """

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.NewShaftCreationOptions(length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def new_spiral_bevel_gear_set_creation_options(self) -> '_1139.SpiralBevelGearSetCreationOptions':
        """ 'NewSpiralBevelGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions
        """

        method_result = self.wrapped.NewSpiralBevelGearSetCreationOptions()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_bearing_from_database(self, rolling_bearing: '_2120.RollingBearing'):
        """ 'RemoveBearingFromDatabase' is the original name of this method.

        Args:
            rolling_bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        """

        self.wrapped.RemoveBearingFromDatabase(rolling_bearing.wrapped if rolling_bearing else None)

    def remove_synchroniser_shift(self, shift: '_2928.SynchroniserShift'):
        """ 'RemoveSynchroniserShift' is the original name of this method.

        Args:
            shift (mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift)
        """

        self.wrapped.RemoveSynchroniserShift(shift.wrapped if shift else None)

    def save(self, file_name: 'str', save_results: 'bool') -> '_1758.Status':
        """ 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)

        Returns:
            mastapy.utility.model_validation.Status
        """

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN](file_name if file_name else '', save_results if save_results else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def save_with_progess(self, file_name: 'str', save_results: 'bool', progress: '_7483.TaskProgress') -> '_1758.Status':
        """ 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)
            progress (mastapy.TaskProgress)

        Returns:
            mastapy.utility.model_validation.Status
        """

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save.Overloads[_STRING, _BOOLEAN, _TASK_PROGRESS](file_name if file_name else '', save_results if save_results else False, progress.wrapped if progress else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def save_load_case_results(self, file_name: 'str', load_cases: 'List[_6730.LoadCase]'):
        """ 'SaveLoadCaseResults' is the original name of this method.

        Args:
            file_name (str)
            load_cases (List[mastapy.system_model.analyses_and_results.static_loads.LoadCase])
        """

        file_name = str(file_name)
        load_cases = conversion.mp_to_pn_objects_in_list(load_cases)
        self.wrapped.SaveLoadCaseResults(file_name if file_name else '', load_cases)

    def save_results(self, file_name: 'str'):
        """ 'SaveResults' is the original name of this method.

        Args:
            file_name (str)
        """

        file_name = str(file_name)
        self.wrapped.SaveResults(file_name if file_name else '')

    def time_series_load_case_group_named(self, name: 'str') -> '_5607.TimeSeriesLoadCaseGroup':
        """ 'TimeSeriesLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup
        """

        name = str(name)
        method_result = self.wrapped.TimeSeriesLoadCaseGroupNamed(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def all_parts(self) -> 'List[_2420.Part]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2420.Part.TYPE]())

    def all_parts_of_type_assembly(self) -> 'List[_2386.Assembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2386.Assembly.TYPE]())

    def all_parts_of_type_abstract_assembly(self) -> 'List[_2387.AbstractAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2387.AbstractAssembly.TYPE]())

    def all_parts_of_type_abstract_shaft(self) -> 'List[_2388.AbstractShaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaft]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2388.AbstractShaft.TYPE]())

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_2389.AbstractShaftOrHousing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2389.AbstractShaftOrHousing.TYPE]())

    def all_parts_of_type_bearing(self) -> 'List[_2392.Bearing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2392.Bearing.TYPE]())

    def all_parts_of_type_bolt(self) -> 'List[_2394.Bolt]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2394.Bolt.TYPE]())

    def all_parts_of_type_bolted_joint(self) -> 'List[_2395.BoltedJoint]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2395.BoltedJoint.TYPE]())

    def all_parts_of_type_component(self) -> 'List[_2396.Component]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2396.Component.TYPE]())

    def all_parts_of_type_connector(self) -> 'List[_2399.Connector]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2399.Connector.TYPE]())

    def all_parts_of_type_datum(self) -> 'List[_2400.Datum]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2400.Datum.TYPE]())

    def all_parts_of_type_external_cad_model(self) -> 'List[_2404.ExternalCADModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2404.ExternalCADModel.TYPE]())

    def all_parts_of_type_fe_part(self) -> 'List[_2405.FEPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FEPart]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2405.FEPart.TYPE]())

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_2406.FlexiblePinAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2406.FlexiblePinAssembly.TYPE]())

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_2407.GuideDxfModel]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2407.GuideDxfModel.TYPE]())

    def all_parts_of_type_mass_disc(self) -> 'List[_2414.MassDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2414.MassDisc.TYPE]())

    def all_parts_of_type_measurement_component(self) -> 'List[_2415.MeasurementComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2415.MeasurementComponent.TYPE]())

    def all_parts_of_type_mountable_component(self) -> 'List[_2416.MountableComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2416.MountableComponent.TYPE]())

    def all_parts_of_type_oil_seal(self) -> 'List[_2418.OilSeal]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2418.OilSeal.TYPE]())

    def all_parts_of_type_planet_carrier(self) -> 'List[_2421.PlanetCarrier]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2421.PlanetCarrier.TYPE]())

    def all_parts_of_type_point_load(self) -> 'List[_2423.PointLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2423.PointLoad.TYPE]())

    def all_parts_of_type_power_load(self) -> 'List[_2424.PowerLoad]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2424.PowerLoad.TYPE]())

    def all_parts_of_type_root_assembly(self) -> 'List[_2426.RootAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2426.RootAssembly.TYPE]())

    def all_parts_of_type_specialised_assembly(self) -> 'List[_2428.SpecialisedAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2428.SpecialisedAssembly.TYPE]())

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_2429.UnbalancedMass]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2429.UnbalancedMass.TYPE]())

    def all_parts_of_type_virtual_component(self) -> 'List[_2431.VirtualComponent]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2431.VirtualComponent.TYPE]())

    def all_parts_of_type_shaft(self) -> 'List[_2434.Shaft]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2434.Shaft.TYPE]())

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_2464.AGMAGleasonConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2464.AGMAGleasonConicalGear.TYPE]())

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_2465.AGMAGleasonConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2465.AGMAGleasonConicalGearSet.TYPE]())

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_2466.BevelDifferentialGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2466.BevelDifferentialGear.TYPE]())

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_2467.BevelDifferentialGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2467.BevelDifferentialGearSet.TYPE]())

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_2468.BevelDifferentialPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2468.BevelDifferentialPlanetGear.TYPE]())

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_2469.BevelDifferentialSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2469.BevelDifferentialSunGear.TYPE]())

    def all_parts_of_type_bevel_gear(self) -> 'List[_2470.BevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2470.BevelGear.TYPE]())

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_2471.BevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2471.BevelGearSet.TYPE]())

    def all_parts_of_type_concept_gear(self) -> 'List[_2472.ConceptGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2472.ConceptGear.TYPE]())

    def all_parts_of_type_concept_gear_set(self) -> 'List[_2473.ConceptGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2473.ConceptGearSet.TYPE]())

    def all_parts_of_type_conical_gear(self) -> 'List[_2474.ConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2474.ConicalGear.TYPE]())

    def all_parts_of_type_conical_gear_set(self) -> 'List[_2475.ConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2475.ConicalGearSet.TYPE]())

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_2476.CylindricalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2476.CylindricalGear.TYPE]())

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_2477.CylindricalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2477.CylindricalGearSet.TYPE]())

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_2478.CylindricalPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2478.CylindricalPlanetGear.TYPE]())

    def all_parts_of_type_face_gear(self) -> 'List[_2479.FaceGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2479.FaceGear.TYPE]())

    def all_parts_of_type_face_gear_set(self) -> 'List[_2480.FaceGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2480.FaceGearSet.TYPE]())

    def all_parts_of_type_gear(self) -> 'List[_2481.Gear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2481.Gear.TYPE]())

    def all_parts_of_type_gear_set(self) -> 'List[_2483.GearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2483.GearSet.TYPE]())

    def all_parts_of_type_hypoid_gear(self) -> 'List[_2485.HypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2485.HypoidGear.TYPE]())

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_2486.HypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2486.HypoidGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_2487.KlingelnbergCycloPalloidConicalGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2487.KlingelnbergCycloPalloidConicalGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_2488.KlingelnbergCycloPalloidConicalGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2488.KlingelnbergCycloPalloidConicalGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2489.KlingelnbergCycloPalloidHypoidGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2489.KlingelnbergCycloPalloidHypoidGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2490.KlingelnbergCycloPalloidHypoidGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2490.KlingelnbergCycloPalloidHypoidGearSet.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2491.KlingelnbergCycloPalloidSpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2491.KlingelnbergCycloPalloidSpiralBevelGear.TYPE]())

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2492.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2492.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE]())

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2493.PlanetaryGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2493.PlanetaryGearSet.TYPE]())

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2494.SpiralBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2494.SpiralBevelGear.TYPE]())

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2495.SpiralBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2495.SpiralBevelGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2496.StraightBevelDiffGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2496.StraightBevelDiffGear.TYPE]())

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2497.StraightBevelDiffGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2497.StraightBevelDiffGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2498.StraightBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2498.StraightBevelGear.TYPE]())

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2499.StraightBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2499.StraightBevelGearSet.TYPE]())

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2500.StraightBevelPlanetGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2500.StraightBevelPlanetGear.TYPE]())

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2501.StraightBevelSunGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2501.StraightBevelSunGear.TYPE]())

    def all_parts_of_type_worm_gear(self) -> 'List[_2502.WormGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2502.WormGear.TYPE]())

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2503.WormGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2503.WormGearSet.TYPE]())

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2504.ZerolBevelGear]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2504.ZerolBevelGear.TYPE]())

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2505.ZerolBevelGearSet]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2505.ZerolBevelGearSet.TYPE]())

    def all_parts_of_type_cycloidal_assembly(self) -> 'List[_2519.CycloidalAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2519.CycloidalAssembly.TYPE]())

    def all_parts_of_type_cycloidal_disc(self) -> 'List[_2520.CycloidalDisc]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.CycloidalDisc]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2520.CycloidalDisc.TYPE]())

    def all_parts_of_type_ring_pins(self) -> 'List[_2521.RingPins]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.cycloidal.RingPins]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2521.RingPins.TYPE]())

    def all_parts_of_type_belt_drive(self) -> 'List[_2527.BeltDrive]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2527.BeltDrive.TYPE]())

    def all_parts_of_type_clutch(self) -> 'List[_2529.Clutch]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2529.Clutch.TYPE]())

    def all_parts_of_type_clutch_half(self) -> 'List[_2530.ClutchHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2530.ClutchHalf.TYPE]())

    def all_parts_of_type_concept_coupling(self) -> 'List[_2532.ConceptCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2532.ConceptCoupling.TYPE]())

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2533.ConceptCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2533.ConceptCouplingHalf.TYPE]())

    def all_parts_of_type_coupling(self) -> 'List[_2534.Coupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2534.Coupling.TYPE]())

    def all_parts_of_type_coupling_half(self) -> 'List[_2535.CouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2535.CouplingHalf.TYPE]())

    def all_parts_of_type_cvt(self) -> 'List[_2537.CVT]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2537.CVT.TYPE]())

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2538.CVTPulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2538.CVTPulley.TYPE]())

    def all_parts_of_type_part_to_part_shear_coupling(self) -> 'List[_2539.PartToPartShearCoupling]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCoupling]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2539.PartToPartShearCoupling.TYPE]())

    def all_parts_of_type_part_to_part_shear_coupling_half(self) -> 'List[_2540.PartToPartShearCouplingHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2540.PartToPartShearCouplingHalf.TYPE]())

    def all_parts_of_type_pulley(self) -> 'List[_2541.Pulley]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2541.Pulley.TYPE]())

    def all_parts_of_type_rolling_ring(self) -> 'List[_2547.RollingRing]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2547.RollingRing.TYPE]())

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2548.RollingRingAssembly]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2548.RollingRingAssembly.TYPE]())

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2549.ShaftHubConnection]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2549.ShaftHubConnection.TYPE]())

    def all_parts_of_type_spring_damper(self) -> 'List[_2551.SpringDamper]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2551.SpringDamper.TYPE]())

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2552.SpringDamperHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2552.SpringDamperHalf.TYPE]())

    def all_parts_of_type_synchroniser(self) -> 'List[_2553.Synchroniser]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2553.Synchroniser.TYPE]())

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2555.SynchroniserHalf]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2555.SynchroniserHalf.TYPE]())

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2556.SynchroniserPart]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2556.SynchroniserPart.TYPE]())

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2557.SynchroniserSleeve]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2557.SynchroniserSleeve.TYPE]())

    def all_parts_of_type_torque_converter(self) -> 'List[_2558.TorqueConverter]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2558.TorqueConverter.TYPE]())

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2559.TorqueConverterPump]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2559.TorqueConverterPump.TYPE]())

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2561.TorqueConverterTurbine]':
        """ 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2561.TorqueConverterTurbine.TYPE]())

    @staticmethod
    def load(file_path: 'str', load_full_fe_option: Optional['_1547.ExternalFullFEFileOption'] = _1547.ExternalFullFEFileOption.MESH_AND_EXPANSION_VECTORS) -> 'Design':
        """ 'Load' is the original name of this method.

        Args:
            file_path (str)
            load_full_fe_option (mastapy.utility.ExternalFullFEFileOption, optional)

        Returns:
            mastapy.system_model.Design
        """

        file_path = str(file_path)
        file_path = path.abspath(file_path)
        load_full_fe_option = conversion.mp_to_pn_enum(load_full_fe_option)
        method_result = Design.TYPE.Load(file_path if file_path else '', load_full_fe_option)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    @staticmethod
    def load_example(example_string: 'str') -> 'Design':
        """ 'LoadExample' is the original name of this method.

        Args:
            example_string (str)

        Returns:
            mastapy.system_model.Design
        """

        example_string = str(example_string)
        method_result = Design.TYPE.LoadExample(example_string if example_string else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def compare_for_test_only(self, design: 'Design', sb: 'str') -> 'bool':
        """ 'CompareForTestOnly' is the original name of this method.

        Args:
            design (mastapy.system_model.Design)
            sb (str)

        Returns:
            bool
        """

        sb = str(sb)
        method_result = self.wrapped.CompareForTestOnly(design.wrapped if design else None, sb if sb else '')
        return method_result

    def add_bearing_detail_configuration_all_bearings(self):
        """ 'AddBearingDetailConfigurationAllBearings' is the original name of this method."""

        self.wrapped.AddBearingDetailConfigurationAllBearings()

    def add_bearing_detail_configuration_rolling_bearings(self):
        """ 'AddBearingDetailConfigurationRollingBearings' is the original name of this method."""

        self.wrapped.AddBearingDetailConfigurationRollingBearings()

    def add_fe_substructure_configuration(self):
        """ 'AddFESubstructureConfiguration' is the original name of this method."""

        self.wrapped.AddFESubstructureConfiguration()

    def add_gear_set_configuration(self):
        """ 'AddGearSetConfiguration' is the original name of this method."""

        self.wrapped.AddGearSetConfiguration()

    def add_shaft_detail_configuration(self):
        """ 'AddShaftDetailConfiguration' is the original name of this method."""

        self.wrapped.AddShaftDetailConfiguration()

    def change_gears_to_clones_where_suitable(self):
        """ 'ChangeGearsToClonesWhereSuitable' is the original name of this method."""

        self.wrapped.ChangeGearsToClonesWhereSuitable()

    def clear_undo_redo_stacks(self):
        """ 'ClearUndoRedoStacks' is the original name of this method."""

        self.wrapped.ClearUndoRedoStacks()

    def compare_results_to_previous_masta_version(self):
        """ 'CompareResultsToPreviousMASTAVersion' is the original name of this method."""

        self.wrapped.CompareResultsToPreviousMASTAVersion()

    def delete_all_gear_set_configurations_that_have_errors_or_warnings(self):
        """ 'DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings' is the original name of this method."""

        self.wrapped.DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings()

    def delete_all_gear_sets_designs_that_are_not_used_in_configurations(self):
        """ 'DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations' is the original name of this method."""

        self.wrapped.DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations()

    def delete_all_inactive_gear_set_designs(self):
        """ 'DeleteAllInactiveGearSetDesigns' is the original name of this method."""

        self.wrapped.DeleteAllInactiveGearSetDesigns()

    def delete_multiple_bearing_detail_configurations(self):
        """ 'DeleteMultipleBearingDetailConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleBearingDetailConfigurations()

    def delete_multiple_fe_substructure_configurations(self):
        """ 'DeleteMultipleFESubstructureConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleFESubstructureConfigurations()

    def delete_multiple_gear_set_configurations(self):
        """ 'DeleteMultipleGearSetConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleGearSetConfigurations()

    def delete_multiple_shaft_detail_configurations(self):
        """ 'DeleteMultipleShaftDetailConfigurations' is the original name of this method."""

        self.wrapped.DeleteMultipleShaftDetailConfigurations()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.dispose()
