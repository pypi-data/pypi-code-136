import inspect
from typing import Any, Callable

from sanic.blueprints import Blueprint as SanicBlueprint
from sanic.constants import HTTP_METHODS

from insanic.tasks import Task, TaskDefinition
from insanic.views import View

__all__ = (
    'Blueprint',
)

# Wrapper for class method routes.
# Inits class instance and executes method
# @TODO: Implement `before_method` for class based views
def wrap_class_handler(view_class: type, handler: Callable) -> Callable:
    def dispatcher(*args: Any, **kwargs: Any) -> Any:
        view = view_class()
        return handler(view, *args, **kwargs)

    # @TODO: Ugly hack and I don't remember for what!
    dispatcher.target = handler  # type: ignore[attr-defined]
    return dispatcher

class Blueprint(SanicBlueprint):  # pylint: disable=abstract-method
    tasks: dict[str, TaskDefinition] = {}

    def register_task(self, name: str, task_cls: type[Task], workers: int = 1, poll_delay: float = 0.5):
        self.tasks[name] = TaskDefinition(task_cls, workers=workers, poll_delay=poll_delay)

    def route_method(self, handler: Callable, *args: Any, http_method: str | None = None, **kwargs: Any) -> None:
        # Support for class methods routes like `ClassName.MethodName`
        # "staticmethod" stlye but with class initialization (see `wrap_class_handler`)
        if inspect.signature(handler).parameters.get('self'):
            handler_module = inspect.getmodule(handler)
            handler_class_name = handler.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0]
            handler_class = getattr(handler_module, handler_class_name)
            handler = wrap_class_handler(handler_class, handler)

        http_method = http_method or 'GET'
        kwargs['methods'] = [http_method]
        self.route(*args, **kwargs)(handler)

    # @FIXME: There is gotta be better way of routing the view
    def route_view(self, view_class: type[View], url: str, *args: Any, mapping: dict[str, Callable | tuple[Callable, str]] | None = None, **kwargs: Any) -> None:  # pylint: disable=line-too-long
        # @TODO: Validate view_class class
        mapping = mapping or {}
        kwargs['strict_slashes'] = kwargs.get('strict_slashes', self.strict_slashes)

        for method in HTTP_METHODS:
            mapped_handler = mapping.get(method.upper(), None)

            if isinstance(mapped_handler, tuple):
                method_url = f'{url.removesuffix("/")}/{mapped_handler[1].removeprefix("/")}'
                mapped_handler = mapped_handler[0]
            else:
                method_url = url

            handler_method = mapped_handler or getattr(view_class, method.lower(), None)

            if handler_method:  # @TODO: Validate handler_method is a method
                handler = wrap_class_handler(view_class, handler_method)
                self.route(method_url, *args, **kwargs, methods=(method,))(handler)

    def route_get(self, *args: Any, **kwargs: Any) -> None:
        kwargs['http_method'] = 'GET'
        self.route_method(*args, **kwargs)

    def route_post(self, *args: Any, **kwargs: Any) -> None:
        kwargs['http_method'] = 'POST'
        self.route_method(*args, **kwargs)
