import logging
import traceback
from typing import Any, Optional

import structlog
from structlog import contextvars

from payla_utils.generic_logger.default_configuration import get_default_logging_conf


class LoggerSetupError(Exception):
    pass


class GenericLogger:
    def __init__(
        self,
        service_name: str,
        default_level: str,
        own_apps: Optional[list] = None,
        config: Optional[dict] = None,
        setup_logging_dict: bool = False,
    ):
        self.service_name = service_name
        self.default_level = default_level.upper()
        self.config = config
        self.own_apps = own_apps or []
        self.setup_logging_dict = setup_logging_dict

    def structured_field_injection(
        self,
        _: Any,
        __: str,
        event_dict: structlog.types.EventDict,
    ) -> structlog.types.EventDict:
        event_dict["microservice"] = self.service_name

        return event_dict

    @staticmethod
    def add_structlog_context(
        _: Any,
        __: str,
        event_dict: structlog.types.EventDict,
    ) -> structlog.types.EventDict:
        """Update ``event_dict`` with context of the ``structlog`` logger."""
        event_dict.update(structlog.get_logger()._context._dict)
        return event_dict

    @staticmethod
    def add_exc_info_flag_for_exception(
        _: Any,
        name: str,
        event_dict: structlog.types.EventDict,
    ) -> structlog.types.EventDict:
        if name in ["exception", "error"]:
            event_dict["stack_info"] = True
        try:
            if event_dict.get("error"):
                tracebacks = traceback.format_exc()
                event_dict["error"] = tracebacks
        except Exception:  # pylint: disable=board-except
            return event_dict

        return event_dict

    def get_processors(self) -> list:
        processors = [
            contextvars.merge_contextvars,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.filter_by_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.ExceptionPrettyPrinter(),
            structlog.processors.CallsiteParameterAdder(),
            structlog.stdlib.ExtraAdder(),
            self.structured_field_injection,
            structlog.processors.EventRenamer(to="event", replace_by="message"),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ]
        return processors

    def configure_structlog(self, custom_processors=None):

        if self.setup_logging_dict:
            logger_init_config = self.config
            if not self.config:
                logger_init_config = get_default_logging_conf(
                    log_level=self.default_level, own_apps=self.own_apps, console_formatter="plain_console"
                )

            logging.config.dictConfig(logger_init_config)

        processors = custom_processors
        if not custom_processors:
            processors = self.get_processors()

        structlog.configure(
            processors=processors,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )
