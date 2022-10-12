import abc
import logging
from dataclasses import dataclass


__all__: list = []


logger = logging.getLogger(__name__)


@dataclass
class BaseMessage(metaclass=abc.ABCMeta):
    """Base message."""

    pass
