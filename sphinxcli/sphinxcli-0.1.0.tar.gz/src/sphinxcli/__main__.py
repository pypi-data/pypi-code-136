import locale
import sys
from dataclasses import fields
from pathlib import Path

import rich_click as click
import rich
import rich.console
import rich.traceback

from sphinxcli import __version__
from sphinxcli.build import BuildParameters, build_docs
from sphinxcli.check import check_build_parameters
from sphinxcli.clean import clean_all
from sphinxcli.defaults import DEFAULT_SOURCE_PATH, DEFAULT_TARGET_PATH
from sphinxcli.help import help_commands
from sphinxcli.repl import build_repl
from sphinxcli.tool_config import ToolConfig
from sphinxcli.util import str_to_list
from sphinxcli.pyproject import ensure_sphinxcli_table

try:
    from sphinx.application import Sphinx
except ImportError:
    Sphinx = None


def sphinx_not_found() -> str:
    env_path = sys.exec_prefix
    return f"[red]Unable to import Sphinx from current environment {env_path}[/]"


class SettingCommand(click.Command):
    """Append the list of settings to the end of the help text"""

    def format_help_text(
        self,
        ctx: click.core.Context,
        formatter: click.formatting.HelpFormatter,
    ):
        help_text = "  "
        help_text += ctx.command.help or ""
        if help_text:
            help_text += ": "
        settings = ctx.obj["config"].settings.names()
        help_text += f"one of {', '.join(settings[:-1])}"
        help_text += f" or {settings[-1]}"
        formatter.write_text("\n")
        formatter.write_text(help_text)


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.core.Context):
    """A Sphinx document creation CLI."""
    rich.traceback.install(suppress=[click])
    console = rich.console.Console(highlight=False)

    if Sphinx is None:
        console.print(sphinx_not_found())
        sys.exit(1)

    tool_config = ToolConfig()
    tool_config.load()

    ctx.ensure_object(dict)
    ctx.obj["console"] = console
    ctx.obj["config"] = tool_config
    ctx.obj["in_repl"] = False

    if ctx.invoked_subcommand is None:
        ctx.invoke(repl)


@cli.group(invoke_without_command=True)
@click.pass_context
def repl(ctx: click.core.Context):
    """Start a REPL (The default if no command specified)"""
    build_repl(ctx)


@cli.command(cls=SettingCommand)
@click.pass_context
@click.argument("setting")
@click.option(
    "-a",
    "--absolute",
    is_flag=True,
    default=False,
    help="Displays paths as abolute",
)
def get(ctx: click.core.Context, setting: str, absolute: bool) -> None:
    """Get a configuration setting"""
    console = ctx.obj["console"]
    try:
        value = ctx.obj["config"].get(setting)
        if isinstance(value, list):
            console.print(value)
        elif absolute and isinstance(value, Path):
            console.print(str(value.resolve()))
        else:
            console.print(value)
    except KeyError as exc:
        console.print(f"[yellow]{exc.args[0]}[/]")


@cli.command(cls=SettingCommand)
@click.pass_context
@click.argument("setting")
@click.argument("value")
def set(ctx: click.core.Context, setting: str, value: str) -> None:
    """Set a configuration setting's value"""
    console = ctx.obj["console"]
    try:
        value = ctx.obj["config"].set(setting, value)
    except KeyError as exc:
        console.print(f"[yellow]{exc.args[0]}[/]")


@cli.command()
@click.pass_context
def settings(ctx: click.core.Context) -> None:
    """Display the current values of all settings"""
    console = ctx.obj["console"]
    settings = str(ctx.obj["config"].settings)
    console.print("\n[green]SphinxCLI Settings[/]")
    console.print(settings)


@cli.command()
@click.pass_context
@click.argument("builders", default="")
@click.argument("languages", default="")
@click.option(
    "-o",
    "--order",
    default="",
    help='Either "builder" to output files in `target/builder/language` or "language" to output files in `target/language/builder`',
)
# @click.option("-a", "--all", is_flag=True, default=False)
def build(
    ctx: click.core.Context,
    builders: str,
    languages: str,
    order: str,
    # all: bool,
) -> None:
    """Build Sphinx the documents

    \f

    If no arguments are specified the values will be taken from the `pyproject.toml`
    `tool.sphinxcli` section

    Arguments:

        builders: A Sphinx builder name or list of builder names separated by | characters e.g. html|latex

        languages: A language or list of languages to generate separated by | characters e.g. `en` or `en|fr`
    """
    console = ctx.obj["console"]
    tool_config = ctx.obj["config"]

    if builders:
        _builders = str_to_list(builders)
    else:
        _builders = tool_config.settings.builders

    if languages:
        _doc_languages = str_to_list(languages)
    else:
        _doc_languages = tool_config.settings.languages

    _source = tool_config.settings.source or Path(DEFAULT_SOURCE_PATH)
    _target = tool_config.settings.target or Path(DEFAULT_TARGET_PATH)
    _config = tool_config.settings.config or _source
    _doctree = tool_config.settings.doctree or _target

    if order:
        _target_order = order
    else:
        _target_order = tool_config.settings.target_order

    build_params: BuildParameters = {
        "builders": _builders,
        "source": _source,
        "target": _target,
        "config": _config,
        "doctree": _doctree,
        "languages": _doc_languages,
        "target_order": _target_order,
    }

    if errors := check_build_parameters(build_params):
        console.print("[red]Configuration errors:[/]")
        for error in errors:
            console.print(f"  [red]{error}[/]")
        sys.exit(2)

    return build_docs(tool_config, build_params)


@cli.command()
@click.pass_context
def clean(ctx: click.core.Context):
    """Clean any generated files"""
    console = ctx.obj["console"]
    tool_config = ctx.obj["config"]
    outdir = Path(tool_config.settings.target or "build")
    doctreedir = Path(tool_config.settings.doctree or outdir)

    result = clean_all(outdir, doctreedir)
    if not ctx.obj["in_repl"]:
        sys.exit(result)
    else:
        console.print("Clean successful")


@cli.command()
@click.pass_context
def version(ctx: click.core.Context):
    """Display the version number of this tool"""
    console = ctx.obj["console"]
    console.print(f"SphinxCLI Version {__version__}")


if __name__ == "__main__":
    cli()
