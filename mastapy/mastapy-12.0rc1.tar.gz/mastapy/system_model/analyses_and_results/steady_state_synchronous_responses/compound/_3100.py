"""_3100.py

CouplingConnectionCompoundSteadyStateSynchronousResponse
"""


from typing import List

from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2966
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3127
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'CouplingConnectionCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingConnectionCompoundSteadyStateSynchronousResponse',)


class CouplingConnectionCompoundSteadyStateSynchronousResponse(_3127.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse):
    """CouplingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    def __init__(self, instance_to_wrap: 'CouplingConnectionCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_2966.CouplingConnectionSteadyStateSynchronousResponse]':
        """List[CouplingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2966.CouplingConnectionSteadyStateSynchronousResponse]':
        """List[CouplingConnectionSteadyStateSynchronousResponse]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
