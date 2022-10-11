"""
Twilio SMS Client functions.
"""

import os
import logging
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from icecommercialpower.sms.sms_client import SmsClient


class TwilioSmsClient(SmsClient):
    """
    This is the Twilio SMS client class used to send SMS to customers.
    """

    def __init__(self, client: Client, from_number: str, fixed_sms_number: str = None):
        super().__init__()
        self.twilio_from_number = from_number
        self.client = client
        self.fixed_sms_number = fixed_sms_number

    @classmethod
    def from_env(cls):
        """
        Create a TwilioSmsClient from environment variables.
        """

        twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        twilio_from_number = os.environ["TWILIO_FROM_NUMBER"]

        fixed_sms_number = os.getenv("FIXED_SMS_NUMBER")
        if fixed_sms_number:
            logging.info("Sending all SMS to fixed number: %s", fixed_sms_number)

        client = Client(twilio_account_sid, twilio_auth_token)
        return cls(client, twilio_from_number, fixed_sms_number)

    # pylint: disable=invalid-name
    def send_sms(self, to: str, body: str) -> str:
        """
        Send an SMS using Twilio.
        Args:
            to (str): Phone number of the recipient.
            body (str): Body text of the SMS.

        Returns:
            str: the message id returned by Twilio.
        """

        to = self.fixed_sms_number or to

        logging.info("Sending message %s to %s through Twilio...", body, to)

        try:
            message = self.client.messages.create(
                to=to, from_=self.twilio_from_number, body=body
            )

        except TwilioRestException:
            logging.exception("Problem communicating with Twilio")
            raise

        logging.info("Sent message %s to %s. SID: %s", body, to, message.sid)
        return message.sid
