"""
Settings for as server in treesync configuration
"""
from sys_toolkit.configuration.base import ConfigurationSection


class ServersConfigurationSection(ConfigurationSection):
    """
    Server specific common sync settings by server name

    Since server names can contain letters that are not valid python identifiers
    this category is handled as special case unlike normal ConfigurationSection
    """
    __name__ = 'servers'

    def __getattribute__(self, attr: str):
        """
        Return server by name
        """
        try:
            settings = super().__getattribute__('__server_settings__')
            if attr in settings:
                return settings[attr]
        except AttributeError:
            pass
        return super().__getattribute__(attr)

    def __load_dictionary__(self, data: dict) -> None:
        """
        Load server flag data from dictionary. Keys in dictionary are not required
        to be valid python identifiers
        """
        self.__server_settings__ = {}
        for server, settings in data.items():
            # Ensure [] and None are cast to empty settings
            if not settings:
                settings = {}
            self.__server_settings__[server] = settings
