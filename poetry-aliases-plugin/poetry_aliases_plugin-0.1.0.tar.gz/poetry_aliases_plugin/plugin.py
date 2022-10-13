from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.plugins.application_plugin import ApplicationPlugin
from poetry_aliases_plugin.commands import AliasCommand

if TYPE_CHECKING:
    from poetry.console.application import Application
    from poetry.console.commands.command import Command


class PoetryAliasesApplicationPlugin(ApplicationPlugin):
    @property
    def commands(self) -> list[type[Command]]:
        return [AliasCommand]
