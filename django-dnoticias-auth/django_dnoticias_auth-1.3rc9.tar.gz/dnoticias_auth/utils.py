import logging
import json
from datetime import datetime, timedelta
from typing import Optional, Union
from time import time

from django.http import HttpResponse, HttpResponseRedirect
from django import VERSION as DJANGO_VERSION
from django.conf import settings

import requests
from dnoticias_services.authentication.keycloak import (
    delete_user_session as delete_session_kc,
    get_user_keycloak_info,
)
from keycloak import KeycloakDeleteError

from .redis import KeycloakSessionStorage, GenericSessionStorage
from keycloak import KeycloakOpenID
from . import cookies_consts

logger = logging.getLogger(__name__)


# DEPRECATED
def get_cookie_equivalency(
    name: Optional[str] = None,
    all_names: Optional[bool] = False
) -> Union[dict, str]:
    """Returns the cookie equivalency for the given name

    :param name: The name of the cookie
    :param all_names: If True, returns all the cookie equivalencies
    :return: The cookie equivalency or a dict with all the equivalencies
    :rtype: Union[dict, str]
    """
    EQUIVALENCY = {
        'oidc_login_next': 'dn_oln',
        'keycloak_session_id': 'dn_ksi',
        'user_context_used': 'dn_ucu',
        'oidc_access_token': 'dn_oat',
        'oidc_access_token_expiration': 'dn_oate',
    }

    return EQUIVALENCY.get(name) if not all_names else EQUIVALENCY


def get_cookie_configuration(
    expiration_minutes: Optional[int] = None,
    http_only: Optional[bool] = False,
) -> dict:
    """Return the cookie configuration

    :param expiration_minutes: The expiration minutes of the cookie
    :param http_only: If True, the cookie is only accessible by the server
    :return: The cookie configuration
    :rtype: dict
    """
    expiration_minutes = expiration_minutes or settings.AUTH_COOKIE_EXPIRATION_MINUTES
    expiration_datetime = datetime.now() + timedelta(minutes=expiration_minutes)
    expires = expiration_datetime.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

    return {
        'expires': expires,
        'domain': settings.AUTH_COOKIE_DOMAIN,
        'secure': settings.AUTH_COOKIE_SECURE,
        'httponly': http_only,
        'samesite': 'Strict'
    }


def set_cookie(
    name: str,
    value: str,
    response: HttpResponse,
    expiration_minutes: Optional[int]=None
) -> HttpResponse:
    """Generates all the cookies needed on another clients to process the user

    :param name: The name of the cookie
    :param value: The value of the cookie
    :param response: The response object
    :param expiration_minutes: The expiration minutes of the cookie
    :return: The response object
    :rtype: HttpResponse
    """
    # Extra kwargs used in set_cookie
    extra_data = get_cookie_configuration(expiration_minutes=expiration_minutes)
    response.set_cookie(name, value, **extra_data)

    return response


def delete_oidc_cookies(redirect_url: str, cookies: dict) -> HttpResponse:
    """Deletes all the cookies needed on another clients to process the user

    :param redirect_url: The redirect_url:
    :param cookies: The cookies to delete
    :return: The response object
    :rtype: HttpResponse
    """
    # Response is defined first because we need to delete the cookies before redirect
    response = HttpResponseRedirect(redirect_url)
    auth_cookies = [
        getattr(cookies_consts, key) for key in dir(cookies_consts) if not key.startswith('__')
    ]

    # This will delete any cookie with session_ (session_editions, session_comments, etc)
    [auth_cookies.append(cookie) for cookie in cookies.keys() if "session_" in cookie]

    extra = {"domain": settings.AUTH_COOKIE_DOMAIN}

    # Fix compatibility issues with django < 2 (CMS)
    if DJANGO_VERSION[0] >= 3:
        extra.update({"samesite": "Strict"})

    # Deletes ONLY the cookies that we need
    logger.debug("Deleting cookies: %s", auth_cookies)
    [response.delete_cookie(cookie, **extra) for cookie in auth_cookies]

    return response


def delete_user_sessions(keycloak_session_id: str) -> None:
    """Deletes all the user sessions for this keycloak_session_id stored in redis

    :param keycloak_session_id: The keycloak_session_id
    :return: None 
    """
    try:
        keycloak_session = KeycloakSessionStorage(keycloak_session_id, ".")
        session_data = keycloak_session.load()
        django_sessions = session_data.split(',') if session_data else []

        for session in django_sessions:
            logger.debug("Deleting django session: %s", session)
            django_session = GenericSessionStorage(f"{settings.SESSION_REDIS_PREFIX}:{session}")
            django_session.delete()

        keycloak_session.delete()
    except:
        logger.exception("Failed to delete sessions using keycloak session %s", keycloak_session_id)


def delete_user_session(keycloak_session_id: str) -> None:
    """Deletes the user session for this keycloak_session_id in redis

    :param keycloak_session_id: The keycloak_session_id
    :return: None 
    """
    try:
        logger.debug("Deleting old session using keycloak session %s", keycloak_session_id)
        django_session = GenericSessionStorage(
            f"{settings.DJANGO_KEYCLOAK_ASSOC_REDIS}:{keycloak_session_id}"
        )
        django_session.delete()
    except:
        logger.exception(
            "Failed to delete session using keycloak session %s",
            keycloak_session_id
        )


def refresh_keycloak_token(refresh_token: str) -> tuple:
    """Refreshes the keycloak token using the refresh_token

    :param refresh_token: The refresh_token
    :return: The access_token, refresh_token and expires_in in timestamp format
    :rtype: tuple
    """
    keycloak_client = KeycloakOpenID(
        server_url=settings.KEYCLOAK_SERVER_URL,
        realm_name=settings.KEYCLOAK_USER_REALM_NAME,
        client_id=settings.KEYCLOAK_CLIENT_ID,
        client_secret_key=settings.KEYCLOAK_CLIENT_SECRET_KEY,
        timeout=5
    )

    token = keycloak_client.refresh_token(refresh_token)
    expires_in = int(time()) + token.get('expires_in', 0)

    return token.get("access_token"), token.get("refresh_token"), expires_in


class SessionChecker:
    LOGIN = "login"
    LOGOUT = "logout"
    UPDATE = "update"

    def __init__(
        self,
        email: str,
        old_keycloak_session_id: str,
        keycloak_session_id: str,
    ):
        self.old_keycloak_session_id = old_keycloak_session_id
        self.keycloak_session_id = keycloak_session_id
        self.email = email.lower()
        self.redis = GenericSessionStorage(self.get_redis_key())

    def get_redis_key(self) -> str:
        return f"inf|{self.email}"

    def get_information(self) -> dict:
        information = self.redis.load()
        return json.loads(information) if information else {}

    def get_information_body(self) -> dict:
        return {"created_at": int(time())}

    def update_session_information(self):
        information = self.get_information()

        if self.old_keycloak_session_id in information.keys():
            information[self.keycloak_session_id] = information.pop(self.old_keycloak_session_id)
            information[self.keycloak_session_id].update({"updated_at": int(time())})
        elif not information:
            information = {self.keycloak_session_id: self.get_information_body()}
        else:
            information.update({self.keycloak_session_id: self.get_information_body()})

        self.redis.save(json.dumps(information))

    def get_session_count(self) -> int:
        information = self.get_information()
        return len(information.keys()) if information else 0

    def get_user_max_sessions(self) -> int:
        user_attributes = get_user_keycloak_info(self.email)
        max_sessions = user_attributes.get("attributes", {}).get("max_sessions", 2)

        if type(max_sessions) == list:
            max_sessions = max_sessions[0]

        return int(max_sessions)

    def notify_deleted_session(self, session_id: str):
        headers = {'Authorization': f'Api-Key {settings.SUBSCRIPTION_SERVICE_ACCOUNT_API_KEY}'}

        try:
            response = requests.post(
                settings.SUBSCRIPTIONS_USER_EVENT_API_URL,
                json={
                    "email": self.email,
                    "event_type": "session_removed",
                    "extra_info": {
                        "keycloak_session_id": session_id
                    }
                },
                headers=headers
            )
            response.raise_for_status()
        except:
            logger.exception("Failed to notify user about deleted session")

    def delete_oldest_session(self):
        information = self.get_information()
        oldest_session = min(information, key=lambda k: information[k]["created_at"])
        information.pop(oldest_session, None)

        try:
            delete_user_sessions(oldest_session)
            delete_session_kc(oldest_session)
        except KeycloakDeleteError:
            logger.debug("Failed to delete oldest session %s", oldest_session)
        else:
            self.notify_deleted_session(oldest_session)

        self.redis.save(json.dumps(information))

    def delete_session(self):
        information = self.get_information()
        information.pop(self.keycloak_session_id, None)
        self.redis.save(json.dumps(information))

    def handle_event(self, event: str):
        if event == self.LOGIN:
            logger.debug("Handling login event for %s", self.email)
            self.update_session_information()

            if self.get_session_count() > self.get_user_max_sessions():
                logger.debug("Deleting old session for %s", self.email)
                self.delete_oldest_session()
        elif event == self.LOGOUT:
            logger.debug("Handling logout event for %s", self.email)
            self.delete_session()
