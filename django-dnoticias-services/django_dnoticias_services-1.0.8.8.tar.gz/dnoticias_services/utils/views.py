from typing import Any, Iterable

from rest_framework import status as http_status
from rest_framework.views import APIView


class APIResponseView(APIView):
    STATUS = http_status

    def dispatch(self, request, *args, **kwargs):
        self.data = {"errors": [], "message": "", "results": {}}
        return super().dispatch(request, *args, **kwargs)

    def add_error(self, message: str):
        """Add an error message to the response

        :param message: Error message
        """
        self.data["errors"].append(message)

    def set_message(self, message: str):
        """Set a message to the response

        :param message: Message to set
        """
        self.data["message"] = message

    def add_errors(self, errors: Iterable):
        """Add errors to the response, this method accepts an iterable of errors only

        :param errors: Iterable of errors
        """
        self.data["errors"] += errors

    def set_results(self, results: Any):
        """Set results to the response

        :param results: Results to set
        """
        self.data["results"] = results
