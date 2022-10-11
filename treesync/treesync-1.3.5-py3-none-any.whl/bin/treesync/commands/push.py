"""
Treesync 'push' subcommand
"""
from argparse import ArgumentParser, Namespace

from treesync.exceptions import SyncError

from .base import TreesyncCommand

DESCRIPTION = """
Push directories to remote targets
"""


class Push(TreesyncCommand):
    """
    Tree push subcommand
    """
    description = DESCRIPTION
    name = 'push'

    def register_parser_arguments(self, parser: ArgumentParser) -> ArgumentParser:
        """
        Register arguments for 'pull' command
        """
        return super().register_rsync_arguments(parser)

    def run(self, args: Namespace) -> None:
        """
        Push specified targets
        """
        if not args.targets:
            self.exit(1, 'No targets specified')
        targets = self.filter_targets(args.targets)
        if not targets:
            self.exit(1, 'No targets specified')

        errors = False
        for target in targets:
            try:
                self.message(f'push {target.source} -> {target.destination}')
                target.push(dry_run=args.dry_run)
            except SyncError as error:
                self.error(error)
                errors = True
        if errors:
            self.exit(1, 'Errors pushing targets')
