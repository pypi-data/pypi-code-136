import io
import logging

import rich
import sphinx.util.logging
from sphinx.application import Sphinx


class CLILogHandler(sphinx.util.logging.NewLineStreamHandler):  # type: ignore
    def __init__(self, log):
        self.stream = log
        super().__init__(self.stream)  # type: ignore

    def emit(self, record: logging.LogRecord):
        message = getattr(record, "message", None)
        msg = getattr(record, "msg", None)

        try:
            msg = self.format(record)
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            stream.write(f"{msg}, {message}{self.terminator}")
            self.flush()
        except RecursionError:  # See issue 36272
            raise
        except Exception:
            self.handleError(record)
        # self.stream.append(f"{message}, {msg}")
        # rich.print(f"[blue]{msg}[/] : [green]{message}[/]")


def add_log_handler(
    app: Sphinx, status: io.StringIO, warning: io.StringIO, log: io.StringIO
):
    sphinx.util.logging.setup(app, status, warning)  # type: ignore
    logger = logging.getLogger(sphinx.util.logging.NAMESPACE)
    logger.addHandler(CLILogHandler(log))
    pass
