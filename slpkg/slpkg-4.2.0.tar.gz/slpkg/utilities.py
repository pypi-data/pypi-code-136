#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import shutil
import tarfile

from dataclasses import dataclass

from slpkg.configs import Configs


@dataclass
class Utilities:
    log_packages: str = Configs.log_packages

    def untar_archive(self, path: str, archive: str, ext_path: str):
        ''' Untar the file to the build folder. '''
        tar_file = f'{path}/{archive}'
        untar = tarfile.open(tar_file)
        untar.extractall(ext_path)
        untar.close()

    def is_installed(self, package: str):
        ''' Returns True if a package is installed. '''
        for pkg in os.listdir(self.log_packages):
            if package in pkg:
                return pkg

    def remove_file_if_exists(self, path: str, file: str):
        ''' Clean the the old files. '''
        archive = f'{path}/{file}'
        if os.path.isfile(archive):
            os.remove(archive)

    def remove_folder_if_exists(self, path: str, folder: str):
        ''' Clean the the old folders. '''
        directory = f'{path}/{folder}'
        if os.path.isdir(directory):
            shutil.rmtree(directory)

    def create_folder(self, path: str, folder: str):
        ''' Creates folder. '''
        directory = f'{path}/{folder}'
        if not os.path.isdir(directory):
            os.makedirs(directory)
