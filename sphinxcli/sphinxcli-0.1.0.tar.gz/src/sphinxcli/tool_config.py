from dataclasses import dataclass, field, fields
from os import environ
from os.path import expanduser
from pathlib import Path
from typing import Any

from typing_extensions import Self

import sphinxcli.pyproject
from sphinxcli.defaults import (
    DEFAULT_BUILDERS,
    DEFAULT_LANGUAGES,
    DEFAULT_TARGET_ORDER,
    PYPROJECT_TABLE_NAME,
)
from sphinxcli.util import str_to_list
from sphinxcli.types import Setting, Builder, Target
from sphinxcli.toml import read_document, get_table


@dataclass
class Settings:
    """SphinxCLI settings

    config:
        Sphinx configuration file or directory
    source:
        Source directory
    target:
        Target (build) directory
    targets:
        Builder specific overrides for target directory
    builder:
        List of builders to run
    builders:
        Configuration for individual builders
    doctree:
        Directory to store doctrees
    languages:
        The target languages for the docs
    target_order:
        The order in which to output files to the target are written either
        "builder" which outputs to "builder/language" (the default) or
        "language" that outputs to "language/builder"
    """

    source: Path | None = None
    target: Path | None = None
    builders: list[Builder] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    config: Path | None = None
    doctree: Path | None = None
    target_order: str = ""

    def names(self) -> list[str]:
        return [f.name for f in fields(self)]

    def __str__(self) -> str:
        def none_to_blank(value: Any | None) -> Any:
            if value is None:
                return ""
            else:
                return value

        def get_value(name: str) -> Any:
            try:
                value = getattr(self, name)
                return none_to_blank(value)
            except:
                pass

        max_len = max([len(f.name) for f in fields(self)])

        info = [(f.name, get_value(f.name)) for f in fields(self)]
        result = [f"  {i[0]:<{max_len}} = {i[1]}" for i in info]
        return "\n".join(result)


class ToolConfig:
    _pyproject: Path
    settings: Settings

    def load(self):
        pyproject, document = sphinxcli.pyproject.load()
        if document is None or pyproject is None:
            raise FileNotFoundError("Unable to find pyproject.toml")

        pyproject_table = get_table(document, PYPROJECT_TABLE_NAME)
        if pyproject_table is None:
            raise ValueError("Unable to get settings ")

        self.pyproject = pyproject

        doctree = pyproject_table.get("doctree", None)
        if doctree is not None:
            doctree = Path(self.resolve_dir(doctree))

        builders = list(pyproject_table.get("builders", DEFAULT_BUILDERS))
        document = str(pyproject_table.get("config", ""))
        source = str(pyproject_table.get("source", ""))
        target = str(pyproject_table.get("target", ""))
        doctree = str(pyproject_table.get("doctree", ""))
        languages = [
            str(lang) for lang in pyproject_table.get("languages", DEFAULT_LANGUAGES)
        ]
        target_order = str(pyproject_table.get("target_order", DEFAULT_TARGET_ORDER))

        self.settings = Settings(
            builders=builders,
            config=Path(self.resolve_dir(document)),
            source=Path(self.resolve_dir(source)),
            target=Path(self.resolve_dir(target)),
            doctree=Path(self.resolve_dir(doctree)),
            languages=languages,
            target_order=target_order,
        )

    def get(self, setting: str) -> Any:
        value = getattr(self.settings, setting, None)
        if value is None:
            raise KeyError(f"Unknown setting name '{setting}'")

        return value

    def set(self, name: str, value: Any) -> Any:
        current_value = self.get(name)
        if current_value is None:
            return current_value

        if isinstance(current_value, Path) and not isinstance(value, Path):
            result = Path(value)
        elif isinstance(current_value, list) and isinstance(value, str):
            result = str_to_list(value)
        else:
            result = value

        setattr(self.settings, name, result)

        setting = Setting(name, result)
        sphinxcli.pyproject.set_value(self.pyproject, setting)
        return result

    def update(self, other: Self):
        self.settings = other.settings

    def resolve_dir(self, dir: str) -> str:
        if dir.startswith("$"):
            slash = dir.find("/")
            if slash != -1:
                envvar = dir[1:slash]
            else:
                envvar = dir[1:]

            try:
                value = environ[envvar]
                dir = dir.replace(f"${envvar}", value)
            except KeyError:
                pass

        if dir.startswith("~"):
            return expanduser(dir)

        return dir
