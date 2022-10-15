# General imports
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class Action(Enum):
    copy = "copy"
    symlink = "symlink"
    script = "script"


@dataclass(frozen=True, order=True)
class ActionType:
    action: Action
    files: Dict[str, str]
    hidden: bool
    sudo: bool
    absolute: bool

    @staticmethod
    def from_dict(data: list[Dict]) -> list['ActionType']:
        return [ActionType.from_action_dict(datum) for datum in data]

    @staticmethod
    def from_action_dict(data: Dict) -> 'ActionType':
        return ActionType(
            action=Action[data.get("action")],
            files=data.get("files"),
            hidden=False if data.get("hidden") is None else data.get("hidden"),
            sudo=False if data.get("sudo") is None else data.get("sudo"),
            absolute=False if data.get("absolute") is None else data.get("absolute"),
        )

    def to_dict(self):
        return {
            'action': self.action.value,
            'files': self.files,
            'hidden': self.hidden,
            'sudo': self.sudo,
            'absolute': self.absolute,
        }
