import logging
from logging import Logger
from typing import Any, List, Optional

from pydantic import Field

from wepipe.core.payload import TextPayload
from wepipe.destination.base_destination import BaseDestination, BaseDestinationConfig, Convertor


class LoggerDestinationConfig(BaseDestinationConfig):
    TYPE: str = "Logging"
    logger: Logger = Field(logging.getLogger(__name__))
    level: int = Field(logging.INFO)


class LoggerDestination(BaseDestination):
    TYPE: str = "Logging"

    def __init__(self, convertor: Convertor = Convertor(), **data: Any):
        super().__init__(convertor=convertor, **data)

    def send_data(  # type: ignore[override]
        self,
        pipeline_responses: List[TextPayload],
        config: LoggerDestinationConfig,
        **kwargs,
    ):
        converted_responses = []
        for pipeline_response in pipeline_responses:
            converted_responses.append(
                self.convertor.convert(pipeline_response=pipeline_response)
            )

        for response in converted_responses:
            dict_to_print = (
                vars(response) if hasattr(response, "__dict__") else response
            )
            config.logger.log(level=config.level, msg=f"{dict_to_print}")
