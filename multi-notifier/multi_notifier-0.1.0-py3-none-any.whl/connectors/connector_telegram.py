"""Module for communication with Telegram, Mail, ..."""
import logging

import requests

import multi_notifier.connectors.exceptions
import multi_notifier.connectors.interface

MODULE_LOGGER = logging.getLogger(__name__)


class Telegram(multi_notifier.connectors.interface.Interface):
	"""Class to send Telegram messages"""

	def __init__(self, bot_token: str) -> None:
		"""Init Telegram class.

		:param bot_token: bot token from telegram
		:raises multi_notifier.connectors.exceptions.ConnectorConfigurationException: if bot configuration is not correct
		"""
		self.__bot_token = bot_token
		self.__test_config()

	def __test_config(self) -> None:
		"""Test if bot token is correct

		:raises multi_notifier.connectors.exceptions.ConnectorConfigurationException: if bot token is not correct
		"""
		response = requests.get(f"https://api.telegram.org/bot{self.__bot_token}/getMe")
		if response.status_code != 200:
			MODULE_LOGGER.error(msg := f"Bot config not valid. Response from Telegram-API: {response.content}")
			raise multi_notifier.connectors.exceptions.ConnectorConfigurationException(msg)

	def send_message(self, recipient: str | list[str], message: str, subject: str | None = None) -> None:
		"""Send a message to one or multiple recipients

		:param recipient: single recipient or list of recipients
		:param message: message which should be sent
		:param subject: subject will be ignored!
		:raises multi_notifier.connectors.exceptions.ConnectorException: if telegram could not be sent
		"""
		recipient = recipient if isinstance(recipient, list) else [recipient]

		for chat_id in recipient:
			MODULE_LOGGER.debug(f"Send message to {recipient}")
			response = requests.get(f"https://api.telegram.org/bot{self.__bot_token}/sendMessage", params={"chat_id": chat_id, "parse_mode": "HTML", "text": message})
			if not response.ok:
				MODULE_LOGGER.error(msg := f"Could not send telegram message '{message}' to chat_id={chat_id}")
				raise multi_notifier.connectors.exceptions.ConnectorException(msg)

	@staticmethod
	def is_valid_recipient(recipient: str) -> bool:
		"""Check if the given recipient is valid.

		:param recipient: Single recipient which should be checked
		:return: True if recipient has a supported format, else False
		"""
		if recipient.isdigit():
			return True
		MODULE_LOGGER.warning(f"The recipient '{recipient}' is not valid !")
		return False
