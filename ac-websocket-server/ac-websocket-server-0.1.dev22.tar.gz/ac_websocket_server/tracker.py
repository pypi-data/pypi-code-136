'''Assetto Corsa stracker class'''

import asyncio
import configparser
from dataclasses import dataclass, field
import os
from typing import List

from ac_websocket_server.child import ChildServer
from ac_websocket_server.error import WebsocketsServerError


@dataclass
class TrackerServer(ChildServer):
    '''Represents an stracker server'''

    child_ini_file: str = field(default='stracker.ini')
    child_title: str = field(default='Stracker')
    child_short: str = field(default='stracker')
    is_optional: bool = True

    ac_server_address: str = field(init=False)
    ac_server_cfg_ini: str = field(init=False)
    log_file: str = field(init=False)
    listening_port: int = field(init=False)
    server_name: str = field(init=False)

    async def consumer(self, message_words: List[str]):
        '''Consume args destined for the server'''

        message_funcs = {'start': self.start,
                         'stop': self.stop,
                         'restart': self.restart}

        if message_funcs.get(message_words[0]):
            await message_funcs[message_words[0]]()

    def __post_init__(self):

        super().__post_init__()

        self._exe = f'{self.directory}/stracker.exe'
        self._args = ('--stracker_ini', self.child_ini_file)
        self._hash = '4c288fe128bae5250c51e07e2a510ccd'

    def pre_start_hook(self):
        '''Read (and correct) the stracker.ini file'''

        ini_file_name = f'{self.directory}/{self.child_ini_file}'

        if not os.path.exists(ini_file_name):
            msg = f'Missing {self.child_ini_file} file in {self.directory}'
            self._logger.error(msg)
            raise WebsocketsServerError(msg)

        cfg = configparser.ConfigParser()
        try:
            cfg.read(ini_file_name)

            self.ac_server_address = cfg['STRACKER_CONFIG']['ac_server_address']
            self.ac_server_cfg_ini = cfg['STRACKER_CONFIG']['ac_server_cfg_ini']
            self.log_file = cfg['STRACKER_CONFIG']['log_file']
            self.listening_port = cfg['STRACKER_CONFIG']['listening_port']
            self.server_name = cfg['STRACKER_CONFIG']['server_name']

        except configparser.Error as error:
            raise WebsocketsServerError(error) from error
