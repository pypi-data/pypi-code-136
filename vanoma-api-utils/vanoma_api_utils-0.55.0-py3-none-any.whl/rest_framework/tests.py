from typing import Any, Dict, List
from rest_framework.test import APIClient, APITestCase


class BaseAPIClient(APIClient):
    ACCEPT_HEADER = "application/json"


class BaseAPITestCase(APITestCase):
    def render_page(
        self, count: int, results: List[Any], next: str = None, previous: str = None
    ) -> Dict[str, Any]:
        return {
            "count": count,
            "next": next,
            "previous": previous,
            "results": results,
        }
