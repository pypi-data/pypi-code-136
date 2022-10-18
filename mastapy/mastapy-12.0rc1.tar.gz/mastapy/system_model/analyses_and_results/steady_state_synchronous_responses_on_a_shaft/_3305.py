"""_3305.py

SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
"""


from mastapy.system_model.part_model.couplings import _2555
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6893
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3306
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'SynchroniserHalfSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfSteadyStateSynchronousResponseOnAShaft',)


class SynchroniserHalfSteadyStateSynchronousResponseOnAShaft(_3306.SynchroniserPartSteadyStateSynchronousResponseOnAShaft):
    """SynchroniserHalfSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    def __init__(self, instance_to_wrap: 'SynchroniserHalfSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6893.SynchroniserHalfLoadCase':
        """SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
