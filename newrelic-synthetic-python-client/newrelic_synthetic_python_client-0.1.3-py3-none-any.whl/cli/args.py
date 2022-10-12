from dataclasses import dataclass
import pathlib
from typing import Sequence, Dict
import argparse
import abc

from newrelic.utils.log import log


class Arguments(abc.ABC):
    @abc.abstractmethod
    def to_dict(self) -> Dict:
        pass


@dataclass
class ScriptedBrowserArguments(Arguments):
    """
    Arguments class for the program.
    """

    monitor_name: str = ""
    status: str = "ENABLED"
    locations: str = "US_WEST_2,AP_NORTHEAST_1"
    period: str = "EVERY_15_MINUTES"
    enable_screenshot: bool = True
    script_content: str = 'const SCRIPT_NAME'

    def to_dict(self) -> Dict:
        script_content = self.script_content
        assume_file = pathlib.Path(self.script_content)
        if assume_file.exists():
            log.info("script content is in a file, reading its content")
            script_content = (
                f"{repr(assume_file.read_text())}"
                ).replace('"', '\\"').strip("'")

        bool_maps = {
            True: "true",
            False: "false"
        }
        return {
            "monitor_name": self.monitor_name,
            "status": self.status.upper(),
            "locations": self.locations.split(",") if self.locations else [],
            "period": self.period.upper(),
            "enable_screenshot": bool_maps[self.enable_screenshot],
            "script_content": script_content
        }


def parse_scripted_browser_args(
    command: Sequence[str]
) -> ScriptedBrowserArguments:
    parser = argparse.ArgumentParser(
        description="newrelic client",
    )
    args = ScriptedBrowserArguments()
    parser.add_argument(
        "--monitor-name",
        type=str,
        required=True,
        help="The Synthetic monitor name"
    )
    parser.add_argument(
        "--status",
        type=str,
        default=args.status,
        choices=["enabled", "disabled", "muted"],
        help="Specify the monitor status",
    )
    parser.add_argument(
        "--locations",
        type=str,
        default=args.locations,
        help="Specify the monitor locations, comma separated for multi values",
    )
    parser.add_argument(
        "--period",
        type=str,
        default=args.period,
        help="Specify the monitor period",
    )
    parser.add_argument(
        "--enable-screenshot",
        action="store_true",
        default=args.enable_screenshot,
        help="Whether take screenshot when failure",
    )
    parser.add_argument(
        "--script-content",
        type=str,
        default=args.script_content,
        help="The script content or file path",
    )
    parser.parse_args(args=command, namespace=args)
    return _post_scripted_browser_args_hook(args)


def _post_scripted_browser_args_hook(
    args: ScriptedBrowserArguments
) -> ScriptedBrowserArguments:
    """
    Extra validations for the arguments.
    """
    return args


@dataclass
class SecureCredentialArguments(Arguments):
    key: str = ""
    value: str = ""
    description: str = "NR PYTHON CLIENT AUTO GENERATED"

    def to_dict(self) -> Dict:
        return {
            "key": self.key,
            "value": self.value,
            "description": self.description
        }


def parse_secure_credential_args(
    command: Sequence[str]
) -> SecureCredentialArguments:
    parser = argparse.ArgumentParser(
        description="newrelic client",
    )
    args = SecureCredentialArguments()
    parser.add_argument(
        "--key", type=str, required=True,
        help="The Synthetic secure credential key"
    )
    parser.add_argument(
        "--value", type=str,
        help="The Synthetic secure credential value"
    )
    parser.add_argument(
        "--description", type=str,
        default=args.description,
        help="The Synthetic secure credential description"
    )
    parser.parse_args(args=command, namespace=args)
    return _post_secure_credential_args_hook(args)


def _post_secure_credential_args_hook(
    args: SecureCredentialArguments
) -> SecureCredentialArguments:
    """
    Extra validations for the arguments.
    """
    return args
