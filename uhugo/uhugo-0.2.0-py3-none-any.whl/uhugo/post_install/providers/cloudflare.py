import logging
import os
from typing import Text, Union

import requests

from . import ProviderBase

log = logging.getLogger(__name__)


class Cloudflare(ProviderBase):
    """
    Cloudflare provider
    """

    def __init__(self, api_key: Text = None, email_address: Text = None, account_id: Text = None, hugo_version: Text = None):
        """

        :param hugo_version: New Hugo version
        :param api_key: Authentication key for Cloudflare
        :param email_address: Registered email address
        :param account_id: Cloudflare worker account ID
        :raises ValueError: If ``email_address`` and ``account_id`` is not provided
        """
        super().__init__(api_key, None, hugo_version)

        self.account_id = account_id

        if not email_address:
            email_address = os.environ.get("CLOUDFLARE_EMAIL", None)

        if not self.account_id:
            self.account_id = os.environ.get("CLOUDFLARE_WORKER_ACCOUNT_ID", None)

        if not email_address and not self.account_id and not self.hugo_version:
            raise ValueError("email_address, account_id or hugo_version not provided")

        self.headers = {
            "X-Auth-Email": email_address,
            "X-Auth-Key": self.api_key
        }

    def update_api(self, project_name: Text) -> requests.Response:
        """
        Updates Cloudflare Pages environment variable of ``HUGO_VERSION``.

        :param project_name: Name of the project to update
        :return:
        """

        data = {
            "deployment_configs": {
                "preview": {
                    "env_vars": {
                        "delete_this_env_var": None,
                        "HUGO_VERSION": {
                            "value": self.hugo_version
                        }
                    }
                },
                "production": {
                    "env_vars": {
                        "delete_this_env_var": None,
                        "HUGO_VERSION": {
                            "value": self.hugo_version
                        }
                    }
                }
            }
        }

        response = requests.patch(f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/pages/projects/{project_name}",
                                  json=data, headers=self.headers)
        return response

    def get_projects(self, project_name: Text = None) -> requests.Response:
        """
        This checks and gets the projects available

        :param project_name: Name of the project to get
        :return: Returns HTTP response
        """

        if not project_name:
            response = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/pages/projects",
                                    headers=self.headers)
        else:
            response = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/pages/projects/{project_name}",
                                    headers=self.headers)
        return response

    def current_version(self, project_name: Text = None) -> Union[str, None]:
        """
        Gets the current Hugo version

        :param project_name: Name of the project to check from
        """
        response = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/pages/projects/{project_name}",
                                headers=self.headers)

        data = response.json()
        try:
            return data['result']['deployment_configs']['production']['env_vars']['HUGO_VERSION']['value']
        except KeyError as e:
            log.debug(e)
            return None
