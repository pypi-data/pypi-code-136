import inspect
from typing import Callable, Generic, List, Optional, Type, TypeVar, Union

from chalk.features.resolver import MachineType
from chalk.streams.StreamResolver import parse_stream_resolver

T = TypeVar("T")


class StateMeta(type):
    kind: Type

    def __getitem__(cls, item) -> "StateMeta":
        cls.kind = item
        return cls


class State(Generic[T], metaclass=StateMeta):
    kind: Type
    value: T

    def __init__(self, initial: T):
        self.value = initial

    def update(self, value):
        assert isinstance(value, self.kind)
        self.value = value


def stream(
    fn: Optional[Callable] = None,
    environment: Optional[Union[List[str], str]] = None,
    machine_type: Optional[MachineType] = None,
):
    caller_filename = inspect.stack()[1].filename

    def decorator(args, cf=caller_filename):
        return parse_stream_resolver(args, cf, environment, machine_type)

    return decorator(fn) if fn else decorator
