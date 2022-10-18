"""_5700.py

HarmonicAnalysisShaftExportOptions
"""


from mastapy.system_model.analyses_and_results.harmonic_analyses import _5696
from mastapy.system_model.analyses_and_results import _2607
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_SHAFT_EXPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'HarmonicAnalysisShaftExportOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicAnalysisShaftExportOptions',)


class HarmonicAnalysisShaftExportOptions(_5696.HarmonicAnalysisExportOptions['_2607.IHaveShaftHarmonicResults', '_2434.Shaft']):
    """HarmonicAnalysisShaftExportOptions

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_SHAFT_EXPORT_OPTIONS

    def __init__(self, instance_to_wrap: 'HarmonicAnalysisShaftExportOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
