import re
import os
import logging

LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40
}

def get_log_level():
    try:
        return LOG_LEVELS[os.environ.get('LOG_LEVEL').upper()]  # type: ignore
    except:
        return LOG_LEVELS['INFO']

def logger():
    logger = logging.getLogger()
    logger.setLevel(get_log_level())
    return logger

class LogMessage:
    """ Create a log message with Splunk formatting

    More on Splunk best practices for logging can be found here:
    https://dev.splunk.com/enterprise/docs/developapps/addsupport/logging/loggingbestpractices/
    """

    def __init__(self) -> None:
        self.log_message = ""

    def clear(self):
        self.log_message = ""

    def add(self, key: str, value: str):
        """Add a key/value pair to the log message
        """
        log_msg = self.log_message + f"{key}=\"{value}\" "
        log_msg = log_msg.replace('\n', '').replace('\r', '')  # remove carriage returns and new lines
        log_msg = re.sub(' +', ' ', log_msg)  # replace multiple spaces with one space
        self.log_message = log_msg

    def __str__(self) -> str:
        return self.log_message