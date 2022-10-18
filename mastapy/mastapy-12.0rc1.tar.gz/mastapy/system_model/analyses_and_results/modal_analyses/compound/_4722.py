"""_4722.py

FaceGearSetCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4572
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4720, _4721, _4727
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'FaceGearSetCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundModalAnalysis',)


class FaceGearSetCompoundModalAnalysis(_4727.GearSetCompoundModalAnalysis):
    """FaceGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2480.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_4572.FaceGearSetModalAnalysis]':
        """List[FaceGearSetModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_compound_modal_analysis(self) -> 'List[_4720.FaceGearCompoundModalAnalysis]':
        """List[FaceGearCompoundModalAnalysis]: 'FaceGearsCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_compound_modal_analysis(self) -> 'List[_4721.FaceGearMeshCompoundModalAnalysis]':
        """List[FaceGearMeshCompoundModalAnalysis]: 'FaceMeshesCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4572.FaceGearSetModalAnalysis]':
        """List[FaceGearSetModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
