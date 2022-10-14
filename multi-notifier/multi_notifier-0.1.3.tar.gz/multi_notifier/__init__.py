"""Init file of send_handler"""
import abc
import dataclasses
import enum

import multi_notifier.connectors.connector_mail
import multi_notifier.connectors.connector_telegram


class NotificationLevel(enum.Enum):
	"""Supported notification levels."""
	ERROR = enum.auto()
	WARNING = enum.auto()
	INFO = enum.auto()
	DEBUG = enum.auto()


@dataclasses.dataclass
class RecipientBase:
	"""Base class for the configuration of the recipients."""
	error: list[str]
	warning: list[str]
	info: list[str]
	debug: list[str]

	@classmethod
	def from_config(cls, config: dict) -> "RecipientBase":
		"""Get a recipient dataclass from configuration dict

		:param config: configuration dict
		:return: Instance of a recipient configuration
		"""
		error = cls._get_valid_recipients(cls, config.get("error"))
		warning = cls._get_valid_recipients(cls, config.get("warning"))
		info = cls._get_valid_recipients(cls, config.get("info"))
		debug = cls._get_valid_recipients(cls, config.get("debug"))

		return cls(error, warning, info, debug)

	def _get_valid_recipients(self, value: str | list[str]) -> list[str]:
		"""Get a list of valid recipients

		:param value:
		:return: list of valid recipients
		"""
		recipients = (value if isinstance(value, list) else [value]) if value else []

		return [recipient for recipient in recipients if self._is_valid_recipient(recipient)]

	@staticmethod
	@abc.abstractmethod
	def _is_valid_recipient(recipient: str) -> bool:
		"""Check if a single recipient name is a valid name for the connector.

		:param recipient: Name of the recipient
		:return: True if it is a valid name, else False
		"""


@dataclasses.dataclass
class RecipientMail(RecipientBase):
	"""Configuration dataclass for mail recipients."""

	@staticmethod
	def _is_valid_recipient(recipient: str) -> bool:
		"""Check if a single recipient name is a valid name for the connector.

		:param recipient: Name of the recipient
		:return: True if it is a valid name, else False
		"""
		return multi_notifier.connectors.connector_mail.Mail.is_valid_recipient(recipient)


@dataclasses.dataclass
class RecipientTelegram(RecipientBase):
	"""Configuration dataclass for telegram recipients."""

	@staticmethod
	def _is_valid_recipient(recipient: str) -> bool:
		"""Check if a single recipient name is a valid name for the connector.

		:param recipient: Name of the recipient
		:return: True if it is a valid name, else False
		"""
		return multi_notifier.connectors.connector_telegram.Telegram.is_valid_recipient(recipient)
