"""_48.py

AnalysisSettings
"""


from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS = python_net_import('SMT.MastaAPI.NodalAnalysis', 'AnalysisSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisSettings',)


class AnalysisSettings(_0.APIBase):
    """AnalysisSettings

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS

    def __init__(self, instance_to_wrap: 'AnalysisSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
