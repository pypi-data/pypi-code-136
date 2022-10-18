#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:42:06 2022

@author: avigailtaylor
"""

import yaml

with open("test_config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)
print(cfg["mysql"])
print(cfg["other"])
