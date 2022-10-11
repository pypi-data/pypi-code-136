"""
Treesync 'list' subcommand
"""

from argparse import ArgumentParser, Namespace

from .base import TreesyncCommand

DESCRIPTION = """
List configured sync targets
"""


class List(TreesyncCommand):
    """
    Tree pull subcommand
    """
    description = DESCRIPTION
    name = 'list'

    def register_parser_arguments(self, parser: ArgumentParser) -> ArgumentParser:
        """
        Register only common base arguments
        """
        return super().register_common_arguments(parser)

    def run(self, args: Namespace) -> None:
        """
        List configured sync targets
        """
        for target in self.filter_targets(args.targets):
            self.message(f'{target.name}')
