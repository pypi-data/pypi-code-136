"""_39.py

ShaftSettingsDatabase
"""


from mastapy.utility.databases import _1791
from mastapy.shafts import _40
from mastapy._internal.python_net import python_net_import

_SHAFT_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Shafts', 'ShaftSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSettingsDatabase',)


class ShaftSettingsDatabase(_1791.NamedDatabase['_40.ShaftSettingsItem']):
    """ShaftSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _SHAFT_SETTINGS_DATABASE

    def __init__(self, instance_to_wrap: 'ShaftSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
