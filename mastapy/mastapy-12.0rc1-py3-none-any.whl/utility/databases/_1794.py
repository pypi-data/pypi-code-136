"""_1794.py

SQLDatabase
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy.utility.databases import _1789, _1792, _1787
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SQL_DATABASE = python_net_import('SMT.MastaAPI.Utility.Databases', 'SQLDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('SQLDatabase',)


TKey = TypeVar('TKey', bound='_1789.DatabaseKey')
TValue = TypeVar('TValue', bound='_0.APIBase')


class SQLDatabase(_1787.Database['TKey', 'TValue'], Generic[TKey, TValue]):
    """SQLDatabase

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _SQL_DATABASE

    def __init__(self, instance_to_wrap: 'SQLDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_network_database(self) -> 'bool':
        """bool: 'AllowNetworkDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowNetworkDatabase

        if temp is None:
            return False

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def uses_database(self) -> 'bool':
        """bool: 'UsesDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UsesDatabase

        if temp is None:
            return False

        return temp

    def delete(self, key: '_1789.DatabaseKey'):
        """ 'Delete' is the original name of this method.

        Args:
            key (mastapy.utility.databases.DatabaseKey)
        """

        self.wrapped.Delete(key.wrapped if key else None)

    def reload(self):
        """ 'Reload' is the original name of this method."""

        self.wrapped.Reload()

    def save(self, item: '_1792.NamedDatabaseItem'):
        """ 'Save' is the original name of this method.

        Args:
            item (mastapy.utility.databases.NamedDatabaseItem)
        """

        self.wrapped.Save(item.wrapped if item else None)
