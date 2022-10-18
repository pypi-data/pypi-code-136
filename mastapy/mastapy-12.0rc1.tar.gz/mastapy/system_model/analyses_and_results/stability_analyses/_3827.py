"""_3827.py

SynchroniserSleeveStabilityAnalysis
"""


from mastapy.system_model.part_model.couplings import _2557
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6896
from mastapy.system_model.analyses_and_results.stability_analyses import _3826
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'SynchroniserSleeveStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveStabilityAnalysis',)


class SynchroniserSleeveStabilityAnalysis(_3826.SynchroniserPartStabilityAnalysis):
    """SynchroniserSleeveStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6896.SynchroniserSleeveLoadCase':
        """SynchroniserSleeveLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
