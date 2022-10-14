#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from dataclasses import dataclass

from slpkg.checks import Check
from slpkg.search import Search
from slpkg.upgrade import Upgrade
from slpkg.version import Version
from slpkg.configs import Configs
from slpkg.utilities import Utilities
from slpkg.views.cli_menu import usage
from slpkg.slackbuild import Slackbuilds
from slpkg.find_installed import FindInstalled
from slpkg.remove_packages import RemovePackages
from slpkg.clean_logs import CleanLogsDependencies
from slpkg.update_repository import UpdateRepository


@dataclass
class Argparse:
    args: list

    def __post_init__(self):
        self.flag()
        self.check = Check()

        if len(self.args) == 0:
            usage(1)

    def flag(self):
        self.flags = []

        self.options = ['--yes',
                        '--jobs',
                        '--resolve-off',
                        '--reinstall',
                        '--skip-installed',
                        '--download-only'
                        ]

        for option in self.options:
            if option in self.args:
                self.args.remove(option)
                self.flags.append(option)

    def help(self):
        if len(self.args) == 1 and not self.flags:
            usage(0)
        usage(1)

    def version(self):
        if len(self.args) == 1 and not self.flags:
            version = Version()
            version.view()
            raise SystemExit()
        usage(1)

    def update(self):
        if len(self.args) == 1 and not self.flags:
            update = UpdateRepository()
            update.sbo()
            raise SystemExit()
        usage(1)

    def upgrade(self):
        if len(self.args) == 1 and not self.flags:
            upgrade = Upgrade()
            packages = list(upgrade.packages())

            if not packages:
                print('\nEverything is up-to-date.\n')
                raise SystemExit()

            install = Slackbuilds(packages, self.flags, install=True)
            install.execute()
            raise SystemExit()
        usage(1)

    def build(self):
        if len(self.args) >= 2 and '--reinstall' not in self.flags:
            packages = list(set(self.args[1:]))

            self.check.exists(packages)
            self.check.unsupported(packages)

            build = Slackbuilds(packages, self.flags, install=False)
            build.execute()
            raise SystemExit()
        usage(1)

    def install(self):
        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            self.check.exists(packages)
            self.check.unsupported(packages)

            install = Slackbuilds(packages, self.flags, install=True)
            install.execute()
            raise SystemExit()
        usage(1)

    def remove(self):
        if [f for f in self.flags if f in self.options[1:]]:
            usage(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))
            packages = self.check.blacklist(packages)

            self.check.installed(packages)

            remove = RemovePackages(packages, self.flags)
            remove.remove()
            raise SystemExit()
        usage(1)

    def search(self):
        if len(self.args) >= 2 and not self.flags:
            packages = list(set(self.args[1:]))
            packages = self.check.blacklist(packages)

            self.check.exists(packages)

            search = Search()
            search.package(packages)
            raise SystemExit()
        usage(1)

    def find(self):
        if len(self.args) >= 2 and not self.flags:
            packages = list(set(self.args[1:]))
            packages = self.check.blacklist(packages)

            find = FindInstalled()
            find.find(packages)
            raise SystemExit()
        usage(1)

    def clean_logs(self):
        if [f for f in self.flags if f in self.options[1:]]:
            usage(1)

        if len(self.args) == 1:
            logs = CleanLogsDependencies(self.flags)
            logs.clean()
            raise SystemExit()
        usage(1)

    def clean_tmp(self):
        if len(self.args) == 1 and not self.flags:
            path = Configs.tmp_path
            tmp_slpkg = Configs.tmp_slpkg
            folder = Configs.prog_name

            utils = Utilities()
            utils.remove_folder_if_exists(path, folder)
            utils.create_folder(tmp_slpkg, 'build')
            raise SystemExit()
        usage(1)


def main():
    args = sys.argv
    args.pop(0)

    argparse = Argparse(args)

    arguments = {
        '-h': argparse.help,
        '--help': argparse.help,
        '-v': argparse.version,
        '--version': argparse.version,
        'update': argparse.update,
        'upgrade': argparse.upgrade,
        'build': argparse.build,
        'install': argparse.install,
        'remove': argparse.remove,
        'search': argparse.search,
        'find': argparse.find,
        'clean-logs': argparse.clean_logs,
        'clean-tmp': argparse.clean_tmp
    }

    try:
        arguments[args[0]]()
    except KeyError:
        usage(1)


if __name__ == '__main__':
    main()
