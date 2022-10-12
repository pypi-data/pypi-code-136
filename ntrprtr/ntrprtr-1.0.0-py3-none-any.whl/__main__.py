import sys

import argparse

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path")
    args = parser.parse_args()

    # Add functionality here


if __name__ == "__main__":
    sys.exit(main())
