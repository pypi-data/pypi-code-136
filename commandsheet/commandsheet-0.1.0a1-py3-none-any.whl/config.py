"""Code for parsing the user config."""

from attrs import define
from attrs import field
from pathlib import Path
from configparser import ConfigParser

CONFIG_FILE_FORMATS = {'.ini'}


@define
class Section:
    name = field()
    contents = field()


def config_empty(config):
    return not config.sections()


def config_exists(path):
    return Path(path).expanduser().exists()


def is_valid_config_file(path):
    return Path(path).expanduser().suffix in CONFIG_FILE_FORMATS


def config_file_path_exists(path):
    """Verifies that, when `commandsheet -c <config>`, that <config> exists."""
    return config_exists(path)


def parse_config(path):
    config = ConfigParser()
    config.read(Path(path).expanduser())

    if config_empty(config):
        return []

    sections_raw = [
        section for section in config.values()
        # In our case, we don't care about the DEFAULT
        # section configparser creates to the config
        # object by default, so we'll just leave it out
        if not section.name == 'DEFAULT'
    ]

    sections_pretty = []
    for section in sections_raw:
        content = []
        for cmd, desc in section.items():
            content.append((cmd, desc))
        sections_pretty.append(Section(name=section.name, contents=content))

    return sections_pretty
