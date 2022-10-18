"""_4180.py

KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2490
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4048
from mastapy.system_model.analyses_and_results.power_flows.compound import _4178, _4179, _4177
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow(_4177.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow):
    """KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4048.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_power_flow(self) -> 'List[_4178.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow]: 'KlingelnbergCycloPalloidHypoidGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_power_flow(self) -> 'List[_4179.KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshCompoundPowerFlow]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4048.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]':
        """List[KlingelnbergCycloPalloidHypoidGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
