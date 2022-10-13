from __future__ import annotations

from cleo.helpers import argument
from poetry.console.commands.command import Command

from poetry_aliases_plugin import utils


def normalize_command(command: str) -> str:
    command = command.removeprefix('poetry').strip()
    command = command if command.startswith('run') else f'run {command}'
    return command.strip()


class AliasCommand(Command):
    name = 'l'

    arguments = [argument('alias', 'Registered alias')]

    @property
    def description(self):
        return 'Run aliases. Available: {0}'.format(', '.join(self.config_aliases))

    @property
    def config_aliases(self) -> dict:
        return self.poetry.pyproject.data.get('tool', {}).get('aliases', utils.default_aliases)

    @property
    def target_alias(self):
        return self.argument('alias')

    @property
    def target_commands(self) -> list[str]:
        command_raw: str = self.config_aliases[self.target_alias]
        return [normalize_command(command) for command in command_raw.split('&&')]

    def exec_command(self, command: str):
        try:
            self.call('run', command)

        except PermissionError as ex:
            if ex.errno == 13:
                raise utils.PluginException(f'У процесса poetry недостаточно прав для запуска программы: {ex.filename}')

            raise ex

        raise utils.PluginException('wtf')

    def exec_commands(self):
        for command in self.target_commands:
            self.exec_command(command)

    @utils.plugin_exception_wrapper
    def handle(self) -> None:
        if self.target_alias not in self.config_aliases:
            raise utils.PluginException(f'alias "{self.target_alias}" not found')

        self.exec_commands()
