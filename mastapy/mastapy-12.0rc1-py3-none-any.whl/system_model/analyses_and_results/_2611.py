"""_2611.py

CompoundAdvancedTimeSteppingAnalysisForModulation
"""


from mastapy.system_model.analyses_and_results import _2570
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAdvancedTimeSteppingAnalysisForModulation',)


class CompoundAdvancedTimeSteppingAnalysisForModulation(_2570.CompoundAnalysis):
    """CompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    def __init__(self, instance_to_wrap: 'CompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
