from typing import Any

from sanic.router import Route

from insanic.app import Application
from insanic.commands import SyncCommand, CommandParser
from insanic.tasks import TaskDefinition, run_workers
from insanic.utils import load_application


class TasksQueueCommand(SyncCommand):
    help = 'Runs workers for specified task'

    def print_tasks_list(self, available_tasks) -> None:
        for task_name, task_defintion in available_tasks.items():
            print(f'{task_name}\tworkers: {task_defintion.workers}, poll_delay: {task_defintion.poll_delay}')

    def get_available_tasks(self, application: Application) -> dict[str, TaskDefinition]:
        available_tasks = {}

        for blueprint_name, blueprint in application.blueprints.items():
            for task_name, task_definition in blueprint.tasks.items():
                available_tasks[f'{blueprint_name}:{task_name}'] = task_definition

        return available_tasks

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('task_name', nargs='?')

    def execute(self, task_name: str | None, **kwargs: Any) -> None:
        application = load_application()

        available_tasks = self.get_available_tasks(application)

        if not task_name:
            return self.print_tasks_list(available_tasks)

        task_definition = available_tasks.get(task_name, None)
        if not task_definition:
            raise Exception(f'Task "{task_name}" is not registered')

        run_workers(task_name, task_definition)
