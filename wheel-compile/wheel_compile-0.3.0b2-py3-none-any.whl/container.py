from os.path import join, splitext
from sys import abiflags
from sysconfig import get_platform
from typing import Iterator

from wheel.vendored.packaging.tags import Tag, interpreter_name, \
    interpreter_version, sys_tags

__all__ = [
    'FilePathInfo',
    'WheelTag',
]

try:
    from functools import cached_property
except ImportError:
    cached_property = property  # type: ignore  # pylint: disable=invalid-name


class FilePathInfo:
    """Package file path information."""
    def __init__(
        self,
        root: str,
        filename: str,
        relative_root: str,
        relative_filepath: str,
    ) -> None:
        self.root = root
        self.filename = filename
        self.relative_root = relative_root
        self.relative_filepath = relative_filepath

    @cached_property
    def filepath(self) -> str:
        return join(self.root, self.filename)

    @cached_property
    def name(self) -> str:
        return splitext(self.filename)[0]

    @cached_property
    def ext(self) -> str:
        return splitext(self.filename)[1].lower()


def _normalize_string(string: str) -> str:
    return string.replace('.', '_').replace('-', '_')


class WheelTag(Tag):
    """Wheel package tag."""

    @classmethod
    def for_generic(cls) -> 'WheelTag':
        return cls(
            'py3',
            'none',
            'any',
        )

    @classmethod
    def for_so_compiled(cls) -> 'WheelTag':
        interpreter = f'{interpreter_name()}{interpreter_version()}'
        return cls(
            interpreter,
            f'{interpreter}{_normalize_string(abiflags)}',
            _normalize_string(get_platform()),
        )

    @staticmethod
    def sys_tags() -> Iterator['WheelTag']:
        for tag in sys_tags():
            yield WheelTag(tag.interpreter, tag.abi, tag.platform)
