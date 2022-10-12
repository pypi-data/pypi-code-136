# std
import argparse

# internal
from tier.cli.subcommands.version import version
from tier.cli.subcommands.deps import deps
from tier.cli.subcommands.init import init
from tier.cli.subcommands.bump import bump
from tier.cli.subcommands.update import update
from tier.cli.subcommands.develop import develop
from tier.cli.subcommands.sync import sync

# constants
DESCRIPTION = """Python versioning CLI"""


parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument('--verbose', '-v', action='count', default=0)
parser.add_argument('--dirty', action='store_true', help='Allow execution with uncommitted changes present.')
parser.add_argument('--dry-run', action='store_true', help='Flag to perform dry run.')

sub_parsers = parser.add_subparsers(required=True, dest='subcommand')

# tier version
parser_version = sub_parsers.add_parser('version')
parser_version.set_defaults(handler=version)

# tier deps
parser_deps = sub_parsers.add_parser('deps')
parser_deps.set_defaults(handler=deps)

# tier init
parser_init = sub_parsers.add_parser(
    'init',
    description='Initialize tier tool.',
)
parser_init.set_defaults(handler=init)
parser_init.add_argument(
    '--recursive', '-r', action='store_true',
    help='Recursively initialize.',
)
parser_init.add_argument(
    '--commit', '-c', action='store_true',
    help='Create a commit after initializing.',
)
parser_init.add_argument(
    '--tag', '-t', action='store_true',
    help='Create a git tag in addition to creating a commit.',
)

# tier bump
parser_bump = sub_parsers.add_parser(
    'bump',
    description='Bump project version.',
)
parser_bump.set_defaults(handler=bump)
parser_bump.add_argument(
    '--recursive', '-r', action='store_true',
    help='Recursively bump.',
)
parser_bump.add_argument(
    '--commit', '-c', action='store_true',
    help='Create a commit after bumping.',
)
parser_bump.add_argument(
    '--tag', '-t', action='store_true',
    help='Create a git tag in addition to creating a commit.',
)
parser_bump.add_argument(
    '--major', action='store_true',
    help='Perform a major bump.',
)
parser_bump.add_argument(
    '--minor', action='store_true',
    help='Perform a minor bump.',
)
parser_bump.add_argument(
    '--patch', action='store_true',
    help='Perform a patch bump.',
)
parser_bump.add_argument(
    '--post', action='store_true',
    help='Perform a post bump.',
)
parser_bump.add_argument(
    '--rc', action='store_true',
    help='Perform a rc bump.',
)
parser_bump.add_argument(
    '--beta', action='store_true',
    help='Perform a beta bump.',
)
parser_bump.add_argument(
    '--alpha', action='store_true',
    help='Perform a alpha bump.',
)
parser_bump.add_argument(
    '--dev', action='store_true',
    help='Perform a dev bump.',
)

# tier update
parser_update = sub_parsers.add_parser(
    'update',
    description='Update version.',
)
parser_update.set_defaults(handler=update)
parser_update.add_argument(
    '--recursive', '-r', action='store_true',
    help='Recursively update versions.',
)
parser_update.add_argument(
    '--commit', '-c', action='store_true',
    help='Create a commit after updating version.',
)
parser_update.add_argument(
    '--tag', '-t', action='store_true',
    help='Create a git tag in addition to creating a commit.',
)

# tier develop
parser_develop = sub_parsers.add_parser(
    'develop',
    description='Switch to develop dependencies.',
)
parser_develop.set_defaults(handler=develop)

# tier sync
parser_sync = sub_parsers.add_parser(
    'sync',
    description='Sync internal dependencies.',
)
parser_sync.set_defaults(handler=sync)
