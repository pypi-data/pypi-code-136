from logging.handlers import SocketHandler

from .formatter import Formatter


AUTHOR = "Joe Tilsed | http://JoeTilsed.com"
CREATED = "11/10/2022"
LAST_UPDATED = "11/10/2022"
VERSION = "0.1.0"


class Handler(SocketHandler):
    """ Python handler to any logging service. Sends events over TCP.
    :param host: The host of the log server.
    :param port: The port of the log server.
    :param label: The label for what is sending the logs, i.e. resource-abc (default is None).
    :param tags: list of tags for a logger (default is None).
    """

    def __init__(self, host, port, label=None, tags=None):
        super().__init__(host, port)
        self.formatter = Formatter(label, tags)

    def makePickle(self, record):
        pickle = self.formatter.format(record)
        return pickle


# That's all folks...
