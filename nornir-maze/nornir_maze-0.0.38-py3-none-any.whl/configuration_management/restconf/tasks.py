#!/usr/bin/env python3
"""
This module contains RESTCONF functions and tasks related to Nornir.

The functions are ordered as followed:
- Single Nornir RESTCONF tasks
- Nornir RESTCONF tasks in regular function
"""

import json
import requests
from nornir.core.task import Result
from nornir_maze.utils import (
    print_task_name,
    task_host,
    task_info,
    task_error,
)


#### Single Nornir RESTCONF Tasks ############################################################################


def rc_cisco_get_task(task, yang_data_query):
    """
    This custom Nornir task executes a RESTCONF GET request to a yang data query and returns a dictionary with
    the whole RESTCONF response as well as some custom formated data for further processing.
    """
    # RESTCONF HTTP URL
    restconf_path = f"/restconf/data/{yang_data_query}"
    url = f"https://{task.host.hostname}:{task.host['restconf_port']}{restconf_path}"

    # RESTCONF HTTP header
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json",
    }

    # RESTCONF HTTP API call
    rc_response = requests.get(  # nosec
        url=url, headers=headers, auth=(task.host.username, task.host.password), verify=False, timeout=120
    )

    # Result dict to return as task result
    result = {
        "url": url,
        "response": rc_response,
        "method": rc_response.request,
        "status_code": rc_response.status_code,
        "elapsed": rc_response.elapsed.total_seconds(),
        "json": rc_response.json(),
    }

    return Result(host=task.host, result=result)


#### Nornir RESTCONF tasks in regular Function ###############################################################


# -> Write a print_rc_get_result() function


def rc_verify_software_version(nr_obj, host_dict, verbose=False):
    """
    This function takes the Nornir result object of the function verify_source_file or a similar Nornir result
    object as an argument and runs custom Nornir task rc_cisco_get_task with a yang data query to get the
    active software version. The active software version will be compared against the desired software version
    from the host_dict. The result will be printed in Nornir style and the return of the function is a list
    with hosts which have a not matching software version to the desired software version.
    """
    # List to fill with hosts not matching the desired software version
    failed_hosts = []

    task_text = "RESTCONF verify current software version"
    print_task_name(task_text)

    # Get software version with RESTCONF
    task_result = nr_obj.run(
        task=rc_cisco_get_task,
        yang_data_query="Cisco-IOS-XE-install-oper:install-oper-data/install-location-information",
    )

    # Print results for each host
    for host in task_result:
        msg_changed = str(task_result[host].changed)
        print(task_host(host=host, changed=msg_changed))

        # If the task fails -> A Traceback is the result
        if isinstance(task_result[host].result, str):
            print(task_result[host].result)
            return False

        # If its a task result
        if isinstance(task_result[host].result, dict):
            index = 0
        # If its a sub-task result
        elif isinstance(task_result[host][1].result, dict):
            index = 1

        # Prepare all variables for printing
        desired_version = host_dict[host].result["desired_version"]
        current_version = task_result[host][index].result["json"][
            "Cisco-IOS-XE-install-oper:install-location-information"
        ][0]["install-version-state-info"][0]["version"]
        response = task_result[host][index].result["response"]
        elapsed = task_result[host][index].result["elapsed"]

        # Slice the variable to have only the fist 8 characters of the version number
        current_version = current_version[:8]

        # Add the current version to the host_dict dictionary
        host_dict[host].result["current_version"] = current_version

        result = (
            f"\nURL: {task_result[host][index].result['url']}\n"
            + f"Method: {task_result[host][index].result['method']}\n"
            + f"Response: {response}\n"
            + f"Current version from JSON payload: {json.dumps(current_version, sort_keys=True, indent=4)}"
        )

        if task_result[host][index].result["status_code"] == 200:
            if desired_version in current_version:
                print(task_info(text=task_text, changed=msg_changed))
                print(
                    f"'{task_text}' -> RestconfResponse {response} in {elapsed}s\n"
                    f"\n-> Desired version {desired_version} match installed version {current_version}"
                )
                # If verbose is True -> Print the whole result
                if verbose:
                    print(result)

            else:
                print(task_error(text=task_text, changed=msg_changed))
                print(
                    f"'{task_text}' -> RestconfResponse {response} in {elapsed}s\n"
                    f"\n-> Desired version {desired_version} don't match installed version {current_version}"
                )
                # If verbose is True -> Print the whole result
                if verbose:
                    print(result)
                # Add the failed host to the failed_hosts list
                failed_hosts.append(host)

        else:
            print(task_error(text=task_text, changed=msg_changed))
            print(f"'{task_text}' -> RestconfResponse {response} in {elapsed}s")
            # Print the whole result
            print(result)
            # Add the failed host to the failed_hosts list
            failed_hosts.append(host)

    return (failed_hosts, host_dict)
