import inspect
from collections import defaultdict
from enum import Enum
from typing import List, Optional


class PlatformKind(str, Enum):
    ANY = 'any'
    AWS_LAMBDA = 'aws_lambda'
    AWS_ECS = 'aws_ecs'
    BUILD = 'build'

    UNKNOWN = 'unknown'


class Endpoint:
    def __init__(self, service: 'Service', *, platform=PlatformKind.ANY):
        self._service = service
        self._platform_hint = platform

    @property
    def service(self) -> 'Service':
        return self._service

    @property
    def platform_hint(self) -> PlatformKind:
        return self._platform_hint

    def __hash__(self):
        raise NotImplementedError

    def get_module(self):
        raise NotImplementedError


class FunctionEndpoint(Endpoint):
    """
    Base class for endpoints that behave like function calls.
    """
    def __init__(self, service, function, *, platform=PlatformKind.ANY):
        super().__init__(service, platform=platform)
        self._function = function

    @property
    def function(self):
        return self._function

    def get_module(self):
        return inspect.getmodule(self._function)

    def __hash__(self):
        return hash(self._function)


class RestFunctionEndpoint(FunctionEndpoint):
    pass


class AWSLambdaFunctionEndpoint(RestFunctionEndpoint):
    """ TODO: deprecate """
    def __init__(self, service, function, *, function_url=None, platform: PlatformKind):
        super().__init__(service, function, platform=platform)
        self.function_url = function_url


class GeneralFunctionEndpoint(RestFunctionEndpoint):
    pass


class FastAPIFunctionEndpoint(RestFunctionEndpoint):
    def __init__(self, service, function, route, fastapi, *, platform=PlatformKind.ANY):
        super().__init__(service, function, platform=platform)
        self.route = route
        self.fastapi = fastapi


class EndpointRegistry:
    def __init__(self):
        self._endpoints = []
        self._endpoints_by_module = defaultdict(list)
        self._callable_to_endpoint = {}

    @property
    def endpoints(self) -> List[Endpoint]:
        return self._endpoints

    def register_endpoint(self, endpoint: Endpoint):
        """ Internal function to register an endpoint with the application. """
        self._endpoints.append(endpoint)
        self._endpoints_by_module[endpoint.get_module()].append(endpoint)

        if isinstance(endpoint, FunctionEndpoint):
            self._callable_to_endpoint[endpoint.function] = endpoint

    def get_endpoint_id(self, endpoint: Endpoint):
        """
        Returns a unique identifier for the specified endpoint.
        This function returns the same result regardless of the environment
        in which this function is invoked (i.e. should return same value in
        compilation environment when compared to a deployed environment).
        """
        module_endpoints = self._endpoints_by_module[endpoint.get_module()]
        endpoint_index = module_endpoints.index(endpoint)

        # TODO: add module path to ID

        if isinstance(endpoint, FunctionEndpoint):
            return f'{endpoint.function.__qualname__}:{endpoint_index}'

    def get_callable_id(self, fn) -> Optional[str]:
        ep = self._callable_to_endpoint.get(fn)
        if ep is None:
            return None

        return self.get_endpoint_id(ep)

    def contains_callable(self, fn) -> bool:
        return fn in self._callable_to_endpoint
