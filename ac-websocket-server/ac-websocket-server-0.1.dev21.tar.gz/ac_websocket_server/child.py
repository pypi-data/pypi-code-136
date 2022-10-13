'''Assetto Corsa Abstract Server Class'''

import asyncio
import hashlib
import logging
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime
import subprocess


from ac_websocket_server.error import WebsocketsServerError
from ac_websocket_server.observer import ObserverNotifier
from ac_websocket_server.protocol import Protocol


@dataclass
class ChildServer(ObserverNotifier):
    '''Represents an Assetto Corsa childserver.'''
    # pylint: disable=logging-fstring-interpolation, invalid-name

    directory: str
    child_ini_file: str  # filename of the child's ini file
    child_title: str  # full title of child server
    child_short: str  # short descriptive name of child server
    is_optional: bool = field(init=False, default=False)

    def __post_init__(self):

        super().__init__()

        self._logger = logging.getLogger(f'ac-ws.{self.child_short}')

        self._cwd: str = self.directory
        self._exe: str   # absolute path to child executable
        self._args: tuple[str]  # arguments to use for exeuction
        self._hash: str  # md5 hash of child executable

        self._logfile_use_timestamp: bool = True
        self._logfile_stdout: str
        self._logfile_stderr: str

        self._process: asyncio.subprocess.Process

        self.running = False    # semaphore if running

    async def log_and_send_error(self, msg: str):
        '''Send error message'''
        self._logger.error(msg)
        await self.put(Protocol.error(msg=msg))

    def post_start_hook(self):
        '''Run after starting'''

    def post_stop_hook(self):
        '''Run after stopping'''

    def pre_start_hook(self):
        '''Run before starting'''

    def pre_stop_hook(self):
        '''Run before stopping'''

    async def restart(self):
        ''''Re-start the child server'''
        self._logger.info(f'Re-starting {self.child_short}')
        await self.stop()
        await self.start()

    async def start(self):
        '''Start the child server.'''
        # pylint: disable=line-too-long

        try:
            self.pre_start_hook()
        except WebsocketsServerError as e:
            msg = f'start command failed - {e}'
            await self.log_and_send_error(msg)
            return

        if self.running:
            msg = f'start command ignored - {self.child_short} already running'
            self._logger.info(msg)
            await self.put(Protocol.error(msg=msg))
            return

        if self._hash:
            try:
                with open(self._exe, 'rb') as file_to_check:
                    data = file_to_check.read()
                    if self._hash != hashlib.md5(data).hexdigest():
                        await self.log_and_send_error(f'{self._exe} checksum mismatch')
                        return
            except FileNotFoundError as e:
                msg = f'{self._exe} missing'
                await self.put(Protocol.error(msg=msg))
                if self.is_optional:
                    return
                else:
                    await self.log_and_send_error(f'{msg}: {e}')
                    return

        self._logger.info(f'Starting {self.child_title} server')

        os.makedirs(f'{self.directory}/logs/session', exist_ok=True)
        os.makedirs(f'{self.directory}/logs/error', exist_ok=True)

        if self._logfile_use_timestamp:
            timestamp = '-' + datetime.now().strftime("%Y%m%d_%H%M%S")
        else:
            timestamp = ''

        self._logfile_stdout = f'{self.directory}/logs/session/output{timestamp}.log'
        self._logfile_stderr = f'{self.directory}/logs/error/error{timestamp}.log'

        session_file = open(self._logfile_stdout, 'w', encoding='utf-8')
        error_file = open(self._logfile_stderr, 'w', encoding='utf-8')

        # Set platform specific options to start process in seperate process group
        kwargs = {}
        if sys.platform.startswith('win'):
            kwargs['creationflags'] = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS | subprocess.CREATE_BREAKAWAY_FROM_JOB
        else:
            kwargs['start_new_session'] = True

        try:
            cmd = (self._exe,) + self._args
            self._process = await asyncio.create_subprocess_exec(
                *cmd, cwd=self._cwd, stdout=session_file, stderr=error_file, **kwargs)

            self.running = True

            self._logger.info(f'Process pid is: {self._process.pid}')
            await self.put(Protocol.success(msg=f'{self.child_title} started'))
        except FileNotFoundError as e:
            await self.log_and_send_error(f'start command failed : {e}')
            return
        except PermissionError as e:
            await self.log_and_send_error(f'start command failed : {e}')
            return

        self.post_start_hook()

    async def stop(self):
        '''Stop the child server'''

        self.pre_stop_hook()

        if not self.running:
            msg = f'stop command ignored - {self.child_short} not running'
            self._logger.info(msg)
            await self.put(Protocol.error(msg=msg))
            return

        self._logger.info(f'Stopping {self.child_title} server')

        try:
            self._process.terminate()

            status_code = await asyncio.wait_for(self._process.wait(), None)

            self._logger.info(
                f'{self.child_title} server exited with {status_code}')
            await self.put(Protocol.success(msg=f'{self.child_title} server stopped'))
        except ProcessLookupError as e:
            self._logger.error(
                f'{self.child_title} server already exited with {e}')
            await self.put(Protocol.error(msg=f'{self.child_title} server ALREADY stopped'))

        self.running = False

        self.post_stop_hook()
