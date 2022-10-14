#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import yaml
from dataclasses import dataclass

from slpkg.configs import Configs


@dataclass
class Blacklist:
    ''' Reads and returns the blacklist. '''
    etc_path: str = Configs.etc_path

    def get(self):
        file = f'{self.etc_path}/blacklist.yml'
        if os.path.isfile(file):
            with open(file, 'r') as black:
                return yaml.safe_load(black)['blacklist']['packages']
