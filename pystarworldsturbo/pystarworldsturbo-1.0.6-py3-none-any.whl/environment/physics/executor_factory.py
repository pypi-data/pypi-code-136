from typing import Optional

from .action_executor import ActionExecutor
from ...common.action import Action
from ...utils.utils import ignore



class ExecutorFactory():
    @staticmethod
    def get_executor_for(action: Action) -> Optional[ActionExecutor]:
        # Abstract.
        ignore(action)

        return None
