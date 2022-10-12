import argparse
from pathlib import Path
from shutil import copytree, ignore_patterns
from typing import Final, Union

_TUTORIAL_DIRECTORY = Path(Path(__file__).parent) / "tutorial"


def copy_tutorial(path: Union[Path, str]) -> None:
    """Copy the tutorial files to the given path."""
    copytree(_TUTORIAL_DIRECTORY, path, ignore=ignore_patterns(".ipynb_checkpoints"))


if __name__ == "__main__":
    parser: Final = argparse.ArgumentParser(  # pylint: disable=invalid-name
        description="Copy the tutorial files."
    )
    parser.add_argument(
        "path",
        help="the path where the tutorial files will be copied to",
        type=str,
    )
    args: argparse.Namespace = parser.parse_args()
    copy_tutorial(args.path)
    print(f"The tutorial files have been copied to {str(Path(args.path).resolve())}")
