# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod


class IExecutionRepo(ABC):
    @abstractmethod
    def execute_function(self, fn: str):
        pass
