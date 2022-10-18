"""_4869.py

KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
"""


from mastapy.system_model.connections_and_sockets.gears import _2272
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6845
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4863
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness',)


class KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness(_4863.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2272.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6845.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
