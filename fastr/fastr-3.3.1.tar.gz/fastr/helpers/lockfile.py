# Copyright 2011-2014 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A module implenting a lock that ensures a directory is only being used
by a single fastr run.
"""

import os
from pathlib import Path
import psutil
from typing import Optional, Union

from ..exceptions import FastrLockNotAcquired


class DirectoryLock:
    """
    A lock for a directory, it creates a directory to set the locked state and
    if successful writes the pid in a file inside that directory to claim the
    lock
    """
    lock_dir_name: str = '.fastr.lock'
    pid_file_name: str = 'pid'

    def __init__(self, directory: Union[str, Path]):
        self._directory = Path(directory)
        self._acquired = False

    @property
    def lock_dir(self) -> Path:
        return self._directory / self.lock_dir_name

    @property
    def pid_file(self) -> Path:
        return self.lock_dir / self.pid_file_name

    def get_pid(self) -> Optional[int]:
        try:
            lock_pid = int(self.pid_file.read_text())
        except (FileNotFoundError, ValueError):
            lock_pid = None

        return lock_pid

    @staticmethod
    def _checkpid(pid) -> bool:
        return psutil.pid_exists(pid)

    def acquire(self) -> bool:
        # If acquired, validate lock is still in place
        if self._acquired:
            lock_pid = self.get_pid()

            if lock_pid is None:
                self.release()
                return False

            if lock_pid == os.getpid():
                return True
            else:
                self.release()
                return False

        # Try to create a lock directory and make sure it does not exist
        if self.lock_dir.exists() or self.lock_dir.is_dir():
            if self.pid_file.exists():
                pid = self.get_pid()

                if not self._checkpid(pid):
                    self.release(force=True)
                else:
                    return False
            else:
                return False

        try:
            self.lock_dir.mkdir(parents=False, exist_ok=False)
        except FileExistsError:
            return False

        # Register creating PID in file in lock dir
        self.pid_file.write_text(str(os.getpid()))

        self._acquired = True

        return True

    def release(self, force: bool=False):
        if not force and not self._acquired:
            return

        lock_pid = self.get_pid()

        if lock_pid is None or force or lock_pid == os.getpid():
            try:
                self.pid_file.unlink()
            except FileNotFoundError:
                pass

            try:
                self.lock_dir.rmdir()
            except FileNotFoundError:
                pass

        self._acquired = False

    def __enter__(self):
        if not self.acquire():
            raise FastrLockNotAcquired(self._directory)

    def __exit__(self, type, value, traceback):
        self.release()

    def __del__(self):
        self.release()


