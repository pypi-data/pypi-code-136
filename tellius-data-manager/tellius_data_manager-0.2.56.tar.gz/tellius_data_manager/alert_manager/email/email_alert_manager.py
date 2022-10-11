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
from typing import List

from tellius_data_manager.alert_manager.alert_manager import AlertManager


class EmailAlertManager(AlertManager):
    """Manage alerts by sending an email to one or more recipients with necessary information.

    Args: email_addresses: List of email addresses.
    """

    def __init__(self, email_addresses: List[str], **kwargs) -> None:
        super().__init__(**kwargs)
        self._email_addresses = email_addresses

    def send_alert(self, message_content: str) -> None:
        """Send alert as an email.

        Args:
            message_content: arbitrary string of message content.

        """
        raise NotImplementedError(
            f"{self.__class__.__name__} is a base class. It must implement the Pipe interface."
        )
