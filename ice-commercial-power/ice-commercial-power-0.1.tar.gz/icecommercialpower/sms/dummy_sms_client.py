"""The test SmsClient to prevent cost for SMS while testing."""

import uuid
import logging
from icecommercialpower.sms.sms_client import SmsClient


class DummySmsClient(SmsClient):
    """This is the test SmsClient to prevent cost for SMS while testing."""

    def send_sms(self, to: str, body: str) -> str:
        sid = str(uuid.uuid4())
        # anonymize number
        to_last_numbers = to[-3:]
        logging.info(
            "Test SMS Client: send_sms: to: ****%s, body: %s, sid: %s",
            to_last_numbers,
            body,
            sid,
        )
        return sid
