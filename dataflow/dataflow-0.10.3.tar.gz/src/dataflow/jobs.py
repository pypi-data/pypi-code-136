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
Job factory an interfaces
-------------------------

Jobs are the the executions of the workflows and can be done in different ways.
The factory discover available jobs from the *dataflow_job* entry point.
"""

import abc
import json
import subprocess
from concurrent.futures import Future
from enum import Enum
from typing import Any, Dict

DATAFLOW_JOB = "dataflow_job"


class JobState(Enum):
    """
    Job state
    """

    FAULT = 0
    RUNNING = 1
    WAITING = 2
    STOPPED = 3


class Job(metaclass=abc.ABCMeta):
    """
    Job base class
    """

    _params: Dict[str, Any] = {}
    _name = "NotDefined"

    def __init__(self):
        self._id = None
        self.state = JobState.STOPPED
        self.future = Future()
        self.last_task = None

    def __getattr__(self, name):
        if name in self._params:
            return self._params[name]

    def __dir__(self):
        attrs = []
        # show only class callables and job parameters
        for key, value in self.__class__.__dict__.items():
            if callable(value):
                attrs.append(key)
        attrs += self._params.keys()
        return attrs

    @abc.abstractmethod
    def prepare(self):
        """
        Prepare the job at the infrastructure and store the job id
        """
        return NotImplementedError

    @abc.abstractmethod
    def submit(self, data):
        """
        Send data to new task
        """
        return NotImplementedError

    @abc.abstractmethod
    def send(self, data, target=None, task_id=None):
        """
        Send new data to the job.

        If no task id is passed, last task_id is used
        """
        return NotImplementedError

    @abc.abstractmethod
    def done(self):
        """
        No more data will be sent to the job.
        """
        return NotImplementedError

    @property
    def id(self):  # pylint: disable=invalid-name
        """
        Get the job id.
        """
        return self._id

    @property
    def name(self):
        """
        Get the job name.
        """
        return self._name

    @property
    def result(self):
        """
        Get job result as list of futures
        """
        return self.future.result()

    def __enter__(self):
        self.prepare()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class NullJob(Job):
    """
    Null Job to represent non existing jobs
    """

    @property
    def name(self):
        """
        Get the job name.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Set the job name.
        """
        self._name = name

    def prepare(self):
        """
        can not be prepared
        """
        print("Unknown job %s" % self.name)  # pylint: disable=C0209
        return None

    def submit(self, data, target=None, task_id=None):
        """
        can not send data
        """

    def send(self, data, target=None, task_id=None):
        """
        can not send data
        """

    def done(self):
        """
        can not be done since it can not send data
        """


class LocalJob(Job):
    """
    Job running in local current process
    """

    _name = "LocalJob"
    workflow_class = None

    def __init__(self):
        super().__init__()
        self.workflow = self.workflow_class()  # pylint: disable=not-callable

    def prepare(self):
        """
        prepare the jobs in the current process
        """
        self.workflow.run()
        if not self.future.set_running_or_notify_cancel():
            self.done()

    def submit(self, data):
        """
        send data to new task
        """
        self.last_task = self.workflow.send(None, data, None)
        print(f"task_id:{self.last_task}")
        return self.last_task

    def send(self, data, target=None, task_id=None):
        """
        send data to the workflow
        """
        if task_id is None:
            task_id = self.last_task
        new_task_id = self.workflow.send(target, data, task_id)
        print(f"task_id:{new_task_id}")
        return new_task_id

    def done(self):
        """
        no more data will be sent to the workflow
        """
        self.workflow.done()
        result = self.workflow.result
        self.future.set_result(result)
        print(json.dumps(result))


class SshJob(Job):
    """
    Job running in remote host
    """

    _name = "SshJob"
    remote_job = "MyJob"
    conda_env = "dataflow"
    user_host = "pcblXXXX"

    def __init__(self):
        super().__init__()
        self.ssh = None

    def prepare(self):
        """
        Prepare jobs in the remote machine
        """
        print(f"preparing job at {self.user_host}")
        command = (
            f"conda activate {self.conda_env}; "
            f"dataflow run {self.remote_job}"
        )
        self.ssh = subprocess.Popen(
            ["ssh", "-tt", self.user_host, command],
            shell=False,
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        for _ in range(7):
            self.ssh.stdout.readline()

        if not self.future.set_running_or_notify_cancel():
            self.done()

    def submit(self, data):
        """
        send data to new task
        """
        self.last_task = self.send(data)

    def send(self, data, target=None, task_id=None):
        """
        send data to the workflow
        """
        if task_id is None:
            task_id = self.last_task

        if task_id is None and target is None:
            command = f"send {str(data)}\n"
        elif target is None:
            command = f"send {str(data)} -> {task_id}\n"
        else:
            if task_id is None:
                task_id = ""
            command = f"send {str(data)} -> {task_id}:{target}\n"
        lines = self._send_cmd(command)
        for line in lines:
            if "task_id:" in line:
                _, task_id, *_ = line.split(":")
                self.last_task = int(task_id)
        return self.last_task

    def done(self):
        """
        no more data will be sent to the workflow
        """
        command = "done\n"
        lines = self._send_cmd(command)
        for line in self.ssh.stderr:
            line = line.rstrip()
            print(line)
        for line in lines:
            if line[0] == "{":
                result = json.loads(line)
        self.future.set_result(result)

    def _send_cmd(self, command, promp="-DF->\n"):
        print(command, file=self.ssh.stdin, flush=True)
        lines = []
        line = " "
        while line != promp:
            line = self.ssh.stdout.readline()
            if promp[:-1] not in line:
                if len(line) > 1:
                    print(line[:-1])
                    lines.append(line)
        return lines


class JobService(object):
    """
    Job Service to create jobs
    """

    _jobs: Dict[str, Job] = {}

    def __init__(self):
        self.load_jobs()

    def load_jobs(self):
        """
        discover jobs from entry points
        """
        # TODO: search for DATAFLOW_JOB entry points
        # meanwhile ...
        self._jobs = {}

    def create(self, jobname, params={}):  # pylint: disable=W0102
        """
        create job with the given jobname and parameters
        """
        if jobname in self.jobs:
            job = self.jobs[jobname]()
            for par, val in params.items():
                if par not in dir(job):
                    raise AttributeError
                setattr(self, par, val)
            return job
        else:
            nulljob_class = NullJob
            nulljob = nulljob_class()
            nulljob.name = jobname
            return nulljob

    @property
    def jobs(self) -> Dict[str, Job]:
        """
        dictionary of available jobs
        """
        return self._jobs


job_service = JobService()
