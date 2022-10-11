"""
Observability utilities for Azure Functions.
"""
from opencensus.trace.tracer import Tracer
from opencensus.trace.tracers.noop_tracer import NoopTracer
import azure.functions as func


def get_tracer(context: func.Context) -> Tracer:
    """
    Gets a tracer for the current Azure Function invocation.
    If it does not exist returns a no op tracer.
    (Will not exist if APPINSIGHTS_INSTRUMENTATIONKEY is not set).
    """

    if hasattr(context, "tracer"):
        return context.tracer

    return NoopTracer()
