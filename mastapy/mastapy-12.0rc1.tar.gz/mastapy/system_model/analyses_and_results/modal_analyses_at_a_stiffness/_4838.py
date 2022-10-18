"""_4838.py

CVTPulleyModalAnalysisAtAStiffness
"""


from mastapy.system_model.part_model.couplings import _2538
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4885
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'CVTPulleyModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyModalAnalysisAtAStiffness',)


class CVTPulleyModalAnalysisAtAStiffness(_4885.PulleyModalAnalysisAtAStiffness):
    """CVTPulleyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'CVTPulleyModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2538.CVTPulley':
        """CVTPulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
