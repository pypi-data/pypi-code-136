"""_3804.py

RootAssemblyStabilityAnalysis
"""


from mastapy.system_model.part_model import _2426
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _2593, _3716
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'RootAssemblyStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyStabilityAnalysis',)


class RootAssemblyStabilityAnalysis(_3716.AssemblyStabilityAnalysis):
    """RootAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'RootAssemblyStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2426.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis_inputs(self) -> '_2593.StabilityAnalysis':
        """StabilityAnalysis: 'StabilityAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
