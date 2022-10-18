"""
   Wrapper around the job class to build a workflow element (production step + job)
"""

__RCSID__ = "$Id$"

# generic imports
from copy import deepcopy
import json

# DIRAC imports
import DIRAC
from CTADIRAC.Interfaces.API.Prod5CtaPipeMergeJob import Prod5CtaPipeMergeJob
from CTADIRAC.ProductionSystem.Client.WorkflowElement import WorkflowElement


class MergingElement(WorkflowElement):
    """Composite class for workflow element (production step + job)"""

    #############################################################################

    def __init__(self, parent_prod_step):
        """Constructor"""
        WorkflowElement.__init__(self, parent_prod_step)
        self.job = Prod5CtaPipeMergeJob(cpuTime=259200.0)
        self.job.setOutputSandbox(["*Log.txt"])
        self.job.merged = 0
        self.prod_step.Type = "DataReprocessing"

    def get_merging_level(self):
        """Get the merging level from parent step or from the user query"""
        if self.parent_step:
            merged = self.prod_step.ParentStep.Outputquery["merged"]
        else:
            merged = self.job.merged
        return merged

    def build_job_attributes(self, workflow_step):
        """Set job attributes, with some limitations for file-specific arguments"""
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
            elif (key == "nsb") & (value is not None):
                self.job.set_output_file_metadata(key, value)
            elif (key == "split") & (value is not None):
                self.job.set_output_file_metadata(key, value)
            else:
                if value is not None:
                    setattr(self.job, key, value)

    def build_element_config(self):
        """Set job and production step attributes specific to the configuration"""
        self.prod_step.Name = "Merge"
        self.prod_step.GroupSize = self.job.group_size
        meta_data = deepcopy(self.prod_step.Inputquery)
        merged = self.get_merging_level()
        meta_data["merged"] = merged
        self.job.set_output_metadata(meta_data)
        self.job.set_executable_sequence(debug=False)
        self.prod_step.Body = self.job.workflow.toXML()

    #############################################################################
