import jsonschema
from typing import Dict, Any
from clients_core.service_clients import E360ServiceClient


class MethodsClient(E360ServiceClient):
    _schemas: Dict[str, dict] = {}
    service_endpoint = ""

    def _get_method_schema(self, method_id: str, **kwargs: Any) -> dict:
        """
        Returns method schema json; schemas are cached.
        """
        if method_id not in self._schemas:
            url = f"{method_id}/schema/"
            response = self.client.get(
                url, headers=self.service_headers, raises=True, **kwargs
            )
            self._schemas[method_id] = response.json()
        return self._schemas[method_id]

    @staticmethod
    def _get_method_id_from_payload(payload: Dict[str, Any]) -> str:
        """Returns a method id from the payload"""
        try:
            return payload["projectType"]
        except KeyError:
            raise KeyError("The method payload is missing mandatory key `projectType`")

    def validate_payload(self, payload: dict) -> None:
        """Validates the method payload; will raise ValidationError on errors"""
        method_id = self._get_method_id_from_payload(payload)
        method_schema = self._get_method_schema(method_id)
        jsonschema.validate(instance=payload, schema=method_schema)
