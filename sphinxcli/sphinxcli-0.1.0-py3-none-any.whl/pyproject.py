"""pyproject.toml handling"""

from json import tool
from pathlib import Path
from pydoc import doc
from turtle import up
from typing import Any

import tomlkit
import tomlkit.container
import tomlkit.items

from sphinxcli.findfile import rfindfile
from sphinxcli.defaults import PYPROJECT_TABLE_NAME
from sphinxcli.types import Setting
from sphinxcli.toml import write_document, read_document, get_table


def sphinxcli_default_table() -> tomlkit.items.Table:
    """Create the default sphinxcli table definition"""
    table = tomlkit.table()
    table.name = "tool.sphinxcli"

    buidlers = tomlkit.array()
    buidlers.extend(["html"])
    table.append("buidlers", buidlers)

    base_path = Path("src") / "docs"

    source = tomlkit.string(str(base_path / "source"))
    table.append("source", source)
    table.append("config", source)

    target = tomlkit.string(str(base_path / "build"))
    table.append("target", target)

    doctree = tomlkit.string(str(base_path / "build" / "doctree"))
    table.append("doctree", doctree)

    languages = tomlkit.array()
    languages.extend(["en"])
    table.append("languages", languages)

    return table


def ensure_sphinxcli_table(document: tomlkit.TOMLDocument) -> bool:
    """Ensure there is a sphinxcli table within the TOML document

    Returns:
        True if the table was created or False if it was already there.
    """
    pyproject_table = get_table(document, PYPROJECT_TABLE_NAME)
    if pyproject_table is None:
        pyproject_table = sphinxcli_default_table()
        document[PYPROJECT_TABLE_NAME] = pyproject_table
        return True

    return False


def find(path: Path | None = None) -> Path | None:
    """Find the pyproject.toml file ion the path specified
    or the current working directory if not specified.
    """
    if path is None:
        path = Path.cwd()
    pyproject = rfindfile("pyproject.toml")
    return pyproject


def load(path: Path | None = None) -> tuple[Path | None, tomlkit.TOMLDocument | None]:
    """Load the pyproject.toml file"""
    if (pyproject := find(path)) is not None:
        document = read_document(pyproject)
        if ensure_sphinxcli_table(document):
            write_document(pyproject, document)
        return pyproject, document

    return None, None


def get_value(pyproject: Path, setting: Setting) -> Any:
    """Read a value from the sphinxcli table"""
    document = read_document(pyproject)
    if document is None:
        return None

    pyproject_table = get_table(document, PYPROJECT_TABLE_NAME)
    if pyproject_table is None:
        return None

    if setting.name not in pyproject_table:
        raise KeyError(f"Unknown setting {setting.name}")

    return pyproject_table[setting.name]


def set_value(pyproject: Path, setting: Setting) -> Any:
    """Set a value in the sphinxcli table and write to disk"""
    document = read_document(pyproject)
    if document is None:
        return None

    pyproject_table = get_table(document, PYPROJECT_TABLE_NAME)
    if pyproject_table is None:
        return None

    if setting.name not in pyproject_table:
        raise KeyError(f"Unknown setting {setting.name}")

    if (
        setting.name in pyproject_table
        and setting.value != pyproject_table[setting.name]
    ):
        pyproject_table[setting.name] = setting.value
        write_document(pyproject, document)
        return setting.value
