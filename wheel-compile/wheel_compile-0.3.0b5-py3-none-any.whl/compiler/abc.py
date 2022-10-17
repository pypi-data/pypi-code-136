from abc import ABCMeta, abstractmethod
from functools import partial
from os import remove, walk
from os.path import abspath, expanduser, join, relpath, sep
from re import compile
from typing import Callable, FrozenSet, Optional, Pattern

from ..container import FilePathInfo, WheelTag

__all__ = [
    'AbstractPackageCompiler',
]


_IGNORED_DIRNAME_PATTERN = compile(r'^\.|^__pycache__$')
_IGNORED_FILENAME_PATTERN = compile(r'^\.')


def _remove_callback(
    source_file_extensions: FrozenSet[str],
    file_path_info: FilePathInfo,
) -> None:
    if file_path_info.ext not in source_file_extensions:
        # File extension is not a source extension.
        return

    remove(file_path_info.filepath)


class AbstractPackageCompiler(metaclass=ABCMeta):
    SOURCE_FILE_EXTENSIONS = frozenset({'.c', '.py', '.pyx', '.o'})

    def __init__(self, package_root: str, package_name: str) -> None:
        self._package_name = package_name
        self._package_root = abspath(expanduser(package_root))

    @property
    def package_root(self) -> str:
        return self._package_root

    @property
    def package_name(self) -> str:
        return self._package_name

    def _walk_package_src_dirpath(
        self,
        callback: Callable[[FilePathInfo], None],
        exclude_pattern: Optional[Pattern] = None,
    ) -> None:
        package_root = self._package_root

        for root, _, filenames in walk(package_root):

            if _does_path_contain_ignored(root):
                continue

            relative_root = relpath(root, start=package_root)

            for filename in filenames:
                if _IGNORED_FILENAME_PATTERN.match(filename):
                    continue

                relative_filepath = join(relative_root, filename)

                if exclude_pattern is not None and exclude_pattern.match(
                    relative_filepath,
                ):
                    continue

                callback(
                    FilePathInfo(
                        root,
                        filename,
                        relative_root,
                        relative_filepath,
                    ),
                )

    def _remove_src_files(
        self,
        exclude_pattern: Optional[Pattern] = None,
        source_file_extensions: FrozenSet[str] = SOURCE_FILE_EXTENSIONS,
    ) -> None:
        self._walk_package_src_dirpath(
            partial(_remove_callback, source_file_extensions),
            exclude_pattern=exclude_pattern,
        )

    @abstractmethod
    def compile(
        self,
        *args,
        exclude_pattern: Optional[Pattern] = None,
        remove_src: bool = False,
        **kwargs,
    ) -> None: ...

    def __call__(self, *args, **kwargs) -> None:
        return self.compile(*args, **kwargs)

    @property
    @abstractmethod
    def wheel_tag(self) -> WheelTag: ...


def _does_path_contain_ignored(checked_path: str) -> bool:
    """
    Check if path includes ignored dirs.
    """
    return any(map(_IGNORED_DIRNAME_PATTERN.match, checked_path.split(sep)))
