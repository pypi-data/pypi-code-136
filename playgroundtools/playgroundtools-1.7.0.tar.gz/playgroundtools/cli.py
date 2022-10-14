from argparse import ArgumentParser

from . import APP_NAME, DESCRIPTION
from .commands import config, delete, new, print_about, print_version, run
from .exceptions import status_manager


def main():
    """The main launch point for the CLI."""
    parser = get_parser()
    args = parser.parse_args()

    if args.about:
        print_about()
    elif args.version:
        print_version()
    elif args.command:
        with status_manager(args):
            args.func(args)
    else:
        parser.print_usage()


def get_parser():
    """Set up an argument parser with commands."""
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "-a",
        "--about",
        action="store_true",
        help=f"Show information about {APP_NAME}.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help=f"Show the installed version of {APP_NAME}.",
    )

    subcommands = parser.add_subparsers(
        title="Commands",
        dest="command",
        description="Commands for managing playgrounds.",
    )

    new_cmd = subcommands.add_parser("new", help="Create a new playground.")
    new_cmd.add_argument("type", help="The type of playground to create.")
    new_cmd.add_argument(
        "-i",
        "--include",
        dest="lib",
        nargs="+",
        default=[],
        help="The packages to be installed via pip upon creation.",
    )
    new_cmd.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Set the verbosity level.",
    )
    new_cmd.add_argument(
        "-n",
        "--name",
        required=True,
        help="The name of the playground to create.",
    )
    new_cmd.set_defaults(func=new)

    delete_cmd = subcommands.add_parser("delete", help="Delete a playground.")
    delete_cmd.add_argument(
        "name", help="The name of the playground to delete."
    )
    delete_cmd.set_defaults(func=delete)

    run_cmd = subcommands.add_parser(
        "run",
        help="Run a playground by running the commands in its settings file.",
    )
    run_cmd.add_argument("name", help="The name of the playground to run.")
    run_cmd.add_argument(
        "-m", "--module", help="Override the default module to run."
    )
    run_cmd.add_argument(
        "-a",
        "--args",
        nargs="+",
        default=[],
        help="Override the arguments to run the module with.",
    )
    run_cmd.set_defaults(func=run)

    config_cmd = subcommands.add_parser(
        "config", help="Read or modify the configuration."
    )
    config_subcommands = config_cmd.add_subparsers(
        title="Commands",
        dest="subcommand",
        help=f"Commands for working with the configuration of {APP_NAME}.",
    )

    config_add_cmd = config_subcommands.add_parser(
        "add", help="Add a playground type to the config file."
    )
    config_add_cmd.add_argument(
        "-t", "--type", help="The name of the new type."
    )
    config_add_cmd.add_argument(
        "-v", "--value", help="The value assigned to the new type (in JSON)"
    )
    config_add_cmd.add_argument(
        "-f", "--file", help="Add options from a custom configuration file."
    )

    config_delete_cmd = config_subcommands.add_parser(
        "delete", help="Delete a playground type from the config file."
    )
    config_delete_cmd.add_argument(
        "-k",
        "--key",
        help="The key to delete (can be a type or in the form {type}.{key}).",
    )
    config_delete_cmd.add_argument(
        "-f",
        "--file",
        help="Delete options specified in a custom configuration file.",
    )

    config_edit_cmd = config_subcommands.add_parser(
        "edit", help="Edit an option for an existing playground type."
    )
    config_edit_cmd.add_argument(
        "key",
        help="The key in the configuration to modify (i.e. {type}.{key}).",
    )
    config_edit_cmd.add_argument(
        "value", help="The value to change the key to (in JSON)"
    )

    config_cmd.add_argument(
        "-k",
        "--key",
        dest="read",
        help="The config key to inspect. (i.e. {type}.{key})",
    )
    config_cmd.set_defaults(func=config)

    return parser
