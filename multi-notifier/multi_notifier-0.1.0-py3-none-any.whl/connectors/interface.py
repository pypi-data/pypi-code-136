"""Interface for all connectors."""
import abc


class Interface:
	"""Interface for all connectors."""
	@abc.abstractmethod
	def send_message(self, recipient: str | list[str], message: str, subject: str | None = None) -> None:
		"""Send a message to one or multiple recipients

		:param recipient:
		:param message:
		:param subject:
		"""

	@staticmethod
	@abc.abstractmethod
	def is_valid_recipient(recipient: str) -> bool:
		"""Check if the given recipient is valid.

		:param recipient: Single recipient which should be checked
		:return: True if recipient has a supported format, else False
		"""
