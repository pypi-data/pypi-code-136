import dataclasses
import logging
from typing import List, Optional
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """'If' conditional branch.

    If the condition is True, runs the tasks in 'then_tasks'. If the 'condition' is False, run the tasks in 'else_tasks'.
    """
    VERSION = '0.1.0'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Config:
        condition: bool
        then_tasks: List[irisml.core.TaskDescription]
        else_tasks: Optional[List[irisml.core.TaskDescription]] = dataclasses.field(default_factory=list)

    def execute(self, inputs):
        logger.info(f"Condition is {self.config.condition}")
        tasks = self.config.then_tasks if self.config.condition else self.config.else_tasks
        for task_description in tasks:
            task = irisml.core.Task(task_description)
            task.load_module()
            task.execute(self.context)

        return self.Outputs()

    def dry_run(self, inputs):
        return self.execute(inputs)
