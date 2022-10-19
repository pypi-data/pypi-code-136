#!/usr/bin/env python3

import os
import argparse
from commands import available_commands

from meta_util import PersistentState, check_for_updates
from commands.utils import Device


def main():

    persistent_state = PersistentState()
    check_for_updates(persistent_state)

    config = {
        "device_address": os.getenv('AUTERION_DEVICE_ADDRESS', "10.41.1.1")
    }
    commands = available_commands(config)

    main_parser = argparse.ArgumentParser()
    command_subparsers = main_parser.add_subparsers(title="command", metavar='<command>', dest="_root_command", required=True)

    for name, command in commands.items():
        parser = command_subparsers.add_parser(name, help=command.help())
        command.setup_parser(parser)

    args = main_parser.parse_args()
    commands[args._root_command].run(args)

    persistent_state.persist()


if __name__ == "__main__":
    main()
