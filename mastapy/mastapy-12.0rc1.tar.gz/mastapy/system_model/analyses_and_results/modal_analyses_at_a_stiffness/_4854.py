"""_4854.py

FlexiblePinAssemblyModalAnalysisAtAStiffness
"""


from mastapy.system_model.part_model import _2406
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6814
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4895
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'FlexiblePinAssemblyModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyModalAnalysisAtAStiffness',)


class FlexiblePinAssemblyModalAnalysisAtAStiffness(_4895.SpecialisedAssemblyModalAnalysisAtAStiffness):
    """FlexiblePinAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2406.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6814.FlexiblePinAssemblyLoadCase':
        """FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
