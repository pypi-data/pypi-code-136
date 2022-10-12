# Python imports
import json
import functools
import logging

# imports from this project
from .utils import StepwiseJSONEncoder, masked_dict

# module initializations
logger = logging.getLogger(__name__)


def app_logger(func):
    """
    Decorate a function to add an entry to the app log with the function name,
    its positional arguments, and keyword pairs presented as a formatted dict.

    sample output:
        2022-10-07 19:45:26,869 INFO app_logger: registration.views.EmailVerificationView().get() ["<WSGIRequest: GET '/verify-email/MjY1/bcxw75-69581da3ea4f0cefad2f0f2205354117/'>"] keyword args: {
            "uid": "MjY1",
            "token": "*** -- REDACTED -- ***"
        }
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name_of_def = func.__name__
        logged_args = args
        kwargs_dict_repr = ""

        # try initializing variables assuming that we were called by a class method
        try:
            cls = args[0].__class__
            name_of_class = cls.__name__ + "()."
            name_of_module = cls.__module__
            # slice off the 'self' positional argument
            logged_args = args[1:]
        except Exception:
            # We weren't called by a class method. Fall back to initializing variables for
            # a standard module function.
            name_of_class = ""
            name_of_module = func.__module__

        positional_args = [repr(a) for a in logged_args]

        if len(kwargs.keys()) > 0:
            kwargs_dict_repr = "keyword args: "
            kwargs_dict_repr += json.dumps(masked_dict(kwargs), cls=StepwiseJSONEncoder, indent=4)

        logger.info(
            "app_logger: {name_of_module}.{name_of_class}{name_of_def}() {args} {kwargs}".format(
                name_of_module=name_of_module,
                name_of_class=name_of_class,
                name_of_def=name_of_def,
                args=positional_args if len(positional_args) > 0 else "",
                kwargs=kwargs_dict_repr,
            )
        )
        return func(*args, **kwargs)

    return wrapper
