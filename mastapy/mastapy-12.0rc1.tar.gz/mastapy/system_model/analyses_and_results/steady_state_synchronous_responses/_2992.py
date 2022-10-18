"""_2992.py

HypoidGearMeshSteadyStateSynchronousResponse
"""


from mastapy.system_model.connections_and_sockets.gears import _2267
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6832
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2933
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'HypoidGearMeshSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshSteadyStateSynchronousResponse',)


class HypoidGearMeshSteadyStateSynchronousResponse(_2933.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse):
    """HypoidGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE

    def __init__(self, instance_to_wrap: 'HypoidGearMeshSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2267.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6832.HypoidGearMeshLoadCase':
        """HypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
