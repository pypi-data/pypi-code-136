import logging
import os
import typing

import jwt

from mlfoundry import env_vars
from mlfoundry.exceptions import MlFoundryException
from mlfoundry.login import get_stored_api_key, login
from mlfoundry.tracking.auth_service import AuthService
from mlfoundry.tracking.entities.user_info import UserInfo

logger = logging.getLogger(__name__)


def is_notebook_or_interactive():
    try:
        shell = get_ipython().__class__
        if shell.__name__ == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        if shell.__name__ == "TerminalInteractiveShell":
            return True  # Terminal running IPython
        if "google.colab" in str(shell):
            return True  # google colab notebook
        return False  # Other type (?)
    except NameError:
        return False


class Session:
    def __init__(self, auth_service: AuthService, tracking_uri: str):
        self.auth_service: AuthService = auth_service
        self.tracking_uri = tracking_uri

    def init_session(
        self,
        api_key: typing.Optional[str] = None,
    ) -> UserInfo:
        final_api_key = (
            api_key
            or os.getenv(env_vars.API_KEY)
            or os.getenv(env_vars.API_KEY_GLOBAL)
            or get_stored_api_key(self.tracking_uri)
        )
        if final_api_key is not None:
            token = self.auth_service.get_token(api_key=final_api_key)
            os.environ[env_vars.TRACKING_TOKEN] = token
            return Session._get_user_info(token)
        # if API key is not present,
        # then take a look if MLFLOW_TRACKING_TOKEN itself has been set.
        # this will be used in sfy.
        existing_token = os.getenv(env_vars.TRACKING_TOKEN, "")
        if existing_token:
            logger.info("API key is not present. Using existing tracking token")
            return Session._get_user_info(existing_token)

        if is_notebook_or_interactive() and login(self.tracking_uri):
            return self.init_session(get_stored_api_key(self.tracking_uri))

        raise MlFoundryException(
            "Could not find API key. Please use `mlfoundry login` to log in."
        )

    @staticmethod
    def _get_user_info(jwt_token: str) -> UserInfo:
        # TODO:- should probably do this whole thing in the backend.
        try:
            json_body = jwt.decode(
                jwt_token,
                options={
                    "verify_signature": False,
                    "verify_aud": False,
                },
            )
            user_info = UserInfo(
                user_id=json_body["username"],
                email=json_body["email"],
            )
            logger.info("Welcome user! You are logged in as %s", user_info.user_id)
        except Exception as ex:
            logger.exception("failed to get user info, %s", ex)
            raise ex

        return user_info
