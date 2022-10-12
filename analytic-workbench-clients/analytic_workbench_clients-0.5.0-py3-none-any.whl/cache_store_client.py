from typing import List, Any
from clients_core.service_clients import E360ServiceClient
from clients_core.exceptions import ClientValueError  # noqa: F401
from pydantic import parse_obj_as
from .models import CacheMemberModel


class AWCacheStoreClient(E360ServiceClient):
    """
    Subclasses dataclass `clients_core.service_clients.E360ServiceClient`.

    Args:
        client (clients_core.rest_client.RestClient): an instance of a rest client
        user_id (str): the user_id guid

    """

    service_endpoint = ""
    extra_headers = {"accept": "application/json"}

    def list_cache(self, job_id: str, **kwargs: Any) -> List[CacheMemberModel]:
        url = f"{job_id}/"
        response = self.client.get(
            url, headers=self.service_headers, raises=True, **kwargs
        )
        models = parse_obj_as(List[CacheMemberModel], response.json())
        return models

    def get_cache_item(self, job_id: str, cache_id: str, **kwargs: Any) -> bytes:
        url = f"{job_id}/{cache_id}/"
        headers = self.extra_headers.copy()
        headers.update(self.service_headers)
        headers.update({"accept": "application/octet-stream"})
        response = self.client.get(url, raises=True, headers=headers, **kwargs)
        return response.content
