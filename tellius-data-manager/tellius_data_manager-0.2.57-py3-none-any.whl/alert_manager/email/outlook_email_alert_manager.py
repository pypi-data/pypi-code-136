# Copyright 2022 Tellius, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tellius_data_manager.alert_manager.email.email_alert_manager import (
    EmailAlertManager,
)


class OutlookEmailAlertManager(EmailAlertManager):
    """Manage alerts by sending an email using a gmail mail server as client.

    Sending an email will require providing the mode of email authentication, the app password or user password.

    Args:
        mode: if 'mfa' then the email account is expected to have mfa enabled.
        password: for use when mode is not mfa.
        app_password: gmail integration requires setting up an app password to bypass the normal MFA authentication
        protocols.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def send_alert(self, message_content: str) -> None:
        """Send an email using a gmail mail server as client.

        Args:
            message_content: arbitrary string of message content.

        """
        message_content = (
            f"During the execution of your pipeline at {datetime.datetime.now()} the following issue "
            f"was encountered \n {message_content}"
        )

        msg = MIMEMultipart()
        msg.attach((MIMEText(message_content, "plain")))

        msg["Subject"] = "tellius_data_manager: Pipeline error encountered."
        msg["From"] = self.secrets.sender
        msg["To"] = ", ".join(self._email_addresses)

        server = smtplib.SMTP("smtp.office365.com", port=587)
        server.starttls()
        server.login(self.secrets.sender, self.secrets.password)
        server.send_message(msg)
        server.quit()
