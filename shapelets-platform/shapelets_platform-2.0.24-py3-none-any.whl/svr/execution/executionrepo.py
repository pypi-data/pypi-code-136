# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .iexecutionrepo import IExecutionRepo


def _execute_function(fn):
    pass


class ExecutionRepo(IExecutionRepo):

    def execute_function(self, fn: str):
        _execute_function(fn)
