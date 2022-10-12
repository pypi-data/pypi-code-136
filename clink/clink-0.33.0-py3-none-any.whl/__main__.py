import getpass
import logging
import os
import sys
from typing import Any, Optional, TextIO, Tuple

import click
import rich.console
import rich.logging
import rich.progress
import sentry_sdk
import yaml

from . import __title__, __version__
from . import api as clink


logger = logging.getLogger(__name__)


sentry_sdk.init(release=f"{__title__}@{__version__}")
sentry_sdk.set_user({"id": os.getuid(), "username": getpass.getuser()})


@click.group()
@click.version_option(__version__)
@click.pass_context
def main(context: click.Context) -> None:
    context.ensure_object(dict)
    context.obj["log_level"] = logging.DEBUG
    context.obj["stderr_console"] = rich.console.Console(stderr=True)
    context.obj["stdout_console"] = rich.console.Console()

    console_handler = rich.logging.RichHandler(
        console=context.obj["stderr_console"],
        rich_tracebacks=True,
        show_time=context.obj["stderr_console"].is_terminal,
        show_path=context.obj["log_level"] == logging.DEBUG,
    )
    console_handler.setFormatter(
        logging.Formatter(
            fmt="{name} - {message}",
            datefmt=f"[{logging.Formatter.default_time_format}]",
            style="{",
        )
    )

    logging.basicConfig(
        format="{asctime} {levelname} - {name} - {message}",
        handlers=[console_handler],
        level=context.obj["log_level"],
        style="{",
    )
    logging.getLogger(name="clink").setLevel(context.obj["log_level"])

    if context.obj["stderr_console"].is_terminal:
        context.obj["stderr_console"].print(
            r"""
        _ _      _
     __| (_)_ _ | |__
    / _| | | ' \| / /
    \__|_|_|_||_|_\_\

        """,
            crop=True,
            highlight=False,
            no_wrap=True,
            overflow="crop",
            style="bold #c837ab",
            width=80,
        )

    context.obj["component"] = clink.Participant("clink.cli")


@main.command()
@click.argument("type_", metavar="type", required=False, type=str)
@click.option(
    "--input",
    "input",
    help="JSON event object.",
    required=False,
    type=click.File(),
)
@click.option("--subject", "subject", required=False, type=str)
@click.option("--dry-run", "dry_run", is_flag=True)
@click.pass_context
def emit_event(
    context: click.Context,
    type_: Optional[str],
    input: Optional[TextIO],
    subject: Optional[str],
    dry_run: bool,
) -> int:
    if (input and type_) or (not input and not type_):
        raise click.BadOptionUsage(
            option_name="type",
            message='Either "type" OR "--input" parameter must be provided.',
            ctx=context,
        )

    component: clink.Participant = context.obj["component"]

    if input:
        data = yaml.safe_load(input)
        event = clink.Event.from_dict(data)
        component.emit_event(event, dry_run=dry_run)
    else:
        component.emit_event(type=type_, subject=subject, dry_run=dry_run)

    return 0


@main.command()
@click.option(
    "--topic",
    "-t",
    "topics",
    type=str,
    multiple=True,
    default=["#"],
    show_default=True,
)
@click.pass_context
def consume(context: click.Context, topics: Tuple[str]) -> None:
    component: clink.Participant = context.obj["component"]

    @component.on_event(*topics, supports_dry_run=True)
    def noop(event: clink.Event, **kwargs: Any) -> None:  # pragma: no cover
        pass

    logging.getLogger("amqp.connection.Connection.heartbeat_tick").setLevel(
        logging.INFO
    )

    component.consume()


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(prog_name=__title__))
