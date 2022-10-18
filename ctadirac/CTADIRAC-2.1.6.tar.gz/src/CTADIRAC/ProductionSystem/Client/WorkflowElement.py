"""
   Wrapper around the job class to build a workflow element (production step + job)
"""

__RCSID__ = "$Id$"

# generic imports
import json

# DIRAC imports
import DIRAC
from DIRAC.Interfaces.API.Job import Job
from DIRAC.ProductionSystem.Client.ProductionStep import ProductionStep
from CTADIRAC.Core.Utilities.tool_box import get_dataset_MQ
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

class WorkflowElement:
    """Composite class for workflow element (production step + job)"""

    #############################################################################

    def __init__(self, parent_prod_step):
        """Constructor"""
        self.job = Job()
        self.prod_step = ProductionStep()
        self.prod_step.ParentStep = parent_prod_step
        self.fc = FileCatalogClient()

    def build_job_attributes(self, workflow_step):
        """Set job attributes"""
        for key, value in workflow_step.items():
            if key == "version":
                if value is None:
                    DIRAC.gLogger.error(
                        "Unknown software version for ProdStep %s" % workflow_step["ID"]
                    )
                    DIRAC.exit(-1)
                else:
                    self.job.version = value
            elif (key == "catalogs") & (value is not None):
                # remove whitespaces between catalogs if there are some and separate between commas
                setattr(
                    self.job, key, json.dumps(value.replace(", ", ",").split(sep=","))
                )
            else:
                if value is not None:
                    setattr(self.job, key, value)

    def build_job_common_attributes(self, workflow_config):
        """Set job attributes concerning the whole production"""
        if "base_path" in workflow_config["Common"]:
            if workflow_config["Common"]["base_path"]:
                self.job.base_path = workflow_config["Common"]["base_path"]
        if "MCCampaign" in workflow_config["Common"]:
            if workflow_config["Common"]["MCCampaign"]:
                self.job.MCCampaign = workflow_config["Common"]["MCCampaign"]
            else:
                DIRAC.gLogger.error("MCCampaign is mandatory")
                DIRAC.exit(-1)
        if "configuration_id" in workflow_config["Common"]:
            if workflow_config["Common"]["configuration_id"]:
                self.job.configuration_id = workflow_config["Common"]["configuration_id"]
            else:
                DIRAC.gLogger.error("configuration_id is mandatory")
                DIRAC.exit(-1)

    def build_input_data(self, workflow_step, mode):
        """Build input data from the parent output data or from the dataset metadata"""
        if self.prod_step.ParentStep:
            self.prod_step.Inputquery = self.prod_step.ParentStep.Outputquery
            for key, value in self.job.output_file_metadata.items():
                self.prod_step.Inputquery[key] = value

        else:
            if workflow_step.get("dataset"):
                self.prod_step.Inputquery = get_dataset_MQ(workflow_step["dataset"])

            else:
                DIRAC.gLogger.error(
                    "A step without parent step must take a dataset as input"
                )
                DIRAC.exit(-1)

        if mode.lower() in ["wms", "local"]:
            res = self.fc.findFilesByMetadata(dict(self.prod_step.Inputquery))
            if not res["OK"]:
                DIRAC.gLogger.error(res["Message"])
                DIRAC.exit(-1)
            input_data = res["Value"]
            if mode.lower() == "local":
                self.job.setInputData(input_data)
            elif not input_data:
                DIRAC.gLogger.error("No job submitted: job must have input data")
                DIRAC.exit(-1)

    def build_output_data(self):
        """Build output data from the job metadata and the metadata added on the files"""
        self.prod_step.Outputquery = self.job.output_metadata
        for key, value in self.job.output_file_metadata.items():
            self.prod_step.Outputquery[key] = value


#############################################################################
