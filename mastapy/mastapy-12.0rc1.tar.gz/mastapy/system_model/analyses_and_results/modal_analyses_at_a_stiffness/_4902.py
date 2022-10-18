"""_4902.py

StraightBevelDiffGearMeshModalAnalysisAtAStiffness
"""


from mastapy.system_model.connections_and_sockets.gears import _2277
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6886
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4812
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'StraightBevelDiffGearMeshModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshModalAnalysisAtAStiffness',)


class StraightBevelDiffGearMeshModalAnalysisAtAStiffness(_4812.BevelGearMeshModalAnalysisAtAStiffness):
    """StraightBevelDiffGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2277.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6886.StraightBevelDiffGearMeshLoadCase':
        """StraightBevelDiffGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
