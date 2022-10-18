"""_2704.py

FlexiblePinAssemblySystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2406
from mastapy.system_model.analyses_and_results.static_loads import _6814
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2750, _2688, _2689, _2690,
    _2644, _2747, _2724, _2729,
    _2691, _2752
)
from mastapy.system_model.analyses_and_results.power_flows import _4034
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FlexiblePinAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblySystemDeflection',)


class FlexiblePinAssemblySystemDeflection(_2752.SpecialisedAssemblySystemDeflection):
    """FlexiblePinAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pin_tangential_oscillation_amplitude(self) -> 'float':
        """float: 'PinTangentialOscillationAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinTangentialOscillationAmplitude

        if temp is None:
            return 0.0

        return temp

    @property
    def pin_tangential_oscillation_frequency(self) -> 'float':
        """float: 'PinTangentialOscillationFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinTangentialOscillationFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def assembly_design(self) -> '_2406.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6814.FlexiblePinAssemblyLoadCase':
        """FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def flexible_pin_shaft_details(self) -> '_2750.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'FlexiblePinShaftDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinShaftDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pin_analysis(self) -> '_2750.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'PinAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4034.FlexiblePinAssemblyPowerFlow':
        """FlexiblePinAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def separate_gear_set_details(self) -> '_2688.CylindricalGearSetSystemDeflection':
        """CylindricalGearSetSystemDeflection: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparateGearSetDetails

        if temp is None:
            return None

        if _2688.CylindricalGearSetSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def separate_gear_set_details_of_type_cylindrical_gear_set_system_deflection_timestep(self) -> '_2689.CylindricalGearSetSystemDeflectionTimestep':
        """CylindricalGearSetSystemDeflectionTimestep: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparateGearSetDetails

        if temp is None:
            return None

        if _2689.CylindricalGearSetSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def separate_gear_set_details_of_type_cylindrical_gear_set_system_deflection_with_ltca_results(self) -> '_2690.CylindricalGearSetSystemDeflectionWithLTCAResults':
        """CylindricalGearSetSystemDeflectionWithLTCAResults: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparateGearSetDetails

        if temp is None:
            return None

        if _2690.CylindricalGearSetSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spindle_analyses(self) -> '_2750.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'SpindleAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpindleAnalyses

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_static_analyses(self) -> 'List[_2644.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'BearingStaticAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingStaticAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_fit_details(self) -> 'List[_2747.ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'FlexiblePinFitDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinFitDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def load_sharing_factor_reporters(self) -> 'List[_2724.LoadSharingFactorReporter]':
        """List[LoadSharingFactorReporter]: 'LoadSharingFactorReporters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadSharingFactorReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def observed_pin_stiffness_reporters(self) -> 'List[_2729.ObservedPinStiffnessReporter]':
        """List[ObservedPinStiffnessReporter]: 'ObservedPinStiffnessReporters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ObservedPinStiffnessReporters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def pin_spindle_fit_analyses(self) -> 'List[_2747.ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'PinSpindleFitAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinSpindleFitAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_gear_system_deflections(self) -> 'List[_2691.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'PlanetGearSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGearSystemDeflections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
