"""CLI script"""

import argparse
import sys


def build_parser(description: str) -> argparse.ArgumentParser:
    """Build the commandline parser."""
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter,  # don't wrap my description
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="count",
        help="increase output verbosity",
        default=0,
    )
    parser.add_argument(
        "inpiuts",
        metavar="FILENAME",
        type=str,
        nargs="+",
        help="the input files to process",
    )

    return parser


def main():
    parser = build_parser(__doc__)
    args = parser.parse_args()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
