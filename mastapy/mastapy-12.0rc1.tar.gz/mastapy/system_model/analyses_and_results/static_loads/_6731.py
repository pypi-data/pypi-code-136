"""_6731.py

StaticLoadCase
"""


from typing import List, Optional

from mastapy.system_model.analyses_and_results import (
    _2597, _2592, _2572, _2583,
    _2591, _2575, _2594, _2586,
    _2576, _2593, _2574, _2580,
    _2634, _2571
)
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _335
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2430
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7199
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5698
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6997
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.load_case_groups import _5597, _5598, _5599
from mastapy.system_model.analyses_and_results.static_loads import _6744, _6730
from mastapy._internal.python_net import python_net_import

_STATIC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StaticLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('StaticLoadCase',)


class StaticLoadCase(_6730.LoadCase):
    """StaticLoadCase

    This is a mastapy class.
    """

    TYPE = _STATIC_LOAD_CASE

    def __init__(self, instance_to_wrap: 'StaticLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def system_deflection(self) -> '_2597.SystemDeflectionAnalysis':
        """SystemDeflectionAnalysis: 'SystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow(self) -> '_2592.PowerFlowAnalysis':
        """PowerFlowAnalysis: 'PowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlow

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def advanced_system_deflection(self) -> '_2572.AdvancedSystemDeflectionAnalysis':
        """AdvancedSystemDeflectionAnalysis: 'AdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis(self) -> '_2583.HarmonicAnalysis':
        """HarmonicAnalysis: 'HarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_study_tool(self) -> '_2591.ParametricStudyToolAnalysis':
        """ParametricStudyToolAnalysis: 'ParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_parametric_study_tool(self) -> '_2575.CompoundParametricStudyToolAnalysis':
        """CompoundParametricStudyToolAnalysis: 'CompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response(self) -> '_2594.SteadyStateSynchronousResponseAnalysis':
        """SteadyStateSynchronousResponseAnalysis: 'SteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponse

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis(self) -> '_2586.ModalAnalysis':
        """ModalAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def critical_speed_analysis(self) -> '_2576.CriticalSpeedAnalysis':
        """CriticalSpeedAnalysis: 'CriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis(self) -> '_2593.StabilityAnalysis':
        """StabilityAnalysis: 'StabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def advanced_time_stepping_analysis_for_modulation(self) -> '_2574.AdvancedTimeSteppingAnalysisForModulation':
        """AdvancedTimeSteppingAnalysisForModulation: 'AdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dynamic_model_for_modal_analysis(self) -> '_2580.DynamicModelForModalAnalysis':
        """DynamicModelForModalAnalysis: 'DynamicModelForModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicModelForModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_time(self) -> 'float':
        """float: 'CurrentTime' is the original name of this property."""

        temp = self.wrapped.CurrentTime

        if temp is None:
            return 0.0

        return temp

    @current_time.setter
    def current_time(self, value: 'float'):
        self.wrapped.CurrentTime = float(value) if value else 0.0

    @property
    def design_state(self) -> 'str':
        """str: 'DesignState' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignState

        if temp is None:
            return ''

        return temp

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property."""

        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    def duration(self, value: 'float'):
        self.wrapped.Duration = float(value) if value else 0.0

    @property
    def input_shaft_cycles(self) -> 'float':
        """float: 'InputShaftCycles' is the original name of this property."""

        temp = self.wrapped.InputShaftCycles

        if temp is None:
            return 0.0

        return temp

    @input_shaft_cycles.setter
    def input_shaft_cycles(self, value: 'float'):
        self.wrapped.InputShaftCycles = float(value) if value else 0.0

    @property
    def is_stop_start_load_case(self) -> 'bool':
        """bool: 'IsStopStartLoadCase' is the original name of this property."""

        temp = self.wrapped.IsStopStartLoadCase

        if temp is None:
            return False

        return temp

    @is_stop_start_load_case.setter
    def is_stop_start_load_case(self, value: 'bool'):
        self.wrapped.IsStopStartLoadCase = bool(value) if value else False

    @property
    def number_of_stop_start_cycles(self) -> 'int':
        """int: 'NumberOfStopStartCycles' is the original name of this property."""

        temp = self.wrapped.NumberOfStopStartCycles

        if temp is None:
            return 0

        return temp

    @number_of_stop_start_cycles.setter
    def number_of_stop_start_cycles(self, value: 'int'):
        self.wrapped.NumberOfStopStartCycles = int(value) if value else 0

    @property
    def percentage_of_shaft_torque_alternating(self) -> 'float':
        """float: 'PercentageOfShaftTorqueAlternating' is the original name of this property."""

        temp = self.wrapped.PercentageOfShaftTorqueAlternating

        if temp is None:
            return 0.0

        return temp

    @percentage_of_shaft_torque_alternating.setter
    def percentage_of_shaft_torque_alternating(self, value: 'float'):
        self.wrapped.PercentageOfShaftTorqueAlternating = float(value) if value else 0.0

    @property
    def planetary_rating_load_sharing_method(self) -> '_335.PlanetaryRatingLoadSharingOption':
        """PlanetaryRatingLoadSharingOption: 'PlanetaryRatingLoadSharingMethod' is the original name of this property."""

        temp = self.wrapped.PlanetaryRatingLoadSharingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_335.PlanetaryRatingLoadSharingOption)(value) if value is not None else None

    @planetary_rating_load_sharing_method.setter
    def planetary_rating_load_sharing_method(self, value: '_335.PlanetaryRatingLoadSharingOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PlanetaryRatingLoadSharingMethod = value

    @property
    def power_convergence_tolerance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PowerConvergenceTolerance' is the original name of this property."""

        temp = self.wrapped.PowerConvergenceTolerance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @power_convergence_tolerance.setter
    def power_convergence_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PowerConvergenceTolerance = value

    @property
    def unbalanced_mass_inclusion(self) -> 'overridable.Overridable_UnbalancedMassInclusionOption':
        """overridable.Overridable_UnbalancedMassInclusionOption: 'UnbalancedMassInclusion' is the original name of this property."""

        temp = self.wrapped.UnbalancedMassInclusion

        if temp is None:
            return None

        value = overridable.Overridable_UnbalancedMassInclusionOption.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @unbalanced_mass_inclusion.setter
    def unbalanced_mass_inclusion(self, value: 'overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()'):
        wrapper_type = overridable.Overridable_UnbalancedMassInclusionOption.wrapper_type()
        enclosed_type = overridable.Overridable_UnbalancedMassInclusionOption.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.UnbalancedMassInclusion = value

    @property
    def advanced_system_deflection_options(self) -> '_7199.AdvancedSystemDeflectionOptions':
        """AdvancedSystemDeflectionOptions: 'AdvancedSystemDeflectionOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflectionOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_options(self) -> '_5698.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        if _5698.HarmonicAnalysisOptions.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options to HarmonicAnalysisOptions. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_options_for_atsam(self) -> '_5698.HarmonicAnalysisOptions':
        """HarmonicAnalysisOptions: 'HarmonicAnalysisOptionsForATSAM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisOptionsForATSAM

        if temp is None:
            return None

        if _5698.HarmonicAnalysisOptions.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_options_for_atsam to HarmonicAnalysisOptions. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def te_set_up_for_dynamic_analyses_options(self) -> '_2634.TESetUpForDynamicAnalysisOptions':
        """TESetUpForDynamicAnalysisOptions: 'TESetUpForDynamicAnalysesOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TESetUpForDynamicAnalysesOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clutch_engagements(self) -> 'List[_5597.ClutchEngagementStatus]':
        """List[ClutchEngagementStatus]: 'ClutchEngagements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchEngagements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_clutch_engagements(self) -> 'List[_5598.ConceptSynchroGearEngagementStatus]':
        """List[ConceptSynchroGearEngagementStatus]: 'ConceptClutchEngagements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptClutchEngagements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def design_state_load_case_group(self) -> '_5599.DesignState':
        """DesignState: 'DesignStateLoadCaseGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStateLoadCaseGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_of(self, analysis_type: '_6744.AnalysisType') -> '_2571.SingleAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.SingleAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_time_series_load_case(self):
        """ 'CreateTimeSeriesLoadCase' is the original name of this method."""

        self.wrapped.CreateTimeSeriesLoadCase()

    def run_power_flow(self):
        """ 'RunPowerFlow' is the original name of this method."""

        self.wrapped.RunPowerFlow()

    def set_face_widths_for_specified_safety_factors_from_power_flow(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow()

    def duplicate(self, new_design_state_group: '_5599.DesignState', name: Optional['str'] = 'None') -> 'StaticLoadCase':
        """ 'Duplicate' is the original name of this method.

        Args:
            new_design_state_group (mastapy.system_model.analyses_and_results.load_case_groups.DesignState)
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase
        """

        name = str(name)
        method_result = self.wrapped.Duplicate(new_design_state_group.wrapped if new_design_state_group else None, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
