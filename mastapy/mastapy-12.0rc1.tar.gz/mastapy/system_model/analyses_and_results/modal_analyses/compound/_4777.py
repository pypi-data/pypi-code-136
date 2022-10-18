"""_4777.py

StraightBevelGearSetCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2499
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4633
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4775, _4776, _4685
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'StraightBevelGearSetCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetCompoundModalAnalysis',)


class StraightBevelGearSetCompoundModalAnalysis(_4685.BevelGearSetCompoundModalAnalysis):
    """StraightBevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2499.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4633.StraightBevelGearSetModalAnalysis]':
        """List[StraightBevelGearSetModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_compound_modal_analysis(self) -> 'List[_4775.StraightBevelGearCompoundModalAnalysis]':
        """List[StraightBevelGearCompoundModalAnalysis]: 'StraightBevelGearsCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_compound_modal_analysis(self) -> 'List[_4776.StraightBevelGearMeshCompoundModalAnalysis]':
        """List[StraightBevelGearMeshCompoundModalAnalysis]: 'StraightBevelMeshesCompoundModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4633.StraightBevelGearSetModalAnalysis]':
        """List[StraightBevelGearSetModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
