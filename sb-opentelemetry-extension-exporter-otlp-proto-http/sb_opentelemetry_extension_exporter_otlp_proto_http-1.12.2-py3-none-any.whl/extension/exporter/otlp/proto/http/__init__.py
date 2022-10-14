# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This library allows to export metric data to an OTLP collector.

Usage
-----

The **OTLP Metrics HTTP Exporter** allows to export `OpenTelemetry`_ metrics to the
`OTLP`_ collector.

You can configure the exporter with the following environment variables:

- :envvar:`OTEL_EXPORTER_OTLP_METRICS_TIMEOUT`
- :envvar:`OTEL_EXPORTER_OTLP_METRICS_PROTOCOL`
- :envvar:`OTEL_EXPORTER_OTLP_METRICS_HEADERS`
- :envvar:`OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`
- :envvar:`OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`
- :envvar:`OTEL_EXPORTER_OTLP_METRICS_CERTIFICATE`
- :envvar:`OTEL_EXPORTER_OTLP_TIMEOUT`
- :envvar:`OTEL_EXPORTER_OTLP_PROTOCOL`
- :envvar:`OTEL_EXPORTER_OTLP_HEADERS`
- :envvar:`OTEL_EXPORTER_OTLP_ENDPOINT`
- :envvar:`OTEL_EXPORTER_OTLP_COMPRESSION`
- :envvar:`OTEL_EXPORTER_OTLP_CERTIFICATE`

.. _OTLP: https://github.com/open-telemetry/opentelemetry-collector/
.. _OpenTelemetry: https://github.com/open-telemetry/opentelemetry-python/

.. code:: python

    from opentelemetry import metrics
    from opentelemetry.extension.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

    # Resource can be required for some backends, e.g. Jaeger
    # If resource wouldn't be set - traces wouldn't appears in Jaeger
    resource = Resource(attributes={
        "service.name": "service"
    })

    metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter())
    provider = MeterProvider(resource=resource, metric_readers=[metric_reader])

    metrics.set_meter_provider(provider)

API
---
"""
