# General imports
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, order=True)
class Symlink:
    initial_origin_file: Path
    destination_in_build_package: Path
    script_origin_file: Path
    script_destination_file: Path
    is_sudo: bool


@dataclass(frozen=True, order=True)
class Copy:
    initial_origin_file: Path
    destination_in_build_package: Path
    script_origin_file: Path
    script_destination_file: Path
    is_sudo: bool


@dataclass(frozen=True, order=True)
class RunScript:
    initial_origin_file: Path
    destination_in_build_package: Path
    script_origin_file: Path
    # No need for script destination file since the command is just being executed,
    # and not copied or symlinked elsewhere
    is_sudo: bool
