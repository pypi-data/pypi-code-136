from abc import abstractmethod
from copy import deepcopy
from dataclasses import dataclass
from typing import Dict
from beam.types import TypeSerializer, Types


class BaseConfigClass:
    def to_dict(self):
        config = deepcopy(self)
        return config.__dict__

class BaseTriggerConfigClass(BaseConfigClass):
    inputs: Dict[str, TypeSerializer]
    outputs: Dict[str, TypeSerializer]
    handler: str
    trigger_type: str

    def to_dict(self):
        config = deepcopy(self)

        if hasattr(config, "inputs"):
            config.inputs = Types.dump_schema(config.inputs)

        if hasattr(config, "outputs"):
            config.outputs = Types.dump_schema(config.outputs)

        return config.__dict__


class BaseConfigurationLoader:
    config: BaseConfigClass

    def dumps(self):
        return self.config.to_dict()


class AbstractDataLoader:
    @abstractmethod
    def dumps(self):
        pass

    @abstractmethod
    def from_config(self):
        pass
