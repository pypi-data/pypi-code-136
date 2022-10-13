#!/usr/bin/env python3

# Copyright 2022 Louis Paternault
#
# This file is part of Chval.
#
# Chval is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Chval is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with Chval.  If not, see <http://www.gnu.org/licenses/>.

"""Parallel `getmail` calls, with progress bars"""

import argparse
import contextlib
import dataclasses
import io
import pathlib
import re
import subprocess
import sys
import threading
import unicodedata

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)
from rich.rule import Rule
from rich.text import Text

console = Console()

VERSION = "1.1.0"
NAME = "chval"
CONFIG = pathlib.Path("~/.config/getmail").expanduser()
PREFIX = "getmailrc-"
GETMAIL = ["getmail", "--rcfile"]

# Set DEBUG to True to log a lot of things
DEBUG = False

RE_MESSAGE = re.compile(r"msg (?P<sub>\d+)/(?P<total>\d+) \(\d+ bytes\) delivered")
RE_END = re.compile(
    r"(?P<messages>\d+) messages \(\d+ bytes\) retrieved, (\d+) skipped"
)


@dataclasses.dataclass
class _Completion:
    """Keep information about a getmail call completion."""

    progress: list[int, int] = dataclasses.field(default_factory=lambda: [0, 0])
    returncode: int | None = None
    error: str = ""


def call_getmail(rcfile, progress, completion):
    """Parse the output of `getmail`.

    :param str rcfile: Name of the configuration file
    :param rich.progress.Progress progress: Shared progress bar.
    :param _Completion completion: Information about this getmail call completion,
        that is "sent" back to the main thread.
    """
    task = progress.add_task(rcfile, start=False, total=0)

    # pylint: disable=consider-using-with
    process = subprocess.Popen(
        # Uncomment to debug
        # [str(pathlib.Path(__file__).parent / "bin" / "fake-getmail.py"), rcfile],
        GETMAIL + [PREFIX + rcfile],
        text=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stderr = io.TextIOWrapper(process.stderr)

    start = None
    while True:
        # Unbuffer standard output
        line = process.stdout.readline()
        if not line:
            break

        if DEBUG:
            console.log(f"[green]{task}[/green] {line.strip()}")
        if match := RE_MESSAGE.search(line):
            sub = int(match.group("sub"))
            total = int(match.group("total"))
            if start is None:
                progress.start_task(task)
                start = sub
            progress.update(task, total=total - start + 1, completed=sub - start + 1)
            completion.progress = [sub - start + 1, total - start + 1]
        elif match := RE_END.search(line):
            pass

    process.wait()
    progress.stop_task(task)
    completion.returncode = process.returncode
    if process.returncode:
        # `getmail` exited with an error
        message = "".join(stderr.buffer.readlines()).strip()
        completion.error = message.rpartition("\n")[-1]

        progress.log(Rule(Text(f"\u26A0\uFE0F {rcfile}")))
        progress.log(message)


def call_all_getmails(keywords):
    """Run getmail calls, and display a progress bar.

    :param List[str] keywords: List of getmailrc keyword
        (a keyword `foo` references a getmail configuration file CONFIG/getmailrc-foo).
    """
    calls = {}

    with Progress(
        TextColumn("[green][{task.completed}/{task.total}][/green] {task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=True,
    ) as progress:
        if DEBUG:
            progress.stop()
        with contextlib.ExitStack() as stack:
            for rcfile in keywords:
                calls[rcfile] = _Completion()
                thread = threading.Thread(
                    target=call_getmail,
                    kwargs={
                        "rcfile": rcfile,
                        "progress": progress,
                        "completion": calls[rcfile],
                    },
                )
                thread.start()
                stack.callback(thread.join)

    # Display summary
    console.rule(Text(f"""{unicodedata.lookup("PARTY POPPER")} Summary"""))
    for getmailrc, completion in calls.items():
        if completion.returncode:
            console.print(
                # pylint: disable=line-too-long
                f"""\u274C [red][{completion.progress[0]}/{completion.progress[1]}] {getmailrc}[/red] {completion.error}"""
            )
        else:
            console.print(
                # pylint: disable=line-too-long
                f"""\u2714\uFE0F [green][{completion.progress[0]}/{completion.progress[1]}] {getmailrc}[/green]"""
            )

    if any(completion.returncode for completion in calls.values()):
        return 1
    return 0


def _type_choice(available):
    def wrapped(txt):
        if txt in available:
            return txt
        raise argparse.ArgumentTypeError(
            f""""{txt}" must be one of : {", ".join(available)}."""
        )

    return wrapped


def main():
    """Main function."""
    # Gather list of configuration files
    available = set(
        filename.name[len(PREFIX) :]
        for filename in CONFIG.glob(f"{PREFIX}*")
        if not str(filename).endswith("~")
    )

    # Parse command line
    parser = argparse.ArgumentParser(
        description="Parallel `getmail` calls, with progress bars",
        prog="chval",
        epilog=f"All getmailrc files must be in the default directory {CONFIG}.",
    )
    parser.add_argument(
        "--version",
        help="Show version and exit.",
        action="version",
        version=f"{NAME} {VERSION}",
    )
    parser.add_argument(
        "GETMAILRC",
        nargs="*",
        # Workaround to bug https://bugs.python.org/issue27227
        # "type=str, choices=available" would have been better
        type=_type_choice(available),
        help=(
            "List of getmailrc files to process. "
            f"""Calling "chval foo" will process configuration file "{CONFIG/"getmailrc-foo"}". """
            "Leave blank to process all getmailrc files."
        ),
    )
    options = parser.parse_args()
    if not options.GETMAILRC:
        options.GETMAILRC = list(sorted(available))

    # Call getmail
    return call_all_getmails(options.GETMAILRC)


if __name__ == "__main__":
    sys.exit(main())
