# Copyright (C) 2022 ALBA Synchrotron
#
# This file is part of dataflow
#
# dataflow is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dataflow is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dataflow.  If not, see <http://www.gnu.org/licenses/>.

"""
Task
----

Task flowing through the workflow
"""

import multiprocessing
import threading


class NestLevel(object):
    """
    Task nested level.

    Counts the level of nested operation.
    When the level get's back to 0 the task is ready.
    """

    def __init__(self, lock=None):
        self._lock = threading.Lock()
        self._ready = threading.Event()
        self.level = 0

    def __enter__(self):
        with self._lock:
            if self.level == 0:
                self._ready.clear()
            self.level += 1

    def __exit__(self, *args):
        with self._lock:
            self.level -= 1
            if self.level == 0:
                self._ready.set()

    @property
    def ready(self):
        return self._ready.is_set()

    def wait(self, timeout=None):
        result = self._ready.wait(timeout)
        return result


class Task(object):
    """
    Task flowing through the workflow

    data key is the name of the operation
    data value is a list of operation results.
    """

    def __init__(self):
        self.data = {}
        self.queue = {}
        self._futures = []
        self._lock = threading.Lock()
        self.last = None
        self.running = NestLevel()

    @property
    def ready(self):
        return self.running.ready and self.remaining == 0

    @property
    def remaining(self):
        with self._lock:
            self._futures = [
                future for future in self._futures if not future.done()
            ]
            remaining = len(self._futures)
        return remaining

    @property
    def results(self):
        with self._lock:
            results = [future.result() for future in self._futures]
        return results

    def add_data(self, operator_name, data):
        """
        Add data to the task from the specific operator
        """
        # print("task:", self.data)
        with self._lock:
            if operator_name not in self.data:
                self.data[operator_name] = []
            self.data[operator_name].append(data)
            self._futures.append(data)
            self.last = operator_name

    def get_data(self, operator_name=None):
        """
        Get data to the task from the specific operator

        If no operator name is provided, data from last operator is given
        """
        if operator_name is None:
            operator_name = self.last
        with self._lock:
            data = self.data[operator_name]
        return data

    def get_queue(self, q_name):
        if q_name not in self.queue:
            with self._lock:
                # print("q>>")
                self.queue[q_name] = multiprocessing.Queue()
                # print("<<")
        return self.queue[q_name]
