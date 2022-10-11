
from argparse import ArgumentParser, Namespace
from typing import List

from cli_toolkit.command import Command

from treesync.configuration import Configuration
from treesync.target import Target


class TreesyncCommand(Command):
    """
    Common base class for treesync subcommands
    """
    config: Configuration = None

    @staticmethod
    def register_common_arguments(parser: ArgumentParser) -> ArgumentParser:
        """
        Add parser arguments common to all commands
        """
        parser.add_argument('--config', help='Configuration file path')
        parser.add_argument('targets', nargs='*', help='Sync command targets')
        return parser

    def register_rsync_arguments(self, parser: ArgumentParser) -> ArgumentParser:
        """
        Register arguments specific to rsync commands (pull/push)
        """
        parser = self.register_common_arguments(parser)
        parser.add_argument(
            '-y', '--dry-run',
            action='store_true',
            help='Run rsync with --dry-run flag'
        )
        return parser

    def parse_args(self, args: Namespace = None, namespace: Namespace = None) -> Namespace:
        """
        Parse arguments and append config to command
        """
        self.config = Configuration(args.config)
        return args

    def filter_targets(self, patterns: List[str]) -> List[Target]:
        """
        Filter targets by list of string patterns, returning list of Target objects
        """
        return self.config.filter_sync_targets(patterns)
