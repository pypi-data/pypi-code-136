# Copyright (C) 2021 ALBA Synchrotron
#
# This file is part SDM Core
#
# SDM Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SDM Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SDM Core.  If not, see <http://www.gnu.org/licenses/>.
"""
Worker
------

Object executing a single operation and keeping persistent artifacts.
"""

from enum import Enum


class WkState(Enum):
    """
    Operator state
    """

    CREATED = 0
    RUNNING = 1
    SUSPENDED = 2
    CLOSED = 3


class Worker(object):
    """
    Worker executing a task and keepig the artefact.

    It stablished the communication with the workflow
    and finishes when the task is done.
    """

    def __init__(self, operator):
        self._state = WkState.CREATED
        self.operator = operator

    @property
    def state(self):
        return self._state

    def run(self):
        self._state = WkState.RUNNING

