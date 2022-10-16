import functools
import inspect
import sys
from typing import Optional, List

from fastapi import FastAPI
from starlette.routing import Route

from myc.awslambda import create_aws_lambda_function_wrapper
from myc.build import create_build_function_wrapper
from myc.endpoint import AWSLambdaFunctionEndpoint, EndpointRegistry, PlatformKind, Endpoint, \
    FastAPIFunctionEndpoint, GeneralFunctionEndpoint
from myc.common import determine_current_platform
from myc.fastapi_ import FastAPIWrapper


class Service:
    """
    Manages a single (micro)service within a Mycelium application.
    """
    def __init__(self, name: str, endpoint_registry: EndpointRegistry):
        self._ep_registry = endpoint_registry
        self._name = name
        self._fastapi: Optional[FastAPIWrapper] = None

    @property
    def name(self):
        return self._name

    def create_fastapi(self) -> FastAPI:
        if self._fastapi is None:
            raw_fastapi = FastAPI()
            self._fastapi = FastAPIWrapper(raw_fastapi, self, self._ep_registry)

        return self._fastapi

    @property
    def fastapi(self) -> FastAPIWrapper:
        if self._fastapi is None:
            return self.create_fastapi()
        return self._fastapi

    def http_endpoint(self, platform=PlatformKind.ANY):
        """ Decorator for creating HTTP endpoints. """
        def decorator(fn):
            self._ep_registry.register_endpoint(GeneralFunctionEndpoint(self, fn, platform=platform))
            return create_general_function_wrapper(fn, self._ep_registry, platform_hint=platform)

        return decorator

    def rpc_endpoint(self):
        """ Decorator for creating RPC endpoints. """
        raise NotImplementedError

    def endpoint(self):
        """ Decorator for creating protocol-agnostic endpoints. """
        raise NotImplementedError

    # ----
    # Internal methods:

    # def _compile_fastapi_endpoints(self):
    #     for route in self._fastapi.routes:
    #         route: Route
    #
    #         if not route.include_in_schema:
    #             continue
    #
    #         if self._ep_registry.contains_callable(route.endpoint):
    #             continue
    #
    #         self._ep_registry.register_endpoint(FastAPIFunctionEndpoint(self, route.endpoint, route, self._fastapi))

    def compile_endpoints(self):
        """ Compiles a list of all endpoints hosted by this service. """
        pass
        # if self._fastapi is not None:
        #     self._compile_fastapi_endpoints()


def create_general_function_wrapper(fn, registry: EndpointRegistry, platform_hint: PlatformKind):
    platform = platform_hint if platform_hint != PlatformKind.ANY else determine_current_platform()
    if platform == PlatformKind.AWS_LAMBDA:
        return create_aws_lambda_function_wrapper(fn, registry)
    elif platform == PlatformKind.BUILD:
        return create_build_function_wrapper(fn)
    else:
        raise Exception('Unknown platform')
