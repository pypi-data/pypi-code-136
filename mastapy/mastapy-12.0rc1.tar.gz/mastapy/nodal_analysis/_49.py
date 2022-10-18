"""_49.py

AnalysisSettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.nodal_analysis import _50
from mastapy._internal.python_net import python_net_import

_ANALYSIS_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.NodalAnalysis', 'AnalysisSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisSettingsDatabase',)


class AnalysisSettingsDatabase(_1791.NamedDatabase['_50.AnalysisSettingsItem']):
    """AnalysisSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'AnalysisSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
