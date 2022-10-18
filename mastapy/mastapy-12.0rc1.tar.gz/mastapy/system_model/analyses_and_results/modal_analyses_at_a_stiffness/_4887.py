"""_4887.py

RingPinsToDiscConnectionModalAnalysisAtAStiffness
"""


from mastapy.system_model.connections_and_sockets.cycloidal import _2293
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6870
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4862
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'RingPinsToDiscConnectionModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionModalAnalysisAtAStiffness',)


class RingPinsToDiscConnectionModalAnalysisAtAStiffness(_4862.InterMountableComponentConnectionModalAnalysisAtAStiffness):
    """RingPinsToDiscConnectionModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2293.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6870.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
