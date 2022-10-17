#!/usr/bin/env python3
"""
This module contains complete RESTCONF configuration workflows from multiple nornir_maze functions.

The functions are ordered as followed:
- Complete RESTCONF configuration workflows
"""


from nornir_maze.utils import print_task_title
from nornir_maze.configuration_management.restconf.cisco_rpc import (
    rc_cisco_rpc_is_syncing,
    rc_cisco_rpc_rollback_config,
)


#### Complete RESTCONF Configuration Workflow 01 #############################################################


def rc_replace_config_01(config_status, nr_obj, rebuild=False, verbose=False):
    """
    This function replace the configuration with the golden-config by default or the day0-config if the
    rebuild argument is set.
    """

    # Return False if config_status argument is False
    if not config_status:
        return False

    # If args.rebuild it True load the day0 config, otherwise load the golden-config
    if rebuild:
        print_task_title("Replace current config with day0-config")
        # Checks if an active datastore sync in ongoing and wait until is finish
        rc_cisco_rpc_is_syncing(nr_obj=nr_obj, silent=False, verbose=verbose)
        # Replace the running-config with the day0 config from the switch flash:
        config_status = rc_cisco_rpc_rollback_config(
            nr_obj=nr_obj,
            task_name="RESTCONF rollback day0-config",
            target_url="flash:day0-config",
            verbose=verbose,
        )

    # Else or by default load the golden-config
    else:
        print_task_title("Replace current config with golden-config")
        # Checks if an active datastore sync in ongoing and wait until is finish
        rc_cisco_rpc_is_syncing(nr_obj=nr_obj, silent=False, verbose=verbose)
        # Replace the running-config with the golden-config from the switch flash:
        config_status = rc_cisco_rpc_rollback_config(
            nr_obj=nr_obj,
            task_name="RESTCONF rollback golden-config",
            target_url="flash:golden-config",
            verbose=verbose,
        )

    return config_status
