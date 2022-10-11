#!/usr/bin/env python3
"""
This module contains general functions and tasks related to Nornir.

The functions are ordered as followed:
- Helper Functions
- Nornir print functions
- Nornir Helper Tasks
"""

import os
import sys
import argparse
import json
import hashlib
from datetime import datetime
from pyfiglet import figlet_format
from nornir.core.filter import F
from nornir_salt.plugins.functions import FFun


#### Helper Functions ########################################################################################


class CustomArgParse(argparse.ArgumentParser):
    """
    This class takes the argparse.ArgumentParser function as a superclass and overwrites the argparse error
    function. Every time that argparse calls the error function the following error function will be executed.
    """

    def error(self, message):
        """
        This function overwrites the standard argparse error function
        """
        print(task_error(text="ARGPARSE verify arguments", changed="False"))
        print("'ARGPARSE verify arguments' -> ArgparseResponse <Success: False>\n")
        print(f"error: {message}\n")
        self.print_help()
        print("\n")
        sys.exit(1)


class CustomArgParseWidthFormatter(argparse.RawTextHelpFormatter):
    """
    This class can be specified as formatter_class argument in argparse.ArgumentParser. This solution is
    preferred as formatter_class argument expects to use a class, not a class instance.
    """

    def __init__(self, prog) -> None:
        super().__init__(prog, width=100)


def construct_filename_with_current_date(filename):
    """
    Construct the new path and filename from the filename argument string variable. The filename string can
    contain as much subfolder as needed. The filename must have a date at the end in the formart _dd-mm-yyyy,
    _yyyy-mm-dd, _dd_mm_yyyy or _yyyy_mm_dd which are 11 characters that will be sliced away and the current
    date will be added. The function returns the new constructed filename.
    """
    # Get the current date in the format YYYY-mm-dd
    date_today = datetime.today().date()

    # Create some variables to construct the destination path and filename
    # Get the path and the filename from file variable string
    path, filename = os.path.split(filename)

    # Create the path folder if it don't exists
    if not os.path.exists(path):
        os.makedirs(path)

    # Get the filename and the extension from the filename variable
    filename, file_extension = os.path.splitext(filename)

    # Slice the date away from the filename
    # Works for various date combinations _dd-mm-yyyy or _yyyy-mm-dd or _dd_mm_yyyy or _yyyy_mm_dd
    # Slicing from the end will ensure that you extract the date no matter what the name is and how long it is
    filename = filename[:-11]

    # Destination filename
    filename = f"{path}/{filename}_{date_today}{file_extension}"

    return filename


def get_pandas_column_width(df):  # pylint: disable=invalid-name
    """
    Helper function to get the width of each pandas dataframe column.
    """
    # Find the maximum length of the index column
    idx_max = max([len(str(s)) for s in df.index.values] + [len(str(df.index.name))])

    # Concatenate this to the max of the lengths of column name and its values for each column, left to right
    return [idx_max] + [max([len(str(s)) for s in df[col].values] + [len(col)]) for col in df.columns]


def list_flatten(original_list):
    """
    This function creates with recursion a flat list from a list of lists and strings or other data types.
    """
    new_list = []
    for item in original_list:
        if isinstance(item, list):
            new_list.extend(list_flatten(item))
        else:
            new_list.append(item)

    return new_list


def compute_md5(file_name):
    """
    This is a helper function which takes a file path as argument and computes a md5 hash which is the return
    of the function.
    """
    hash_md5 = hashlib.md5()  # nosec

    with open(file_name, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def iterate_all(iterable, returned="key"):
    """Returns an iterator that returns all keys or values of a (nested) iterable.
    Arguments:
        - iterable: <list> or <dictionary>
        - returned: <string> "key" or "value" or <tuple of strings> "key-value"
    Returns:
        - <iterator>
    """
    if isinstance(iterable, dict):
        for key, value in iterable.items():
            if returned == "key":
                yield key
            elif returned == "value":
                if not isinstance(value, dict) or isinstance(value, list):
                    yield value
            elif returned == "key-value":
                if not isinstance(value, dict) or isinstance(value, list):
                    yield key, value
            else:
                raise ValueError("'returned' keyword only accepts 'key' or 'value' or 'key-value'.")
            for ret in iterate_all(value, returned=returned):
                yield ret
    elif isinstance(iterable, list):
        for item in iterable:
            for ret in iterate_all(item, returned=returned):
                yield ret


def transform_env(iterable, startswith="env_"):
    """
    This function loops over a nested dictionary and if the key startswith the specific string and the value
    is a string, it loads the environment variable specified by the value and replace the value with the
    environment variable.
    """
    for key, value in iterable.copy().items():
        # If Value == DICT -> Continue with nested dict
        if isinstance(value, dict):
            iterable[key] = transform_env(value, startswith)
        # If Value == LIST -> Replace the value of each list item with the env variable
        elif isinstance(value, list):
            if key.startswith(startswith):
                for index, item in enumerate(value.copy()):
                    iterable[key][index] = os.environ[item]
        # If Value == STR -> Replace the value with the env variable
        elif isinstance(value, str):
            if key.startswith(startswith):
                iterable[key] = os.environ[value]

    return iterable


def nr_transform_default_creds_from_env(nr_obj, verbose=False):
    """
    This function loads the login credentials from environment variables and stores them in the defaults
    """
    # Verify that login credentials are set as environment variables. Raise a KeyError when is None
    task_text = "NORNIR transform credentials env variable"

    try:
        print_task_name(text="NORNIR transform default credentials env variable")

        default_username = nr_obj.inventory.defaults.username
        default_password = nr_obj.inventory.defaults.password

        nr_obj.inventory.defaults.username = os.environ[default_username]
        nr_obj.inventory.defaults.password = os.environ[default_password]

        print(task_info(text=task_text, changed="False"))
        print(f"'Transform env {default_username}' -> OS.EnvironResponse <Success: True>")
        print(f"'Transform env {default_password}' -> OS.EnvironResponse <Success: True>")
        if verbose:
            print(f"\n-> Default username: {nr_obj.inventory.defaults.username}")
            print(f"-> Default password: {nr_obj.inventory.defaults.password}")

    except KeyError as error:
        print(task_error(text=task_text, changed="False"))
        print(f"'Transform env {error}' -> OS.EnvironResponse <Success: False>")
        print(f"\nEnvironment variable {error} not found\n")
        sys.exit(1)

    except TypeError:
        print(task_error(text=task_text, changed="False"))
        print("'Transform default credentials from env variable' -> OS.EnvironResponse <Success: False>")
        print("\nNornir inventory default username or/and password not found\n")
        sys.exit(1)


def nr_transform_inv_from_env(iterable, mandatory=False, verbose=False):
    """
    This function transforms all environment variables in the iterable. It loops over a nested dictionary and
    if the key startswith "env_", it loads the environment variable specified by the value and replace the
    value with the environment variable. Optional a mandatory argument which have to be a dictionary can be
    specified. This dictionary must be part of the iterable and follows the same procedure to transform the
    environment variables. The optional argument verbose prints extensive results. The function returns None.
    """
    # pylint: disable=too-many-branches

    #### Prepare mandatory and non-mandatory env variables ###################################################

    mandatory_transform_env_keys = []
    mandatory_transform_envs = []
    transform_env_keys = []
    transform_envs = []

    # Iterate over all nested dict or list elements and return a generator object
    for env in iterate_all(iterable=mandatory, returned="key-value"):
        if env[0].startswith("env_"):
            mandatory_transform_env_keys.append(env[0])
            mandatory_transform_envs.append(env[1])

    # Iterate over all nested dict or list elements and return a generator object
    for env in iterate_all(iterable=iterable, returned="key-value"):
        if env[0].startswith("env_"):
            transform_env_keys.append(env[0])
            transform_envs.append(env[1])

    # Subtract the non-mandatory env_keys and envs from the mandatory env_keys and envs list
    transform_env_keys = [item for item in transform_env_keys if item not in mandatory_transform_env_keys]
    transform_envs = [item for item in transform_envs if item not in mandatory_transform_envs]

    # Flatten the transform_envs if it contains lists of lists
    transform_envs = list_flatten(transform_envs)

    #### Transform all mandatory env variables ###############################################################

    if mandatory_transform_env_keys:
        task_text = f"NORNIR transform {list(mandatory.keys())[0]} env variable"
        print_task_name(text=task_text)

        if mandatory.items() <= iterable.items():
            try:
                # Loop over the generator object items and add the matching elemens based on the key to a list
                for env_key in mandatory_transform_env_keys:
                    # If the environ load fails a KeyError would be raised
                    transform_env(iterable=iterable, startswith=env_key)

                # Print all transformed envs from the transform_envs list
                print(task_info(text=task_text, changed="False"))
                for env in mandatory_transform_envs:
                    print(f"'Transform env {env}' -> OS.EnvironResponse <Success: True>")
                # If args.verbose is True
                if verbose:
                    print("\n", json.dumps(iterable, sort_keys=False, indent=4))

            except KeyError as error:
                print(task_error(text=task_text, changed="False"))
                print(f"'Transform env {error}' -> OS.EnvironResponse <Success: False>")
                print(f"\nEnvironment variable {error} not found\n")
                sys.exit(1)

        else:
            print(task_error(text=task_text, changed="False"))
            print(f"'Transform {list(mandatory.keys())[0]} env' -> OS.EnvironResponse <Success: False>")
            print("\nMandatory argument dict is not part of defaults.yaml")
            print(json.dumps(iterable, sort_keys=False, indent=4), "\n")
            sys.exit(1)

    #### Transform all other envs if transform_envs is not empty #############################################

    # If the transform_env_keys list it not empty -> Transform all env variables in the list
    if transform_envs:
        task_text = "NORNIR transform env variable"
        print_task_name(text=task_text)

        try:
            # Loop over the generator object items and add the matching elemens based on the key to a list
            for env_key in transform_env_keys:
                # If the environ load fails a KeyError would be raised
                transform_env(iterable=iterable, startswith=env_key)

            # Print all transformed envs from the transform_envs list
            print(task_info(text=task_text, changed="False"))
            for env in transform_envs:
                print(f"'Transform env {env}' -> OS.EnvironResponse <Success: True>")
            # If args.verbose is True
            if verbose:
                print("\n", json.dumps(iterable, sort_keys=False, indent=4))

        except KeyError as error:
            print(task_error(text=task_text, changed="False"))
            print(f"'Transform env {error}' -> OS.EnvironResponse <Success: False>")
            print(f"\nEnvironment variable {error} not found\n")
            sys.exit(1)


def nr_filter_args(nr_obj, args):
    """
    This function filters the Nornir inventory with a tag or a host argument provided by argparse. Prior
    Argparse validation needs to ensure that only one argument is present and that the tag or host argument
    creates a correct inventory filtering will be verified. The new filtered Nornir object will be returned
    or the script terminates with an error message.
    """
    task_text = "NORNIR filter inventory"
    print_task_name(task_text)

    # If the --hosts argument is set, verify that the host exist
    if hasattr(args, "hosts"):
        # Create a list from the comma separated hosts argument
        args_hosts_list = args.hosts.split(",")

        # Use Nornir-Salt FFun Filter-List option to filter on a list of hosts
        nr_obj = FFun(nr_obj, FL=args_hosts_list)

        # Create a list with all filteres Nornir hosts for verification
        nr_hosts_list = list(nr_obj.inventory.hosts.keys())

        # Verify that each host in from the --host argument is part of the filtered Nornir inventory, else
        # the diff host will be in the list
        host_diff_list = [x for x in args_hosts_list if x not in nr_hosts_list]
        if host_diff_list:
            print(task_error(text=task_text, changed="False"))
            print(f"'{task_text} for hosts' -> NornirResponse <Success: False>")
            print("\nHosts not part of the hosts.yaml inventory file")
            for host in host_diff_list:
                print(f"-> {host}")
            print(
                "\n\033[1m\u001b[31m"
                "-> Analyse the Nornir inventory and filter for an existing host\n\n"
                "\033[0m"
            )
            sys.exit(1)
        else:
            print(task_info(text=task_text, changed="False"))
            print(f"'{task_text} for hosts' -> NornirResponse <Success: True>\n")
            for host in nr_hosts_list:
                print(f"-> {host}")

    # If the --tag argument is set, verify that the tag has hosts assigned to
    elif hasattr(args, "tag"):
        # Filter the inventory based on the argument tag
        nr_obj = nr_obj.filter(F(tags__contains=args.tag))

        # If the filteres object have no hosts, exit with a error message
        if nr_obj.inventory.hosts.keys():
            print(task_info(text=task_text, changed="False"))
            print(f"'{task_text} for tag {args.tag}' -> NornirResult <Success: True>")

        else:
            print(task_error(text=task_text, changed="False"))
            print(
                f"'Filter inventory for tag {args.tag}' -> NornirResult <Success: False>"
                + f"\n\nNo host with tag '{args.tag}' in hosts.yaml inventory file"
                + "\n\033[1m\u001b[31m"
                + "-> Analyse the Nornir inventory and filter for a tag assigned to hosts\n\n"
                + "\033[0m"
            )
            sys.exit(1)

    else:
        print(task_error(text=task_text, changed="False"))
        print(
            f"'{task_text}' -> NornirResult <Success: False>"
            "\n\n\U0001f4a5 ALERT: NOT SUPPORTET ARGPARSE ARGUMENT FOR NORNIR INVENTORY FILTERING! \U0001f4a5"
            "\n\033[1m\u001b[31m-> Analyse the python function for missing Argparse filtering\n\n\033[0m"
        )
        sys.exit(1)

    return nr_obj


def nr_filter_inventory_from_host_list(nr_obj, filter_reason, host_list):
    """
    This function takes a Nornir object, a filter reason to print in Nornir style to std-out and a list of
    hosts. It can be a list of hosts or a list of strings where the hostname is part of the string, as the
    function checks if the hostname from the Nornir object is in that host list or list of strings. Every host
    that matches will be added to the new filter target and the new filtered Nornir object will be returned.
    """
    task_text = "NORNIR re-filter inventory"
    print_task_name(task_text)

    # Re-filter the Nornir inventory only on hosts that need to be reconfigured.
    # Create an empty list to fill with all hosts that need reconfiguration.
    filter_target = []

    # Iterate over all diff files and add the host to the filter_target list if the Nornir inventory host is
    # in the diff file name
    for item in host_list:
        for host in nr_obj.inventory.hosts.keys():
            if host in item:
                filter_target.append(host)
                break

    # Remove possible duplicate hosts in the list
    filter_target = list(set(filter_target))

    # Use Nornir-Salt FFun Filter-List option to filter on a list of hosts
    nr_obj = FFun(nr_obj, FL=filter_target)

    print(task_info(text=task_text, changed="False"))
    print(f"'{task_text} for hosts' -> NornirResponse <Success: True>")
    print(f"\n{filter_reason}")
    for host in nr_obj.inventory.hosts.keys():
        print(f"-> {host}")

    return nr_obj


#### Nornir Print Functions ##################################################################################


def print_script_banner(title, text):
    """
    Print a custom script banner with pyfiglet
    """
    print(f"\n\033[92m{figlet_format(title, width=110)}" f"{text}\033[0m")


def print_task_title(text):
    """
    Prints a Nornir style title
    """
    asteriks_line = (84 - len(text)) * "*"
    color = "\033[1m\u001b[32m"
    color_end = "\033[0m"

    print(f"\n{color}**** {text} {asteriks_line}{color_end}")


def print_task_name(text):
    """
    Returns a Nornir style host task name
    """
    asteriks_line = (89 - len(text)) * "*"
    color = "\033[1m\u001b[36m"
    color_reset = "\033[0m"

    print(f"\n{color}{text} {asteriks_line}{color_reset}")


def task_host(host, changed):
    """
    Returns a Nornir style host task title
    """
    text = f"* {host} ** changed : {changed}"

    asteriks_line = (89 - len(text)) * "*"
    color = "\033[1m\u001b[34m"
    color_reset = "\033[0m"

    return f"{color}{text} {asteriks_line}{color_reset}"


def task_info(text, changed):
    """
    Returns a Nornir style task info message
    """
    text = f"---- {text} ** changed : {changed}"

    if "True" in changed:
        color = "\033[1m\u001b[33m"
    else:
        color = "\033[1m\u001b[32m"

    dash_line = (89 - len(text)) * "-"
    color_reset = "\033[0m"

    return f"{color}{text} {dash_line} INFO{color_reset}"


def task_error(text, changed):
    """
    Returns a Nornir style task error message
    """
    text = f"---- {text} ** changed : {changed}"

    dash_line = (89 - len(text)) * "-"
    color = "\033[1m\u001b[31m"
    color_reset = "\033[0m"

    return f"{color}{text} {dash_line} ERROR{color_reset}"
