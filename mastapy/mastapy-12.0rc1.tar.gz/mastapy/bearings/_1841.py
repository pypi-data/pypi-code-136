"""_1841.py

BearingSettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.bearings import _1842
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettingsDatabase',)


class BearingSettingsDatabase(_1791.NamedDatabase['_1842.BearingSettingsItem']):
    """BearingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'BearingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
