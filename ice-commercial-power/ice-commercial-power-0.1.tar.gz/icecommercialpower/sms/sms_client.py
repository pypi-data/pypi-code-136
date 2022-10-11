"""
Base class for sending SMS
"""
from __future__ import annotations
import os

# pylint: disable=too-few-public-methods
class SmsClient:
    """
    Base class SMS client that can instantiateTermiiClient or TwilioSmsClient based on the
    existence of the API key env vars.
    """

    def __init__(self):
        pass

    # pylint: disable=invalid-name, unused-argument, no-self-use
    def send_sms(self, to: str, body: str) -> str:
        """
        Sends an SMS message.
        Args:
            to (str): The to address.
            body (str): The SMS body.
        Returns:
            str: the message id returned.
        """
        return None

    @classmethod
    def from_env(cls) -> SmsClient:
        """
        Creates a TermiiClient or TwilioSmsClient.
        Returns:
            SmsClient: The TermiiClient or TwilioSmsClient instantiated.
        """
        # pylint: disable=import-outside-toplevel
        import icecommercialpower

        if os.getenv("TERMII_API_KEY"):
            return icecommercialpower.sms.TermiiClient.from_env()
        if os.getenv("TWILIO_AUTH_TOKEN"):
            return icecommercialpower.sms.TwilioSmsClient.from_env()
        if os.getenv("DUMMY_SMS_CLIENT"):
            return icecommercialpower.sms.DummySmsClient()

        raise ValueError(
            "All environment variables TERMII_API_KEY, TWILIO_AUTH_TOKEN "
            "and DUMMY_SMS_CLIENT are missing. "
            "Can not instantiate an SmsClient without either of these services configured."
        )
