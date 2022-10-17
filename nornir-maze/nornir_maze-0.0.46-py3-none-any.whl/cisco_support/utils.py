#!/usr/bin/env python3
"""
This module contains general functions and tasks related to the Cisco Support APIs with Nornir.

The functions are ordered as followed:
- Helper Functions
"""


import argparse
from nornir_maze.utils import (
    print_task_name,
    task_info,
    CustomArgParse,
    CustomArgParseWidthFormatter,
)


#### Helper Functions ########################################################################################


def init_args(argparse_prog_name):
    """
    This function initialze all arguments which are needed for further script execution. The default arguments
    will be supressed. Returned will be a tuple with a use_nornir variable which is a boolian to indicate if
    Nornir should be used for dynamically information gathering or not.
    """
    task_text = "ARGPARSE verify arguments"
    print_task_name(text=task_text)

    # Define the arguments which needs to be given to the script execution
    argparser = CustomArgParse(
        prog=argparse_prog_name,
        description="Gather information dynamically with Nornir or use static provided information",
        epilog="Only one of the mandatory arguments can be specified.",
        argument_default=argparse.SUPPRESS,
        formatter_class=CustomArgParseWidthFormatter,
    )

    # Create a mutually exclusive group.
    # Argparse will make sure that only one of the arguments in the group is present on the command line
    arg_group = argparser.add_mutually_exclusive_group(required=True)

    # Add arg_group exclusive group parser arguments
    arg_group.add_argument(
        "--tag", type=str, metavar="<VALUE>", help="nornir inventory filter on a single tag"
    )
    arg_group.add_argument(
        "--hosts", type=str, metavar="<VALUE>", help="nornir inventory filter on comma seperated hosts"
    )
    arg_group.add_argument(
        "--serials", type=str, metavar="<VALUE>", help="comma seperated list of serial numbers"
    )
    arg_group.add_argument("--excel", type=str, metavar="<VALUE>", help="excel file with serial numbers")

    # Add the optional client_key argument that is only needed if Nornir is not used
    argparser.add_argument(
        "--api_key", type=str, metavar="<VALUE>", help="specify Cisco support API client key"
    )
    # Add the optional client_key argument that is only needed if Nornir is not used
    argparser.add_argument(
        "--api_secret", type=str, metavar="<VALUE>", help="specify Cisco support API client secret"
    )
    # Add the optional tss argument
    argparser.add_argument(
        "--tss", type=str, default=False, metavar="<VALUE>", help="add a IBM TSS Excel report file"
    )
    # Add the optional verbose argument
    argparser.add_argument(
        "-r", "--report", action="store_true", default=False, help="create and Excel report file"
    )
    # Add the optional verbose argument
    argparser.add_argument(
        "-v", "--verbose", action="store_true", default=False, help="show extensive result details"
    )

    # Verify the provided arguments and print the custom argparse error message in case of an error
    args = argparser.parse_args()

    # Verify that --api_key and --api_secret is present when --serials or --excel is used
    if ("serials" in vars(args) or "excel" in vars(args)) and (
        "api_key" not in vars(args) or "api_secret" not in vars(args)
    ):
        # Raise an ArgParse error if --api_key or --api_secret is missing
        argparser.error("The --api_key and --api_secret argument is required for static provided data")

    print(task_info(text=task_text, changed=False))
    print(f"'{task_text}' -> ArgparseResponse <Success: True>\n")

    if hasattr(args, "tag") or hasattr(args, "hosts"):
        print("-> Gather data dynamically with Nornir")
        use_nornir = True
    else:
        print("-> Use static provided data")
        use_nornir = False

    return (use_nornir, args)
