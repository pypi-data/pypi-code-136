from typing import Callable

from poetry_aliases_plugin import config


default_aliases = {'this': 'poetry run python -m this'}


class PluginException(RuntimeError):
    def __str__(self) -> str:
        return f'{config.PLUGIN_NAME}: {super().__str__()}'


def plugin_exception_wrapper(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except PluginException as ex:
            raise ex

        except BaseException as ex:
            raise PluginException(ex) from ex

    return wrapper
