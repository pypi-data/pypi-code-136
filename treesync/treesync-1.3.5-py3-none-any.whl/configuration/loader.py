"""
Configuration loader for treesync
"""
from fnmatch import fnmatch
from typing import List, Optional

from sys_toolkit.configuration.yaml import YamlConfiguration

from ..constants import DEFAULT_CONFIGURATION_PATHS
from ..target import Target, TargetList

from .defaults import Defaults
from .hosts import HostsSettings
from .servers import ServersConfigurationSection
from .sources import SourcesConfigurationSection
from .targets import TargetsConfigurationSection


class Configuration(YamlConfiguration):
    """
    Yaml configuration file for 'treesync' CLI
    """
    defaults: Optional[Defaults] = None
    hosts: Optional[HostsSettings] = None
    servers: Optional[ServersConfigurationSection] = None
    sources: Optional[SourcesConfigurationSection] = None
    targets: Optional[TargetsConfigurationSection] = None
    __sync_targets__: Optional[TargetList] = None

    __default_paths__ = []
    __section_loaders__ = (
        Defaults,
        HostsSettings,
        ServersConfigurationSection,
        SourcesConfigurationSection,
        TargetsConfigurationSection,
    )

    def __init__(self, path=None, parent=None, debug_enabled=False, silent=False) -> None:
        self.__default_paths__ = DEFAULT_CONFIGURATION_PATHS
        super().__init__(path, parent, debug_enabled, silent)

    def __repr__(self) -> str:
        return 'treesync config'

    @property
    def sync_targets(self) -> List[Target]:
        """
        Get configured sync targets
        """
        if self.__sync_targets__ is None:
            targets = TargetList()
            for host in self.hosts:  # pylint: disable=not-an-iterable
                for target in host.sync_targets:
                    targets.append(target)
            for target in self.targets.sync_targets:  # pylint: disable=not-an-iterable
                if target not in targets:
                    targets.append(target)
            targets.sort()
            self.__sync_targets__ = targets
        return self.__sync_targets__

    def filter_sync_targets(self, patterns: List[str]) -> List[Target]:
        """
        Filter sync targets by list of patterns as strings
        """
        def match_patterns(patterns, target):
            """
            Match target to specified patterns
            """
            for pattern in patterns:
                if target.hostname and fnmatch(target.hostname, pattern):
                    return True
                if str(target.name) == pattern or fnmatch(str(target.name), pattern):
                    return True
                try:
                    _host, name = target.name.split(':', 1)
                    if fnmatch(name, pattern):
                        return True
                except ValueError:
                    pass
            return False

        matches = []
        if not patterns:
            return self.sync_targets
        for target in self.sync_targets:
            if match_patterns(patterns, target):
                matches.append(target)
        return matches
