import os
from typing import Optional

from servicefoundry.lib.clients.auth_service_client import AuthServiceClient
from servicefoundry.lib.config_utils import (
    _get_profile,
    _get_session,
    _migrate_old_session_to_new_config,
    _save_session,
)
from servicefoundry.lib.const import (
    API_KEY_ENV_NAME,
    DEFAULT_PROFILE_NAME,
    HOST_ENV_NAME,
)
from servicefoundry.lib.exceptions import BadRequestException
from servicefoundry.lib.model.entity import Profile, ServerConfig
from servicefoundry.lib.model.session import (
    EphemeralServiceFoundrySession,
    ServiceFoundrySession,
)


def _get_api_key_from_env() -> Optional[str]:
    return os.getenv(API_KEY_ENV_NAME)


def _get_host_from_env() -> Optional[str]:
    return os.getenv(HOST_ENV_NAME)


def _create_profile_from_env_host() -> Optional[Profile]:
    tfy_host = _get_host_from_env()
    if tfy_host is None:
        return None

    if _get_api_key_from_env() is None:
        raise Exception(f"{HOST_ENV_NAME} value set but {API_KEY_ENV_NAME} not found")

    return Profile(server_config=ServerConfig.from_base_url(tfy_host))


def get_session(profile_name: str = DEFAULT_PROFILE_NAME):
    _migrate_old_session_to_new_config()
    profile = _create_profile_from_env_host()
    if not profile:
        profile = _get_profile(name=profile_name)

    api_key = _get_api_key_from_env()
    if api_key:
        auth_client = AuthServiceClient(profile=profile)
        return auth_client.login_with_api_token(
            api_key=api_key, session_class=EphemeralServiceFoundrySession
        )

    auth_client = AuthServiceClient(profile=profile)
    session = ServiceFoundrySession.from_profile(
        profile=profile, refresher=auth_client.refresh_token
    )
    if session:
        return session
    else:
        raise BadRequestException(403, f"Please login before running this command.")


def logout_session(profile_name: str = DEFAULT_PROFILE_NAME):
    # TODO: Implement logout if using api key
    _session_dict = _get_session(profile_name=profile_name)
    if _session_dict:
        _save_session(session={}, profile_name=profile_name)
    else:
        raise BadRequestException(403, f"Please login before running this command.")
