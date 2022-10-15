import functools
import inspect
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Generic, Iterable, Optional, Type, TypeVar

from pydantic.fields import Undefined
from typing_extensions import ParamSpec

from .errors import ResolutionError
from .models import Arguments, BoundArguments, Parameter, Resolvable
from .parameters import Param
from .resolvers import RESOLVERS, Resolver, Resolvers

PS = ParamSpec("PS")
RT = TypeVar("RT")

R = TypeVar("R", bound=Callable)


def _bind_arguments(func: Callable, arguments: Arguments) -> BoundArguments:
    signature: inspect.Signature = inspect.signature(func)

    bound_arguments: inspect.BoundArguments = arguments.call(signature.bind)

    bound_arguments.apply_defaults()

    bound_args: Dict[str, Any] = dict(zip(signature.parameters, bound_arguments.args))
    bound_kwargs: Dict[str, Any] = bound_arguments.kwargs

    return BoundArguments(args=bound_args, kwargs=bound_kwargs)


@dataclass
class ParameterManager(Generic[R]):
    resolvers: Resolvers[R]

    @staticmethod
    def get_parameters(func: Callable, /) -> Dict[str, Parameter]:
        return {
            parameter.name: Parameter.from_parameter(parameter)
            for parameter in inspect.signature(func).parameters.values()
        }

    def get_param(self, parameter: Parameter, /) -> Optional[Param]:
        if isinstance(parameter.default, Param):
            return parameter.default
        else:
            return None

    def get_resolver(self, param_cls: Type[Param], /) -> R:
        resolver: Optional[R] = self.resolvers.get(param_cls)

        if resolver is not None:
            return resolver
        else:
            raise ResolutionError(f"No resolver for parameter {param_cls}")

    def resolve(self, resolvable: Resolvable) -> Any:
        raise ResolutionError("Resolution method not implemented")

    def resolve_all(
        self,
        resolvables: Iterable[Resolvable],
        /,
    ) -> Dict[str, Any]:
        return {
            resolvable.parameter.name: self.resolve(resolvable)
            for resolvable in resolvables
        }

    def get_resolvables(
        self, func: Callable, arguments: Arguments, /
    ) -> Dict[str, Resolvable]:
        bound_arguments: BoundArguments = _bind_arguments(func, arguments)
        parameters: Dict[str, Parameter] = self.get_parameters(func)
        resolvables: Dict[str, Resolvable] = {}

        parameter_name: str
        argument: Any
        for parameter_name, argument in bound_arguments.arguments.items():
            parameter: Parameter = parameters[parameter_name]
            specification: Optional[Param] = self.get_param(parameter)

            if specification is None:
                continue

            if argument is specification:
                argument = Undefined

            resolvable: Resolvable = Resolvable(
                parameter=parameter, field=specification, argument=argument
            )

            resolvables[parameter_name] = resolvable

        return resolvables

    def get_arguments(self, func: Callable, arguments: Arguments) -> BoundArguments:
        resolvables: Dict[str, Resolvable] = self.get_resolvables(func, arguments)
        parameters: Dict[str, Parameter] = self.get_parameters(func)
        bound_arguments: BoundArguments = _bind_arguments(func, arguments)
        resolved_arguments: Dict[str, Any] = self.resolve_all(resolvables.values())

        args: Dict[str, Any] = {}
        kwargs: Dict[str, Any] = {}

        parameter: Parameter
        for parameter in parameters.values():
            destination: Dict[str, Any]

            if parameter.name in bound_arguments.args:
                destination = args
            else:
                destination = kwargs

            argument: Any

            if parameter.name in resolvables:
                argument = resolved_arguments[parameter.name]
            else:
                argument = bound_arguments.arguments[parameter.name]

            destination[parameter.name] = argument

        return BoundArguments(args=args, kwargs=kwargs)

    def params(self, func: Callable[PS, RT], /) -> Callable[PS, RT]:
        @functools.wraps(func)
        def wrapper(*args: PS.args, **kwargs: PS.kwargs) -> RT:
            arguments: Arguments = Arguments(args=args, kwargs=kwargs)

            bound_arguments: BoundArguments = self.get_arguments(func, arguments)

            return bound_arguments.call(func)

        return wrapper


@dataclass
class ParamManager(ParameterManager[Resolver]):
    resolvers: Resolvers[Resolver] = field(default_factory=lambda: RESOLVERS)

    def get_param(self, parameter: Parameter, /) -> Param:
        specification: Optional[Param] = super().get_param(parameter)

        if specification is not None:
            return specification
        else:
            return Param(default=parameter.default)

    def resolve(
        self,
        resolvable: Resolvable,
    ) -> Any:
        resolver_cls: Type[Param] = type(resolvable.field)
        resolver: Resolver = self.get_resolver(resolver_cls)

        return resolver(resolvable)
