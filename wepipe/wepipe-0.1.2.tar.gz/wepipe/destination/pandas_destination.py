from typing import Any, Dict, List, Optional

from pandas import DataFrame

from wepipe.core.payload import TextPayload
from wepipe.integrate.utils import flatten_dict
from wepipe.destination.base_destination import BaseDestination, BaseDestinationConfig, Convertor


class PandasConvertor(Convertor):
    def convert(
        self,
        pipeline_response: TextPayload,
        base_payload: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        base_payload = base_payload or {}
        merged_dict = {**base_payload, **pipeline_response.to_dict()}
        return flatten_dict(merged_dict)


class PandasDestinationConfig(BaseDestinationConfig):
    TYPE: str = "Pandas"
    dataframe: Optional[DataFrame] = None
    # By default it will include all the columns
    include_columns_list: Optional[List[str]] = None

    def __init__(self, **data: Any):
        super().__init__(**data)

        if self.dataframe is None:
            self.dataframe = DataFrame()


class PandasDestination(BaseDestination):
    TYPE: str = "Pandas"

    def __init__(self, convertor: Convertor = PandasConvertor(), **data: Any):
        super().__init__(convertor=convertor, **data)

    def send_data(  # type: ignore[override]
        self,
        pipeline_responses: List[TextPayload],
        config: PandasDestinationConfig,
        **kwargs,
    ):
        responses = []
        for pipeline_response in pipeline_responses:
            converted_response = self.convertor.convert(
                pipeline_response=pipeline_response
            )
            response: Optional[Dict[str, Any]]
            if config.include_columns_list:
                response = dict()
                for k, v in converted_response.items():
                    if k in config.include_columns_list:
                        response[k] = v
            else:
                response = converted_response
            responses.append(response)

        if config.dataframe is not None:
            config.dataframe = config.dataframe.append(responses)

        return config.dataframe
