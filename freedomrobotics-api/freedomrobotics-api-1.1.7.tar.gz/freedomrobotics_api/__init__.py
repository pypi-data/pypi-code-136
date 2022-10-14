import os
import sys
import platform
import threading
import traceback

from .api_handler import APIHandler
from .account import Account
from .user import User
from .token import Token

__version__ = "1.1.7"


class FreedomClient(object):
    """Freedom Robotics API client library. Instantiate this first and access all API functions from within a FreedomClient.

    You can instantiate `FreedomClient` using either no arguments (in which case credentials are searched for in ~/.freedom_credentials), a `token` and `secret`, or a `username` and `password`. You can also specify an url or an environment to select which API to use.

    Args:
        token (str): API token. Can be a session or user token.
        secret (str): API secret.
        username (str): Username.
        password (str): Password.
        url (str): API url.
        env (str): Environment to select API (dev, qa, staging, release).
    """
    def __init__(self, token=None, secret=None, username=None, password=None, url=None, env=None, **api_args):
        self.api = APIHandler.get_instance(
            url=url,
            token=token,
            secret=secret,
            username=username,
            password=password,
            env=env,
            **api_args
        )
        assert self.api is not None

    def get_account(self, account_id, params=None, api_call_kwargs={}):
        """:obj:`Account`: Fetch an account by its account ID (Axxxxxxxxxxxx).

        Args:
            account_id (str): Account ID.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        account_data = self.api.call(
            "GET",
            "/accounts/{}".format(account_id),
            params=params,
            **api_call_kwargs,
        )
        if not account_data:
            return None
        return Account(account_data["account"], account_data, api=self.api)

    def get_accounts(self, params=None, api_call_kwargs={}):
        """:obj:`list` of :obj:`Account`: Fetch a list of all accounts that are visible/accessible.

        Args:
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        result = self.api.call("GET", "/accounts", params=params, **api_call_kwargs)
        if not result:
            return []
        return [
            Account(account_data["account"], account_data, api=self.api)
            for account_data in result
        ]

    def get_users(self, params=None, api_call_kwargs={}):
        """:obj:`list` of :obj:`User`: Fetch a list of all users that are visible/accessible.

        Args:
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        result = self.api.call("GET", "/users", params=params, **api_call_kwargs)
        if not result:
            return []
        return [User(user_data["user"], user_data, api=self.api) for user_data in result]

    def get_token(self, token_id, params=None, api_call_kwargs={}):
        """:obj:`list` of :obj:`dict`: Fetch a list of tokens.

        Args:
            token_id (str): Token ID.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        data = self.api.call(
            "GET",
            "/tokens/{}".format(token_id),
            params=params,
            **api_call_kwargs
        )
        return Token(data['token'], data, api=self.api, **api_call_kwargs)

    def create_token(
            self,
            allowed_actions,
            accounts,
            devices,
            description,
            create_secret=False,
            params=None,
            raw=True,
            api_call_kwargs={},
            **kwargs
            ):
        """:obj:`dict`: Creates a token and returns it.

        Args:
            description (str) Token description
            allowed_actions (dict): Allowed actions for the new token.
            accounts (list or *): List of accounts ids on which this token will have access.
                Use '*' if the token needs access to all accounts
            devices (list or *): List of devices ids on which this token will have access.
                Use '*' if the token needs access to all devices
            create_secret (bool): If true, will create a token with a secret.
            params (dict): Optional query parameters.
            raw (bool): If true, will return the raw response of the API.
                Otherwise it will create a Token object and return it with the returned token id.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **kwargs (dict): All extra attributes for the new token.
        """
        body = {
            "allowed_actions": allowed_actions,
            "accounts": accounts,
            "devices": devices,
            "description": description,
        }
        body.update(kwargs)
        if create_secret:
            if params is None:
                params = {}
            params['create_secret'] = 'true'
        result = self.api.call("POST", "/tokens", data=body, params=params, **api_call_kwargs)
        if raw:
            return result
        else:
            return Token(result['token'], result, api=self.api)

    def delete_token(self, token_id, params=None, api_call_kwargs={}):
        """Deletes a specified token.

        Args:
            token_id (str): The Token id
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
        """

        result = self.api.call("DELETE", "/tokens/{}".format(token_id), params=params, **api_call_kwargs)
        return result

    def trace(self, account_id, data, **api_call_kwargs):
        result = self.api.call("PUT", f"/accounts/{account_id}/trace", data={'events': data}, **api_call_kwargs)
        return result

    def report_issue(
            self,
            message,
            level,
            logs=None,
            account=None,
            device=None,
            user=None,
            params=None,
            api_call_kwargs={},
            **kwargs):
        """Reports an issue to the API

        Args:
            message (str): The string with the error message.
            level (str): One of info, warning, error or fatal.
            logs (list of str): List of logs describing the issue.
            account (str): The account id if present.
            device (str): The device id if present.
            user (str): The user if present.
            params (dict): Optional query parameters.
            api_call_kwargs (dict): Optional keyword arguments for api call.
            **kwargs (dict): All the extra arguments will be sent into the body.
        """

        if level not in ('fatal', 'warning', 'error', 'info'):
            raise Exception(
                "Invalid level {}. Must be one of fatal, warning or error".format(level)
            )

        freedom_data = {
            "token": '*' * 3 + self.api.token[-8:],
        }
        if account is not None:
            freedom_data['account'] = account
        if device is not None:
            freedom_data['device'] = device
        if user is not None:
            freedom_data['user'] = user

        system_data = {
            "platform": platform.platform(),
            "processor": platform.processor(),
            "os": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "environment": os.environ.copy(),
        }
        if logs is None:
            logs = []

        exc_info = sys.exc_info()
        if any(exc_info):
            logs.extend(traceback.format_exception(**exc_info))

        data = {
            "message": message,
            "level": level,
            "logs": logs,
            "component": "api_client",
            "attributes": {
                "freedom_robotics": freedom_data,
                "python": {
                    "build": platform.python_build(),
                    "implementation": platform.python_implementation(),
                    "version": platform.python_version(),
                },
                "freedomrobotics_api_client": {
                    "version": __version__,
                    "install_path": os.path.abspath(os.path.dirname(__file__)),
                },
                "system": system_data,
                "thread": {
                    "name": threading.current_thread().name,
                    "daemon": threading.current_thread().daemon
                }
            }
        }
        data.update(kwargs)

        self.api.call("PUT", "/issues", data=data, params=params, **api_call_kwargs)
