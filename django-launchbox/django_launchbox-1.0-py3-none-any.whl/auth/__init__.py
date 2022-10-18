import logging
import os

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect

import requests

logger = logging.getLogger(__name__)


class LBAuth:
    bridge_endpoint = f"{os.environ.get('LB_CONNECT_API')}/auth"

    def login(self, request, callback):
        # Call
        response = requests.get(f"{self.bridge_endpoint}/login")
        # Check
        if response.status_code == 200:
            try:
                payload = response.json()
            except Exception:
                logger.error("LBAuth.login: Unable to decode response JSON")
                return False
            else:
                HttpResponseRedirect(f"{payload['url']}/")
        else:
            logger.error(
                f"LBAuth.login: Invalid response [code: {response.status_code}]",
            )
            return False

    def verify(self, request):
        # Parse out the request GET and POST data
        data = request['get']
        # Call
        response = requests.post(f"{self.bridge_endpoint}/verify", data)
