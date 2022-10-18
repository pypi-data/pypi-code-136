"""_3471.py

ClutchConnectionSteadyStateSynchronousResponseAtASpeed
"""


from mastapy.system_model.connections_and_sockets.couplings import _2294
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6759
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3487
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'ClutchConnectionSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionSteadyStateSynchronousResponseAtASpeed',)


class ClutchConnectionSteadyStateSynchronousResponseAtASpeed(_3487.CouplingConnectionSteadyStateSynchronousResponseAtASpeed):
    """ClutchConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'ClutchConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2294.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6759.ClutchConnectionLoadCase':
        """ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
