"""Display catalog of commands user uses often."""

from commandsheet.cli import options
from commandsheet.cli import argparser
from commandsheet.const import XDG_CONFIG_PATH
from commandsheet.config import parse_config
from commandsheet.config import config_exists
from commandsheet.config import is_valid_config_file
from commandsheet.config import config_file_path_exists
from commandsheet.errors import not_a_valid_config_file
from commandsheet.errors import no_config_file_found
from commandsheet.errors import no_config_file_sections_found
from commandsheet.errors import no_config_file_path_exists
from commandsheet.output import header
from commandsheet.output import display_commandsheet


def main():
    parser = argparser()
    options(parser)
    args = parser.parse_args()

    fillchar = args.fillchar
    section_numbers = args.section_numbers
    config_file = args.config_file if args.config_file else XDG_CONFIG_PATH

    if not config_file_path_exists(config_file):
        no_config_file_path_exists(parser, config_file)
    if not is_valid_config_file(config_file):
        not_a_valid_config_file(parser, file=config_file)
    if not config_exists(config_file):
        no_config_file_found(parser)

    commandsheet = parse_config(config_file)
    if not commandsheet:
        no_config_file_sections_found(parser)

    header()
    display_commandsheet(
        commandsheet, fillchar=fillchar, section_numbers=section_numbers,
    )


if __name__ == '__main__':
    main()
