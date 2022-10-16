import os
import sys
from typing import cast

from insanic.commands import (
    AsyncCommand,
    CommandParser,
    SyncCommand,
)
from insanic.commands.migrations import (
    MigrationsApplyCommand,
    MigrationsGenerateCommand,
    MigrationsListCommand,
)
from insanic.commands.routes import RoutesCommand
from insanic.commands.server import ServerCommand
from insanic.commands.tasks import TasksQueueCommand
from insanic.utils import run_async

# @TODO: Implement dynamic commands loading
def load_commands() -> dict[str, AsyncCommand | SyncCommand]:
    return {
        'routes': RoutesCommand(),
        'server': ServerCommand(),

        'tasks_queue': TasksQueueCommand(),

        'migrations:apply': MigrationsApplyCommand(),
        'migrations:generate': MigrationsGenerateCommand(),
        'migrations:list': MigrationsListCommand(),
    }

def execute() -> None:
    # Adding `./src` into sys path to be able to import relative modules
    app_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'src')
    sys.path = [app_path] + sys.path

    parser = CommandParser(prog='Insanic CLI')
    subparsers = parser.add_subparsers(dest='command_name')

    commands = load_commands()

    # @TODO: Sort commands
    for name, command in commands.items():
        subparser = subparsers.add_parser(name, help=command.help)
        command.add_arguments(cast(CommandParser, subparser))

    cli_args = parser.parse_args().__dict__

    command_name = cli_args.pop('command_name', None)
    if not command_name:
        parser.print_help()
        sys.exit()

    # @TODO: Handle error
    command = commands[command_name]
    if isinstance(command, AsyncCommand):
        run_async(command.execute_with_context(**cli_args))
    else:
        command.execute(**cli_args)
