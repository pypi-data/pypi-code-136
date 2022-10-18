"""_4147.py

CouplingConnectionCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4013
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4174
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CouplingConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundPowerFlow',)


class CouplingConnectionCompoundPowerFlow(_4174.InterMountableComponentConnectionCompoundPowerFlow):
    """CouplingConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_POWER_FLOW

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_4013.CouplingConnectionPowerFlow]':
        """List[CouplingConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4013.CouplingConnectionPowerFlow]':
        """List[CouplingConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
