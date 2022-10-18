from typing import Any, Dict
from requests import Response
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from vanoma_api_utils.http import client
from djangorestframework_camel_case.util import camelize  # type: ignore


class AuthApiException(Exception):
    pass


def create_login(data: Dict[str, Any]) -> Response:
    response = client.post(
        f"{settings.VANOMA_AUTH_API_URL}/login-creation",
        data=camelize(data),
    )

    if not response.ok:
        raise AuthApiException(
            _("Unable to create login. Please contact customer support.")
        )

    return response
