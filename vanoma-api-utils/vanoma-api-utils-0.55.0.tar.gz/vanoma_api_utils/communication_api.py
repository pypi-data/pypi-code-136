from typing import Any, Dict
from requests import Response
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from vanoma_api_utils.http import client
from djangorestframework_camel_case.util import camelize  # type: ignore


class CommunicationApiException(Exception):
    pass


def send_sms(data: Dict[str, Any]) -> Response:
    response = client.post(
        f"{settings.VANOMA_COMMUNICATION_API_URL}/sms", data=camelize(data)
    )

    if not response.ok:
        raise CommunicationApiException(
            _(f"Unable to send SMS. Please contact customer support.")
        )

    return response


def send_push(data: Dict[str, Any]) -> Response:
    response = client.post(
        f"{settings.VANOMA_COMMUNICATION_API_URL}/push", data=camelize(data)
    )

    if not response.ok:
        raise CommunicationApiException(
            _(f"Unable to send push notification. Please contact customer support.")
        )

    return response


def verify_otp(otp_id: str, otp_code: str, phone_number: str) -> Response:
    response = client.post(
        f"{settings.VANOMA_COMMUNICATION_API_URL}/otp/{otp_id}/verification",
        data={"otpCode": otp_code, "phoneNumber": phone_number},
    )

    if not response.ok:
        raise CommunicationApiException(
            _(
                f"Unable to validate your verification code. Please contact customer support."
            )
        )

    return response
