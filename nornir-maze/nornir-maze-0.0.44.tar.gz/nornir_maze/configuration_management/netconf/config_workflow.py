#!/usr/bin/env python3
"""
This module contains complete NETCONF configuration workflows from multiple nornir_maze functions.

The functions are ordered as followed:
- Complete NETCONF configuration workflows
"""


from nornir_maze.utils import print_task_title
from nornir_maze.configuration_management.restconf.config_workflow import rc_replace_config_01
from nornir_maze.configuration_management.netconf.config_tasks import nc_cfg_jinja2, nc_cfg_tpl_int
from nornir_maze.configuration_management.netconf.ops_tasks import (
    nc_lock,
    nc_unlock,
    nc_validate,
    nc_discard,
    nc_commit,
)
from nornir_maze.configuration_management.restconf.cisco_rpc import (
    rc_cisco_rpc_is_syncing,
    rc_cisco_rpc_save_config,
)


#### Complete NETCONF Configuration Workflow 01 ##############################################################


def nc_configuration_01(config_status, nr_obj, verbose=False):
    """
    This function locks the configuration datastore, executes all configurations in the candidate datastore
    and commits the configuration. In case of configuration errors, the candidate datastore configuration will
    be discarded and the configuration datastore will be unlocked at the end of the function.
    """

    # Return False if config_status argument is False
    if not config_status:
        return False

    print_task_title("Prepare NETCONF for configuration")

    # Checks if an active datastore sync in ongoing and wait until is finish
    rc_cisco_rpc_is_syncing(nr_obj=nr_obj, silent=False, verbose=verbose)

    # Lock the NETCONF candidate datastore
    nc_lock_status = nc_lock(nr_obj=nr_obj, datastore="candidate", verbose=verbose)
    # nc_status controls the NETCONF configuration and nc_lock_status controls
    # the NETCONF unlock task at the end of the function
    nc_status = nc_lock_status

    # Start NETCONF configuration if the datastore is locked
    if nc_status:
        print_task_title("Configure NETCONF payload templates")
        nc_status = nc_cfg_jinja2(nr_obj=nr_obj, verbose=verbose)

    # Continue NETCONF configuration if the config_status is still True
    if nc_status:
        print_task_title("Configure NETCONF interface templates")
        nc_status = nc_cfg_tpl_int(nr_obj=nr_obj, verbose=verbose)

    print_task_title("Verify and commit or discard NETCONF configuration")

    # Validate NETCONF configuration if the config_status is still True
    if nc_status:
        nc_status = nc_validate(nr_obj=nr_obj, datastore="candidate", verbose=verbose)

    # Commit NETCONF configuration if the config_status is still True
    if nc_status:
        # Commit all changes on the NETCONF candidate datastore
        nc_status = nc_commit(nr_obj=nr_obj, verbose=verbose)

    # Discard the NETCONF configuration as there happen and error
    if not nc_status:
        # Discard all changes on the NETCONF candidate datastore
        nc_discard(nr_obj=nr_obj, verbose=verbose)

    # Unlock the NETCONF datastore if the datastore is locked
    if nc_lock_status:
        nc_unlock(nr_obj=nr_obj, datastore="candidate", verbose=verbose)

    return nc_status


def nc_cfg_network_from_code_01(nr_obj, rebuild=False, verbose=False):
    """
    This function improves modularity as it is used within multiple scripts. The network will be reconfigured
    to from the day0-config or the golden-config to its desired state.
    """

    # Replace the configuration with a Cisco specific RESTCONF RPC. Initial config_status argument is True
    config_status = rc_replace_config_01(config_status=True, nr_obj=nr_obj, rebuild=rebuild, verbose=verbose)

    # Execute all NETCONF configurations if the config_status is True
    config_status = nc_configuration_01(config_status=config_status, nr_obj=nr_obj, verbose=verbose)

    if config_status:
        # Checks if an active datastore sync in ongoing and wait until is finish
        rc_cisco_rpc_is_syncing(nr_obj=nr_obj, silent=False, verbose=verbose)

        # Send the Cisco save config RESTCONF RPC
        config_status = rc_cisco_rpc_save_config(nr_obj=nr_obj, verbose=verbose)

    return config_status
