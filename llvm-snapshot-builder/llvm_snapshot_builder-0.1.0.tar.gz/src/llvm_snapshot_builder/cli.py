#!/bin/env python3

"""
llvm_snapshot_builder.cli provides a CLI interface to the llvm_snapshot_builder
"""

import argparse
import sys
import logging

from .actions.action import CoprAction
from .actions.build_all_packages import CoprActionBuildAllPackages
from .actions.build_packages import CoprActionBuildPackages
from .actions.cancel_builds import CoprActionCancelBuilds
from .actions.delete_builds import CoprActionDeleteBuilds
from .actions.delete_project import CoprActionDeleteProject
from .actions.fork_project import CoprActionForkProject
from .actions.make_or_edit_packages import CoprActionMakeOrEditPackages
from .actions.make_or_edit_project import CoprActionMakeOrEditProject
from .actions.project_exists import CoprActionProjectExists
from .actions.regenerate_repos import CoprActionRegenerateRepos
from .copr_project_ref import CoprProjectRef
from .__init__ import __version__


# pylint: disable=too-few-public-methods
class HelpAction(CoprAction):
    """ Prints the help message. """

    def __init__(self, arg_parser: argparse.ArgumentParser, **kwargs):
        self.__arg_parser = arg_parser
        super().__init__(**kwargs)

    def run(self) -> bool:
        """ Runs the action. """
        self.__arg_parser.print_help()
        return True
# pylint: enable=too-few-public-methods


def get_action(
        arg_parser: argparse.ArgumentParser,
        arguments=None) -> CoprAction:
    """ Parses all arguments set up by build_main_parser() and returns the
    action to execute. """

    args = arg_parser.parse_args(arguments)
    if not args.command:
        return HelpAction(arg_parser)
    cmd = args.command

    cmd_action_map = {
        'build-all-packages': CoprActionBuildAllPackages,
        'build-packages': CoprActionBuildPackages,
        'cancel-builds': CoprActionCancelBuilds,
        'create-or-edit-packages': CoprActionMakeOrEditPackages,
        'create-or-edit-project': CoprActionMakeOrEditProject,
        'delete-builds': CoprActionDeleteBuilds,
        'delete-project': CoprActionDeleteProject,
        'fork-project': CoprActionForkProject,
        'project-exists': CoprActionProjectExists,
        'regenerate-repos': CoprActionRegenerateRepos,
    }

    if cmd not in cmd_action_map:
        return HelpAction(arg_parser)

    # Sanitize action arguments
    # -------------------------
    # We pass all arguments to the action as keyword arguments. That's why we
    # fist need to clean up the variables a bit.
    vargs = dict(vars(args))
    del vargs["command"]
    if "proj" in vargs:
        vargs["proj"] = CoprProjectRef(vargs["proj"])
    if "description_file" in vargs:
        vargs["description"] = vargs["description_file"].read()
        del vargs["description_file"]
    if "instructions_file" in vargs:
        vargs["instructions"] = vargs["instructions_file"].read()
        del vargs["instructions_file"]
    if "log_level" in vargs:
        logging.basicConfig(level=vargs["log_level"])
        del vargs["log_level"]
    return cmd_action_map[cmd](**vargs)


def build_main_parser() -> argparse.ArgumentParser:
    """ Returns the main parser for command line arguments """

    proj_kwargs = {
        "dest": 'proj',
        "metavar": '"OWNER/PROJECT"',
        "type": str,
        "required": True,
        "help": "owner (or group) and project name of the copr project to "
        "work with (e.g. 'foo/bar')"
    }
    chroots_kwargs = {
        "dest": 'chroots',
        "metavar": 'CHROOT',
        "nargs": '+',
        "default": "",
        "type": str,
        "help": "list of chroots to work on"
    }
    parser = argparse.ArgumentParser(
        description='Interact with the LLVM snapshot builds on Fedora Copr.',
        allow_abbrev=True)

    parser.add_argument(
        '--version',
        action='version',
        version=f"llvm_snapshot_builder {__version__}")

    logging_group = parser.add_mutually_exclusive_group()
    logging_group.add_argument(
        '--debug',
        action="store_const",
        dest="log_level",
        const=logging.DEBUG,
        default=logging.WARNING)
    logging_group.add_argument(
        '--verbose',
        action="store_const",
        dest="log_level",
        const=logging.INFO)

    # Subparsers

    subparsers = parser.add_subparsers(
        help='sub-command --help', dest="command")

    # FORK

    parser_fork = subparsers.add_parser(
        'fork-project', help='fork from a given project and then exit')
    parser_fork.add_argument(
        '--source',
        dest='source',
        required=True,
        type=str,
        help="the project to fork from (e.g. @fedora-llvm-team/llvm-snapshots-incubator")

    parser_fork.add_argument(
        '--target',
        dest='target',
        required=True,
        type=str,
        help="the project to fork to (e.g. foo/bar")

    # BUILD ALL PACKAGES

    parser_build_all_packages = subparsers.add_parser(
        'build-all-packages', help='build packages')
    parser_build_all_packages.add_argument('--proj', **proj_kwargs)
    parser_build_all_packages.add_argument('--chroots', **chroots_kwargs)

    # BUILD PACKAGES

    parser_build_packages = subparsers.add_parser(
        'build-packages', help='build packages')
    parser_build_packages.add_argument('--proj', **proj_kwargs)
    parser_build_packages.add_argument('--chroots', **chroots_kwargs)
    parser_build_packages.add_argument(
        '--packagenames',
        dest='packagenames',
        metavar='PACKAGENAME',
        required=True,
        nargs='+',
        type=str,
        help="list of LLVM packagenames to build in order")
    parser_build_packages.add_argument(
        '--timeout',
        dest='timeout',
        default=30 * 3600,
        type=int,
        help="build timeout in seconds for each package (defaults to: 30*3600=108000)")
    parser_build_packages.add_argument(
        '--wait-on-build-id',
        dest='wait_on_build_id',
        default=None,
        type=int,
        help="wait on the given build ID before starting the build")

    # CANCEL BUILDS

    parser_cancel_builds = subparsers.add_parser(
        'cancel-builds',
        help="""
        cancel builds with these states before creating new ones and
        then exits: "pending", "waiting", "running", "importing"
        """)
    parser_cancel_builds.add_argument('--proj', **proj_kwargs)
    parser_cancel_builds.add_argument('--chroots', **chroots_kwargs)

    # DELETE BUILDS

    parser_delete_builds = subparsers.add_parser(
        'delete-builds', help='cancel running builds and delete all builds afterwards')
    parser_delete_builds.add_argument('--proj', **proj_kwargs)
    parser_delete_builds.add_argument('--chroots', **chroots_kwargs)

    # PROJECT EXISTS

    parser_project_exists = subparsers.add_parser(
        'project-exists', help='checks if the project exists in copr, then exit')
    parser_project_exists.add_argument('--proj', **proj_kwargs)

    # DELETE PROJECT

    parser_delete_project = subparsers.add_parser(
        'delete-project', help='Deletes the project')
    parser_delete_project.add_argument('--proj', **proj_kwargs)

    # REGENERATE REPOS

    parser_regenerate_repos = subparsers.add_parser(
        'regenerate-repos', help='Regenerates the repo for the project')
    parser_regenerate_repos.add_argument('--proj', **proj_kwargs)

    # CREATE OR EDIT PROJECT

    parser_create_or_edit_project = subparsers.add_parser(
        'create-or-edit-project', help='Creates or edits a project')
    parser_create_or_edit_project.add_argument('--proj', **proj_kwargs)
    parser_create_or_edit_project.add_argument(
        '--description_file',
        dest='description_file',
        default="project-description.md",
        required=False,
        type=argparse.FileType('r', encoding='UTF-8'),
        help="file containing the project description in markdown format")
    parser_create_or_edit_project.add_argument(
        '--instructions_file',
        dest='instructions_file',
        default="project-instructions.md",
        required=False,
        type=argparse.FileType('r', encoding='UTF-8'),
        help="file containing the project instructions in markdown format")
    parser_create_or_edit_project.add_argument(
        '--delete-after-days',
        dest='delete_after_days',
        default=0,
        type=int,
        help="delete the project to be created after a given number of days "
        "(default: 0 which means \"keep forever\")")

    return parser


if __name__ == "__main__":
    sys.exit(0 if get_action(build_main_parser()).run() else 1)
