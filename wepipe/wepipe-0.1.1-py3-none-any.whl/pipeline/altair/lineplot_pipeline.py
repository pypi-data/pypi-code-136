from typing import Any, List, Optional, Type, Iterator, Union
from wepipe.pipeline.altair import (
    AltairPipelineConfig,
    AltairPipeline
)
from wepipe.core.payload import BasePayload, PlotPayload
from wepipe.integrate.utils import responses_to_df
from wepipe.pipeline.altair.client import *

        
class LineplotPipelineConfig(AltairPipelineConfig):
    TYPE: str = "Lineplot"
    is_timeseries: bool = True
    x: str
    y: str
    color: str
    title: str
    x_title: str
    y_title: str

    def __init__(self, **data: Any):
        super().__init__(**data)


class LineplotPipeline(AltairPipeline):
    TYPE: str = "Lineplot"

    def __init__(self, **data: Any):
        super().__init__(**data)

    def pipe_input(
        self,
        source_response_list: Union[List[Type[BasePayload]], Iterator[Type[BasePayload]]],
        pipeline_config: AltairPipelineConfig = None,
        **kwargs,
    ) -> List[PlotPayload]:
        # pipeline output
        pipeline_output = []
        # convert to dataframe
        df = responses_to_df(source_response_list)
        source_name = df['source_name'][0]
        # add raw on columns name
        # altair plot
        plot = plot_ts_line(
            df,
            x='raw_' + pipeline_config.x,
            y='raw_' + pipeline_config.y,
            color='raw_' + pipeline_config.color,
            x_title=pipeline_config.x_title,
            y_title=pipeline_config.y_title,
            title=pipeline_config.title,
        )
        pipeline_output.append(
            PlotPayload(
                source_name=source_name, 
                plot=plot 
            )
        )
        return pipeline_output
