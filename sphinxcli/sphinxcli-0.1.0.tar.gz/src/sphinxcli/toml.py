"""Reading and writing of TOML files"""

from pathlib import Path

import tomlkit
import tomlkit.items
import tomlkit.container
import tomlkit.toml_file


def read_document(tomlfile: Path) -> tomlkit.TOMLDocument:
    """Read a TOMLDocument from a file"""
    tfile = tomlkit.toml_file.TOMLFile(str(tomlfile))
    document = tfile.read()
    return document


def write_document(
    tomlfile: Path,
    document: tomlkit.TOMLDocument,
) -> None:
    """Write a TOMLDocument to a file"""
    tfile = tomlkit.toml_file.TOMLFile(str(tomlfile))
    tfile.write(document)


def get_table(
    document: tomlkit.TOMLDocument, table_name: str
) -> tomlkit.items.Table | None:
    tool_table = document["tool"]
    if isinstance(tool_table, tomlkit.container.OutOfOrderTableProxy):
        sphinxcli_table = tool_table[table_name]
        if isinstance(sphinxcli_table, tomlkit.items.Table):
            return sphinxcli_table
