"""Logger"""
import logging
from typing import Optional
from logging.handlers import TimedRotatingFileHandler

import coloredlogs

coloredlogs.DEFAULT_LEVEL_STYLES = {
    'info': {},
    'notice': {'color': 'magenta'},
    'verbose': {'color': 'blue'},
    'success': {'color': 'green', 'bold': True},
    'spam': {'color': 'cyan'},
    'critical': {'color': 'red', 'bold': True},
    'error': {'color': 'red'},
    'debug': {'color': 'green'},
    'warning': {'color': 'yellow'}}


class LoggerBase:
    def __init__(self, name=None):
        self._logger = logging.getLogger(name or __name__)
        self._default_format = "%(asctime)s %(name)s [%(levelname)s] %(message)s"
        self.update_logger()

    def get_logger(self):
        return self._logger

    def __getattr__(self, name):
        try:
            return self._logger.__getattribute__(name)
        except AttributeError:
            return self.__getattribute__(name)

    def _reset_handlers(self):
        for handler in self._logger.handlers[:]:
            self._logger.removeHandler(handler)

    def update_logger(self,
                      log_level: Optional[int] = None,
                      log_format=None,
                      log_path=None,
                      stream_out: Optional[bool] = None,
                      coloredlog: bool = False,
                      **optionals):
        _log_level = log_level or logging.DEBUG
        _log_format = log_format or self._default_format
        _stream_out = True if log_path is None and stream_out is None else stream_out
        self._logger.setLevel(_log_level)
        formatter = logging.Formatter(_log_format)

        self._reset_handlers()

        if _stream_out:
            console = logging.StreamHandler()
            console.setLevel(_log_level)
            console.setFormatter(formatter)
            self._logger.addHandler(console)

            if coloredlog:
                style = coloredlogs.DEFAULT_LEVEL_STYLES.copy()
                coloredlogs.install(reconfigure=True,
                                    level=logging.getLevelName(_log_level), milliseconds=True, logger=self._logger,
                                    fmt=_log_format,
                                    datefmt='%H:%M:%S',
                                    level_styles=style)

        if log_path:
            file_handler = logging.FileHandler(filename=log_path)

            if optionals:
                log_when = optionals.get('log_when')
                log_interval = optionals.get('log_interval')
                log_backup_count = optionals.get('log_backup_count')

                if None not in [log_when, log_interval, log_backup_count]:
                    file_handler = TimedRotatingFileHandler(
                        filename=log_path,
                        when=log_when,
                        interval=log_interval,
                        backupCount=log_backup_count
                    )

            file_handler.setLevel(_log_level)
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)


class Logger(LoggerBase):
    pass
