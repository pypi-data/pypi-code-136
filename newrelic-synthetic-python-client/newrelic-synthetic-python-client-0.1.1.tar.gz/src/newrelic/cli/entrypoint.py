import sys
import json
from typing import Callable, Sequence

from newrelic.utils.log import log
from newrelic.nerdgraph.client import NerdGraphClient, NerdGraphConfig
from newrelic.synthetic import Synthetic
import newrelic.cli.args as newrelic_cli
import newrelic.utils.config as config

modules = {
        "synthetic": Synthetic
    }


def do_action(func: Callable, args: newrelic_cli.Arguments = None):
    return func() if args is None else func(**args.to_dict())


def main(cmd: Sequence[str] = sys.argv):
    assert len(cmd) >= 4, (
        "Command argument not sufficient.\n"
        "Command format:\n"
        "PROG MODULE SUBMODULE ACTION [ARGUMENTS]"
        )

    module_name = cmd[1]
    log.debug(f"{module_name=}")
    assert module_name in modules.keys(), f"{module_name} is not supported"

    module = modules[module_name](
        client=NerdGraphClient(
            config=NerdGraphConfig.from_json_file(
                filepath=config.get_json_file()
                )
            )
        )
    log.debug(f"{module=}")

    submodule_name = cmd[2]
    log.debug(f"{submodule_name=}")
    submodule = getattr(module, submodule_name, None)
    assert submodule is not None, (
        f"{submodule_name} not supported in {module_name}"
    )
    log.debug(f"{submodule=}")

    action_name = cmd[3]
    log.debug(f"{action_name=}")
    action = getattr(submodule, action_name, None)
    assert action is not None, (
        f"{action_name} is not support in {module_name}:{submodule_name}"
    )
    log.debug(f"{action=}")

    args_parser = getattr(newrelic_cli, f"parse_{submodule_name}_args", None)
    log.debug(f"{args_parser=}")

    action_args = cmd[4:]
    log.debug(f"{action_args=}")

    args = args_parser(action_args) if action_args else None

    log.debug(f"{args=}")

    result = do_action(action, args)
    print(json.dumps(result, indent=4))
