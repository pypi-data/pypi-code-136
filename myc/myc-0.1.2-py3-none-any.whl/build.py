import functools


is_building = [False]
""" True if the application is invoked while building the app. """


class EndpointInvokedDuringBuildError(Exception):
    def __init__(self, fn):
        self._fn = fn

    @property
    def function(self):
        return self._fn


def create_build_function_wrapper(fn):
    """
    Creates a wrapper for endpoints that protects them from being invoked
    during the build process.
    """
    @functools.wraps(fn)
    def wrapper(*_args, **_kwargs):
        raise EndpointInvokedDuringBuildError(fn)

    return wrapper
