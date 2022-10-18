import typing
from typing import Callable, List, Optional, Union


class TaskDeclarations:
    def __init__(self):
        self.tasks = {}
        self.aliases = {}
        self.dependencies = {}


class TaskDeclarationsHolder:
    INSTANCE: Optional[TaskDeclarations] = None

    def __enter__(self):
        TaskDeclarationsHolder.INSTANCE = TaskDeclarations()
        return TaskDeclarationsHolder.INSTANCE

    def __exit__(self, exc_type, exc_val, exc_tb):
        TaskDeclarationsHolder.INSTANCE = None


def task(
    task_callable: Callable = None,
    *,
    aliases: Optional[List[str]] = None,
    depends_on: Optional[List[Union[str, Callable]]] = None,
) -> Callable:
    if task_callable is None:
        return lambda func: task(func, aliases=aliases, depends_on=depends_on)

    if aliases is None:
        aliases = []
    if depends_on is None:
        depends_on = []

    def resolve_callable_name(callable_or_name: Union[Callable, str]) -> str:
        if isinstance(callable_or_name, typing.Callable):
            return callable_or_name.__name__
        elif isinstance(callable_or_name, str):
            return callable_or_name
        else:
            raise ValueError(f"Cannot resolve name for type {callable_or_name.__class__}")

    task_name = resolve_callable_name(task_callable)

    TaskDeclarationsHolder.INSTANCE.tasks[task_name] = task_callable
    TaskDeclarationsHolder.INSTANCE.aliases[task_name] = aliases
    TaskDeclarationsHolder.INSTANCE.dependencies[task_name] = [resolve_callable_name(d) for d in depends_on]

    return task_callable
