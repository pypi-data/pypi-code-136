"""_6489.py

BoltCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model import _2394
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6758
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6495
from mastapy._internal.python_net import python_net_import

_BOLT_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'BoltCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltCriticalSpeedAnalysis',)


class BoltCriticalSpeedAnalysis(_6495.ComponentCriticalSpeedAnalysis):
    """BoltCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLT_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'BoltCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2394.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6758.BoltLoadCase':
        """BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
