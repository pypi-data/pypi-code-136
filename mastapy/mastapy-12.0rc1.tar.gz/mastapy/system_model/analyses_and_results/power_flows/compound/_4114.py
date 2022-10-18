"""_4114.py

AGMAGleasonConicalGearMeshCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _3980
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4142
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'AGMAGleasonConicalGearMeshCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundPowerFlow',)


class AGMAGleasonConicalGearMeshCompoundPowerFlow(_4142.ConicalGearMeshCompoundPowerFlow):
    """AGMAGleasonConicalGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_3980.AGMAGleasonConicalGearMeshPowerFlow]':
        """List[AGMAGleasonConicalGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_3980.AGMAGleasonConicalGearMeshPowerFlow]':
        """List[AGMAGleasonConicalGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
