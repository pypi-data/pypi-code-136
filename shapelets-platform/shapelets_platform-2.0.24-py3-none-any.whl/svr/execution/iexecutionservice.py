# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod

from ..model.function import FunctionProfile
from ...dsl.widgets import Widget


class IExecutionService(ABC):
    @abstractmethod
    def execute_function(self, fn: FunctionProfile) -> Widget:
        pass
