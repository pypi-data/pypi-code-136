"""_6197.py

FlexiblePinAnalysis
"""


from mastapy.system_model.analyses_and_results.flexible_pin_analyses import _6202, _6196
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses', 'FlexiblePinAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAnalysis',)


class FlexiblePinAnalysis(_6196.CombinationAnalysis):
    """FlexiblePinAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS

    def __init__(self, instance_to_wrap: 'FlexiblePinAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_options(self) -> '_6202.FlexiblePinAnalysisOptions':
        """FlexiblePinAnalysisOptions: 'AnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
