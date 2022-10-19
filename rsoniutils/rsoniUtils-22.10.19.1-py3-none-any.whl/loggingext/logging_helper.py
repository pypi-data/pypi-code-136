from logging import Logger, log
from opencensus.ext.azure.log_exporter import AzureLogHandler

original_excepthook = None
original_logger = None


def enable_appinsights(logger: Logger, instrumentation_key: str):
    if instrumentation_key == None or instrumentation_key == "":
        return

    logger.addHandler(AzureLogHandler(
        connection_string='InstrumentationKey='+instrumentation_key,
        export_interval=1.0)
    )