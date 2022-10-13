from __future__ import annotations

import abc

from typing import Iterator


class BusInterface(metaclass=abc.ABCMeta):

    @classmethod
    @abc.abstractmethod
    def open(cls, connection_string: str) -> BusInterface:
        raise NotImplementedError()

    @abc.abstractmethod
    def read_json_messages(self, queue_name: str = None) -> Iterator[dict]:
        raise NotImplementedError()

    @abc.abstractmethod
    def send_json_message(self, data: dict, queue_name: str = None):
        raise NotImplementedError()


__all__ = ("BusInterface", )
