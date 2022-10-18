"""_4542.py

ConceptCouplingModalAnalysis
"""


from mastapy.system_model.part_model.couplings import _2532
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6766
from mastapy.system_model.analyses_and_results.system_deflections import _2665
from mastapy.system_model.analyses_and_results.modal_analyses import _4554
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ConceptCouplingModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingModalAnalysis',)


class ConceptCouplingModalAnalysis(_4554.CouplingModalAnalysis):
    """ConceptCouplingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConceptCouplingModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2532.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6766.ConceptCouplingLoadCase':
        """ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2665.ConceptCouplingSystemDeflection':
        """ConceptCouplingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
