from pathlib import Path
from typing import cast

import click
import xdg
from click_repl import repl as click_repl  # type: ignore
from click_repl.exceptions import ExitReplException  # type: ignore
from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.history import FileHistory

from sphinxcli.help import help_commands


@click.command(name="?")
@click.pass_context
def question(ctx: click.core.Context):
    """Display this list of commands"""
    help_commands(ctx)


@click.command(name="help")
@click.pass_context
def help(ctx: click.core.Context):
    """Display this list of commands"""
    help_commands(ctx)


@click.command()
@click.pass_context
def exit(ctx: click.core.Context):
    """Exit the REPL"""
    raise ExitReplException()


@click.command()
@click.pass_context
def quit(ctx: click.core.Context):
    """Quit the REPL"""
    raise ExitReplException()


def build_repl(ctx: click.core.Context) -> None:
    xdg_cache = xdg.xdg_cache_home()
    if xdg_cache:
        history_file = Path(xdg_cache) / "sphinx" / "history"
    else:
        history_file = Path("~/.cache/sphinx/history").resolve()

    if not history_file.exists():
        history_file.parent.mkdir(exist_ok=True)
        history_file.touch()

    prompt = HTML("\n<ansigreen>sphinxcli</ansigreen>&gt; ")

    prompt_kwargs = {
        "message": prompt,
        "history": FileHistory(str(history_file)),
    }
    ctx.obj["in_repl"] = True

    if ctx.parent is not None:
        g = cast(click.Group, ctx.parent.command)
        assert g.name == "cli"

        g.add_command(help)
        g.add_command(question)
        g.add_command(exit)
        g.add_command(quit)
        if "repl" in g.commands:
            del g.commands["repl"]

        click_repl(ctx.parent, prompt_kwargs=prompt_kwargs)
