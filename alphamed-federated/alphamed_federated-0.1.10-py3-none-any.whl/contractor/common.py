"""Common components for contracts."""

import base64
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field, fields
from typing import Optional

from requests import Response

__all__ = [
    'ContractException',
    'Contractor',
    'ContractEvent'
]


class ContractException(Exception):
    ...


class Contractor(ABC):

    _URL = None

    _HEADERS = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }

    EVERYONE = ['*']

    @abstractmethod
    def _validate_response(self, resp: Response) -> None:
        """Validate response. Should only focus on problems unrelated to business logic."""
        ...


@dataclass
class ContractEvent(ABC):
    """合约事件."""

    TYPE = None

    type: str = field(init=False)

    def __post_init__(self):
        self.type = self.TYPE

    @classmethod
    @abstractmethod
    def contract_to_event(cls, contract: dict) -> 'ContractEvent':
        ...

    def event_to_contract(self) -> dict:
        dict_obj = asdict(self)
        for _key, _value in dict_obj.items():
            if isinstance(_value, bytes):
                dict_obj[_key] = base64.b64encode(_value).decode()
        return dict_obj

    def validate(self) -> None:
        """To validate event data and raise errors if failed."""
        for _field in fields(self):
            _name = _field.name
            _type = _field.type
            _default = _field.default
            _value = self.__getattribute__(_name)
            if _type.__module__ == 'typing':
                if _default is None:
                    assert (
                        _value is None or isinstance(_value, _type.__origin__)
                    ), f'invalid {_name} value: {_value}'
                else:
                    assert (
                        _value is not None and isinstance(_value, _type.__origin__)
                    ), f'invalid {_name} value: {_value}'
            else:
                if _default is None:
                    assert (
                        _value is None or isinstance(_value, _type)
                    ), f'invalid {_name} value: {_value}'
                else:
                    assert (
                        _value is not None and isinstance(_value, _type)
                    ), f'invalid {_name} value: {_value}'


class ContractEventFactory(ABC):
    """A factory to convert contract text to a ContractEvent object."""

    @classmethod
    @abstractmethod
    def contract_to_event(cls, contract: dict) -> Optional[ContractEvent]:
        """Decode contract data into event objects and handle errors."""
        ...
