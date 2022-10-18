"""_5213.py

ConceptGearCompoundModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2472
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5085
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5242
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'ConceptGearCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundModalAnalysisAtASpeed',)


class ConceptGearCompoundModalAnalysisAtASpeed(_5242.GearCompoundModalAnalysisAtASpeed):
    """ConceptGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2472.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5085.ConceptGearModalAnalysisAtASpeed]':
        """List[ConceptGearModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5085.ConceptGearModalAnalysisAtASpeed]':
        """List[ConceptGearModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
