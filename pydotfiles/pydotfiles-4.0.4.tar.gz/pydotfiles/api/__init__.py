# General imports
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from pathlib import Path
from os import getcwd
from logging import getLogger
from json import dumps as json_dumps

# Project imports
from .deprecated import ArgumentDispatcher
from pydotfiles.v4.builder import Builder
from pydotfiles.v4.loader import load_configuration
from pydotfiles import __version__ as version
from pydotfiles.v4.logging import set_logging
from pydotfiles.v4.common import PydotfilesError
from pydotfiles.v4.logging import PrettyPrint

logger = getLogger(__name__)


class ArgumentDispatcherFacade:
    def __init__(self, api_arguments: list[str]):
        self.api_arguments = api_arguments
        self.deprecated_dispatcher = ArgumentDispatcher(api_arguments)

    def dispatch(self) -> None:
        valid_commands = {
            'download',
            'install',
            'uninstall',
            'update',
            'clean',
            'set',
            'validate',
            'build',
        }

        parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter, description="""
        Python Dotfiles Manager, enabling configuration-based management of your system!

        Commands:
          - download: Downloads your dotfiles onto your computer
          - install: Installs all/part of your dotfiles
          - uninstall: Uninstalls all/part of your dotfiles
          - update: Updates all/part of your dotfiles
          - clean: Removes the pydotfiles cache/default
          - set: Sets configuration values for managing your dotfiles
          - validate: Validates that a given directory is pydotfiles-compliant
          - build: Generates dotfile profile builder packages (can be used as part of a CI/CD pipeline)
        """)
        parser.add_argument('--version', action='version', version='%(prog)s ' + version)
        parser.add_argument("command", help="Runs the command given", choices=valid_commands)

        command = self.api_arguments[1:2]
        command_arguments = self.api_arguments[2:]

        args = parser.parse_args(command)

        # Dynamically dispatches to the relevant method
        if command[0] == "build":
            getattr(self, args.command)(command_arguments)
            return

        try:
            getattr(self.deprecated_dispatcher, args.command)(command_arguments)
        except PydotfilesError as e:
            logger.exception(f"an error occurred: {e.context_map}")

    def build(self, command_arguments: list[str]) -> None:
        help_description = """
        Builds any/all profiles into self-contained builder packages, which can be easily downloaded
        and installed without having to install/run pydotfiles.

        (default: Checks the current working directory)
        """
        parser = self.__get_base_parser(help_description, "build")
        parser.add_argument("-d", "--directory", help="Builds all/indicated profile build packages located in the passed-in directory. Defaults to the current working directory", default=getcwd())
        parser.add_argument("-p", "--profiles", nargs='+', help="Indicates which profiles should be built, and how they should be composed. Defaults to all profiles being built independently")
        parser.add_argument("-o", "--operating-systems", nargs='+', help="Indicates which operating system build packages should be built. Defaults to all profiles being built independently")

        args = parser.parse_args(command_arguments)

        set_logging(args.quiet, args.verbose)

        configurations = load_configuration(Path(args.directory))
        builder = Builder(configurations, Path(args.directory))
        build_packages = builder.build(args.profiles, args.operating_systems)
        for name, build_package_path in build_packages.items():
            PrettyPrint.success(f"[{name}]\tSuccessfully generated build package in: {build_package_path}")

    @staticmethod
    def __get_base_parser(description: str, sub_command: str) -> ArgumentParser:
        parser = ArgumentParser(
            prog=f"pydotfiles {sub_command}",
            formatter_class=RawDescriptionHelpFormatter,
            description=description
        )
        logging_parser_group = parser.add_mutually_exclusive_group()
        logging_parser_group.add_argument("-v", "--verbose", help="Enables more verbose logging", action="store_true")
        logging_parser_group.add_argument("-q", "--quiet", help="Squelches the default logging (still outputs to stderr upon failures)", action="store_true")
        return parser
