"""All connector exceptions."""
import multi_notifier.exceptions


class ConnectorException(multi_notifier.exceptions.NotificationException):
	"""Exception which is raised by connectors."""


class ConnectorConfigurationException(ConnectorException):
	"""Exception which is raised if configuration is faulty."""


class ConnectorTimeoutException(ConnectorException):
	"""Exception which is raised if a timeout is raised."""
