"""Exceptions of notification SEND_HANDLER package."""

class NotificationException(Exception):
	"""Exception which is raised by this python package."""


class ConfigurationException(NotificationException):
	"""Exception which is raised if configuration is faulty."""
