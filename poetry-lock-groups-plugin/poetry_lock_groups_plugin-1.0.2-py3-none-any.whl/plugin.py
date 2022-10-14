from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_lock_groups.ExtendedLockCommand import ExtendedLockCommand


def extendedLockCommandFactory():
    return ExtendedLockCommand()


class LockGroupsPlugin(ApplicationPlugin):
    def activate(self, application: Application) -> None:
        application.command_loader._factories.pop("lock")
        application.command_loader.register_factory("lock", extendedLockCommandFactory)
