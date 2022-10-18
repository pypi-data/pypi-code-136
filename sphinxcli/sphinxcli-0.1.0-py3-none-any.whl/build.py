import io
import types
from itertools import product
from pathlib import Path
from typing import Any, Generator, NamedTuple, TypedDict

import rich
from sphinx.util.console import nocolor
from sphinx.util.docutils import patch_docutils, docutils_namespace

from sphinxcli.defaults import DEFAULT_TARGET_ORDER, LIST_SEPARATOR
from sphinxcli.exec import exec_sphinx
from sphinxcli.logging import add_log_handler
from sphinxcli.parse import parse_sphinx_output
from sphinxcli.tool_config import ToolConfig
from sphinxcli.util import str_to_list

try:
    from sphinx.application import Sphinx
except ImportError:
    Sphinx = None

Builder = str


class BuildParameters(TypedDict):
    source: Path
    target: Path
    config: Path
    doctree: Path
    builders: list[Builder] | Builder
    languages: list[str]
    # messages: str
    target_order: str


class BuildTarget(NamedTuple):
    builder: str
    language: str
    target: Path


def calc_build_targets(
    base: Path,
    builders: list[str],
    languages: list[str],
    order: str = DEFAULT_TARGET_ORDER,
) -> Generator[BuildTarget, None, None]:
    targets = list(product(builders, languages))

    if len(targets) == 1:
        yield BuildTarget(builders[0], languages[0], base)
    else:
        for builder, lang in targets:
            if order == "builder":
                yield BuildTarget(builder, lang, base / builder / lang)
            else:
                yield BuildTarget(builder, lang, base / lang / builder)


def build_docs(tool_config: ToolConfig, params: BuildParameters) -> None:
    if Sphinx is None:
        return

    _builders = params["builders"]
    if not _builders:
        builders = tool_config.settings.builders
    elif isinstance(_builders, str):
        builders = str_to_list(_builders)
    else:
        builders = _builders

    pyproject = tool_config.pyproject
    if pyproject is not None:
        root_path = pyproject.parent
    else:
        root_path = Path.cwd()

    source = params["source"]
    if not source.is_absolute():
        source = root_path / source

    base = params["target"]
    if not base.is_absolute():
        base = root_path / base

    doctree = params["doctree"]
    if not doctree.is_absolute():
        doctree = root_path / doctree

    config = params["config"]
    if not config.is_absolute():
        config = root_path / config

    languages = params["languages"]
    target_order = params["target_order"]

    if not builders:
        rich.print("[yellow]No builders specified[/]")
        return

    first_build = True

    rich.print("[green]Build Settings[/]")
    rich.print(f"  [blue]config[/]  = [white]{config}[/]")
    rich.print(f"  [blue]source[/]  = [white]{source}[/]")
    rich.print(f"  [blue]doctree[/] = [white]{doctree}[/]")

    status = io.StringIO()
    warning = io.StringIO()
    log = io.StringIO()
    for build_target in calc_build_targets(base, builders, languages, target_order):
        builder = build_target.builder
        language = build_target.language
        target = build_target.target

        rich.print()
        rich.print(f"[green]Building {builder}[/]")
        rich.print(f"  [blue]language[/]  = [white]{language}[/]")
        rich.print(f"  [blue]directory[/] = [white]{target}[/]")

        confoverrides: dict[str, Any] = {"language": language}
        if not first_build:
            confoverrides["suppress_warnings"] = ["app"]
        else:
            first_build = False

        nocolor()

        with patch_docutils(str(config)), docutils_namespace():
            app = Sphinx(
                srcdir=str(source),
                confdir=str(config),
                outdir=str(target),
                doctreedir=str(doctree),
                buildername=builder,
                status=status,
                warning=warning,
                confoverrides=confoverrides,
            )
            add_log_handler(app, status, warning, log)

            args = types.SimpleNamespace()
            exec_sphinx(app, args)

    # parse_sphinx_output(status, warning, log)
