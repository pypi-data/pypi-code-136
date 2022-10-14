OTEL_EXPORTER_OTLP_METRICS_ENDPOINT = "OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"
"""
.. envvar:: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT

The :envvar:`OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` target to which the span exporter is going to send spans.
The endpoint MUST be a valid URL host, and MAY contain a scheme (http or https), port and path.
A scheme of https indicates a secure connection and takes precedence over this configuration setting.
"""

OTEL_EXPORTER_OTLP_METRICS_CERTIFICATE = "OTEL_EXPORTER_OTLP_METRRICS_CERTIFICATE"
"""
.. envvar:: OTEL_EXPORTER_OTLP_METRICS_CERTIFICATE

The :envvar:`OTEL_EXPORTER_OTLP_METRICS_CERTIFICATE` stores the path to the certificate file for
TLS credentials of gRPC client for traces. Should only be used for a secure connection for tracing.
"""

OTEL_EXPORTER_OTLP_METRICS_HEADERS = "OTEL_EXPORTER_OTLP_METRICS_HEADERS"
"""
.. envvar:: OTEL_EXPORTER_OTLP_METRICS_HEADERS

The :envvar:`OTEL_EXPORTER_OTLP_METRICS_HEADERS` contains the key-value pairs to be used as headers for spans
associated with gRPC or HTTP requests.
"""

OTEL_EXPORTER_OTLP_METRICS_TIMEOUT = "OTEL_EXPORTER_OTLP_METRICS_TIMEOUT"
"""
.. envvar:: OTEL_EXPORTER_OTLP_METRICS_TIMEOUT

The :envvar:`OTEL_EXPORTER_OTLP_METRICS_TIMEOUT` is the maximum time the OTLP exporter will
wait for each batch export for spans.
"""

OTEL_EXPORTER_OTLP_METRICS_COMPRESSION = "OTEL_EXPORTER_OTLP_METRICS_COMPRESSION"
"""
.. envvar:: OTEL_EXPORTER_OTLP_METRICS_COMPRESSION

Same as :envvar:`OTEL_EXPORTER_OTLP_COMPRESSION` but only for the span
exporter. If both are present, this takes higher precendence.
"""
