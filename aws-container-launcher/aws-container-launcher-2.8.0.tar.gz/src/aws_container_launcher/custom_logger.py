import threading
import os
from ._util import StructuredLogMessage as _


class CustomLogger:
    def __init__(self, logger):
        self.logger = logger
        self.log_level = os.environ.get('ACL_LOG_LEVEL')

    def info(self, *args):
        if self.log_level and (self.log_level == 'INFO' or self.log_level == 'DEBUG' or self.log_level == 'TRACE'):
            self.logger.notice(
                _(
                    *args,
                    thread=threading.get_ident(),
                )
            )
        else:
            self.logger.info(
                _(
                    *args,
                    thread=threading.get_ident(),
                )
            )

    def error(self, *args):
        self.logger.error(
            _(
                *args,
                thread=threading.get_ident(),
            )
        )

    def notice(self, *args):
        self.logger.notice(
            _(
                *args,
                thread=threading.get_ident(),
            )
        )

    def warning(self, *args):
        self.logger.warning(
            _(
                *args,
                thread=threading.get_ident(),
            )
        )

    def debug(self, *args):
        if self.log_level and (self.log_level == 'DEBUG' or self.log_level == 'TRACE'):
            self.logger.notice(
                _(
                    *args,
                    thread=threading.get_ident(),
                )
            )
        else:
            self.logger.debug(
                _(
                    *args,
                    thread=threading.get_ident(),
                )
            )
