import os
import time


def is_testing():
    """ Returns True if the binary is running inside a Kubernetes cluster."""
    return os.environ.get("PYTEST_CURRENT_TEST") is not None


def current_time_ms():
    """ Returns the current time in milliseconds since EPOCH """
    return time.time_ns() // 1_000_000
