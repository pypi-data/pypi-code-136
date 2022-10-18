"""_6261.py

FaceGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6812
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6259, _6260, _6266
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'FaceGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetDynamicAnalysis',)


class FaceGearSetDynamicAnalysis(_6266.GearSetDynamicAnalysis):
    """FaceGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetDynamicAnalysis.TYPE'):
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
    def face_gears_dynamic_analysis(self) -> 'List[_6259.FaceGearDynamicAnalysis]':
        """List[FaceGearDynamicAnalysis]: 'FaceGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_dynamic_analysis(self) -> 'List[_6260.FaceGearMeshDynamicAnalysis]':
        """List[FaceGearMeshDynamicAnalysis]: 'FaceMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
