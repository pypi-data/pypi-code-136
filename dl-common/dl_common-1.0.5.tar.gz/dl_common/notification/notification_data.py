from typing import Dict, List

class NotificationsDataHandler:
    SENDGRID_CHANNEL_NAME = "sendgrid"

    def __init__(self, title: str, notification_text: str, event_name: str = None) -> None:
        self.title = title
        self.notification_text = notification_text
        self.event_name = event_name
        self.channels = []

    def __add_channel(self, channel_data: Dict):
        self.channels.append(channel_data)

    def __wrap_notification_data_with_channel_name(self, channel_name: str, **kwargs):
        return {"channel_name": channel_name, "data": kwargs}

    def convert_to_json(self):
        return {"title": self.title, "notification_text": self.notification_text, "channels": self.channels}

    def add_sendgrid_channel(self, receipient_ids: List[str], template_data: Dict, template_id: str = None):
        sendgrid_data = {"receipient_ids": receipient_ids, "template_id": template_id, "template_data": template_data}
        sendgrid_data_with_channel_name = self.__wrap_notification_data_with_channel_name(
            channel_name="sendgrid", **sendgrid_data)
        self.__add_channel(sendgrid_data_with_channel_name)

    def add_slack_channel(self):
        pass

    def add_email_channel(self):
        pass
