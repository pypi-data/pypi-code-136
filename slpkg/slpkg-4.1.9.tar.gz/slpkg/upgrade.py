#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from dataclasses import dataclass
from distutils.version import LooseVersion

from slpkg.configs import Configs
from slpkg.queries import SBoQueries


@dataclass
class Upgrade:
    log_packages: str = Configs.log_packages
    repo_tag: str = Configs.repo_tag

    def packages(self):
        ''' Compares version of packages and returns the maximum. '''
        for pkg in os.listdir(self.log_packages):
            if pkg.endswith(self.repo_tag):
                name = '-'.join(pkg.split('-')[:-3])
                installed_ver = pkg.replace(name + '-', '').split('-')[0]
                repo_ver = SBoQueries(name).version()

                if LooseVersion(repo_ver) > LooseVersion(installed_ver):
                    yield name
