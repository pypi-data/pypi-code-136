# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from blacksheep import Request, FromJSON
from blacksheep.server.controllers import ApiController, get, post, delete, ws
from requests import Session
from typing import List, Optional

from .iexecutionservice import IExecutionService
from ..docs import docs
from ..model.function import FunctionProfile
from ...dsl.widgets import Widget


class ExecutionHttpServer(ApiController):
    def __init__(self, svr: IExecutionService) -> None:
        self._svr = svr
        super().__init__()

    @classmethod
    def route(cls) -> Optional[str]:
        return '/api/executions'

    @post("/runFn")
    async def run_execution(self, fn: FromJSON[FunctionProfile]) -> Widget:
        function = FunctionProfile(body=fn.value.body,
                                   parameters=fn.value.parameters,
                                   result=fn.value.result)
        result = self._svr.execute_function(function)
        return result.to_dict_widget()


class ExecutionHttpProxy(IExecutionService):
    def __init__(self, session: Session) -> None:
        self.session = session

    def execute_function(self):
        return self.session.post('/api/executions/runFn/')
