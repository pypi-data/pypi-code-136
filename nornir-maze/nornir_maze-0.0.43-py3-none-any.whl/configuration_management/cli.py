#!/usr/bin/env python3
"""
This module contains screen-scraping functions and tasks related to Nornir.

The functions are ordered as followed:
- Complete CLI configuration workflows
- Screen-Scraping Helper Functions
- Single Nornir Jinja2 Tasks
- Single Nornir Screen-Scraping Tasks
- Nornir Screen-Scraping Tasks in regular Functions
"""

import sys
import time
from nornir_scrapli.tasks import send_config, send_configs, send_command, send_commands
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.tasks.files import write_file
from nornir.core.task import Result
from nornir_maze.utils import (
    print_task_title,
    print_task_name,
    task_host,
    task_info,
    task_error,
)
from nornir_maze.configuration_management.utils import (
    create_tpl_int_list,
    create_single_interface_list,
    template_file_custom,
)


#### Complete CLI Configuration Workflow 01 ##################################################################


def cli_cfg_network_from_code_01(nr_obj, banner_motd, rebuild=False, verbose=False):
    """
    This function improves modularity as it is used within multiple scripts. The network will be reconfigured
    to from the day0 config its desired state.
    """
    print_task_title("Configure network from code")

    # Set a variable to verify the network config status
    config_status = True

    # Returns a Nornir AggregatedResult object containing all generated configs by Jinja2 or terminates the
    # script if one or more tasks failed
    j2_base_config = jinja2_generate_config(
        nr_obj=nr_obj,
        name="Jinja2 render base config",
        path="cli_path_tpl_base_config",
        template="cli_payload_tpl_base_config",
        verbose=verbose,
    )
    # config_status validation is not needed as the script ends with an error in case there is an issue with
    # one or more config renderings

    # If args.rebuild it True load the day0 config, otherwise load the golden-config
    if rebuild:
        # Replace the running-config with the day0 config from the switch flash:
        config_status = cfg_eem_replace_config(
            nr_obj=nr_obj,
            name="Scrapli load day0-config",
            eem_name="eem_load_day0_config",
            file="flash:day0-config",
            verbose=verbose,
        )

    else:
        # Replace the running-config with the golden-config from the switch flash:
        config_status = cfg_eem_replace_config(
            nr_obj=nr_obj,
            name="Scrapli load golden-config",
            eem_name="eem_load_golden_config",
            file="flash:golden-config",
            verbose=verbose,
        )

    # Configures the Jinja2 generated config from the jinja2_generate_config() function returned
    # AggregatedResult object -> j2_config
    if config_status:
        config_status = cfg_jinja2_config(
            nr_obj=nr_obj,
            name="Scrapli apply Jinja2 rendered base config",
            jinja2_result=j2_base_config,
            verbose=verbose,
        )

    # Configures the Cisco motd multi-line banner
    if config_status:
        config_status = cfg_multiline_banner(
            nr_obj=nr_obj,
            name="Scrapli configure motd multi-line banner",
            multiline_banner=banner_motd,
            verbose=verbose,
        )

    # Configures all interfaces which are part of an interface template template
    if config_status:
        config_status = cfg_tpl_int_cli(
            nr_obj=nr_obj,
            name="Scrapli configure interface templates",
            verbose=verbose,
        )

    # Save the config to startup-config
    if config_status:
        config_status = save_config_cli(
            nr_obj=nr_obj,
            name="Netmiko save running-config to startup-config",
            verbose=verbose,
        )

    return config_status


#### Screen-Scraping Helper Functions ########################################################################


def create_tpl_int_config_content(task_host_obj, tpl_int_group):
    """
    This is a helper function for scrapli_replace_tpl_int_config() and creates the interface config contect
    from the Nornir host inventory object which is then appended to the interface configuration
    """
    # Create an empty list to append with the config
    config = []
    base_config = []
    add_config = []

    # Iterate over all host inventory keys
    for key in task_host_obj.keys():
        # Match the interface template config prefix
        if key.startswith(f"cfg_{tpl_int_group}"):
            # Match the key cfg_{tpl_int_group}_base
            if key in f"cfg_{tpl_int_group}_base":
                # Add the interface base config list to base_config
                base_config = task_host_obj[key]

            # Match all keys except cfg_{tpl_int_group}_base
            if key not in f"cfg_{tpl_int_group}_base":
                # Add all other interface config lists to add_config
                add_config += task_host_obj[key]

    # Add the base_config first and then the add_config
    config += base_config
    config += add_config

    # Return the list of the interface template config content
    return config


#### Single Nornir Jinja2 Tasks ##############################################################################


#### Single Nornir Screen Scraping Tasks #####################################################################


def verify_destination_md5(task, host_dict):
    """
    This custom Nornir task takes the result of the function host_dict as an argument and runs the
    Scrapli task send_command to verify the source md5 hast with the md5 hash computed on the switch. The
    standard Scrapli result is returned at the end of the task.
    """

    dest_file = host_dict[str(task.host)].result["dest_file"]
    source_md5 = host_dict[str(task.host)].result["source_md5"]

    result = task.run(
        task=send_command,
        command=f"verify /md5 flash:{dest_file} {source_md5}",
        strip_prompt=True,
        timeout_ops=180,
    )

    return Result(host=task.host, result=result)


def scrapli_apply_jinja2_config(task, jinja2_result_obj):
    """
    This function takes the Nornir AggregatedResult object from function jinja2_generate_config() and applies
    the Jinja2 rendered configuration to each host.
    """

    # Access the jinja2_result which is a AggregatedResult object and split the config into a list of strings.
    config_list = jinja2_result_obj[str(task.host)][1].result.splitlines()

    # Run the standard Nornir Scrapli task send_configs
    result = task.run(
        name="Scrapli apply Jinja2 rendered config",
        task=send_configs,
        configs=config_list,
        strip_prompt=False,
        timeout_ops=180,
    )

    return Result(host=task.host, result=result)


def scrapli_replace_tpl_int_config(task, tpl_int_group):
    """
    Sets each interface in the interface_group to default and applies then the config template to the
    specified interfaces defined in hosts.yaml
    """
    try:
        # Create an interface list with full interface names, Gi -> GigabitEthernet
        single_interface_list = create_single_interface_list(task.host[tpl_int_group])

        # Construct config for each interface and apply the config
        for interface in single_interface_list:
            # Empty the list to append with the interface config
            interface_config = []

            # Set the interface to default and then enter the interface config
            interface_config.append("!")
            interface_config.append(f"default interface {interface}")
            interface_config.append("!")
            interface_config.append(f"interface {interface}")

            # Create the interface template content
            config = create_tpl_int_config_content(task_host_obj=task.host, tpl_int_group=tpl_int_group)

            # Add the interface template content to the interface config
            for line in config:
                interface_config.append(line)

            # Exit the interface config mode back to the config mode
            interface_config.append("exit")
            interface_config.append("!")

            # Apply interface config
            task.run(
                name="Scrapli interface config",
                task=send_configs,
                configs=interface_config,
                strip_prompt=False,
                stop_on_failed=False,
                timeout_ops=180,
            )

        return Result(host=task.host)

    except TypeError:
        # TypeError Exception handles empty host inventory interface lists
        # Print the exception result to avoid that Nornir interrupts the script
        return Result(host=task.host, result=f"No interface in template group {tpl_int_group}")
        # No interfaces in tpl_int_group (emtpy list)
        # Return the Nornir result as True as no interface should be configured

    except KeyError:
        # KeyError exception handles not existing host inventory data keys
        return Result(host=task.host, result=f"No template group {tpl_int_group} associated")
        # No tpl_int_group (template group key not in host inventory)
        # Return the Nornir result as True as no interface should be configured


def custom_write_file(task, commands, path, filename_suffix, backup_config=False):
    """
    This custom Nornir task takes a list of commands to execute, a path and a filename suffix as arguments and
    writes the output of the commands to that file. The start of the filename is the hostname and as suffix
    can any text be added.
    """
    # The emtpy string will be filled and written to file
    content = ""

    # Execute each command individual to add custom content for each command
    for command in commands:
        command_response = task.run(task=send_command, command=command, strip_prompt=True, timeout_ops=180)

        if backup_config:
            # If the file should be a backup of the configuration, then remove unwanted lines which are not
            # real configurations and to avoid unwanted git commits
            for line in command_response.result.splitlines():
                if line.startswith("Building configuration..."):
                    continue
                if line.startswith("Current configuration :"):
                    continue
                if line.startswith("! Last configuration change"):
                    continue
                if line.startswith("! NVRAM config last updated"):
                    continue

                # If no line to exclude matched, add the line to the content
                content += f"{line}\n"

        else:
            # Add the promt with the command and then the command result
            content += f"{task.host}#{command}\n"
            content += f"{command_response.result}\n\n"

        # Remove any possible starting or ending blank lines
        content = content.rstrip()
        content = content.lstrip()

    # Write the content variable to the file specified by the arguments
    task.run(task=write_file, filename=f"{path}/{task.host}{filename_suffix}", content=content, append=False)


#### Nornir Task in regular Functions ########################################################################


def cli_verify_destination_file(nr_obj, host_dict):
    """
    This function takes the result of the function host_dict as an argument and runs fist the
    custom Nornir task verify_destination_md5 to verify the destination file with its md5 hash against the
    source file md5 hash. In case of an error, a not correct uploaded software file or a not existing file, a
    info message is printed and exits the script.
    """
    # List to fill with hosts with not matching destination file md5 hash or not existing destination file
    failed_hosts = []

    task_text = "CLI verify destination file"
    print_task_name(task_text)

    # Run the custom Nornir task verify_destination_md5
    md5_result = nr_obj.run(task=verify_destination_md5, host_dict=host_dict)

    # If the task verify_destination_md5 failed -> Print results and exit the script
    if md5_result.failed:
        # Print the task results
        for host in md5_result:
            print(task_host(host=host, changed="False"))

            # If the task fails and a exceptions is the result
            if isinstance(md5_result[host].result, str):
                print(md5_result[host].result)
            else:
                for result in md5_result[host].result:
                    print(result)

        print("\n")
        print(task_error(text=task_text, changed="False"))
        print("\U0001f4a5 ALERT: CLI DESTINATION FILE VERIFICATION FAILED! \U0001f4a5")
        print(
            "\n\033[1m\u001b[31m"
            "-> Analyse the Nornir output for failed task results\n"
            "-> May apply Nornir inventory changes and run the script again\n"
            "\033[0m"
        )
        sys.exit()

    # Print the task results of upload_file_task and verify_destination_md5
    for host in md5_result:
        print(task_host(host=host, changed="False"))

        # Set the source md5 hash
        source_md5 = host_dict[host].result["source_md5"]

        # Save the md5_result as string to variable for parsing
        dest_md5 = str(md5_result[host].result[0])

        # Extract the md5 hash from the md5_result
        for line in dest_md5.splitlines():
            # Source and destination md5 hast are identical
            if line.startswith("Verified"):
                # Extract the md5 hash from the md5_result
                dest_md5 = line
                # Split the string into words
                dest_md5 = dest_md5.split()
                # Slicing the list -> -1 means the last element of the list
                dest_md5 = dest_md5[-1]
                print(task_info(text=task_text, changed="False"))
                print(f"'{task_text}' -> CliResponse <Success: True>")
                print("\nMD5-Hashes are identical:")
                print(f"-> Source MD5-Hash: {source_md5}")
                print(f"-> Destination MD5-Hash: {dest_md5}")

            # Source and destination md5 hash are different -> Upload failed
            elif line.startswith("Computed signature"):
                # Extract the md5 hash from the md5_result
                dest_md5 = line
                # Split the string into words
                dest_md5 = dest_md5.split()
                # Slicing the list -> -1 means the last element of the list
                dest_md5 = dest_md5[-1]
                print(task_error(text=task_text, changed="False"))
                print(f"'{task_text}' -> CliResponse <Success: False>")
                print("\nMD5-Hashes are not identical:")
                print(f"-> Source MD5-Hash: {source_md5}")
                print(f"-> Destination MD5-Hash: {dest_md5}")
                failed_hosts.append(host)

            # There is an %Error as the file don't exist
            elif line.startswith("%Error"):
                print(task_error(text=task_text, changed="False"))
                print(f"'{task_text}' -> CliResponse <Success: False>")
                print(f"\n-> {line}")
                failed_hosts.append(host)

    return failed_hosts


def save_config_cli(nr_obj, name, verbose=False):
    """
    This function runs a Nornir task to execute with Netmiko netmiko_save_config a write memory on each device
    and prints the result to std-out
    """
    print_task_name(text=name)

    task = nr_obj.run(task=netmiko_save_config, cmd="write memory", on_failed=True)

    for host in task:
        msg_changed = str(task[host].changed)
        print(task_host(host=host, changed=msg_changed))

        # If the host failed -> print the failed configuration
        if task[host].failed:
            print(task_error(text=name, changed=msg_changed))
            print(task[host][0].result)

        # If verbose is True -> print all results
        elif verbose:
            print(task_info(text=name, changed=msg_changed))
            print(task[host][0].result)

        # If the host succeeded and verbose is False -> print info
        else:
            print(task_info(text=name, changed=msg_changed))
            print("Saved config to startup-config successfully")

    # Return True if the task were successful
    if not task.failed:
        return True
    return False


def cfg_eem_replace_config(nr_obj, name, eem_name, file, verbose=False):
    """
    This function uses Scrapli send_configs to configure a EEM applet which replace the config from a
    specified file path. After this config will be executed to replace the configuration. It's basically a
    rollback function.
    """
    print_task_name(text=name)

    # Load day0 EEM applet config
    # fmt: off
    config_list = [
        f'event manager applet {eem_name}',
        'event none maxrun 60',
        'action 1.0 cli command "enable"',
        f'action 2.0 syslog msg "{eem_name} -> Started"',
        f'action 2.1 cli command "{eem_name} -> Started"',
        f'action 3.0 cli command "configure replace {file} force"',
        f'action 4.0 syslog msg "{eem_name} -> Finish"',
        f'action 4.1 cli command "{eem_name} -> Finish"',
    ]
    # fmt: on

    # Execute the EEM applet configuration. Run the standard Nornir Scrapli task send_configs
    task1 = nr_obj.run(
        name=f"Scrapli configure EEM applet {eem_name}",
        task=send_configs,
        configs=config_list,
        strip_prompt=False,
        timeout_ops=180,
    )

    # Execute the EEM applet to replace the config. Run the standard Nornir Scrapli task send_configs
    task2 = nr_obj.run(
        name=f"Scrapli execute EEM applet {eem_name}",
        task=send_commands,
        commands=[f"event manager run {eem_name}"],
        strip_prompt=False,
        timeout_ops=180,
    )

    # Wait some seconds to allow the EEM applet to replace the config
    # Tested on a C9300 with 1700 lines of config to replace -> needs arround 25s
    time.sleep(40)

    # Delete the EEM applet after it have been executed. Run the standard Nornir Scrapli task send_configs
    task3 = nr_obj.run(
        name=f"Scrapli delete EEM applet {eem_name}",
        task=send_configs,
        configs=[f"no event manager applet {eem_name}"],
        strip_prompt=False,
        timeout_ops=180,
    )

    task1_msg = "Scrapli configure EEM applet"
    task2_msg = "Scrapli execute EEM applet"
    task3_msg = "Scrapli delete EEM applet"

    for host in task1:
        msg_changed = str(task1[host].changed)
        print(task_host(host=host, changed=msg_changed))

        # If the host failed -> print the failed configuration
        if task1[host].failed:
            print(task_error(text=task1_msg, changed=msg_changed))
            print(f"'Configure {eem_name}' -> CliResponse <Success: False>\n")
            print(task1[host][0].result)
            print(task_error(text=task2_msg, changed="False"))
            print(f"'Execute {eem_name}' -> CliResponse <Success: False>\n")
            print(task2[host][0].result)
            print(task_error(text=task3_msg, changed="False"))
            print(f"'Delete {eem_name}' -> CliResponse <Success: False>\n")
            print(task3[host][0].result)

        # If verbose is True -> print all results
        elif verbose:
            print(task_info(text=task1_msg, changed=msg_changed))
            print(f"'Configure {eem_name}' -> CliResponse <Success: True>\n")
            print(task1[host][0].result)
            print(task_info(text=task2_msg, changed="True"))
            print(f"'Execute {eem_name}' -> CliResponse <Success: True>\n")
            print(task2[host][0].result)
            print(task_info(text=task3_msg, changed="True"))
            print(f"'Delete {eem_name}' -> CliResponse <Success: True>\n")
            print(task3[host][0].result)

        # If the host succeeded and verbose is False -> print info
        else:
            print(task_info(text=task1_msg, changed=msg_changed))
            print(f"'Configure {eem_name}' -> CliResponse <Success: True>")
            print(task_info(text=task2_msg, changed="True"))
            print(f"'Execute {eem_name}' -> CliResponse <Success: True>")
            print(task_info(text=task3_msg, changed="True"))
            print(f"'Delete {eem_name}' -> CliResponse <Success: True>")

    # Return True if both tasks were successful
    if not (task1.failed and task2.failed):
        return True
    return False


def jinja2_generate_config(nr_obj, name, path, template, verbose=False):
    """
    This function runs the standard Nornir task template_file and generates a config for each host. If one or
    more hosts failed the function print a error std-out message and terminates the script. Only when all
    hosts were successful the Nornir AggregatedResult object will be returned
    """
    print_task_name(text=name)

    # Run the Nornir Task template_file
    j2_config = nr_obj.run(task=template_file_custom, task_msg=name, template=template, path=path)

    for host in j2_config:
        print(task_host(host=host, changed="False"))

        if j2_config[host].failed:

            # If the subtask failed print its exception
            if j2_config[host].result.startswith("Subtask:"):
                print(task_error(text=name, changed="False"))

                # If the Jinja2 template is not found by the template_file task
                if "TemplateNotFound" in j2_config[host][1].result:
                    file = j2_config[host][1].exception
                    print(f"Jinja2 template '{file}' not found")

                # If the Jinja2 templating rendering catches another exception
                else:
                    print(j2_config[host][1].result)

            # If the task fails print the returned result
            elif j2_config[host].failed:
                print(j2_config[host].result)

        # If no condition matched the task was successful
        else:
            print(task_info(text="Jinja2 template file", changed="False"))
            # Read the template filename from the Nornir inventory
            file = nr_obj.inventory.hosts[host][template]
            print(f"Jinja2 template '{file}' rendered successfully")

            if verbose:
                print(f"\n{j2_config[host][1].result}")

    if j2_config.failed_hosts:
        # If one or more of the Jinja2 template tasks failed
        print("\n")
        print(task_error(text=name, changed="False"))
        print("\U0001f4a5 ALERT: JINJA2 CONFIG TEMPLATING FAILED! \U0001f4a5")
        print(
            "\n\033[1m\u001b[31m"
            "-> Analyse the Nornir output for failed Jinja2 tasks\n"
            "-> May apply Nornir inventory changes and run the script again\n\n"
            "No config changes has been made yet!\n"
            "\033[0m"
        )
        # Terminate the script with successful exit code 0
        sys.exit()

    # If the task was successful return its result object
    return j2_config


def cfg_jinja2_config(nr_obj, name, jinja2_result, verbose=False):
    """
    This function takes a Nornir AggregatedResult object which contains the configuration that should be
    applied to each device. It can continue with the result of the function jinja2_generate_config to apply a
    Jinja2 config to devices and prints the result is the Nornir style.
    """
    print_task_name(text=name)

    # Run the custom nornir task scrapli_apply_jinja2_config
    task = nr_obj.run(task=scrapli_apply_jinja2_config, jinja2_result_obj=jinja2_result, on_failed=True)

    for host in task:
        msg_changed = str(task[host].changed)
        print(task_host(host=host, changed=msg_changed))

        # If the host failed -> print the failed configuration
        if task[host].failed:
            print(task_error(text=name, changed=msg_changed))

            # If verbose is True -> print all results
            if verbose:
                print(task[host][1].result)

            # If verbose is False -> print only failed results
            else:
                lines = task[host][1].result.splitlines()
                for index, line in enumerate(lines):
                    if "'^'" in line:
                        print(lines[index - 3])
                        print(lines[index - 2])
                        print(lines[index - 1])
                        print(line)

        # If the host succeeded and verbose is False -> print info
        else:
            print(task_info(text=name, changed=msg_changed))

            # If verbose is True -> print all results
            if verbose:
                print(task[host][1].result)
            else:
                print("Configuration successful")

    return not task.failed


def cfg_multiline_banner(nr_obj, name, multiline_banner, verbose=False):
    """
    This function takes a multiline string as variable multiline_banner and configures this banner with the
    help of Scrapli eager=True option. Because the banner "input mode" is basically like a text editor where
    we dont get the prompt printed out between sending lines of banner config we need to use the 'eager' mode
    to force scrapli to blindly send the banner/macro lines without looking for the prompt in between each
    line. You should *not* use eager unless you need to and know what you are doing as it basically disables
    one of the core features that makes scrapli reliable!
    """
    print_task_name(text=name)

    # Run the standard nornir task send_config
    task = nr_obj.run(
        task=send_config,
        config=multiline_banner,
        strip_prompt=False,
        eager=True,
        on_failed=True,
        timeout_ops=180,
    )

    for host in task:
        msg_changed = str(task[host].changed)
        print(task_host(host=host, changed=msg_changed))

        # If the host failed -> print the failed configuration
        if task[host].failed:
            print(task_error(text=name, changed=msg_changed))
            print(task[host][0].result)

        # If verbose is True -> print all results
        elif verbose:
            print(task_info(text=name, changed=msg_changed))
            print(task[host][0].result)

        # If the host succeeded and verbose is False -> print info
        else:
            print(task_info(text=name, changed=msg_changed))
            print("Configured multi-line banner successfully")

    # Return True if both tasks were successful
    if not task.failed:
        return True
    return False


def cfg_tpl_int_cli(nr_obj, name, verbose=False):
    """
    This function takes a Nornir object and a filter tag to execute all tasks within this function on the
    given inventory subset. Each interface group will be configured by Scrapli.
    """
    # Set the variable to return at the end of the function to True
    config_status = True

    # Gather the tpl_int template groups from all hosts
    result = nr_obj.run(task=create_tpl_int_list)

    # Create a union of the results from all hosts -> no duplicate items
    tpl_int_groups = []
    for host in result:
        tpl_int_groups = list(set().union(tpl_int_groups, result[host].result))

    for group in tpl_int_groups:
        print_task_name(text=f"{name} {group}")

        # Run the custom nornir task scrapli_replace_tpl_int_config
        task = nr_obj.run(task=scrapli_replace_tpl_int_config, tpl_int_group=group, on_failed=True)

        for host, multi_result in task.items():
            print(task_host(host=host, changed=str(task[host].changed)))

            for result in multi_result:
                # Nornir result is None and therefor also the Scrapli result is None. If the result starts
                # with Subtask and configuration error has occured and the parent task error won't be printed
                if (result.result is None) or result.result.startswith("Subtask:"):
                    continue

                # Get the attribute scrapli_response from result into a variable. Return None if the attribute
                # scrapli_response is not existing
                scrapli_multi_result = getattr(result, "scrapli_response", None)

                # If the scrapli_multi_result is None but the result.result is present this means an TypeError
                # or KeyError handled inside the task is present
                if scrapli_multi_result is None:
                    print(task_info(text=result.name, changed=str(result.changed)))
                    print(result.result)
                    continue

                # Find the interface from the Scrapli result
                for scrapli_result in scrapli_multi_result:
                    if scrapli_result.channel_input.startswith("interface"):
                        interface = scrapli_result.channel_input
                        # Remove the word interface and leading whitespaces
                        interface = interface.replace("interface", "").lstrip()

                # Print the result for a failed task
                if result.failed:
                    print(task_error(text=result.name, changed=str(result.changed)))
                    print(f"{interface} -> {scrapli_multi_result}")
                    print(result.result)
                    config_status = False

                # Print the result for a successful task
                else:
                    print(task_info(text=result.name, changed=str(result.changed)))
                    print(f"{interface} -> {scrapli_multi_result}")
                    if verbose:
                        # Print the whole CLI result
                        print(result.result)

    return config_status


def write_commands_to_file(nr_obj, name, commands, path, filename_suffix, backup_config=False, verbose=False):
    """
    This function takes a list of commands to execute, a path and a filename suffix as arguments and writes
    the output of the commands to that file. The start of the filename is the hostname and as suffix can any
    text be added.
    """
    # pylint: disable=too-many-arguments,too-many-locals

    # Set the variable to return at the end of the function to True
    config_status = True

    print_task_name(text=name)

    task_result = nr_obj.run(
        task=custom_write_file,
        commands=commands,
        path=path,
        filename_suffix=filename_suffix,
        backup_config=backup_config,
        on_failed=True,
    )

    for host, multi_result in task_result.items():
        print(task_host(host=host, changed=str(task_result[host].changed)))

        # Print first all Scrapli send_command results
        for result in multi_result:
            # Get the attribute scrapli_response from result into a variable -> Return None if don't exist
            scrapli_result = getattr(result, "scrapli_response", None)

            if scrapli_result is None:
                continue

            task_text = "Execute command"
            cmd = str(scrapli_result.channel_input)

            if scrapli_result.failed:
                print(task_error(text=task_text, changed=str(scrapli_result.failed)))
                print(f"'{cmd}' -> CliResponse <Success: False>\n")
                print(f"{host}#{cmd}")
                print(scrapli_result.result)
            else:
                print(task_info(text=task_text, changed=str(scrapli_result.failed)))
                print(f"'{cmd}' -> CliResponse <Success: True>")
                if verbose:
                    print(f"{host}#{cmd}")
                    print(scrapli_result.result)

        # The write_file result is only present if all Scrapli send_command tasks were successful
        filepath = f"{path}/{host}{filename_suffix}"

        # pylint: disable=undefined-loop-variable
        if [True for result in multi_result if result.name == "write_file"]:
            # The write_file result is present and no exception exists
            if result.exception is None:
                print(task_info(text="Save command(s) to file", changed="False"))
                print(f"'{filepath}' -> NornirResponse <Success: True>")

            # An exception is raised when the folder don't exist
            else:
                print(task_error(text="Save command(s) to file", changed="False"))
                print(f"'{filepath}' -> NornirResponse <Success: False>\n")
                print(result.exception)
                config_status = False

        # The write_file result is not present as one or more commands have failed
        else:
            print(task_error(text="Save command(s) to file", changed="False"))
            print(f"'{filepath}' -> NornirResponse <Success: False>\n")
            print("Command(s) failed -> Command(s) have not been written to file\n")
            print(result.exception)
            print(result.result)
            config_status = False

    return config_status
