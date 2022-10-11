"""
Tree sync target
"""

import os
import sys

from collections.abc import MutableSequence
from operator import ge, gt, le, lt
from pathlib import Path, _windows_flavour, _posix_flavour
from typing import List, Optional, TYPE_CHECKING

from tempfile import NamedTemporaryFile
from subprocess import run, CalledProcessError

from sys_toolkit.textfile import LineTextFile

from .exceptions import SyncError

if TYPE_CHECKING:  # pragma: no cover
    from treesync.configuration.targets import TargetConfiguration


class ExcludesFile(Path):
    """
    Rsync excludes parser
    """
    # pylint: disable=protected-access
    _flavour = _windows_flavour if os.name == 'nt' else _posix_flavour

    @property
    def excludes(self) -> List[LineTextFile]:
        """
        Return excludes file items
        """
        if self.is_file():
            return list(LineTextFile(self))
        return []


# pylint: disable=too-few-public-methods
class TemporaryExcludesFile:
    """
    A temporary excludes file, merging excludes flags from various
    sources for rsync
    """
    def __init__(self, target) -> None:
        self.target = target
        # pylint: disable=consider-using-with
        self.__tempfile__ = NamedTemporaryFile(mode='w', prefix=f'treesync-{self.target.name}')
        for line in self.target.excluded:
            self.__tempfile__.write(f'{line}\n')
        self.__tempfile__.flush()

    def __repr__(self) -> str:
        """
        Return path to temporary file
        """
        return self.__tempfile__.name


class Target:
    """
    Tree sync target, defined by hostname and target name
    """
    def __init__(self,
                 hostname: str,
                 name: str,
                 source: str,
                 destination: str,
                 settings: 'TargetConfiguration') -> None:

        self.hostname = hostname
        self.name = name
        self.source = Path(source)
        self.destination = destination
        self.settings = settings if settings else {}
        self.__excludes_file__ = None

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.__repr__() == other
        for attr in ('hostname', 'name'):
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __cmp_targets__(self, other, op, default: bool):  # pylint: disable=invalid-name
        if isinstance(other, str):
            return op(self.__repr__(), other)
        for attr in ('hostname', 'name'):
            a = getattr(self, attr, None)
            b = getattr(other, attr, None)
            if a is not None and b is not None and a != b:
                return op(a, b)
        return default

    def __ge__(self, other):
        return self.__cmp_targets__(other, ge, True)

    def __gt__(self, other):
        return self.__cmp_targets__(other, gt, False)

    def __le__(self, other):
        return self.__cmp_targets__(other, le, True)

    def __lt__(self, other):
        return self.__cmp_targets__(other, lt, False)

    @property
    def default_settings(self):
        """
        Configuration section for target settings
        """
        return self.settings.__config_root__.defaults

    @property
    def host_configuration(self):
        """
        Get host configuration
        """
        if not self.hostname:
            return None
        return self.settings.__config_root__.hosts.get(self.hostname)

    @property
    def excluded(self) -> List[Path]:
        """
        Return list of excluded filenames applicable to target
        """
        excluded = list(self.default_settings.never_sync_paths)
        if not self.settings.ignore_default_excludes:
            excluded.extend(self.default_settings.excluded_paths)
        if self.settings.excludes:
            excluded.extend(self.settings.excludes)
        if self.tree_excludes_file is not None:
            excluded.extend(self.tree_excludes_file.excludes)
        return sorted(set(excluded))

    @property
    def tree_excludes_file(self) -> Optional[ExcludesFile]:
        """
        Return tree specific excludes file
        """
        path = self.settings.excludes_file
        if path:
            return ExcludesFile(
                self.source.joinpath(self.settings.excludes_file)
            )
        if self.default_settings.tree_excludes_file:
            return ExcludesFile(
                self.source.joinpath(self.default_settings.tree_excludes_file)
            )
        return None

    @property
    def excludes_file(self) -> TemporaryExcludesFile:
        """
        Return temporary excludes file for commands
        """
        if self.__excludes_file__ is None:
            self.__excludes_file__ = TemporaryExcludesFile(self)
        return self.__excludes_file__

    @property
    def flags(self) -> List[str]:
        """
        Return list of rsync flags for commands
        """
        flags = []
        if not self.settings.ignore_default_excludes:
            flags.extend(list(self.default_settings.flags))
        for flag in self.settings.flags:
            if flag not in flags:
                flags.append(flag)
        if self.host_configuration:
            for flag in self.host_configuration.destination_server_flags:
                if flag not in flags:
                    flags.append(flag)
        for flag in self.settings.destination_server_flags:
            if flag not in flags:
                flags.append(flag)
        if not flags:
            raise ValueError(f'Target defines no rsync flags: {self}')
        if self.settings.iconv:
            flags.append(f'--iconv={self.settings.iconv}')
        flags.append(f'--exclude-from={self.excludes_file}')
        return flags

    @staticmethod
    def run_sync_command(*args):
        """
        Run rsync command
        """
        try:
            return run(
                args,
                stdout=sys.stdout,
                stderr=sys.stderr,
                check=True
            )
        except CalledProcessError as error:
            raise SyncError(error) from error

    def get_rsync_cmd_args(self, dry_run: bool = False):
        """
        Return rsync command and arguments excluding source and destination
        """
        args = [self.default_settings.rsync_command] + self.flags
        if dry_run:
            args.append('--dry-run')
        return args

    def get_pull_command_args(self, dry_run: bool = False):
        """
        Return 'pull' command arguments
        """
        args = self.get_rsync_cmd_args(dry_run=dry_run)
        args.extend([
            f'{self.destination.rstrip("/")}/',
            f'{str(self.source).rstrip("/")}/',
        ])
        return args

    def get_push_command_args(self, dry_run: bool = False) -> List[str]:
        """
        Return 'push' command arguments
        """
        args = self.get_rsync_cmd_args(dry_run=dry_run)
        args.extend([
            f'{str(self.source).rstrip("/")}/',
            f'{self.destination.rstrip("/")}/',
        ])
        return args

    def pull(self, dry_run: bool = False) -> None:
        """
        Pull data from destination to source with rsync
        """
        self.run_sync_command(*self.get_pull_command_args(dry_run))

    def push(self, dry_run: bool = False) -> None:
        """
        Push data from source to destination with rsync
        """
        if not self.source.is_dir():
            raise SyncError(f'Source directory does not exist: {self.source}')
        return self.run_sync_command(*self.get_push_command_args(dry_run))


class TargetList(MutableSequence):
    """
    List of targets with lookup
    """
    def __init__(self):
        self.__items__ = []

    def __delitem__(self, index):
        """
        Delete specified item from cache
        """
        self.__items__.__delitem__(index)

    def __setitem__(self, index, value):
        """
        Set specified value to given index
        """
        self.__items__.__setitem__(index, value)

    def __getitem__(self, index):
        """
        Get specified item from cache
        """
        return self.__items__.__getitem__(index)

    def __len__(self):
        """
        Return size of collection
        """
        return len(self.__items__)

    def __iter__(self):
        """
        Set specified value to given index
        """
        return iter(self.__items__)

    def insert(self, index, value):
        """
        Append target to items
        """
        self.__items__.insert(index, value)

    def sort(self, key=None, reverse=False):
        """
        Sort targets
        """
        self.__items__.sort(key=key, reverse=reverse)

    def get(self, name: str) -> Optional[Target]:
        """
        Find first target matching specified name
        """
        for item in self:
            if str(item) == name:
                return item
        return None
