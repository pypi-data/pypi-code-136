from typing import List

from myc.endpoint import Endpoint, EndpointRegistry
from myc.service import Service


class MyceliumServices:
    pass


class Mycelium:
    """

    """

    def __init__(self):
        self._services = {}
        self._services_object = MyceliumServices()
        self._endpoint_registry = EndpointRegistry()

    @property
    def endpoint_registry(self) -> EndpointRegistry:
        return self._endpoint_registry

    def compile_endpoints(self) -> List[Endpoint]:
        """ Compiles a list of all endpoints used by this application. """
        for service in self._services.values():
            service.compile_endpoints()

        return self._endpoint_registry.endpoints

    def create_service(self, name: str):
        """ Creates and registers a new service with the application. """
        if name in self._services:
            raise ValueError('service with the same name already registered')

        service = Service(name, self._endpoint_registry)
        self._services[name] = service
        setattr(self._services_object, name, service)
        return service
