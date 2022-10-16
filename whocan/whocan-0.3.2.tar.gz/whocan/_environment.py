import dataclasses
import typing


ConditionFunc = typing.Callable[[typing.Any, typing.Any], bool]


@dataclasses.dataclass
class PolicyEnvironment:
    """Environment in which policies are being created."""

    condition_functions: typing.Dict[str, ConditionFunc]
