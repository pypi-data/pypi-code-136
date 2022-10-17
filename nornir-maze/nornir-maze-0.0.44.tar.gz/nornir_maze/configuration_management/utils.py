#!/usr/bin/env python3
"""
This module contains general configuration management functions and tasks related to Nornir.

The functions are ordered as followed:
- Helper Functions
- Nornir print functions
- Nornir Helper Tasks
"""

import re
import argparse
from nornir_jinja2.plugins.tasks import template_file
from nornir.core.task import Result
from nornir_maze.utils import (
    print_task_name,
    task_info,
    task_error,
    CustomArgParse,
    CustomArgParseWidthFormatter,
)


#### Helper Functions ########################################################################################


def index_of_first_number(string):
    """
    Return the index of the first number in a string
    """
    # pylint: disable=invalid-name
    for i, c in enumerate(string):
        if c.isdigit():
            index = i
            break

    return index


def extract_interface_number(string):
    """
    Removes the interface name and returns only the interface number
    """
    try:
        index = index_of_first_number(string)
        interface_number = string[index:]

    except UnboundLocalError:
        interface_number = string

    return interface_number


def extract_interface_name(string):
    """
    Removes the interface number and returns only the interface name
    """
    try:
        index = index_of_first_number(string)
        interface_name = string[:index]

    except UnboundLocalError:
        interface_name = string

    return interface_name


def complete_interface_name(interface_string):
    """
    This function takes a string with an interface name only or a full interface with its number and returns
    the full interface name but without the number:
    Gi -> GigabitEthernet
    Tw -> TwentyFiveGigE
    etc.
    """
    # pylint: disable=no-else-return, unidiomatic-typecheck

    error_msg = "Variable interface_string"

    if type(interface_string) is str:
        # Extract the interface name / delete the interface number
        interface_name = extract_interface_name(interface_string)
        # Define the name of the interface
        if interface_name.startswith("Eth"):
            interface_name = "Ethernet"
        elif interface_name.startswith("Fa"):
            interface_name = "FastEthernet"
        elif interface_name.startswith("Gi"):
            interface_name = "GigabitEthernet"
        elif interface_name.startswith("Te"):
            interface_name = "TenGigabitEthernet"
        elif interface_name.startswith("Tw"):
            interface_name = "TwentyFiveGigE"
        elif interface_name.startswith("Hu"):
            interface_name = "HundredGigE"
        else:
            raise ValueError(f"{error_msg} value is not a known interface name")

        return interface_name

    else:
        raise TypeError(f"{error_msg} is not a type string")


def create_single_interface_list(interface_list):
    """
    This function takes a list of interfaces that are like the cisco interface range command and makes a list
    of full interface names for each interface:
    Gi1/0/1 -> GigabitEthernet1/0/1
    Gi1/0/1 - 10 -> GigabitEthernet1/0/1, GigabitEthernet1/0/2, etc.
    Gi1/0/1 - Gi1/0/10 -> GigabitEthernet1/0/1, GigabitEthernet1/0/2, etc.
    """
    # Define a list to return at the end of the function
    single_interface_list = []

    # Create the full interface name
    for interface in interface_list:
        # Create the full name of the interface, eg. Gi -> GigabitEthernet
        interface_name = complete_interface_name(interface)

        # If the list element is a interface range fullfil every single interface
        if "-" in interface:
            # Create a list with the two interfaces for the range
            interface_range = interface.replace(" ", "")
            interface_range = interface.split("-")

            # Regex pattern to match only the last number after the /
            pattern = r"(\d+)(?!.*\d)"

            # 1. Match the interface number prefix without the last number
            interface_prefix = extract_interface_number(interface_range[0])
            interface_prefix = re.sub(pattern, "", interface_prefix)

            # 2. Match the number after the last / in the interface number
            last_interface_numbers = []
            for interface in interface_range:
                # Extract only the interface number
                interface_number = extract_interface_number(interface)
                last_interface_number = re.findall(pattern, interface_number)
                last_interface_numbers.append(last_interface_number[0])

            # Define integers for the first and the last number of the range
            range_first_number = int(last_interface_numbers[0])
            range_last_number = int(last_interface_numbers[1])
            # Iterate over the range and construct each single interface
            while range_first_number <= range_last_number:
                single_interface = interface_name + interface_prefix + str(range_first_number)
                single_interface = single_interface.replace(" ", "")
                single_interface_list.append(single_interface)
                range_first_number += 1

        # If the list element is a single interface add it to the list to return
        else:
            interface_number = extract_interface_number(interface)
            single_interface = interface_name + interface_number
            single_interface_list.append(single_interface)

    return single_interface_list


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
        description="Filter the Nornir inventory based on a tag or a host",
        epilog="Only one of the mandatory arguments can be specified.",
        argument_default=argparse.SUPPRESS,
        formatter_class=CustomArgParseWidthFormatter,
    )

    # Create a mutually exclusive group. Argparse will make sure that only one of the arguments in the group
    # was present on the command line
    arg_group = argparser.add_mutually_exclusive_group(required=True)

    # Add arg_group parser arguments
    arg_group.add_argument(
        "--tag", type=str, metavar="<TAG>", help="inventory filter for a single Nornir tag"
    )
    arg_group.add_argument(
        "--hosts", type=str, metavar="<HOST-NAMES>", help="inventory filter for comma seperated Nornir hosts"
    )

    # Add the optional verbose argument
    argparser.add_argument(
        "-v", "--verbose", action="store_true", default=False, help="show extensive result details"
    )

    # Add the optional rebuild argument
    argparser.add_argument(
        "-r",
        "--rebuild",
        action="store_true",
        default=False,
        help="rebuild the config from day0 (default: golden-config)",
    )

    # Verify the provided arguments and print the custom argparse error message in case any error or wrong
    # arguments are present and exit the script
    args = argparser.parse_args()

    # If argparser.parse_args() is successful -> no argparse error message
    print(task_info(text=task_text, changed=False))
    print(f"'{task_text}' -> ArgparseResponse <Success: True>")
    if args.verbose:
        print(f"\n{args}")

    return args


#### Nornir Helper Tasks #####################################################################################


def create_tpl_int_list(task):
    """
    This function loops over all host inventory keys and append the key which start with tpl_int to the list
    of interface groups and returns a Nornir AggregatedResult Object
    """
    tpl_int_list = []
    for key in task.host.keys():
        if key.startswith("tpl_int"):
            tpl_int_list.append(key)

    return tpl_int_list


def template_file_custom(task, task_msg, path, template):
    """
    This custom Nornir task generates a configuration from a Jinja2 template based on a path and a template
    filename. The path and the template filename needs to be Nornir inventory keys which holds the needed
    information as value.
    """
    try:
        path = task.host[path]
        template = task.host[template]

    except KeyError as error:
        # Jinja2 Nornir inventory key not found. Key which specify the path and the file don't exist
        error_msg = (
            f"{task_error(text=task_msg, changed=False)}\n"
            + f"'nornir.core.inventory.Host object' has no attribute {error}"
        )

        # Return the Nornir result as error -> interface can not be configured
        return Result(host=task.host, result=error_msg, failed=True)

    # Run the Nornir Task template_file
    j2_tpl_result = task.run(task=template_file, template=template, path=path, on_failed=True)

    return Result(host=task.host, result=j2_tpl_result)


#### Nornir Helper tasks in regular Function #################################################################
