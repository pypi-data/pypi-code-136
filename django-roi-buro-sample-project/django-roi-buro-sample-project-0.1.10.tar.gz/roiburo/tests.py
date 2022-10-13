"""App base test class"""

from typing import Dict, Any

from django.core.management import call_command
from django.db import connections
from django.test import TransactionTestCase
from rest_framework.response import Response
from rest_framework.test import APIClient


class CustomTestCase(TransactionTestCase):
    """Custom test case"""

    databases = {"default"}

    def _fixture_teardown(self):
        # Allow TRUNCATE ... CASCADE and don't emit the post_migrate signal
        # when flushing only a subset of the apps
        for db_name in self._databases_names(include_mirrors=False):  # type: ignore
            # Flush the database
            inhibit_post_migrate = (
                self.available_apps is not None
                or (  # Inhibit the post_migrate signal when using serialized
                    # rollback to avoid trying to recreate the serialized data.
                    self.serialized_rollback
                    and hasattr(connections[db_name], "_test_serialized_contents")
                )
            )
            call_command(
                "flush",
                verbosity=0,
                interactive=False,
                database=db_name,
                reset_sequences=False,
                allow_cascade=True,
                inhibit_post_migrate=inhibit_post_migrate,
            )

    def setUp(self):
        """Creating api client"""
        self.client = APIClient()

    def _process_request(self, url: str, method, data=None) -> Response:
        """Send request"""
        response = getattr(self.client, method)(path=url, data=data)
        return response

    @staticmethod
    def _get_formatted_response(
        test_description: str, request: Dict[str, Any], response: Response
    ) -> str:
        """Formatting api response to log message"""
        return (
            f"{test_description}: \n"
            f"request: {request} \n"
            f"response status code: {response.status_code} \n"
            f"response JSON: {response.json()}"
        )
