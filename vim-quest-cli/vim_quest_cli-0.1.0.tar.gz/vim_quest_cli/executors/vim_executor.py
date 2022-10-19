from vim_quest_cli.executors.executor_interface import Executor
from vim_quest_cli.status import VimGlobalStatus


class VimExecutor(Executor):

    def execute_command(self, state: VimGlobalStatus) -> VimGlobalStatus:
        # TODO : use real vim there
        pass
