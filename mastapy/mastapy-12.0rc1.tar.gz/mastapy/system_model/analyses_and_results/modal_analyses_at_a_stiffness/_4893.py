"""_4893.py

ShaftModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.part_model.shaft_model import _2434
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6876
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4797
from mastapy._internal.python_net import python_net_import

_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'ShaftModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftModalAnalysisAtAStiffness',)


class ShaftModalAnalysisAtAStiffness(_4797.AbstractShaftModalAnalysisAtAStiffness):
    """ShaftModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'ShaftModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2434.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6876.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftModalAnalysisAtAStiffness]':
        """List[ShaftModalAnalysisAtAStiffness]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
