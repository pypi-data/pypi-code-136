import contextvars
import functools
import inspect

from fastapi import FastAPI

from myc.common import CURRENT_PLATFORM_OVERRIDE, set_current_platform
from myc.endpoint import EndpointRegistry, FastAPIFunctionEndpoint, PlatformKind
from myc.invoke import invoke_endpoint, invoke_endpoint_async

IN_FASTAPI_CTXVAR = contextvars.ContextVar('in_fastapi', default=False)


class FastAPIWrapper:
    """
    FastAPI application instrumentalization wrapper.
    """
    def __init__(self, app: FastAPI, service: 'Service', ep_registry: EndpointRegistry):
        self._app = app
        self._service = service
        self._ep_registry = ep_registry

    def get(self, *args, **kwargs):
        fastapi_decorator = self._app.get(*args, **kwargs)

        def decorator(fn):
            wrapper = create_fastapi_function_wrapper(fn, ep_registry=self._ep_registry)
            result = fastapi_decorator(wrapper)

            # find matching FastAPI route
            # TODO: verify that this logic is correct:
            route = self._app.routes[-1]
            assert route.endpoint == wrapper

            self._ep_registry.register_endpoint(
                FastAPIFunctionEndpoint(
                    self._service,
                    fn,
                    route,
                    self._app,
                )
            )

            return result

        return decorator

    async def __call__(self, scope, receive, send):
        set_current_platform(PlatformKind.AWS_ECS)
        IN_FASTAPI_CTXVAR.set(True)
        try:
            return await self._app(scope, receive, send)
        finally:
            IN_FASTAPI_CTXVAR.set(False)

    def __getattr__(self, item):
        return getattr(self._app, item)


def create_fastapi_function_wrapper(fn, ep_registry: EndpointRegistry):
    if inspect.iscoroutinefunction(fn):
        # create asynchronous wrapper
        @functools.wraps(fn)
        async def wrapper(*args, **kwargs):
            in_runtime = IN_FASTAPI_CTXVAR.get()
            endpoint_id = ep_registry.get_callable_id(fn)

            token = IN_FASTAPI_CTXVAR.set(False)
            try:
                return await invoke_endpoint_async(endpoint_id, fn, in_runtime, args, kwargs)
            finally:
                IN_FASTAPI_CTXVAR.reset(token)
    else:
        # create synchronous wrapper
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            in_runtime = IN_FASTAPI_CTXVAR.get()
            endpoint_id = ep_registry.get_callable_id(fn)

            token = IN_FASTAPI_CTXVAR.set(False)
            try:
                return invoke_endpoint(endpoint_id, fn, in_runtime, args, kwargs)
            finally:
                IN_FASTAPI_CTXVAR.reset(token)

    return wrapper
