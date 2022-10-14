from poetry.console.commands.installer_command import InstallerCommand
from poetry.console.commands.lock import LockCommand


class ExtendedLockCommand(LockCommand):
    name = "lock"

    options = [*InstallerCommand._group_dependency_options(), *LockCommand.options]

    def handle(self) -> int:
        self.installer.set_package(self.project_with_activated_groups_only())
        return super().handle()
