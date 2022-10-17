from functools import partial
from py_compile import compile
from typing import Optional, Pattern

from .abc import AbstractPackageCompiler
from ..container import FilePathInfo, WheelTag

__all__ = [
    'NativePackageCompiler',
]


def _native_callback(optimize: int, file_path_info: FilePathInfo):
    if file_path_info.ext != '.py':
        return

    filepath = file_path_info.filepath
    compile(
        filepath,
        cfile=filepath + 'c',
        dfile=file_path_info.relative_filepath,
        optimize=optimize,
    )


class NativePackageCompiler(AbstractPackageCompiler):

    def compile(
        self,
        *args,
        remove_src: bool = False,
        optimize: int = 2,
        exclude_pattern: Optional[Pattern] = None,
        **kwargs,
    ) -> None:

        self._walk_package_src_dirpath(
            partial(_native_callback, optimize),
            exclude_pattern=exclude_pattern,
        )

        if remove_src:
            self._remove_src_files(exclude_pattern)

    @property
    def wheel_tag(self) -> WheelTag:
        return WheelTag.for_generic()
