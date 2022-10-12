from typing import Any
from clients_core.service_clients import E360ServiceClient
from clients_core.exceptions import ClientValueError  # noqa: F401


class AWResourcesClient(E360ServiceClient):
    """
    Subclasses dataclass `clients_core.service_clients.E360ServiceClient`.

    Args:
        client (clients_core.rest_client.RestClient): an instance of a rest client
        user_id (str): the user_id guid

    """

    service_endpoint = ""
    extra_headers = {"accept": "application/octet-stream"}

    def get_bytes_by_slug(
        self, slug_name: str, password: str = None, **kwargs: Any
    ) -> bytes:
        """
        Returns bytes object by the ``slug_name`` provided.

        Args:
            slug_name: name of the slug the file is saved under.
            password: optional, only if password-protected content.

        """
        request_url = f"{slug_name}/"
        if password is not None:
            raise NotImplementedError(
                "Password feature is not yet ready, please do not use."
            )  # noqa

        response = self.client.get(
            request_url, headers=self.service_headers, raises=True, **kwargs
        )

        return response.content
