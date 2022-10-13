"""Main file of the notification SEND_HANDLER"""
import inspect
import logging
import pathlib

import yaml

import multi_notifier.connectors.connector_mail
import multi_notifier.connectors.connector_telegram
import multi_notifier.connectors.exceptions
import multi_notifier.exceptions

MODULE_LOGGER = logging.getLogger(__name__)


class SendHandler:
	"""The notification SEND_HANDLER can be used to send notifications depending on the level and source file to different recipients."""

	def __init__(self, config: dict | pathlib.Path):
		"""Create instance of the notification SEND_HANDLER.

		:param config: Configuration of the send_handler can be given as dict or path to a yaml file
		"""
		self.__config = config if isinstance(config, dict) else self.__get_config_from_yaml(config)
		self.__validate_config()
		self._mail = self.__init_mail()
		self._telegram = self.__init_telegram()
		self.__init_send_config()

	@staticmethod
	def __get_config_from_yaml(path: pathlib.Path) -> dict:
		"""Get configuration dictionary from yaml file.

		:param path: path of configuration yaml file
		:return: values from yaml file as dictionary
		:raises multi_notifier.exceptions.ConfigurationException: if given path is not a yaml file
		"""
		if not path.suffix == ".yml":
			MODULE_LOGGER.error(msg := "Configuration file must be a yml file!")
			raise multi_notifier.exceptions.ConfigurationException(msg)

		with path.open("r", encoding="utf-8") as config_file:
			return yaml.load(config_file, yaml.Loader)

	def __validate_config(self) -> None:
		"""Validate config dict

		:raises multi_notifier.exceptions.ConfigurationException: if mandatory keys are missing
		"""
		if "connectors" not in self.__config:
			MODULE_LOGGER.error(msg := "No configuration for any connector was found")
			raise multi_notifier.exceptions.ConfigurationException(msg)

		if "recipients" not in self.__config:
			MODULE_LOGGER.error(msg := "No configuration for any recipient was found")
			raise multi_notifier.exceptions.ConfigurationException(msg)

	def __init_mail(self) -> multi_notifier.connectors.connector_mail.Mail | None:
		"""Create instance of the mail connector.

		:return: Instance of mail connector, or None if it could not be created.
		:raises multi_notifier.exceptions.ConfigurationException: If configuration is not correct.
		"""
		if not (mail_config := self.__config["connectors"].get("mail")):
			MODULE_LOGGER.info("Mail is not configured")
			return None

		try:
			return multi_notifier.connectors.connector_mail.Mail(mail_config["user"], mail_config["password"], mail_config["smtp_server"], mail_config["smtp_port"], mail_config["imap_server"])
		except multi_notifier.connectors.exceptions.ConnectorConfigurationException:
			MODULE_LOGGER.exception(msg := "Check configuration of mail!")
			raise multi_notifier.exceptions.ConfigurationException(msg)
		except KeyError as exc:
			MODULE_LOGGER.exception(msg := f"The key {exc} is missing in the mail configuration")
			raise multi_notifier.exceptions.ConfigurationException(msg)

	def __init_telegram(self) -> multi_notifier.connectors.connector_telegram.Telegram | None:
		"""Create instance of the telegram connector

		:return: Instance of telegram connector, or None if it could not be created.
		:raises multi_notifier.exceptions.ConfigurationException: If configuration is not correct.
		"""
		if not (telegram_config := self.__config["connectors"].get("telegram")):
			MODULE_LOGGER.info("Telegram is not configured")
			return None
		try:
			return multi_notifier.connectors.connector_telegram.Telegram(telegram_config["bot_token"])
		except multi_notifier.connectors.exceptions.ConnectorConfigurationException:
			MODULE_LOGGER.exception(msg := "Check configuration of telegram!")
			raise multi_notifier.exceptions.ConfigurationException(msg)
		except KeyError as exc:
			MODULE_LOGGER.exception(msg := f"The key {exc} is missing in the mail configuration")
			raise multi_notifier.exceptions.ConfigurationException(msg)

	def __init_send_config(self) -> None:
		"""Parse send config."""
		MODULE_LOGGER.debug("Init send configuration")
		self._send_config = {}

		for config_name, config_value in self.__config["recipients"].items():
			self._send_config[config_name] = {
				"mail": multi_notifier.RecipientMail.from_config(config_value.get("mail", {})),
				"telegram": multi_notifier.RecipientTelegram.from_config(config_value.get("telegram", {}))
			}

	@staticmethod
	def __get_caller_module() -> str:
		"""Get the caller module, which want to send a notification.

		:return: Name of the caller module
		:raises multi_notifier.exceptions.NotificationException: if caller module could not be found
		"""
		for frame_info in inspect.stack()[1:]:
			if frame_info.filename != __file__:
				module = inspect.getmodule(frame_info[0])
				return module.__name__

		MODULE_LOGGER.error(msg := "Could not find caller method!")
		raise multi_notifier.exceptions.NotificationException(msg)

	def error(self, message: str) -> None:
		"""Send a error notification to the configured recipients.

		:param message: Message which should be sent.
		"""
		self._send_message(message, multi_notifier.NotificationLevel.ERROR)

	def warning(self, message: str) -> None:
		"""Send a warning notification to the configured recipients.

		:param message: Message which should be sent.
		"""
		self._send_message(message, multi_notifier.NotificationLevel.WARNING)

	def info(self, message: str) -> None:
		"""Send a info notification to the configured recipients.

		:param message: Message which should be sent.
		"""
		self._send_message(message, multi_notifier.NotificationLevel.INFO)

	def debug(self, message: str) -> None:
		"""Send a debug notification to the configured recipients.

		:param message: Message which should be sent.
		"""
		self._send_message(message, multi_notifier.NotificationLevel.DEBUG)

	def _send_message(self, message: str, level: multi_notifier.NotificationLevel, caller_module_name: str | None = None) -> None:
		"""Send a message to the configured recipients.

		:param message: Message which should be sent
		:param level: Notification level of the message
		:param caller_module_name: Name of the caller module
		"""
		MODULE_LOGGER.debug(f"Send message '{message[:20]}...` with level {level.name}")
		caller_module_name = caller_module_name if caller_module_name else self.__get_caller_module()
		recipient_config = self._send_config.get(caller_module_name, self._send_config["default"])

		short_message = message if len(message) < 50 else f"{message[:50]}..."

		if self._mail:
			for recipient in getattr(recipient_config.get("mail"), level.name.lower(), []):
				MODULE_LOGGER.debug(f"Send mail to '{recipient}': {short_message} | (This request came from '{caller_module_name}')")
				self._mail.send_message(recipient, message, f"{level.name} from {caller_module_name}")

		if self._telegram:
			for recipient in getattr(recipient_config.get("telegram"), level.name.lower(), []):
				MODULE_LOGGER.debug(f"Send telegram to '{recipient}': {short_message} | (This request came from '{caller_module_name}')")
				self._telegram.send_message(recipient, message)
