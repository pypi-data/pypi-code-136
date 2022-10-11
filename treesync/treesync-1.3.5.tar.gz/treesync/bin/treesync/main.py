
from cli_toolkit.script import Script

from .commands.list import List
from .commands.pull import Pull
from .commands.push import Push
from .commands.show import Show

DESCRIPTION = """
Synchrohize directory trees with known parameters using rsync pull and push
"""


class Treesync(Script):
    """
    CLI command 'treesync' main  entrypoint
    """
    description = DESCRIPTION
    subcommands = (
        List,
        Pull,
        Push,
        Show,
    )


def main() -> None:
    """
    CLI command 'treesync' main  entrypoint
    """
    Treesync().run()
