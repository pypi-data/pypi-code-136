"""_1790.py

DatabaseSettings
"""


from mastapy.utility.databases import _1788
from mastapy._internal import constructor
from mastapy.utility import _1559
from mastapy._internal.python_net import python_net_import

_DATABASE_SETTINGS = python_net_import('SMT.MastaAPI.Utility.Databases', 'DatabaseSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('DatabaseSettings',)


class DatabaseSettings(_1559.PerMachineSettings):
    """DatabaseSettings

    This is a mastapy class.
    """

    TYPE = _DATABASE_SETTINGS

    def __init__(self, instance_to_wrap: 'DatabaseSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_settings(self) -> '_1788.DatabaseConnectionSettings':
        """DatabaseConnectionSettings: 'ConnectionSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
