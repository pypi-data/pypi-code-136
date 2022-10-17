from email import message_from_file
from email.generator import Generator
from email.message import Message
from os import remove
from os.path import dirname, join
from tempfile import TemporaryDirectory
from typing import Match, Optional, Pattern, Type

from wheel.wheelfile import WheelFile

from .audit import audit_and_repair_wheel
from .compiler import AbstractPackageCompiler
from .container import WheelTag

__all__ = [
    'compile_wheel',
]


_GENERIC_WHEEL_TAG = WheelTag.for_generic()


def _get_final_wheel_tag(
    wheel_info: Match,
    compiled_wheel_tag: WheelTag,
) -> WheelTag:
    try:
        current_tag = WheelTag(
            wheel_info.group('pyver'),
            wheel_info.group('abi'),
            wheel_info.group('plat'),
        )
    except IndexError:
        current_tag = _GENERIC_WHEEL_TAG

    possible_tags = frozenset({current_tag, compiled_wheel_tag})

    for tag in WheelTag.sys_tags():
        if tag in possible_tags:
            return tag


def _make_compiled_wheel_filename(
    wheel_info: Match,
    wheel_tag: WheelTag,
) -> str:
    return '-'.join(
        filter(
            None,
            (
              wheel_info.group('namever'),
              wheel_info.group('build'),
              str(wheel_tag),
            ),
        ),
    )


def compile_wheel(  # pylint: disable=too-many-locals
    wheel_filepath: str,
    compilator_cls: Type[AbstractPackageCompiler],
    exclude_pattern: Optional[Pattern] = None,
    remove_src: bool = False,
    audit_wheel: bool = False,
) -> str:
    """
    Wheel extracting, compiling and re-assembling.
    """
    wheel_dirpath = dirname(wheel_filepath)

    with TemporaryDirectory(dir=wheel_dirpath) as temp_dirpath:

        # Extract wheel file content and read some info from it.
        with WheelFile(wheel_filepath) as wheel_file:
            wheel_info: Match = wheel_file.parsed_filename
            dist_info_dirpath = join(temp_dirpath, wheel_file.dist_info_path)
            wheel_file.extractall(temp_dirpath)

        package_name = wheel_info.group('name')

        # File tree of wheel package compilation.
        compiler = compilator_cls(temp_dirpath, package_name)
        compiler.compile(
            exclude_pattern=exclude_pattern,
            remove_src=remove_src,
        )

        # Read WHEEL dist-info file content.
        wheel_metadata_filepath = join(dist_info_dirpath, 'WHEEL')

        with open(wheel_metadata_filepath, 'r', encoding='utf-8') as file:
            wheel_metadata: Message = message_from_file(file)

        # WHEEL dist-info tag changing.
        final_wheel_tag = _get_final_wheel_tag(wheel_info, compiler.wheel_tag)
        del wheel_metadata['Tag']
        wheel_metadata['Tag'] = str(final_wheel_tag)

        # Writing out WHEEL dist-info metadata changes.
        with open(wheel_metadata_filepath, 'w', encoding='utf-8') as file:
            Generator(file, maxheaderlen=0).flatten(wheel_metadata)

        # Wheel re-assembling.
        remove(wheel_filepath)

        compiled_wheel_filename = _make_compiled_wheel_filename(
            wheel_info,
            final_wheel_tag,
        )

        wheel_filepath = join(wheel_dirpath, f'{compiled_wheel_filename}.whl')

        with WheelFile(
            wheel_filepath,
            mode='w',
        ) as compiled_wheel_file:
            compiled_wheel_file.write_files(temp_dirpath)

        if not audit_wheel or final_wheel_tag == _GENERIC_WHEEL_TAG:
            return wheel_filepath

        return audit_and_repair_wheel(wheel_filepath)
