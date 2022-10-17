from argparse import ArgumentParser
from contextlib import suppress
from re import compile

from .compile import compile_wheel
from .compiler import COMPILATOR_MAP

__all__ = [
    'run_wheel_compile',
]


def run_wheel_compile():
    parser = ArgumentParser(description='Wheel package recompiler.')
    parser.add_argument(
        '-e',
        '--exclude-pattern',
        type=str,
        nargs='*',
        help='Regex patterns for excluding some files from compilation.',
    )
    parser.add_argument(
        '-s',
        '--save-sources',
        action='store_true',
        default=False,
        help='Flag to force saving sources with compiled files in package.',
    )
    parser.add_argument(
        '-t',
        '--type',
        choices=frozenset(COMPILATOR_MAP),
        default=next(iter(COMPILATOR_MAP)),
        help='Type of compilation.',
    )
    parser.add_argument(
        'wheel_filepath',
        help='path to wheel file.',
    )

    with suppress(ImportError):
        # pylint: disable=import-outside-toplevel,unused-import
        import auditwheel  # noqa

        parser.add_argument(
            '-a',
            '--audit-wheel',
            action='store_true',
            default=False,
            help='Flag to force audit and repair wheel package.',
        )

    args = parser.parse_args()

    exclude_pattern = args.exclude_pattern

    compile_wheel(
        args.wheel_filepath,
        COMPILATOR_MAP[args.type],
        exclude_pattern=compile(
            '|'.join(
                map(
                    '(?:{})'.format,  # pylint: disable=consider-using-f-string
                    exclude_pattern,
                ),
            ),
        ) if exclude_pattern else None,
        remove_src=not args.save_sources,
        audit_wheel=getattr(args, 'audit_wheel', False),
    )


if __name__ == '__main__':
    run_wheel_compile()
