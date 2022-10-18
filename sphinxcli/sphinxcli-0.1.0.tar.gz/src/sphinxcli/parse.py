"""Parse the Sphinx output"""
import re
from io import StringIO
from typing import Callable

import rich
from sphinx.locale import __

LineParser = Callable[[str], str]
LineParsers = dict[str, LineParser]


def po_to_re(line: str) -> re.Pattern[str]:
    re_line = line.replace("%s", r"(\w)+")
    return re.compile(re_line)


def parse_updated_environment(line: str):

    return line


important_linesLineParsers = {__("updating environment"): parse_updated_environment}


def strip_escape(data: bytes) -> bytes:
    """Strip 7-bit and 8-bit C1 ANSI sequences
    https://stackoverflow.com/a/14693789/3253026
    """
    ansi_escape_8bit = re.compile(
        rb"(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])"
    )
    return ansi_escape_8bit.sub(b"", data)


def parse_sphinx_output(output: StringIO, warning: StringIO, log: StringIO):
    rich.print("[green]Output[/]")
    # rich.print(output.readlines())
    data = output.getvalue()
    b = strip_escape(data.encode("utf-8"))
    data = b.decode("utf-8")
    for line in data.split("\n"):
        print(line)

    rich.print("[green]Warnings[/]")
    data = warning.getvalue()
    print(data)

    rich.print("[green]Logging[/]")
    data = log.getvalue()
    print(data)
