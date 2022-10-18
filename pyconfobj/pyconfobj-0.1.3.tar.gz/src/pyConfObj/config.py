#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2022'
__date__ = '18/10/22'
__credits__ = ['Otger Ballester', ]
__license__ = 'MIT License'
__version__ = '0.1.3'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

import inspect
import json
import yaml


class ConfObj:
    def __init__(self):
        self._file_path = None
        self._loaded_json = {}
        self._loaded_yaml = {}
    
    def get_loaded_json(self):
        return self._loaded_json

    def get_loaded_yaml(self):
        return self._loaded_yaml

    def load_dict(self, conf):
        if not isinstance(conf, dict):
            raise Exception('Configuration must be a dictionary')

        for k in conf.keys():
            try:
                a = getattr(self, k)
                if not inspect.ismethod(a):
                    if isinstance(a, ConfObj):
                        a.load_dict(conf[k])
                    else:
                        setattr(self, k, conf[k])
            except AttributeError:
                pass

    def as_dict(self):
        t = {}
        for mem in inspect.getmembers(self):
            if not mem[0].startswith('_') and not inspect.ismethod(mem[1]):
                if isinstance(mem[1], ConfObj):
                    t[mem[0]] = mem[1].as_dict()
                else:
                    t[mem[0]] = mem[1]
        return t

    def as_json(self):
        return json.dumps(self.as_dict(), indent=2)

    def load_json(self, json_path):
        if json_path is None:
            json_path = self._file_path
        elif self._file_path is None:
            self._file_path = json_path
        with open(json_path, 'r') as json_file:
            self._loaded_json = json.load(json_file)
            self.load_dict(self._loaded_json)

    def save_as_json(self, json_path):
        if json_path is None:
            json_path = self._file_path
        with open(json_path, 'w') as json_file:
            json.dump(self.as_dict(), json_file)

    def load_yaml(self, yaml_path):
        if yaml_path is None:
            yaml_path = self._file_path
        elif self._file_path is None:
            self._file_path = yaml_path
        with open(yaml_path, 'r') as yaml_fp:
            self._loaded_yaml = yaml.safe_load(yaml_fp)
            self.load_dict(self._loaded_yaml)

    def save_as_yaml(self, yaml_path=None):
        if yaml_path is None:
            yaml_path = self._file_path
        with open(yaml_path, 'w') as yaml_fp:
            yaml.dump(self.as_dict(), yaml_fp)

    def set_file_path(self, full_path):
        self._file_path = full_path

    def check_pass(self) -> bool:
        """
        To be overwritten when a child class wants to implement a valid configuration check
        """
        return True

    def check(self) -> bool:
        """
        Return if all checks have passed
        For it to work, any 
        """
        retval = self.check_pass()
        if not self.check_pass() is True:
            return False
        # Check for any confObj instances if check has not already failed
        for mem in inspect.getmembers(self):
            if not mem[0].startswith('_') and not inspect.ismethod(mem[1]):
                if isinstance(mem[1], ConfObj):
                    if not  mem[1].check() is True:
                        return False
        return True
