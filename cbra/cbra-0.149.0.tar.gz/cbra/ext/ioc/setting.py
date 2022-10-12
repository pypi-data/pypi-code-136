"""Declares :class:`Setting`."""
from cbra.conf import settings
from .dependency import Dependency


class Setting(Dependency):
    """A :class:`cbra.Dependency` implementation that points to a setting."""
    __module__: str = 'cbra.ext.ioc'

    def __init__(self, name: str):
        self.name = name
        super().__init__(use_cache=True)

    async def resolve(self):
        return getattr(settings, self.name)
