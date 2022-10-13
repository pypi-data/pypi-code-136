import argparse
from math import inf


def ranged_type(min_value=0, max_value=inf):
    """Return a function that checks if a value is within a range.
    Used for argparse to require a minimum or maximum integer value."""

    def check_range(value):
        value = int(value)
        if value < min_value or value > max_value:
            raise argparse.ArgumentTypeError(
                "Value must be between {} and {}".format(min_value, max_value)
            )
        return value

    return check_range


def parse_args():
    """"""
    parser = argparse.ArgumentParser(description="Generate a username or passphrase.")
    # add parent for shared commands between subparsers
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "-w",
        "--wordlist",
        default="eff_large_wordlist.txt",
        help="Wordlist to use (default: %(default)s)",
    )
    parent_parser.add_argument(
        "-C", "--copy", action="store_true", help="Copy passphrase to clipboard"
    )
    parent_parser.add_argument(
        "-i",
        "--include-numbers",
        action="store_true",
        help="Include numbers in passphrase",
    )

    # add sub commands
    subparsers = parser.add_subparsers(
        help="command to run",
        required=True,
        dest="command",
        title="commands",
        description="valid commands",
    )

    parser_passphrase = subparsers.add_parser("passphrase", parents=[parent_parser])
    parser_username = subparsers.add_parser("username", parents=[parent_parser])

    # passphrase specific args
    parser_passphrase.add_argument(
        "-n",
        "--num-words",
        type=ranged_type(min_value=1),
        default=3,
        help="Number of words in passphrase (default: %(default)s)",
    )
    parser_passphrase.add_argument(
        "-c",
        "--capitalize",
        action="store_true",
        help="Capitalize the first letter of each word",
    )
    s_group = parser_passphrase.add_argument_group("Separator options")
    separator_group = s_group.add_mutually_exclusive_group()
    separator_group.add_argument(
        "-s",
        "--separator",
        default="-",
        help="Separator between words (default: %(default)s)",
    )
    separator_group.add_argument(
        "-xs",
        "--no-separator",
        action="store_true",
        help="Do not use a separator between words",
    )
    return parser.parse_args()
