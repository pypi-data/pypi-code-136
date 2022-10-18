"""_5596.py

AbstractStaticLoadCaseGroup
"""


from typing import List

from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5605, _5606, _5594, _5604,
    _5595
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5609, _5612, _5613
from mastapy.system_model.part_model import (
    _2392, _2405, _2423, _2424
)
from mastapy.system_model.analyses_and_results.static_loads import (
    _6746, _6787, _6789, _6791,
    _6813, _6864, _6865, _6731,
    _6744
)
from mastapy.system_model.part_model.gears import _2477, _2476
from mastapy.system_model.connections_and_sockets.gears import _2261
from mastapy.system_model.analyses_and_results.power_flows.compound import _4158
from mastapy.system_model.analyses_and_results import (
    _2632, _2627, _2609, _2619,
    _2629, _2622, _2612, _2628,
    _2611, _2616, _2570
)
from mastapy._internal.python_net import python_net_import

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'AbstractStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractStaticLoadCaseGroup',)


class AbstractStaticLoadCaseGroup(_5595.AbstractLoadCaseGroup):
    """AbstractStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_STATIC_LOAD_CASE_GROUP

    def __init__(self, instance_to_wrap: 'AbstractStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_optimisation(self) -> '_5605.SystemOptimiserGearSetOptimisation':
        """SystemOptimiserGearSetOptimisation: 'GearSetOptimisation' is the original name of this property."""

        temp = self.wrapped.GearSetOptimisation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_5605.SystemOptimiserGearSetOptimisation)(value) if value is not None else None

    @gear_set_optimisation.setter
    def gear_set_optimisation(self, value: '_5605.SystemOptimiserGearSetOptimisation'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.GearSetOptimisation = value

    @property
    def max_number_of_load_cases_to_display(self) -> 'int':
        """int: 'MaxNumberOfLoadCasesToDisplay' is the original name of this property."""

        temp = self.wrapped.MaxNumberOfLoadCasesToDisplay

        if temp is None:
            return 0

        return temp

    @max_number_of_load_cases_to_display.setter
    def max_number_of_load_cases_to_display(self, value: 'int'):
        self.wrapped.MaxNumberOfLoadCasesToDisplay = int(value) if value else 0

    @property
    def number_of_configurations_to_create(self) -> 'int':
        """int: 'NumberOfConfigurationsToCreate' is the original name of this property."""

        temp = self.wrapped.NumberOfConfigurationsToCreate

        if temp is None:
            return 0

        return temp

    @number_of_configurations_to_create.setter
    def number_of_configurations_to_create(self, value: 'int'):
        self.wrapped.NumberOfConfigurationsToCreate = int(value) if value else 0

    @property
    def number_of_possible_system_designs(self) -> 'int':
        """int: 'NumberOfPossibleSystemDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPossibleSystemDesigns

        if temp is None:
            return 0

        return temp

    @property
    def optimum_tooth_numbers_target(self) -> '_5606.SystemOptimiserTargets':
        """SystemOptimiserTargets: 'OptimumToothNumbersTarget' is the original name of this property."""

        temp = self.wrapped.OptimumToothNumbersTarget

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_5606.SystemOptimiserTargets)(value) if value is not None else None

    @optimum_tooth_numbers_target.setter
    def optimum_tooth_numbers_target(self, value: '_5606.SystemOptimiserTargets'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.OptimumToothNumbersTarget = value

    @property
    def system_optimiser_log(self) -> 'str':
        """str: 'SystemOptimiserLog' is the original name of this property."""

        temp = self.wrapped.SystemOptimiserLog

        if temp is None:
            return ''

        return temp

    @system_optimiser_log.setter
    def system_optimiser_log(self, value: 'str'):
        self.wrapped.SystemOptimiserLog = str(value) if value else ''

    @property
    def bearings(self) -> 'List[_5609.ComponentStaticLoadCaseGroup[_2392.Bearing, _6746.BearingLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[Bearing, BearingLoadCase]]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5612.GearSetStaticLoadCaseGroup[_2477.CylindricalGearSet, _2476.CylindricalGear, _6787.CylindricalGearLoadCase, _2261.CylindricalGearMesh, _6789.CylindricalGearMeshLoadCase, _6791.CylindricalGearSetLoadCase]]':
        """List[GearSetStaticLoadCaseGroup[CylindricalGearSet, CylindricalGear, CylindricalGearLoadCase, CylindricalGearMesh, CylindricalGearMeshLoadCase, CylindricalGearSetLoadCase]]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def design_states(self) -> 'List[_5594.AbstractDesignStateLoadCaseGroup]':
        """List[AbstractDesignStateLoadCaseGroup]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_5609.ComponentStaticLoadCaseGroup[_2405.FEPart, _6813.FEPartLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[FEPart, FEPartLoadCase]]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def loaded_gear_sets(self) -> 'List[_4158.CylindricalGearSetCompoundPowerFlow]':
        """List[CylindricalGearSetCompoundPowerFlow]: 'LoadedGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def parts_with_excitations(self) -> 'List[_5613.PartStaticLoadCaseGroup]':
        """List[PartStaticLoadCaseGroup]: 'PartsWithExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartsWithExcitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_5609.ComponentStaticLoadCaseGroup[_2423.PointLoad, _6864.PointLoadLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[PointLoad, PointLoadLoadCase]]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_5609.ComponentStaticLoadCaseGroup[_2424.PowerLoad, _6865.PowerLoadLoadCase]]':
        """List[ComponentStaticLoadCaseGroup[PowerLoad, PowerLoadLoadCase]]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
    def static_loads_limited_by_max_number_of_load_cases_to_display(self) -> 'List[_6731.StaticLoadCase]':
        """List[StaticLoadCase]: 'StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def system_optimisation_gear_sets(self) -> 'List[_5604.SystemOptimisationGearSet]':
        """List[SystemOptimisationGearSet]: 'SystemOptimisationGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemOptimisationGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def compound_system_deflection(self) -> '_2632.CompoundSystemDeflectionAnalysis':
        """CompoundSystemDeflectionAnalysis: 'CompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_power_flow(self) -> '_2627.CompoundPowerFlowAnalysis':
        """CompoundPowerFlowAnalysis: 'CompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundPowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_advanced_system_deflection(self) -> '_2609.CompoundAdvancedSystemDeflectionAnalysis':
        """CompoundAdvancedSystemDeflectionAnalysis: 'CompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundAdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_harmonic_analysis(self) -> '_2619.CompoundHarmonicAnalysis':
        """CompoundHarmonicAnalysis: 'CompoundHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundHarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_steady_state_synchronous_response(self) -> '_2629.CompoundSteadyStateSynchronousResponseAnalysis':
        """CompoundSteadyStateSynchronousResponseAnalysis: 'CompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_modal_analysis(self) -> '_2622.CompoundModalAnalysis':
        """CompoundModalAnalysis: 'CompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_critical_speed_analysis(self) -> '_2612.CompoundCriticalSpeedAnalysis':
        """CompoundCriticalSpeedAnalysis: 'CompoundCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_stability_analysis(self) -> '_2628.CompoundStabilityAnalysis':
        """CompoundStabilityAnalysis: 'CompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(self) -> '_2611.CompoundAdvancedTimeSteppingAnalysisForModulation':
        """CompoundAdvancedTimeSteppingAnalysisForModulation: 'CompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_dynamic_model_for_modal_analysis(self) -> '_2616.CompoundDynamicModelForModalAnalysis':
        """CompoundDynamicModelForModalAnalysis: 'CompoundDynamicModelForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundDynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def calculate_candidates(self):
        """ 'CalculateCandidates' is the original name of this method."""

        self.wrapped.CalculateCandidates()

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        """ 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method."""

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()

    def create_designs(self):
        """ 'CreateDesigns' is the original name of this method."""

        self.wrapped.CreateDesigns()

    def optimise_gear_sets_quick(self):
        """ 'OptimiseGearSetsQuick' is the original name of this method."""

        self.wrapped.OptimiseGearSetsQuick()

    def perform_system_optimisation(self):
        """ 'PerformSystemOptimisation' is the original name of this method."""

        self.wrapped.PerformSystemOptimisation()

    def run_power_flow(self):
        """ 'RunPowerFlow' is the original name of this method."""

        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    def analysis_of(self, analysis_type: '_6744.AnalysisType') -> '_2570.CompoundAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.CompoundAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
