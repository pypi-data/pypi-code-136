"""_2984.py

FaceGearSetSteadyStateSynchronousResponse
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6812
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2985, _2983, _2989
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'FaceGearSetSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetSteadyStateSynchronousResponse',)


class FaceGearSetSteadyStateSynchronousResponse(_2989.GearSetSteadyStateSynchronousResponse):
    """FaceGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    def __init__(self, instance_to_wrap: 'FaceGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6812.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears_steady_state_synchronous_response(self) -> 'List[_2985.FaceGearSteadyStateSynchronousResponse]':
        """List[FaceGearSteadyStateSynchronousResponse]: 'FaceGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_steady_state_synchronous_response(self) -> 'List[_2983.FaceGearMeshSteadyStateSynchronousResponse]':
        """List[FaceGearMeshSteadyStateSynchronousResponse]: 'FaceMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
