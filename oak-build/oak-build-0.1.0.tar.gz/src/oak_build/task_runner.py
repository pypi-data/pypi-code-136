from collections import OrderedDict
from dataclasses import dataclass
from inspect import signature
from typing import List, Dict, Any, Callable, Optional

from toposort import toposort_flatten

from oak_build.oak_file import OakFile


DUMMY = 0


def unify_task_name(name: str):
    return name.replace("-", "_")


@dataclass
class TaskResult:
    exit_code: int
    exit_params: Dict
    error: Optional[Exception]


class TaskRunner:
    def run_tasks(self, oak_file: OakFile, tasks: List[str]) -> List[str]:
        errors = []

        tasks = [unify_task_name(t) for t in tasks]

        known_tasks = set(oak_file.tasks.keys()).union(oak_file.aliases.keys())
        for task in tasks:
            if task not in known_tasks:
                errors.append(f"Unknown task {task}")
        if errors:
            return errors

        tasks_to_run = self._deduct_tasks_to_run(oak_file, tasks)
        arguments = {}  # Maybe fill params
        for task in tasks_to_run:
            task_result = self.run_task(task, oak_file.tasks[task], oak_file.context, arguments)
            if task_result.exit_code == 0:
                arguments.update({f"{task}_{key}": value for key, value in task_result.exit_params.items()})
            elif task_result.error is None:
                return [f"Task {task} failed with exit code {task_result.exit_code}"]
            else:
                return [f"Task {task} failed with exception {task_result.error}"]  # Return Exception?
        return []

    @staticmethod
    def _deduct_tasks_to_run(oak_file: OakFile, tasks: List[str]) -> List[str]:
        edges = {}

        for dependant, dependencies in oak_file.dependencies.items():
            edges[dependant] = set(dependencies)

        result = OrderedDict()

        def recursive_append(target: Dict, source: Dict, key: Any):
            if key in source:
                target[key] = source[key]
                for x in target[key]:
                    if x not in target.keys():
                        recursive_append(target, source, x)

        for task in tasks:
            # Here we create subset of all dependencies that includes only selected tasks and its dependencies
            dependencies_subset = {}
            recursive_append(dependencies_subset, edges, task)
            task_required = toposort_flatten(dependencies_subset)
            for x in task_required:
                result[x] = DUMMY

        return list(result.keys())

    def run_task(self, task_name: str, task_callable: Callable, context: Dict, arguments: Dict):
        sig = signature(task_callable)
        locals_values = {}
        for arg in sig.parameters:
            locals_values[arg] = arguments.get(arg)
        exception = None

        try:
            exec(f'RESULT = {task_name}({", ".join(locals_values.keys())})', context, locals_values)
        except Exception as e:
            exception = e
        res = locals_values.get("RESULT")

        if exception is not None:
            return TaskResult(1, {}, exception)
        elif res is None:
            return TaskResult(0, {}, None)
        elif isinstance(res, int):
            return TaskResult(res, {}, None)
        elif isinstance(res, dict):
            return TaskResult(0, res, None)
        elif isinstance(res, tuple) and (len(res) == 2) and isinstance(res[0], int) and isinstance(res[1], dict):
            return TaskResult(res[0], res[1], None)
        else:
            return TaskResult(1, {}, Exception(f"Incorrect return type for task {task_name}. Must be int, dict or tuple(int, dict)"))
