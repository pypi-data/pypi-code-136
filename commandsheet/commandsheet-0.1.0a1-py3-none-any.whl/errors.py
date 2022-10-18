"""CLI errors."""

from pathlib import Path
from commandsheet.locale import _


def no_config_file_found(parser):
    msg = _('No `commandsheet.ini` file found :(')
    parser.exit(status=1, message=msg, newline=True)


def no_config_file_sections_found(parser):
    msg = _('No sections to display from commandsheet.ini :(')
    parser.exit(status=1, message=msg, newline=True)


def no_config_file_path_exists(parser, file):
    path = Path(file).expanduser()
    msg = _('Config file `%(file)s` does not exist')
    parser.exit(status=1, message=msg % {'file': str(path)}, newline=True)


def not_a_valid_config_file(parser, file):
    path = Path(file).expanduser()
    filename = Path(path).expanduser().name
    msg = _('File `%(file)s` is not of valid config file format')
    parser.exit(status=1, message=msg % {'file': filename}, newline=True)
