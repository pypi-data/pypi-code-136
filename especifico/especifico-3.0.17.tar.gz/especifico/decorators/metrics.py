"""
This module defines view function decorator to collect UWSGI metrics and expose them via an
endpoint.
"""

import functools
import os
import time

from werkzeug.exceptions import HTTPException

from especifico.exceptions import ProblemException

try:
    import uwsgi_metrics

    HAS_UWSGI_METRICS = True  # pragma: no cover
except ImportError:
    uwsgi_metrics = None
    HAS_UWSGI_METRICS = False


class UWSGIMetricsCollector:
    def __init__(self, path, method):
        self.path = path
        self.method = method
        swagger_path = path.strip("/").replace("/", ".").replace("<", "{").replace(">", "}")
        self.key_suffix = f"{method.upper()}.{swagger_path}"
        self.prefix = os.getenv("HTTP_METRICS_PREFIX", "especifico.response")

    @staticmethod
    def is_available():
        return HAS_UWSGI_METRICS

    def __call__(self, function):
        """
        :type function: types.FunctionType
        :rtype: types.FunctionType
        """

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            status = 500
            start_time_s = time.time()
            try:
                response = function(*args, **kwargs)
                status = response.status_code
            except HTTPException as http_e:
                status = http_e.code
                raise http_e
            except ProblemException as prob_e:
                status = prob_e.status
                raise prob_e
            finally:
                end_time_s = time.time()
                delta_s = end_time_s - start_time_s
                delta_ms = delta_s * 1000
                key = f"{status}.{self.key_suffix}"
                uwsgi_metrics.timer(self.prefix, key, delta_ms)
            return response

        return wrapper
