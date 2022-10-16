from typing import Any, Dict, List, Optional
from pydantic import ValidationError, validator 
import streamlit as st

from wepipe.core.payload import PlotPayload
from wepipe.integrate.utils import flatten_dict
from wepipe.destination.base_destination import BaseDestination, BaseDestinationConfig, Convertor


class StreamlitChartConvertor(Convertor):
    def convert(
        self,
        pipeline_response: PlotPayload,
        base_payload: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        base_payload = base_payload or {}
        merged_dict = {**base_payload, **pipeline_response.to_dict()}
        return flatten_dict(merged_dict)


class StreamlitChartDestinationConfig(BaseDestinationConfig):
    TYPE: str = "StreamlitChart"
    # By default it will include all the columns
    # chart_element: str = "altair_chart"
    # chart_style: str = "weanalyze"
    use_container_width: bool = True
    
    # @validator('chart_element')
    # def chart_element_must_st(cls, v):
    #     chart_elements = [
    #         'pyplot', 'altair_chart', 'vega_little_chart', 
    #         'plotly_chart', 'bokeh_chart', 'pydeck_chart', 'graphviz_chart'
    #     ]
    #     if v not in chart_elements:
    #         raise ValueError('must contain in streamlit chart elements')
    #     return v

    def __init__(self, **data: Any):
        super().__init__(**data)


class StreamlitChartDestination(BaseDestination):
    TYPE: str = "StreamlitChart"

    def __init__(self, convertor: Convertor = StreamlitChartConvertor(), **data: Any):
        super().__init__(convertor=convertor, **data)

    def send_data(  # type: ignore[override]
        self,
        pipeline_responses: List[PlotPayload],
        config: StreamlitChartDestinationConfig,
        **kwargs,
    ):
        destination_responses = []
        for pipeline_response in pipeline_responses:
            converted_response = self.convertor.convert(
                pipeline_response=pipeline_response
            )
            # converted_response = pipeline_response
            # plot = converted_response['plot']
            # st_ploter = getattr(st, config.chart_element)
            # destination_response = (st_ploter, plot)
            destination_response = converted_response['plot']
            destination_responses.append(destination_response)
        return destination_responses
