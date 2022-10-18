"""_3033.py

SpringDamperHalfSteadyStateSynchronousResponse
"""


from mastapy.system_model.part_model.couplings import _2552
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6883
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2967
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'SpringDamperHalfSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfSteadyStateSynchronousResponse',)


class SpringDamperHalfSteadyStateSynchronousResponse(_2967.CouplingHalfSteadyStateSynchronousResponse):
    """SpringDamperHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE

    def __init__(self, instance_to_wrap: 'SpringDamperHalfSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6883.SpringDamperHalfLoadCase':
        """SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
