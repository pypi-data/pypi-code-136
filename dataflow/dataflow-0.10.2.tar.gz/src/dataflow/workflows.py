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
Workflow interfaces
-------------------

Workflows define the chain of operations for a data analysis.
"""

import abc
import functools
import inspect
from concurrent.futures import Future, ThreadPoolExecutor

from dataflow.operators import DummyOP, ctx_workflow
from dataflow.task import Task

DONE = type("DONE", (object,), {})
TIMEOUT = 3


class Workflow(metaclass=abc.ABCMeta):
    """
    Workflow base class

    Any workflow is a dag of operators, starting from the head operations
    and finishing in the out operator.

    The workflow may have sink operations that does not connect to other
    opeations and entry operations to receive inputs.

    A workflow has to be started with the run method.
    One can send data to an entry operation with the send method. Head is
    the default entry operation.
    The workflow will be waiting for inputs until the done method is called.

    One can concatenate workflows with >> instruction
    """

    def __init__(self):
        ctx_workflow.set(self)
        self._tasks = {}
        self.operator = {}
        DummyOP(name="head")
        DummyOP(name="out")
        self._init_dag()

    def register(self, operator):
        """
        Register operator in the workflow
        """
        name = operator.name
        # log print("Register", name)
        if name in self.operator:
            raise RuntimeError(f"{name} operator already exist in workflow")
        self.operator[name] = operator

    @property
    def head(self):
        """
        get workflow head operator
        """
        return self.operator["head"]

    @property
    def out(self):
        """
        get workflow out operator
        """
        return self.operator["out"]

    def get_data(self, op_name="out"):
        """
        Get workflow data from a given operator
        """
        result = {}
        for _, task in self._tasks.items():
            if op_name in task.data:
                result[id(task)] = task.data[op_name]
        return result

    @property
    def result(self):
        """
        Workflow result
        """
        return self.get_data()

    @abc.abstractmethod
    def _init_dag(self):
        """
        initialize the operations DAG
        """
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        """
        run workflow processing
        """
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, op_name, data, task_id):
        """
        send dataset to the operator
        """
        raise NotImplementedError

    def done(self):
        """
        no more data will be sent
        """
        for task_id in self._tasks.keys():
            self.send("head", DONE, task_id)

    def __rshift__(self, other):
        """
        Add the outputs of the workflow as the inputs of other operator
        self >> other
        """
        if isinstance(other, Workflow):
            other = other.head
        return self.out >> other


def wf_decorator(wf_class):
    """
    Workflow decorator

    Generic function decorator to create a class derived from the specified
    workflow class.

    """

    def decorator(func):
        @functools.wraps(func)
        def _init_dag(self):
            func(self.head, self.out)

        klass = type(func.__name__, (wf_class,), {"_init_dag": _init_dag})
        klass.__module__ = func.__module__
        return klass

    return decorator


# _init_dag is overridden with the wf_decorator
# pylint: disable=abstract-method
class ThreadWF(Workflow):
    """
    Workflow to run operations in threads
    """

    def __init__(self):
        super().__init__()
        n_threads = len(self.operator)
        self.executor = ThreadPoolExecutor(n_threads)

    def run(self):
        pass

    def send(self, op_name, data, task_id):
        if op_name is None:
            op_name = "head"
        operator = self.operator[op_name]

        if task_id is None:
            task = Task()
            task_id = id(task)
            self._tasks[task_id] = task
        task = self._tasks[task_id]

        with task.running:
            if data is None:
                pass
                # Broken task: output would be None

            else:
                output = self.executor.submit(self._process_data, operator,
                                              data, task)
                task.add_data(operator.name, output)
        return task_id

    def _process_data(self, operator, data, task):
        output = None
        # Enter to a new context of the running task.
        # This increases the number of running operations in the task.
        with task.running:
            if hasattr(
                operator.operation, "__wrapped__"
            ) and inspect.isgeneratorfunction(operator.operation.__wrapped__):
                generator = operator.send(data, task)
                output = []
                for out in generator:
                    output.append(out)
                    self._on_output(operator, out, id(task))
            else:
                output = operator.send(data, task)
                self._on_output(operator, output, id(task))

        return output

    def _on_output(self, operator, output, task_id):
        for next_op in operator.downstream:
            self.send(next_op.name, output, task_id)

    @property
    def result(self):
        """
        Workflow result
        """
        res = {}
        ready = [False]
        while not all(ready):
            ready = [task.ready for task in self._tasks.values()]
            for task_id, task in self._tasks.items():
                if not task.running.wait():
                    print(f"WARNING: task {task_id} timeout")
                # access results and rise exceptions
                if task_id not in res and task.ready:
                    if "out" in task.data:
                        result_list = task.data["out"]
                        values = []
                        for result in result_list:
                            if isinstance(result, Future):
                                result = result.result()
                                values.append(result)
                        res[task_id] = values
        for _, task in self._tasks.items():
            task.results
        return res
