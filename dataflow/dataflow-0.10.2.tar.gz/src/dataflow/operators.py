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
Operator interfaces
-------------------

Operators are nucleare operations that can be chained to create a workflow.
"""

import abc
import functools
from contextvars import ContextVar

from dataflow.task import Task

ctx_workflow: ContextVar = ContextVar("workflow")


class Operator(metaclass=abc.ABCMeta):
    """
    Operator base class
    """

    def __init__(self, name=None):
        if name is not None:
            self.name = name
        self.downstream = []
        self.workflow = ctx_workflow.get()
        self.workflow.register(self)

    @property
    def name(self):
        """
        Get operator's name
        """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __rshift__(self, other):
        """
        Add the outputs of self as the inputs of other
        self >> other
        """
        if isinstance(other, Operator):
            self.set_downstream(other)

        return other

    def set_downstream(self, other_operator):
        """
        add operator to downstream
        """
        self.downstream.append(other_operator)

    @abc.abstractmethod
    def send(self, data, task):
        """
        Send data and task to the operation.

        return stdout captured output
        """
        raise NotImplementedError

    @abc.abstractmethod
    def operation(self, *args, **kwargs):
        """
        Operation assigned by the decorator
        """
        raise NotImplementedError


class DummyOP(Operator):
    """
    Dummy operator
    """

    def send(self, data, task):
        return data

    def operation(self, *args, **kwargs):
        pass


# pylint: disable=abstract-method
class BasicOP(Operator):
    """
    Basic operator
    """

    def send(self, data, task: Task):
        outvalue = self.operation(data, task=task)  # pylint: disable=E1128
        # log print("Op", self.name, outvalue)
        # if a generator is received, run for all values.
        return outvalue


def op_decorator(op_class):
    """
    Operator decorator

    Generic function decorator to create a class derived from the specified
    operator class.

    Operation method of the new class is overriden by the decorated function.
    """

    def decorator(func):
        """
        Specific function decorator for the given operation class
        """
        # Function to override the operation method in the operator class
        # pylint: disable=unused-argument
        @functools.wraps(func)
        def operation(self, *args, **kwargs):
            return func(*args, **kwargs)

        # Class construction overiding operation method
        klass = type(func.__name__, (op_class,), {"operation": operation})
        klass.__module__ = func.__module__
        klass._name = func.__name__  # pylint: disable=protected-access
        return klass

    return decorator
