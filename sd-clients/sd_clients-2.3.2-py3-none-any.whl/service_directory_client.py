from typing import List, Dict
from clients_core.rest_client import RestClient
from clients_core.service_list_provider import Service, ServiceListProvider


class ServiceDirectoryClient(ServiceListProvider):
    service_version = "3.0.0"  # TODO: Pull from environment
    service_endpoint = "services"

    def __init__(self, rest_client: RestClient):
        self.client = rest_client

    def _get_service_directory_url(self) -> str:
        return f"api/v{self.service_version}/{self.service_endpoint}"

    @property
    def source(self) -> str:
        return self.client.base_url

    def get_service_list(self, name: str, endpoint_name: str, version_major: int, version_minor: int, version_patch: int) -> List[Service]:  # type: ignore
        params = {
            "name": name,
            "endpoint.name": endpoint_name,
            "endpoint.version.major": version_major,
            "endpoint.version.minor": version_minor,
            "endpoint.version.patch": version_patch,
        }
        response = self.client.get(self._get_service_directory_url(), params=params)
        if response.status_code == 200:
            return self._parse_response(response.json())
        return []

    def _parse_response(self, response: Dict) -> List[Service]:
        return [Service.from_service(service) for service in response["resources"]]
