"""_3825.py

SynchroniserHalfStabilityAnalysis
"""


from mastapy.system_model.part_model.couplings import _2555
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6893
from mastapy.system_model.analyses_and_results.stability_analyses import _3826
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'SynchroniserHalfStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfStabilityAnalysis',)


class SynchroniserHalfStabilityAnalysis(_3826.SynchroniserPartStabilityAnalysis):
    """SynchroniserHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'SynchroniserHalfStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6893.SynchroniserHalfLoadCase':
        """SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
