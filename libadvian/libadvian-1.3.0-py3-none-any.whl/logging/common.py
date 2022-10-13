"""Things common for all handlers"""
import json
from typing import Optional, Mapping, Any, Callable
import logging
import time
import datetime


class UTCISOFormatter(logging.Formatter):
    """Output timestamps in UTC ISO timestamps"""

    converter = time.gmtime

    def formatTime(self, record: logging.LogRecord, datefmt: Optional[str] = None) -> str:
        converted = datetime.datetime.fromtimestamp(record.created, tz=datetime.timezone.utc)
        if datefmt:
            formatted = converted.strftime(datefmt)
        else:
            formatted = converted.isoformat(timespec="milliseconds")
        return formatted.replace("+00:00", "Z")


DEFAULT_LOG_FORMAT = (
    "[%(asctime)s][%(levelname)s] %(name)s (%(process)d) %(pathname)s:%(funcName)s:%(lineno)d | %(message)s"
)
DEFAULT_LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "utc": {
            "()": UTCISOFormatter,
            "format": DEFAULT_LOG_FORMAT,
        },
        "local": {
            "format": DEFAULT_LOG_FORMAT,
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "utc",
        },
    },
    "root": {
        "handlers": ["console"],
    },
}

DEFAULT_RECORD_DIR = set(
    list(logging.LogRecord("dummy", 10, "dummy.py", 228, "Dummy", None, None, "dummy", None).__dir__())
    + ["message", "asctime"]
)


def log_metrics(
    method: Callable[..., Any], metrics: Mapping[str, Any], *, extra: Optional[Mapping[str, Any]] = None
) -> None:
    """Create a log message that can easily parsed into metrics by Vector

    Usage:
        log_metrics(LOGGER.info, {"key1": 1.2, "key2": 0.2})
        log_metrics(LOGGER.info, {"key1": 1.2, "key2": 0.2}, extra={"label1": "value", "label2": "valuetwo"})
    """
    method(f"METRICS:{json.dumps(metrics)}", extra=extra)


class AddExtrasFilter(logging.Filter):  # pylint: disable=R0903
    """Add the extra properties and values given at init"""

    def __init__(self, extras: Mapping[str, Any], name: str = "") -> None:
        """init"""
        if not extras or not isinstance(extras, Mapping):
            raise ValueError("extras must be non-empty mapping")
        self.add_extras = extras
        super().__init__(name)

    def filter(self, record: logging.LogRecord) -> bool:
        """Add the extras then call parent filter"""
        for key in self.add_extras:
            setattr(record, key, self.add_extras[key])
        return super().filter(record)
