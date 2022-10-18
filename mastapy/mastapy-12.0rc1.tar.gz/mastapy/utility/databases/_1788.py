"""_1788.py

DatabaseConnectionSettings
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATABASE_CONNECTION_SETTINGS = python_net_import('SMT.MastaAPI.Utility.Databases', 'DatabaseConnectionSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('DatabaseConnectionSettings',)


class DatabaseConnectionSettings(_0.APIBase):
    """DatabaseConnectionSettings

    This is a mastapy class.
    """

    TYPE = _DATABASE_CONNECTION_SETTINGS

    def __init__(self, instance_to_wrap: 'DatabaseConnectionSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def can_use_local_db(self) -> 'bool':
        """bool: 'CanUseLocalDB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CanUseLocalDB

        if temp is None:
            return False

        return temp

    @property
    def display_sql_connection_integrated_security(self) -> 'bool':
        """bool: 'DisplaySQLConnectionIntegratedSecurity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DisplaySQLConnectionIntegratedSecurity

        if temp is None:
            return False

        return temp

    @property
    def force_use_of_local_db2012(self) -> 'bool':
        """bool: 'ForceUseOfLocalDB2012' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceUseOfLocalDB2012

        if temp is None:
            return False

        return temp

    @property
    def is_local_db_path_specified(self) -> 'bool':
        """bool: 'IsLocalDBPathSpecified' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLocalDBPathSpecified

        if temp is None:
            return False

        return temp

    @property
    def local_db_file_path(self) -> 'str':
        """str: 'LocalDBFilePath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LocalDBFilePath

        if temp is None:
            return ''

        return temp

    @property
    def network_connection_string(self) -> 'str':
        """str: 'NetworkConnectionString' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NetworkConnectionString

        if temp is None:
            return ''

        return temp

    @property
    def sql_connection_db_name(self) -> 'str':
        """str: 'SQLConnectionDbName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SQLConnectionDbName

        if temp is None:
            return ''

        return temp

    @property
    def sql_connection_integrated_security(self) -> 'bool':
        """bool: 'SQLConnectionIntegratedSecurity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SQLConnectionIntegratedSecurity

        if temp is None:
            return False

        return temp

    @property
    def sql_connection_server_name(self) -> 'str':
        """str: 'SQLConnectionServerName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SQLConnectionServerName

        if temp is None:
            return ''

        return temp

    @property
    def sql_connection_user_name(self) -> 'str':
        """str: 'SQLConnectionUserName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SQLConnectionUserName

        if temp is None:
            return ''

        return temp

    @property
    def specified_local_db_file_path(self) -> 'str':
        """str: 'SpecifiedLocalDBFilePath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedLocalDBFilePath

        if temp is None:
            return ''

        return temp

    @property
    def use_file_db(self) -> 'bool':
        """bool: 'UseFileDB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UseFileDB

        if temp is None:
            return False

        return temp

    @property
    def use_local_database(self) -> 'bool':
        """bool: 'UseLocalDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UseLocalDatabase

        if temp is None:
            return False

        return temp

    @property
    def use_network_database(self) -> 'bool':
        """bool: 'UseNetworkDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UseNetworkDatabase

        if temp is None:
            return False

        return temp

    @property
    def uses_network_database_or_local_database_is_on_network_path(self) -> 'bool':
        """bool: 'UsesNetworkDatabaseOrLocalDatabaseIsOnNetworkPath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UsesNetworkDatabaseOrLocalDatabaseIsOnNetworkPath

        if temp is None:
            return False

        return temp
