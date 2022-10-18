"""_6288.py

PartToPartShearCouplingHalfDynamicAnalysis
"""


from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6856
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6244
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'PartToPartShearCouplingHalfDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfDynamicAnalysis',)


class PartToPartShearCouplingHalfDynamicAnalysis(_6244.CouplingHalfDynamicAnalysis):
    """PartToPartShearCouplingHalfDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6856.PartToPartShearCouplingHalfLoadCase':
        """PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
