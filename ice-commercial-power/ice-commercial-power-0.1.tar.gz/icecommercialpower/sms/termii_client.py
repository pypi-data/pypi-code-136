"""
Module for sending SMS using the Termii.com REST API
"""
# pylint: disable=too-few-public-methods

import os
import json
import logging
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, Timeout
from urllib3.util import Retry

from icecommercialpower.sms.sms_client import SmsClient

DEFAULT_REQUEST_TIMEOUT = 60


class TermiiClient(SmsClient):
    """
    Class for sending SMS using the Termii.com REST API
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        api_endpoint: str,
        api_key: str,
        from_address: str,
        retry_count: int,
        channel: str,
        fixed_sms_number: str = None,
        timeout_sec: int = 60,
    ):
        """
        Creates a new TermiiClient instance for sending SMS.
        """
        # * these values are directly gathered from ENV vs being passed in at construction time
        # * as currently there is no apparent need for different values at run time.
        super().__init__()
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.from_address = from_address
        self.retry_count = retry_count
        self.channel = channel
        self.fixed_sms_number = fixed_sms_number
        self.timeout_sec = timeout_sec

    @classmethod
    def from_env(cls):
        """
        Create a TwilioSmsClient from environment variables.
        """

        api_endpoint = os.environ["TERMII_API_ENDPOINT"]
        api_key = os.environ["TERMII_API_KEY"]
        from_address = os.environ["TERMII_FROM_ADDRESS"]
        retry_count = int(os.environ["TERMII_MAX_RETRIES"])
        channel = os.environ["TERMII_CHANNEL"]
        timeout_sec = int(os.getenv("TERMII_TIMEOUT", str(DEFAULT_REQUEST_TIMEOUT)))

        fixed_sms_number = os.getenv("FIXED_SMS_NUMBER")
        if fixed_sms_number:
            logging.info("Sending all SMS to fixed number: %s", fixed_sms_number)

        return cls(
            api_endpoint,
            api_key,
            from_address,
            retry_count,
            channel,
            fixed_sms_number,
            timeout_sec,
        )

    def send_sms(self, to: str, body: str) -> str:  # pylint: disable=invalid-name
        """
        Sends an SMS using Termii.

        Args:
            to (str): Phone number of the recipient.
            body (str): Body text of the SMS.

        Returns:
            str: the message id returned by Termii.
        """

        to = self.fixed_sms_number or to

        try:
            retry_strategy = Retry(
                total=int(self.retry_count),
                backoff_factor=1,
                status_forcelist=[429, 500, 502, 503],
                allowed_methods=["POST", "GET", "HEAD"],
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            http = requests.Session()
            http.mount("http://", adapter)
            http.mount("https://", adapter)

            response = http.post(
                self.api_endpoint,
                timeout=self.timeout_sec,
                json={
                    "to": to,
                    "from": self.from_address,
                    "sms": body,
                    "type": "plain",
                    "channel": self.channel,
                    "api_key": self.api_key,
                },
            )

            if response.status_code != 200:
                if "message" in response.text:
                    logging.error(
                        "Trying to send SMS using Termii returned status: %s. Message: %s",
                        response.status_code,
                        json.loads(response.text)["message"],
                    )
                else:
                    logging.error(
                        "Trying to send SMS using Termii returned status: %s",
                        response.status_code,
                    )
                return None

            response_json = json.loads(response.text)
            message_id = response_json["message_id"]
            status_message = response_json["message"]

            logging.info(
                "SMS sent via Termii to: %s, body: %s, " "status: %s, message id: %s",
                to,
                body,
                status_message,
                message_id,
            )
            return message_id

        except (RequestException, Timeout):
            logging.exception("Error sending SMS via Termii.")
            return None
