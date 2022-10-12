"""Connector for mail."""
import email.mime.text
import imaplib
import logging
import re
import smtplib
import socket
import time
import typing

import multi_notifier.connectors.exceptions
import multi_notifier.connectors.interface

MODULE_LOGGER = logging.getLogger(__name__)

_T = typing.TypeVar("_T")


class Mail(multi_notifier.connectors.interface.Interface):
	"""Class to send e-mails."""

	def __init__(self, user: str, password: str, smtp_host: str, smtp_port: int, imap_host: str):
		"""Init Mail class.

		:param user: username to log in to mail account
		:param password: password to log in to mail account
		:param smtp_host: smtp host name (e.g. smtp.1und1.de)
		:param smtp_port: smtp port
		:param imap_host: imap host name (e.g. imap.1und1.de)
		:raises multi_notifier.connectors.exceptions.ConnectorConfigurationException: If mail configuration is faulty
		"""
		self.__user = user
		self.__password = password
		self.__smtp_host = smtp_host
		self.__smtp_port = smtp_port
		self.__imap_host = imap_host

		try:
			self.__smtp_connection = smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=10)
		except (smtplib.SMTPConnectError, TimeoutError, socket.gaierror):
			MODULE_LOGGER.exception(msg := "Could not connect to smtp server. Check mail configuration")
			raise multi_notifier.connectors.exceptions.ConnectorConfigurationException(msg)

		self.__test_config()

	def __test_config(self) -> None:
		"""Test mail configuration.

		:raises multi_notifier.connectors.exceptions.ConnectorConfigurationException: if configuration is faulty
		"""
		# check user and password
		try:
			self.__smtp_connection.ehlo_or_helo_if_needed()
			self.__smtp_connection.login(self.__user, self.__password)
		except smtplib.SMTPAuthenticationError:
			MODULE_LOGGER.exception(msg := "Could not login to smtp server. Authentication failed. Check mail configuration.")
			raise multi_notifier.connectors.exceptions.ConnectorConfigurationException(msg)

		# check imap server
		try:
			imaplib.IMAP4_SSL(self.__imap_host)
		except socket.gaierror:
			MODULE_LOGGER.exception(msg := "Could not check imap settings. Check mail configuration.")
			raise multi_notifier.connectors.exceptions.ConnectorConfigurationException(msg)

	def __assert_smtp_connected(self):
		"""Check if smtp is connected and connect if not connected."""
		try:
			status = self.__smtp_connection.noop()[0]
		except smtplib.SMTPServerDisconnected:
			MODULE_LOGGER.debug("smtp not connected!")
			status = -1

		if status != 250:
			MODULE_LOGGER.debug("Reconnect smtp")
			self.__smtp_connection.connect(self.__smtp_host, self.__smtp_port)
			self.__smtp_connection.login(self.__user, self.__password)

	def send_message(self, recipient: str | list[str], message: str, subject: str | None = None) -> None:
		"""Send a message to one or multiple recipients

		:param recipient: one or multiple recipients. (Must be mail addresses!)
		:param message: Message which should be sent
		:param subject: Subject of the mail
		:raises multi_notifier.connectors.exceptions.ConnectorException: if mail could not be sent
		"""
		recipients = recipient if isinstance(recipient, list) else [recipient]

		mail_msg = email.mime.text.MIMEText(message)
		mail_msg["Subject"] = subject
		mail_msg["From"] = self.__user

		self.__assert_smtp_connected()

		for mail_address in recipients:
			try:
				MODULE_LOGGER.debug(f"Send message to {mail_address}")
				self.__smtp_connection.sendmail(self.__user, mail_address, mail_msg.as_string())
			except (smtplib.SMTPHeloError, smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused, smtplib.SMTPDataError, smtplib.SMTPNotSupportedError) as exc:
				MODULE_LOGGER.exception(msg := f"Could not send mail to '{recipient}")
				raise multi_notifier.connectors.exceptions.ConnectorException(f"{msg} | {exc}")

	@staticmethod
	def __check_imap_result(result: tuple[str, _T]) -> _T:
		"""Check the result of an imap call.

		:param result: return value of an imap call. Must be a tuple of status and result
		:return: result of the call
		:raises multi_notifier.connectors.exceptions.ConnectorException: if result is not OK.
		"""
		if not result[0] == "OK":
			MODULE_LOGGER.exception(msg := "imap result was not ok!")
			raise multi_notifier.connectors.exceptions.ConnectorException(msg)

		return result[1]

	def get_unread_mails(self) -> list[email.message.Message]:
		"""Get a list of unread mails.

		:return: list of unread mails
		:raises multi_notifier.connectors.exceptions.ConnectorException: if any imap call was not OK.
		"""
		MODULE_LOGGER.debug("Try to get unread mails")
		imap_server = imaplib.IMAP4_SSL(self.__imap_host, timeout=10)
		self.__check_imap_result(imap_server.login(self.__user, self.__password))
		self.__check_imap_result(imap_server.select("Inbox"))

		# get unread mails
		messages = self.__check_imap_result(imap_server.search(None, "UNSEEN"))

		# get id's of unread mails
		unread_mails_ids = messages[0].split()

		unread_mails = []
		for mail_id in unread_mails_ids:
			# download a message and parse it to a email message
			data = self.__check_imap_result(imap_server.fetch(mail_id, "(RFC822)"))
			unread_mails.append(email.message_from_bytes(data[0][1]))

		imap_server.logout()

		return unread_mails

	def wait_for_incoming_mail(self, max_time: int, expected_payload: str | None = None, sender_address: str | None = None) -> None:
		"""Wait for a incoming mail.

		If expected_payload or sender_address is given only mails will be accepted which fulfill all filters.
		:param max_time: Maximum time to wait
		:param expected_payload: text which must be part of the payload
		:param sender_address: sender address which must be contained in the "from" string
		:raises multi_notifier.connectors.exceptions.ConnectorTimeoutException: If expected mail was not received in time.
		"""
		MODULE_LOGGER.debug(f"Wait for incoming mail. Max_time = {max_time} | expected_payload = {expected_payload} | sender_address = {sender_address}")
		for idx in range(max_time + 1):
			for unread_mail in self.get_unread_mails():
				if expected_payload and expected_payload not in unread_mail.get_payload():
					continue
				if sender_address and sender_address not in unread_mail["From"]:
					continue
				return

			if idx < max_time:
				time.sleep(1)
		MODULE_LOGGER.error(msg := "Expected mail did not receive in time!")
		raise multi_notifier.connectors.exceptions.ConnectorTimeoutException(msg)

	@staticmethod
	def is_valid_recipient(recipient: str) -> bool:
		"""Check if the given recipient is valid.

		:param recipient: Single recipient which should be checked
		:return: True if recipient has a supported format, else False
		"""
		if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", recipient):
			return True
		MODULE_LOGGER.warning(f"The recipient '{recipient}' is not valid !")
		return False
