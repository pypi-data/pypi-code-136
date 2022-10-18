# General imports
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Optional, Callable, Any
from pathlib import Path

# Project imports
from .alpha import get_schema as alpha_schema


@dataclass(frozen=True, order=True)
class Configuration:
    file_path: Path
    data: Any


@dataclass(frozen=True, order=True)
class ProfileComposition:
    """
    Indicates how to compose different base profiles together, e.g:
    - work: a composition of core + work profiles
    - personal: a composition of core + dev + personal profiles
    """
    name: str
    profiles: list[str]


class ErrorReason(Enum):
    """
    Represents a particular reason why
    the validation of a given dotfiles,
    module, or file failed
    """

    # Loading errors
    UNSUPPORTED_CONFIG_FILE_TYPE = auto()
    PARSING_ERROR_YAML = auto()

    INVALID_TARGET = auto()

    INVALID_EMPTY_FILE = auto()
    INVALID_SYNTAX = auto()
    INVALID_SCHEMA = auto()

    # Specific schema issues
    INVALID_DATA = auto()
    INVALID_SCHEMA_VERSION = auto()
    INVALID_SCHEMA_TYPE = auto()

    @staticmethod
    def get_help_message(reason):
        help_message_map = {
            ErrorReason.INVALID_EMPTY_FILE: "An empty invalid configuration file was detected",
            ErrorReason.INVALID_SCHEMA: "A given configuration file contains an invalid schema"
        }
        return help_message_map.get(reason)


class PydotfilesError(Exception):

    def __init__(self, reason: ErrorReason, help_message_override: Optional[str] = None, context_map: Optional[Dict] = None):
        super().__init__()
        self.reason = reason
        self.help_message_override = help_message_override
        if context_map is None:
            context_map = {
                "help": "If you need additional context like a stack trace, please run in verbose mode (with the -v flag)"
            }
        self.context_map = context_map

    @property
    def help_message(self):
        undecorated_original_help_message = ErrorReason.get_help_message(self.reason) if self.help_message_override is None else self.help_message_override

        if len(self.context_map) == 0:
            serialized_context_decoration = ""
        else:
            serialized_context_decoration = '\n'.join([f"\t{context_type}: {context_reason}" for context_type, context_reason in self.context_map.items()])

        decorated_error_message = f"{undecorated_original_help_message} [\n{serialized_context_decoration}\n]"
        return decorated_error_message

    @staticmethod
    def due_to_yaml_error() -> 'PydotfilesError':
        return PydotfilesError(ErrorReason.PARSING_ERROR_YAML, "Loader: An invalid YAML syntax error was detected")

    @staticmethod
    def due_to_unsupported_config_filetype() -> 'PydotfilesError':
        return PydotfilesError(ErrorReason.UNSUPPORTED_CONFIG_FILE_TYPE, "Loader: An invalid config filetype could not be parsed (are you using .json or .yaml)?")


def get_configuration_version(version: str, schema: str) -> type:
    configuration_map: Dict[str, Callable] = {
        "alpha": alpha_schema,
    }

    return configuration_map.get(version)(schema)
