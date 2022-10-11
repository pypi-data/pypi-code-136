"""
Sources configuration for treesync
"""
from typing import Optional

from sys_toolkit.configuration.base import ConfigurationSection, ConfigurationList


class SourceConfiguration(ConfigurationSection):
    """
    A single sync source condiguration item
    """
    name: str = ''
    path: str = ''

    __required_settings__ = (
        'name',
        'path',
    )
    __path_settings__ = (
        'path',
    )

    def __repr__(self):
        return f'{self.name} {self.path}'


class SourcesConfigurationSection(ConfigurationList):
    """
    Configuration for sync sources
    """
    __name__ = 'sources'
    __dict_loader_class__ = SourceConfiguration

    def get(self, name: str) -> Optional[SourceConfiguration]:
        """
        Get source configuration matching name
        """
        for source in self:
            if source.name == name:
                return source
        return None
