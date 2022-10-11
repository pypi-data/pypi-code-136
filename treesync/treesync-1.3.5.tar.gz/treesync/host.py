"""
Target host configured in treesync settings
"""
from collections.abc import Iterator, MutableMapping
from typing import Optional


# pylint: disable=too-few-public-methods
class TargetHost:
    """
    Treesync sync target host
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


class Hosts(MutableMapping):
    """
    Loader for sync target hosts
    """
    def __init__(self):
        self.__items__ = {}

    def __delitem__(self, name: str) -> None:
        del self.__items__[name]

    def __getitem__(self, name: str) -> Optional[TargetHost]:
        return self.__items__[name]

    def __iter__(self) -> Iterator[TargetHost]:
        return iter(self.__items__)

    def __len__(self) -> int:
        return len(self.__items__)

    def __setitem__(self, name: str, host: TargetHost) -> None:
        self.__items__[name] = host

    # pylint: disable=arguments-differ
    def get(self, name: str) -> TargetHost:
        """
        Get a host, create new item if not found
        """
        if name in self:
            return self[name]
        host = TargetHost(name)
        self[host.name] = host
        return host
