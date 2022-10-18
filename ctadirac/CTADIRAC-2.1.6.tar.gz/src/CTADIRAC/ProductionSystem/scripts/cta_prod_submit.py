#!/usr/bin/env python
"""
Launch a production from a workflow description

Usage:
    cta-prod-submit <name of the production> <YAML file with workflow description> <execution mode>
Arguments:
   name of the production
   YAML file with the workflow description
   execution mode is optional:
     ps: submit the workflow to the Production System (default)
     wms: submit individual jobs to the WMS
     local: execute the workflow locally as individual jobs
Example:
    cta-prod-submit TestProd production_config.yml
Example for local execution (for testing):
    cta-prod-submit TestProd production_config.yml local
"""

__RCSID__ = "$Id$"

from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script

Script.parseCommandLine()
import DIRAC
import yaml
import json

from DIRAC.ProductionSystem.Client.ProductionClient import ProductionClient
from DIRAC.Interfaces.API.Dirac import Dirac
from CTADIRAC.ProductionSystem.Client.SimulationElement import SimulationElement
from CTADIRAC.ProductionSystem.Client.CtapipeModelingElement import (
    CtapipeModelingElement,
)
from CTADIRAC.ProductionSystem.Client.EvnDispElement import EvnDispElement
from CTADIRAC.ProductionSystem.Client.MergingElement import MergingElement


def check_id(workflow_config):
    """Check step ID values"""
    for workflow_step in workflow_config:
        if not workflow_step.get("ID"):
            DIRAC.gLogger.error("Unknown step ID")
            DIRAC.exit(-1)
        elif not isinstance(workflow_step["ID"], int):
            DIRAC.gLogger.error("step ID must be integer")
            DIRAC.exit(-1)
    return True


def sort_by_id(workflow_config):
    """Sort workflow steps by ID"""
    return sorted(workflow_config, key=lambda k: k["ID"])


def check_parents(workflow_config):
    """Check if parent step is listed before child step"""
    for workflow_step in workflow_config:
        if workflow_step.get("parentID"):
            if workflow_step["parentID"] > workflow_step["ID"]:
                DIRAC.gLogger.error(
                    "A step can only have a parent which ID is inferior to its ID"
                )
                DIRAC.exit(-1)
    return True


def instantiate_workflow_element_from_type(workflow_step, parent_prod_step):
    """Instantiate workflow element class based on the step type required"""
    wf_elt = None
    if workflow_step["type"].lower() == "mcsimulation":
        wf_elt = SimulationElement(parent_prod_step)
    elif workflow_step["type"].lower() == "ctapipeprocessing":
        wf_elt = CtapipeModelingElement(parent_prod_step)
    elif workflow_step["type"].lower() == "evndispprocessing":
        wf_elt = EvnDispElement(parent_prod_step)
    elif workflow_step["type"].lower() == "merging":
        wf_elt = MergingElement(parent_prod_step)
    else:
        DIRAC.gLogger.error("Unknown job type")
        DIRAC.exit(-1)
    return wf_elt


def find_parent_prod_step(workflow_element_list, workflow_step):
    """Find parent prod step for a given workflow element"""
    parent_prod_step = None
    if "parentID" in workflow_step:
        if workflow_step["parentID"] is not None:
            parent_prod_step = workflow_element_list[
                workflow_step["parentID"] - 1
            ].prod_step  # Python starts indexing at 0
    return parent_prod_step


def get_parents_list(workflow_config):
    parents_list = []
    for workflow_step in workflow_config:
        if workflow_step.get("parentID"):
            parents_list.append(workflow_step["parentID"])
    return parents_list


def check_destination_catalogs(workflow_element, workflow_step, parents_list):
    """If a change in the destination catalogs is asked by the user, check that the step does not have any children.
    This function needs to be called before setting job attributes."""
    if workflow_step.get("catalogs"):
        if workflow_step["ID"] in parents_list:
            # Check that the default catalogs value is different from the catalogs value asked by the user
            # to issue an error
            if workflow_element.job.catalogs != json.dumps(
                workflow_step["catalogs"].replace(", ", ",").split(sep=",")
            ):
                DIRAC.gLogger.error(
                    "Catalogs can only be changed for production steps without any children."
                )
                DIRAC.exit(-1)
    return True


def build_workflow(workflow_config, prod_sys_client, mode):
    """For each workflow step, build the associated workflow element composed of a job and a production step"""
    workflow_element_list = []
    check_id(workflow_config["ProdSteps"])
    workflow_config["ProdSteps"] = sort_by_id(workflow_config["ProdSteps"])
    check_parents(workflow_config["ProdSteps"])
    parents_list = get_parents_list(workflow_config["ProdSteps"])
    for workflow_step in workflow_config["ProdSteps"]:
        parent_prod_step = find_parent_prod_step(workflow_element_list, workflow_step)
        workflow_element = instantiate_workflow_element_from_type(
            workflow_step, parent_prod_step
        )
        check_destination_catalogs(workflow_element, workflow_step, parents_list)
        DIRAC.gLogger.notice("\tBuilding Production step: %s" % workflow_step["type"])

        workflow_element.build_job_attributes(workflow_step)
        workflow_element.build_job_common_attributes(workflow_config)
        workflow_element.build_input_data(workflow_step, mode)
        workflow_element.build_element_config()
        workflow_element.build_output_data()

        prod_sys_client.addProductionStep(workflow_element.prod_step)
        workflow_element_list.append(workflow_element)

        # For local and wms mode : build and submit the job in the same loop
        if mode.lower() in ["wms", "local"]:
            res = Dirac().submitJob(workflow_element.job, mode=mode)
            if not res["OK"]:
                DIRAC.gLogger.error(res["Message"])
                DIRAC.exit(-1)
            DIRAC.gLogger.notice("\tSubmitted job:", res["Value"])


@Script()
def main():
    arguments = Script.getPositionalArgs()
    if len(arguments) not in list(range(2, 4)):
        Script.showHelp()

    # Read the arguments
    prod_name = arguments[0]
    workflow_config_file = arguments[1]
    mode = "ps"
    if len(arguments) == 3:
        mode = arguments[2]
    if mode not in ["ps", "wms", "local"]:
        Script.showHelp()

    with open(workflow_config_file, "r") as stream:
        workflow_config = yaml.safe_load(stream)

    ##################################
    # Create the production
    DIRAC.gLogger.notice("Building new production: %s" % prod_name)
    prod_sys_client = ProductionClient()

    ##################################
    # Build production steps according to the workflow description
    build_workflow(workflow_config, prod_sys_client, mode)
    ##################################

    # The default mode is ps, i.e. submit the worflow to the Production System
    if mode.lower() == "ps":
        # Get the production description
        prod_description = prod_sys_client.prodDescription
        # Create the production
        res = prod_sys_client.addProduction(prod_name, json.dumps(prod_description))
        if not res["OK"]:
            DIRAC.gLogger.error(res["Message"])
            DIRAC.exit(-1)

        # Start the production, i.e. instantiate the transformation steps
        res = prod_sys_client.startProduction(prod_name)

        if not res["OK"]:
            DIRAC.gLogger.error(res["Message"])
            DIRAC.exit(-1)

        DIRAC.gLogger.notice("Production %s successfully created" % prod_name)

        # Print the submitted transformations
        res = prod_sys_client.getProductionTransformations(prod_name)
        if res["OK"]:
            transList = res["Value"]
            if not transList:
                DIRAC.gLogger.notice(
                    "No transformation associated with production %s" % prod_name
                )
                DIRAC.exit(-1)
            for trans in transList:
                DIRAC.gLogger.notice(
                    "Submitted transformation:", trans["TransformationID"]
                )
        else:
            DIRAC.gLogger.error(res["Message"])
            DIRAC.exit(-1)


########################################################
if __name__ == "__main__":
    main()
