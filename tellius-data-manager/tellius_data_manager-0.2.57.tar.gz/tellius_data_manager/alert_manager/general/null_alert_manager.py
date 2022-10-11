from tellius_data_manager.alert_manager.alert_manager import AlertManager
from tellius_data_manager.config_reader.config_reader_factory import ConfigReaderFactory


class NullAlertManager(AlertManager):
    """Abstraction to manage the process sending an alert."""

    _config_reader_factory = ConfigReaderFactory

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def send_alert(self, message_content: str) -> None:
        """Prints a message to STDIO.

        Args:
            message_content: message to be printed

        """
        print(message_content)
