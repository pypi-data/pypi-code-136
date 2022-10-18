"""_2596.py

SteadyStateSynchronousResponseOnAShaftAnalysis
"""


from mastapy.system_model.analyses_and_results import _2571
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SteadyStateSynchronousResponseOnAShaftAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseOnAShaftAnalysis',)


class SteadyStateSynchronousResponseOnAShaftAnalysis(_2571.SingleAnalysis):
    """SteadyStateSynchronousResponseOnAShaftAnalysis

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT_ANALYSIS

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseOnAShaftAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
