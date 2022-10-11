#!/usr/bin/env python3
"""
This module contains general configuration management functions and tasks related to Nornir.

The functions are ordered as followed:
- Helper Functions
- Nornir print functions
- Nornir Helper Tasks
"""

import os
import sys
import time
import subprocess  # nosec
import argparse
from alive_progress import alive_bar
from nornir.core.task import Result
from nornir_netmiko.tasks import netmiko_file_transfer
from nornir_maze.utils import (
    print_task_title,
    print_task_name,
    task_host,
    task_info,
    task_error,
    CustomArgParse,
    CustomArgParseWidthFormatter,
    compute_md5,
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
        "-l",
        "--local_upload",
        action="store_true",
        default=False,
        help="disable Cisco cloud download and enable local upload with SCP",
    )

    # Verify the provided arguments and print the custom argparse error message in case any error or wrong
    # arguments are present and exit the script
    args = argparser.parse_args()

    # If argparser.parse_args() is successful -> no argparse error message
    print(task_info(text=task_text, changed="False"))
    print(f"'{task_text}' -> ArgparseResponse <Success: True>")

    if args.local_upload:
        print("\n-> Upgrade with local software image upload with SCP")
    else:
        print("\n-> Upgrade with Cisco automated software distribution API")

    if args.verbose:
        print(f"\n{args}")

    return args


def fping_track_upgrade_process(nr_obj):
    """
    This function creates a dictionary with the installation process status of each host and runs the custom
    Nornir task fping_task in a range loop. In each loop the software installation status will be updated and
    printed to std-out. There are three expected status which each host will go through the installation
    process. These status are "Installing software", "Rebooting device" and the final status will be "Upgrade
    finish". When all hosts are upgraded successful the script exits the range loop and prints the result to
    std-out. In case the software upgrade is not successful after the range loop is finish, an info message
    will be printed and exit the script.
    """
    # Printout sleep and refresh values
    refresh_timer = 60
    max_refresh = 40
    elapsed_time = 0
    ansi_yellow = "\033[4m\033[1;33m"
    ansi_red = "\033[4m\033[0;31m"
    ansi_green = "\033[4m\033[0;32m"
    ansi_reset = "\033[0m"

    # Dict to track the host software upgrade status
    update_status = {}
    for host in nr_obj.inventory.hosts:
        update_status[host] = "Installing software"

    for _ in range(max_refresh):
        # Run the custom Nornir task fping_task
        task = nr_obj.run(task=fping_task, on_failed=True)

        # fmt: off
        subprocess.run(["clear"], check=True)  # nosec
        # fmt: on

        print_task_title("RESTCONF software upgrade in progress")
        task_text = "Fping track software upgrade process"
        print_task_name(task_text)

        # Update the host software upgrade status and print the result
        for host in task:
            # host fping task result
            fping = task[host].result["output"].rstrip()

            # Initial status -> Host is alive and is installing the software
            if "alive" in fping and "Installing software" in update_status[host]:
                update_status[host] = f"{ansi_yellow}Installing software{ansi_reset}"
            # Second status -> Host is not alive and is rebooting
            if "alive" not in fping and "Installing software" in update_status[host]:
                update_status[host] = f"{ansi_red}Reboot device{ansi_reset}"
            if "alive" not in fping and "Rebooting device" in update_status[host]:
                pass
            # Third status -> host is rebooted with new software release
            if "alive" in fping and "Reboot device" in update_status[host]:
                update_status[host] = f"{ansi_green}Upgrade finish{ansi_reset}"

            # Print the host software upgrade status result
            print(task_host(host=host, changed="False"))
            print(f"Status: {update_status[host]} (fping: {fping})")

        print("\n")

        # Check if all hosts have upgraded successfull
        if not all(f"{ansi_green}Upgrade finish{ansi_reset}" in value for value in update_status.values()):
            # Continue the range loop to track to software upgrade status
            print(
                "\033[1m\u001b[31m"
                f"The fping task result will refresh in {refresh_timer}s ...\n"
                f"Elapsed waiting time: {elapsed_time}/{max_refresh * refresh_timer}s"
                "\033[0m"
            )
            elapsed_time += refresh_timer
            time.sleep(refresh_timer)

        else:
            # Print result and exit the range loop
            print(
                "\033[1m\u001b[32m"
                f"Elapsed waiting time: {elapsed_time}/{max_refresh * refresh_timer}s\n"
                "Wait 120s until the device NGINX RESTCONF server is ready"
                "\033[0m"
            )
            # Sleep for some seconds until the device NGINX RESTCONF server is ready
            time.sleep(120)
            break

    # If the range loop reached the end -> Software upgrade not successful
    else:
        print(
            "\n\033[1m\u001b[31m"
            f"Total software upgrade waiting time of {max_refresh * refresh_timer}s exceeded"
            "\033[0m"
        )


#### Nornir Helper Tasks #####################################################################################


def prepare_local_upgrade_data_task(task):
    """
    This custom Nornir task gets the desired software file path from the Nornir inventory, verifies the file
    exists and computes the md5 hash. The result is a dictionary with infos about the source and the
    destination file which can be used for further processing.
    """
    task_text = "NORNIR prepare upgrade data"

    try:
        # Get the version string and source file from the Nornir inventory
        desired_version = task.host["software"]["version"]
        source_file = task.host["software"]["file"]

    except KeyError as error:
        # KeyError exception handles not existing host inventory data keys
        result = (
            f"{task_error(text=task_text, changed='False')}\n"
            + f"'Key task.host[{error}] not found' -> NornirResponse: <Success: False>"
        )
        # Return the Nornir result as error
        return Result(host=task.host, result=result, failed=True)

    # Verify that the software file exists
    if not os.path.exists(source_file):
        result = (
            f"{task_error(text=task_text, changed='False')}\n"
            + f"'File {source_file} not found' -> OSResponse: <Success: False>\n"
        )
        # Return the Nornir result as error
        return Result(host=task.host, result=result, failed=True)

    # Compute the original md5 hash value
    source_md5 = compute_md5(source_file)
    # Get the filesize and format to GB
    # pylint: disable=consider-using-f-string
    file_size = "%.2f" % (os.path.getsize(source_file) / (1024 * 1024 * 1024))
    # Extract only the filename and prepare the destination path
    dest_file = os.path.basename(source_file)

    result_info = (
        f"{task_info(text=task_text, changed='False')}\n"
        + f"'{task_text}' -> OSResponse: <Success: True>\n"
        + f"\n-> Desired version: {desired_version}\n"
        + f"-> Source file: {source_file}\n"
        + f"-> Source MD5-Hash: {source_md5}"
    )

    result = {
        "result_info": result_info,
        "desired_version": desired_version,
        "source_file": source_file,
        "source_md5": source_md5,
        "file_size": file_size,
        "dest_file": dest_file,
    }

    # Return the Nornir result as success
    return Result(host=task.host, result=result)


def prepare_upgrade_data_task(task):
    """
    This custom Nornir task gets the desired software file path from the Nornir inventory, verifies the file
    exists and computes the md5 hash. The result is a dictionary with infos about the source and the
    destination file which can be used for further processing.
    """
    task_text = "NORNIR prepare desired software version"

    try:
        # Get the version string and source file from the Nornir inventory
        desired_version = task.host["software"]["version"]

    except KeyError as error:
        # KeyError exception handles not existing host inventory data keys
        result = (
            f"{task_error(text=task_text, changed='False')}\n"
            + f"'Key task.host[{error}] not found' -> NornirResponse: <Success: False>"
        )
        # Return the Nornir result as error
        return Result(host=task.host, result=result, failed=True)

    result_info = (
        f"{task_info(text=task_text, changed='False')}\n"
        + f"'{task_text}' -> OSResponse: <Success: True>\n"
        + f"\n-> Desired version: {desired_version}"
    )

    result = {
        "result_info": result_info,
        "desired_version": desired_version,
    }

    # Return the Nornir result as success
    return Result(host=task.host, result=result)


def scp_upload_file_task(task, host_dict):
    """
    This custom Nornir task takes the result of the function host_dict as an argument and runs the
    task netmiko_file_transfer to upload the software file to each host. The standard task result is returned.
    """

    source_file = host_dict[str(task.host)].result["source_file"]
    dest_file = host_dict[str(task.host)].result["dest_file"]

    with alive_bar(spinner="waves2", unknown="waves2"):
        # Run the standard Nornir task netmiko_file_transfer
        result = task.run(
            task=netmiko_file_transfer, source_file=source_file, dest_file=dest_file, direction="put"
        )

    return Result(host=task.host, result=result)


def fping_task(task):
    """
    This custom Nornir task runs the linux command fping to the host IP-address. The returned result is a
    dictionary with the fping output and the retruncode.
    """

    # fmt: off
    fping = subprocess.run( # nosec
        ["fping", "-A", "-d", task.host.hostname,], check=False, capture_output=True
    )
    # fmt: on

    result = {"returncode": fping.returncode, "output": fping.stdout.decode("utf-8")}

    return Result(host=task.host, result=result)


#### Nornir Helper tasks in regular Function #################################################################


def prepare_upgrade_data(nr_obj, local_upload=False):
    """
    This function runs the custom Nornir task prepare_upgrade_data_task to get the desired software file path
    from the Nornir inventory, verifies the file exists and computes the md5 hash. The result will be printed
    to std-out in custom Nornir style and a dictionary with infos about the source and the destination file
    is returned which can be used for further processing. In case of a source file verification error a info
    message will be printed and the script terminates.
    """

    if local_upload:
        print_task_name("NORNIR prepare upgrade data")
        # Run the custom Nornir task prepare_local_upgrade_data_task
        task_result = nr_obj.run(task=prepare_local_upgrade_data_task)
    else:
        print_task_name("NORNIR prepare desired software version")
        # Run the custom Nornir task prepare_upgrade_data_task
        task_result = nr_obj.run(task=prepare_upgrade_data_task)

    # Print the task results
    for host in task_result:
        print(task_host(host=host, changed="False"))

        # If the task fails and a exceptions is the result
        if isinstance(task_result[host].result, str):
            print(task_result[host].result)
        # Else print the result_info from the custom returned dict
        else:
            print(task_result[host].result["result_info"])

    # If one or more host inside the task has failed -> Exit the script
    if task_result.failed:
        print("\n")
        print(task_error(text="Verify source file", changed="False"))
        if local_upload:
            print("\U0001f4a5 ALERT: NORNIR PREPARE UPGRADE DATA FAILED! \U0001f4a5")
        else:
            print("\U0001f4a5 ALERT: NORNIR PREPARE DESIRED SOFTWARE VERSION FAILED! \U0001f4a5")
        print(
            "\n\033[1m\u001b[31m"
            "-> Analyse the Nornir output for failed task results\n"
            "-> May apply Nornir inventory changes and run the script again\n"
            "\033[0m"
        )
        sys.exit()

    return task_result


def scp_upload_file(nr_obj, host_dict):
    """
    This function takes the result of the function host_dict as an argument and runs fist the custom Nornir
    task scp_upload_file_task to upload the software file to the switch. If the software upload is not
    successful for all hosts, a info message will be printed and the scripts terminates.
    """

    task_text = "NETMIKO upload file with SCP"
    print_task_name(task_text)

    # Print some info for each host
    for host in host_dict:
        dest_file = host_dict[host].result["dest_file"]
        file_size = host_dict[host].result["file_size"]
        print(task_host(host=host, changed="False"))
        print(task_info(text=task_text, changed="False"))
        print(f"'Copy {dest_file} ({file_size} GB) to flash:' -> SCPResponse <Success: True>")

    # Run the custom Nornir task scp_upload_file_task
    print("\n")
    upload_result = nr_obj.run(task=scp_upload_file_task, host_dict=host_dict)

    # If scp_upload_file_task failed -> Print results and exit the script
    if upload_result.failed:
        # Print the task results
        for host in upload_result:
            print(task_host(host=host, changed="False"))

            # If the task fails and a exceptions is the result
            if isinstance(upload_result[host].result, str):
                print(upload_result[host].result)
            else:
                for result in upload_result[host].result:
                    print(result)

        print("\n")
        print(task_error(text=task_text, changed="False"))
        print("\U0001f4a5 ALERT: NETMIKO FILE UPLOAD FAILED! \U0001f4a5")
        print(
            "\n\033[1m\u001b[31m"
            "-> Analyse the Nornir output for failed task results\n"
            "-> May apply Nornir inventory changes and run the script again\n"
            "\033[0m"
        )
        sys.exit()
