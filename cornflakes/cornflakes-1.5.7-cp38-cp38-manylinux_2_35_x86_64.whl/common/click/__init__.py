"""Click Extension for better CLI.

See referenced Code at https://github.com/ewels/rich-click.git
"""
from functools import partial
from typing import TYPE_CHECKING, Union, Any, Optional

import click
from click import *  # noqa: F401, F403
from click import argument as click_argument
from click import command as click_command
from click import group as click_group

from cornflakes.common.click._rich_argument import RichArg
from cornflakes.common.click._rich_command import RichCommand
from cornflakes.common.click._rich_config import Config
from cornflakes.common.click._rich_group import RichGroup
from cornflakes.common.click._rich_config import Config as RichConfig


def group(*args, cls=RichGroup, **kwargs) -> click_group:  # type: ignore
    """Group decorator function.

    Defines the group() function so that it uses the RichGroup class by default.
    """
    return click_group(*args, cls=cls, **kwargs)
    # group.add_command = partial(RichGroup.add_command, group)
    # return group

def command(*args, cls=RichCommand, **kwargs) -> click_command:  # type: ignore
    """Command decorator function.

    Defines the command() function so that it uses the RichCommand class by default.
    """
    return click_command(*args, cls=cls, **kwargs)


def argument(*args, cls=RichArg, **kwargs) -> click_argument:  # type: ignore
    """Command decorator function.

    Defines the command() function so that it uses the RichCommand class by default.
    """
    return click_argument(*args, cls=cls, **kwargs)


click.Group = RichGroup  # type: ignore
click.Command = RichCommand  # type: ignore

if TYPE_CHECKING:
    from click import Choice, Path, option, version_option, style  # noqa: F401

__all__ = [
    "argument",
    "Choice",
    "option",
    "Path",
    "version_option",
    "group",
    "command",
    "RichGroup",
    "RichCommand",
    "RichConfig",
    "Config",
]
