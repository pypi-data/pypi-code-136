import logging
from typing import Optional

from pydantic import BaseModel

from wepipe.pipeline.base_pipeline import BasePipeline, BasePipelineConfig
from wepipe.destination.base_destination import BaseDestination, BaseDestinationConfig
from wepipe.source.base_source import BaseSource, BaseSourceConfig
from wepipe.core.workflow.workflow import Workflow

logger = logging.getLogger(__name__)


class Processor(BaseModel):
    pipeline: BasePipeline
    pipeline_config: Optional[BasePipelineConfig] = None
    source: Optional[BaseSource] = None
    source_config: Optional[BaseSourceConfig] = None
    destination: Optional[BaseDestination] = None
    destination_config: Optional[BaseDestinationConfig] = None

    def process(
        self,
        workflow: Optional[Workflow] = None,
        source: Optional[BaseSource] = None,
        source_config: Optional[BaseSourceConfig] = None,
        destination: Optional[BaseDestination] = None,
        destination_config: Optional[BaseDestinationConfig] = None,
        pipeline: Optional[BasePipeline] = None,
        pipeline_config: Optional[BasePipelineConfig] = None,
    ):
        source = source or self.source
        destination = destination or self.destination
        pipeline = pipeline or self.pipeline

        id: Optional[str] = None
        if workflow:
            destination_config = workflow.config.destination_config
            source_config = workflow.config.source_config
            pipeline_config = workflow.config.pipeline_config
            id = workflow.id
        else:
            destination_config = destination_config or self.destination_config
            source_config = source_config or self.source_config
            pipeline_config = pipeline_config or self.pipeline_config

        if source is None or source_config is None:
            return
        if destination is None or destination_config is None:
            return

        source_response_list = source.load(config=source_config, id=id)
        for idx, source_response in enumerate(source_response_list):
            logger.info(f"source_response#'{idx}'='{source_response}'")

        pipeline_response_list = pipeline.pipe_input(
            source_response_list=source_response_list,
            pipeline_config=pipeline_config,
            id=id,
        )
        for idx, pipeline_response in enumerate(pipeline_response_list):
            logger.info(f"pipeline_response#'{idx}'='{pipeline_response}'")

        destination_response_list = destination.send_data(
            pipeline_responses=pipeline_response_list, config=destination_config, id=id
        )
        for idx, destination_response in enumerate(destination_response_list):
            logger.info(f"destination_response#'{idx}'='{destination_response}'")
