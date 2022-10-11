"""
Helper functions for observability.
"""
# pylint: disable=too-few-public-methods

import os
from opencensus.extension.azure.functions import OpenCensusExtension
from opencensus.trace import config_integration


class FuncObservability:
    """
    This class is a helper for OpenCensus observability extension
    in Azure Functions with Application Insights.
    """

    _configured = False

    @classmethod
    def initialize(cls):
        """
        Initialize the OpenCensus observability extension
        in Azure Functions.
        """

        if not cls._configured:
            if os.getenv("APPINSIGHTS_INSTRUMENTATIONKEY"):
                # enable tracing of http requests
                config_integration.trace_integrations(["requests"])

                OpenCensusExtension.configure()
            cls._configured = True
