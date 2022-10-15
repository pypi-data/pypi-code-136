from typing import Callable, Dict, TypeVar

from typing_extensions import ParamSpec

from .manager import ParameterManager, ParamManager
from .models import Arguments, BoundArguments, Parameter

PS = ParamSpec("PS")
RT = TypeVar("RT")

MANAGER: ParameterManager = ParamManager()


def get_parameters(func: Callable, /) -> Dict[str, Parameter]:
    return MANAGER.get_parameters(func)


def get_arguments(func: Callable, arguments: Arguments) -> BoundArguments:
    return MANAGER.get_arguments(func, arguments)


def params(func: Callable[PS, RT], /) -> Callable[PS, RT]:
    return MANAGER.params(func)
