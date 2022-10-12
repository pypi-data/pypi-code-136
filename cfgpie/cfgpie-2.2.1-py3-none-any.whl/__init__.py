# -*- coding: UTF-8 -*-

from .constants import INSTANCES
from .handlers import CfgParser


def get_config(**kwargs):
    name: str = f"{kwargs.pop('instance', 'default')}.{CfgParser.__name__}"

    if name not in INSTANCES:

        instance: CfgParser = CfgParser(**kwargs)
        INSTANCES[name] = instance

    return INSTANCES[name]


__all__ = ["CfgParser", "get_config"]
