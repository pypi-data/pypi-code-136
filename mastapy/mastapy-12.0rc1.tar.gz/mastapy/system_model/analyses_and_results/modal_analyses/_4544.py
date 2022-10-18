"""_4544.py

ConceptGearModalAnalysis
"""


from mastapy.system_model.part_model.gears import _2472
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6767
from mastapy.system_model.analyses_and_results.system_deflections import _2668
from mastapy.system_model.analyses_and_results.modal_analyses import _4577
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ConceptGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearModalAnalysis',)


class ConceptGearModalAnalysis(_4577.GearModalAnalysis):
    """ConceptGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConceptGearModalAnalysis.TYPE'):
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
    def component_load_case(self) -> '_6767.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2668.ConceptGearSystemDeflection':
        """ConceptGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
