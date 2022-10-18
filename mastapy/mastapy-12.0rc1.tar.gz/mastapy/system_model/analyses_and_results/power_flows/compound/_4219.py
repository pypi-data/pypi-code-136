"""_4219.py

StraightBevelGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2499
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4089
from mastapy.system_model.analyses_and_results.power_flows.compound import _4217, _4218, _4127
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'StraightBevelGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetCompoundPowerFlow',)


class StraightBevelGearSetCompoundPowerFlow(_4127.BevelGearSetCompoundPowerFlow):
    """StraightBevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4089.StraightBevelGearSetPowerFlow]':
        """List[StraightBevelGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_compound_power_flow(self) -> 'List[_4217.StraightBevelGearCompoundPowerFlow]':
        """List[StraightBevelGearCompoundPowerFlow]: 'StraightBevelGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_compound_power_flow(self) -> 'List[_4218.StraightBevelGearMeshCompoundPowerFlow]':
        """List[StraightBevelGearMeshCompoundPowerFlow]: 'StraightBevelMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesCompoundPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4089.StraightBevelGearSetPowerFlow]':
        """List[StraightBevelGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
