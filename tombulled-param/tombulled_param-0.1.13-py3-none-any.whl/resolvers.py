from typing import Any, Callable, Protocol, Type, TypeVar, Union

from pydantic.fields import Undefined, UndefinedType
from roster import Register

from .errors import ResolutionError
from .parameters import Param

R = TypeVar("R", bound=Callable)


class Resolver(Protocol):
    def __call__(self, param: Param, argument: Union[Any, UndefinedType]) -> Any:
        ...


class Resolvers(Register[Type[Param], R]):
    pass


RESOLVERS: Resolvers[Resolver] = Resolvers()


@RESOLVERS(Param)
def resolve_param(param: Param, argument: Union[Any, UndefinedType]) -> Any:
    if argument is not Undefined:
        return argument
    elif param.has_default():
        return param.get_default()
    else:
        raise ResolutionError("No value provided and parameter has no default")
