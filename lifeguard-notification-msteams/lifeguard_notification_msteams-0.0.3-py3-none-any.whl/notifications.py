"""
Base of notification system
"""
import pymsteams

from datetime import datetime

from lifeguard.logger import lifeguard_logger as logger
from lifeguard.notifications import NotificationBase

from lifeguard_notification_msteams.settings import (
    MSTEAMS_DEFAULT_CHAT_ROOM,
)


DEFAULT_TITLES = {
    "single": "Single Notification",
    "open": "Problem Found",
    "update": "Updating Problem Status",
    "close": "Problem Solved",
}


class MSTeamsNotificationBase(NotificationBase):
    """
    Base of notification
    """

    @property
    def name(self):
        return "msteams"

    @staticmethod
    def __init_connectorcard(url, title):
        card = pymsteams.connectorcard(url)
        card.title(title)

        return card

    @staticmethod
    def __get_title(title_attribute, settings):
        return (
            settings.get("notification", {})
            .get("msteams", {})
            .get("titles", {})
            .get(title_attribute, DEFAULT_TITLES[title_attribute])
        )

    def send_single_message(self, content, settings):
        logger.info("seding single message to msteams")

        self.__send_message(self.__get_title("single", settings), content, settings)

    def init_thread(self, content, settings):
        logger.info("notify a new problem")

        self.__send_message(self.__get_title("open", settings), content, settings)

        return [datetime.now().strftime("%Y%m%d%H%M")]

    def update_thread(self, threads, content, settings):
        logger.info("notify updating problem status %s", threads)
        self.__send_message(self.__get_title("update", settings), content, settings)

    def close_thread(self, threads, content, settings):
        logger.info("notify closing problem status %s", threads)
        self.__send_message(self.__get_title("close", settings), content, settings)

    def __send_message(self, title, content, settings):
        if not isinstance(content, list):
            content = [content]

        for room in (
            settings.get("notification", {})
            .get("msteams", {})
            .get("channels", [MSTEAMS_DEFAULT_CHAT_ROOM])
        ):
            card = self.__init_connectorcard(room, title)

            text = []
            for entry in content:
                text.append(entry)
            card.text("\n".join(text))
            card.send()
