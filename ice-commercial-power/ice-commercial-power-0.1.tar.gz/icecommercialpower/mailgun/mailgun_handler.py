""" Module for handling alerts by sending email messages via Mailgun

    Returns:
        MailgunHandler: class which deals with sending messages to Mailgun
"""
# pylint: disable=too-few-public-methods

import logging
import os

import requests
from requests.exceptions import RequestException, Timeout
from requests.adapters import HTTPAdapter

from urllib3.util import Retry

DEFAULT_REQUEST_TIMEOUT = 60


class MailgunHandler:
    """Class which deals with sending messages to Mailgun"""

    def __init__(self):
        """Creates a new MailgunHandler instance for sending mail alerts."""
        # * these values are directly gathered from ENV vs being passed in at construction time
        # * as currently there is no apparent need for different values at run time.

        self.api_endpoint = os.environ["MAILGUN_API_ENDPOINT"]
        self.api_key = os.environ["MAILGUN_API_KEY"]
        self.from_address = os.environ["MAILGUN_FROM_ADDRESS"]
        self.to_addresses = os.environ["MAILGUN_TO_ADDRESSES"]
        self.retry_count = os.environ["MAILGUN_MAX_RETRIES"]

        self.timeout_sec = int(
            os.getenv("MAILGUN_TIMEOUT", str(DEFAULT_REQUEST_TIMEOUT))
        )

    def send_alert_mail(self, subject: str, body: str) -> bool:
        """Sends an alert mail

        Args:
            subject (string): Subject of the mail to send.
            body (string): Body text of the mail.

        Returns:
            bool: indicates if the mail was successfully send or not
        """
        try:
            retry_strat = Retry(
                total=int(self.retry_count),
                backoff_factor=1,
                status_forcelist=[429, 500, 502, 503],
                allowed_methods=["GET", "POST", "HEAD"],
            )
            adapter = HTTPAdapter(max_retries=retry_strat)
            http = requests.Session()
            http.mount("http://", adapter)
            http.mount("https://", adapter)

            resp = http.post(
                self.api_endpoint,
                timeout=self.timeout_sec,
                auth=("api", self.api_key),
                data={
                    "from": self.from_address,
                    "to": [self.to_addresses],
                    "subject": subject,
                    "text": body,
                },
            )

            status = resp.status_code

            if 200 <= status < 300:
                logging.info("Low balance notification mail sent successfully")
                return True

            logging.info(
                "Trying to send Email using Mailgun returned status: %s. "
                "Sending low balance notification mail via Mailgun failed",
                status,
            )
            return False

        except (RequestException, Timeout):
            logging.exception(
                "Error trying to send low balance notification mail via Mailgun"
            )
            return False
