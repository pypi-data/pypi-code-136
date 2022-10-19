import logging


class LoggingMixin:
    @property
    def _logger(self):
        if not hasattr(self, '_logobj'):
            self._logobj = \
                logging.getLogger(f'{__name__}.{self.__class__.__name__}')
        return self._logobj
