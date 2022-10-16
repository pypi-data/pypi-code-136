import os
from datetime import datetime, date
from typing import Union

import pendulum
from dotenv import load_dotenv

from easy_pysi.plugin import Plugin

SupportedTypes = Union[str, int, float, bool, datetime, date]  # TODO: Bad typing
# TODO: dict and list


class ConfigurationPlugin(Plugin):
    def init(self, app):
        super().init(app)
        load_dotenv(app.dotenv_path)


def config(key: str, type: SupportedTypes = str, default=None, raise_if_not_found=False):
    raw = os.getenv(key)

    if raw is None and raise_if_not_found:
        raise ConfigNotFoundError(f'Config {key} not found')
    elif raw is None:
        return default

    if type == str:
        return raw
    elif type == int:
        return int(raw)
    elif type == float:
        return float(raw)
    elif type == bool:
        return raw.lower() == 'true' or raw == '1'
    elif type == datetime:
        return pendulum.parse(raw)
    elif type == date:
        return pendulum.parse(raw).date()
    else:
        raise TypeNotSupportedError(f'Type {type} is not supported for configuration')


class ConfigNotFoundError(Exception):
    pass


class TypeNotSupportedError(Exception):
    pass
