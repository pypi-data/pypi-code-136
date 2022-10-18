"""_1935.py

ISO14179SettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.bearings.bearing_results.rolling import _1934
from mastapy._internal.python_net import python_net_import

_ISO14179_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'ISO14179SettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO14179SettingsDatabase',)


class ISO14179SettingsDatabase(_1791.NamedDatabase['_1934.ISO14179Settings']):
    """ISO14179SettingsDatabase

    This is a mastapy class.
    """

    TYPE = _ISO14179_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'ISO14179SettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
