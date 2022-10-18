"""_6263.py

FlexiblePinAssemblyDynamicAnalysis
"""


from mastapy.system_model.part_model import _2406
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6814
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'FlexiblePinAssemblyDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyDynamicAnalysis',)


class FlexiblePinAssemblyDynamicAnalysis(_6304.SpecialisedAssemblyDynamicAnalysis):
    """FlexiblePinAssemblyDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyDynamicAnalysis.TYPE'):
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
