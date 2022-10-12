"""Source file for imarac CLI."""
import pathlib
from typing import Tuple

import click
import filetype
import imagesize
from rich import print as rich_print
from rich.console import Console
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree

from imarac import __version__

console = Console()


@click.command()
@click.version_option(__version__)
@click.option('-d', '--directory', required=True, type=click.Path(exists=True, file_okay=False, resolve_path=True), help='Directory to check.')
@click.option('-r', '--ratio', required=True, type=click.FloatRange(min=0, min_open=True), help='Image desired ratio.')
@click.option('-v', '--verbose', is_flag=True, show_default=True, default=False, help="Add more information during processing.")
def check_ratio(directory, ratio, verbose):
    """Checks the ratio of every image contains in a directory"""

    tree = Tree(
        f":open_file_folder: [link file://{directory}]{directory}",
        guide_style="bold bright_blue",
    )

    walk_directory(pathlib.Path(directory), ratio, verbose, tree)
    rich_print(tree)


def walk_directory(directory: pathlib.Path, ratio: float, verbose: bool, tree: Tree) -> None:
    """Recursively build a Tree with directory contents and check ratio."""

    # Sort dirs first then by filename
    paths = sorted(
        pathlib.Path(directory).iterdir(),
        key=lambda path: (path.is_file(), path.name.lower()),
    )

    for path in paths:
        # Remove hidden files
        if path.name.startswith("."):
            continue
        # Add directory and walk recursively
        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
                style=style,
                guide_style=style,
            )
            walk_directory(path, ratio, verbose, branch)
        # If it's a file, check type and ratio if needed
        else:
            kind = filetype.guess(path)
            if kind is not None and kind.mime.startswith("image/"):
                image_ratio = get_ratio(file_path=path)

                if image_ratio != ratio or verbose:
                    text_filename = Text(path.name)
                    text_filename.stylize(f"link file://{path}")
                    if image_ratio is None:
                        text_filename.append(" (unknown ratio)", "bold bright_black")
                    else:
                        color = "bold red" if image_ratio != ratio else "blue"
                        text_filename.append(f" (ratio: {image_ratio})", color)
                    tree.add(text_filename)


def get_ratio(file_path: str, round_ratio: int = 2) -> float:
    """Takes a image file path, returns the ratio"""

    width, height = get_image_size(file_path)
    if width == -1 or height == -1:
        return None

    if width > height:
        ratio = width / height
    else:
        ratio = height / width
    return round(ratio, round_ratio)


def get_image_size(file_path: str) -> Tuple[float, float]:
    """Takes a image file path, returns the size"""

    return imagesize.get(file_path)
