import logging

from wepipe.core.configuration import WepipeConfiguration

logger = logging.getLogger(__name__)

# Extract config via yaml file using `config_path` and `config_filename`
wepipe_configuration = WepipeConfiguration()

# Initialize objects using configuration
source_config = wepipe_configuration.initialize_instance("source_config")
source = wepipe_configuration.initialize_instance("source")
pipeline = wepipe_configuration.initialize_instance("pipeline")
pipeline_config = wepipe_configuration.initialize_instance("pipeline_config")
destination_config = wepipe_configuration.initialize_instance("destination_config")
destination = wepipe_configuration.initialize_instance("destination")

# This will fetch information from configured source ie twitter, app store etc
source_response_list = source.load(source_config)
for idx, source_response in enumerate(source_response_list):
    logger.info(f"source_response#'{idx}'='{vars(source_response)}'")

# This will execute pipeline (Sentiment, classification etc) on source data with provided pipeline_config
# Pipeline will it's output to `segmented_data` inside `pipeline_response`
pipeline_response_list = pipeline.pipe_input(
    source_response_list=source_response_list,
    pipeline_config=pipeline_config
)
for idx, pipeline_response in enumerate(pipeline_response_list):
    logger.info(f"source_response#'{idx}'='{vars(pipeline_response)}'")

# This will send piped output to configure destination. e.g. Feishu, Pandas
destination_response_list = destination.send_data(pipeline_response_list, destination_config)
for idx, destination_response in enumerate(destination_response_list):
    logger.info(f"source_response#'{idx}'='{vars(destination_response)}'")
