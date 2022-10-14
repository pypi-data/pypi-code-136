#!/usr/bin/python3
# -*- coding: utf-8 -*-


import hashlib
from dataclasses import dataclass

from slpkg.views.views import ViewMessage


@dataclass
class Md5sum:
    ''' Checksum the sources. '''
    flags: str

    def check(self, path: str, source: str, checksum: str, name: str):
        filename = f'{path}/{source.split("/")[-1]}'

        md5 = self.read_file(filename)

        file_check = hashlib.md5(md5).hexdigest()

        if file_check not in checksum:
            print('\nExpected:', ''.join(checksum))
            print('Found:', file_check)
            print(f'\nMD5SUM check for {name} FAILED.')

            view = ViewMessage()
            view.question(self.flags)

    def read_file(self, filename: str):
        with open(filename, 'rb') as f:
            return f.read()
