from contextlib import suppress
from distutils.core import run_setup  # pylint: disable=deprecated-module
from functools import partial
from os import chdir, cpu_count, getcwd
from os.path import exists, join, sep
from re import compile
from shutil import rmtree
from typing import List, Optional, Pattern

from setuptools import Distribution, Extension

from .abc import AbstractPackageCompiler
from ..container import FilePathInfo, WheelTag

__all__ = [

]


_COMPILABLE_EXTS = frozenset({'.py', '.pyx'})


def _append_extension_callback(
    extensions: List[Extension],
    file_info: FilePathInfo,
) -> None:
    ext = file_info.ext
    if ext not in _COMPILABLE_EXTS:
        # Ignoring of non compilable exts.
        return

    name = file_info.name
    if name == '__init__':
        return

    module_name = join(file_info.relative_root, name).replace(sep, '.')

    extensions.append(
        Extension(
            module_name,
            sources=[file_info.relative_filepath],
            undef_macros=['NDEBUG'],
            extra_compile_args=['-g0'],
        ),
    )


with suppress(ImportError):
    from Cython.Build import cythonize

    class CythonPackageCompiler(AbstractPackageCompiler):

        def compile(
            self,
            *args,
            exclude_pattern: Optional[Pattern] = None,
            remove_src: bool = False,
            **kwargs,
        ):
            extensions: List[Extension] = []
            package_name = self.package_name
            package_root = self.package_root

            self._walk_package_src_dirpath(
                partial(_append_extension_callback, extensions),
                exclude_pattern=exclude_pattern,
            )

            cwd = getcwd()
            chdir(package_root)

            extensions = cythonize(extensions, language_level=3)

            script_args = [
                'build_ext',
                '--inplace',
                '--parallel',
                str(cpu_count()),
            ]
            script_name = 'setup.py'

            if exists('setup.py'):
                distribution: Distribution = run_setup(  # type: ignore
                    script_name,
                    script_args=script_args,
                    stop_after='commandline',
                )
                distribution.ext_modules = extensions

            else:
                distribution = Distribution(
                    dict(
                        name=package_name,
                        packages=[package_name],
                        ext_modules=extensions,
                        script_args=script_args,
                        script_name=script_name,
                    ),
                )
                distribution.parse_command_line()

            distribution.run_commands()

            chdir(cwd)

            rmtree(join(package_root, 'build'))

            if not remove_src:
                return

            # Python thinks, that only directories with file "__init__.py"
            # are packages:
            # https://mail.python.org/pipermail/python-ideas/2008-October/002292
            # .html
            pattern = r'.+__init__\.py$'

            if exclude_pattern is not None:
                pattern = f'(?:{exclude_pattern.pattern}|{pattern})'

            self._remove_src_files(exclude_pattern=compile(pattern))

        @property
        def wheel_tag(self) -> WheelTag:
            return WheelTag.for_so_compiled()

    __all__.append(CythonPackageCompiler.__name__)
