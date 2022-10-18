"""Utility functions to find files in directories"""
from pathlib import Path


def rfindfile(
    filename: str,
    path: Path | None = None,
    stop_file: str | None = None,
) -> Path | None:
    """Scan for a filename in the specified path moving up the directory tree.

    Args:
        filename: filename to find
        path: Path to search or current working directory if not specified
        stop_file: If specified and a file with the same name exists in the folder
                   being scanned before the filename we're searching for is found then
                   return None
    """
    if path is None:
        path = Path.cwd().resolve()

    while True:
        entries = [p.name for p in path.glob("*")]
        if stop_file is not None and stop_file in entries and filename == stop_file:
            return None

        if filename in entries:
            return path / filename

        # Can't go any further up
        if path.parent == path:
            return None

        return rfindfile(filename, path.parent)


def rfindfile_in_paths(
    filename: str,
    paths: list[Path] = [],
    stop_file: str | None = None,
    first: bool = False,
) -> list[Path] | None:
    """Scan for a filename in the specified paths moving up the directory tree.

    Args:
        filename: filename to find
        paths: Paths to search or current working directory if not specified
        stop_file: If specified and a file with the same name exists in the folder
                   being scanned before the filename we're searching for is found then
                   return None
        first: If True then the first match found is returned else all matches are returned


    """
    if paths is None or len(paths) == 0:
        paths = [Path.cwd()]

    entries: list[Path] = []
    for path in paths:
        if (file := rfindfile(filename, path, stop_file)) != None:
            entries.append(file)

            if first:
                break

    return entries


def findfile_in_paths(
    filename: str,
    paths: list[Path] = [],
    recursive: bool = False,
    first: bool = False,
) -> list[Path] | None:
    """Scan for a filename in the specified paths.

    Args:
        filename: filename to find
        paths: Paths to search or current working directory if not specified
        recursive: Recurse into sub directories
        first: If True then the first match found is returned else all matches are returned

    Returns:
        list of file Paths found
    """
    if not paths:
        paths = [Path.cwd().resolve()]

    entries: list[Path] = []
    for path in paths:
        if (
            file := findfile(filename, path, recursive)
        ) != None and file not in entries:
            entries.append(file)

            if first:
                break

    return entries


def findfile(
    filename: str,
    path: Path,
    recursive: bool = False,
) -> Path | None:
    """Scan for a filename in the specified path."""
    entries = [p.name for p in path.glob("*")]
    if filename in entries:
        return path / filename

    if recursive:
        dirs = [d for entry in entries if (d := (path / entry)).is_dir()]
        for dir in dirs:
            if (file := findfile(filename, dir)) is not None:
                return file

    return None
