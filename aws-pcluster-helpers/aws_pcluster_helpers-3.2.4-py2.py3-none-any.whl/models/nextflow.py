import os
from typing import Dict, Optional

from aws_pcluster_helpers.models.sinfo import SInfoTable, SinfoRow
from jinja2 import Environment, BaseLoader
from pcluster import utils
from pydantic import validator

PCLUSTER_VERSION = utils.get_installed_version()

defaults = {
    "queue": None,
    "sinfo_name": None,
    "constraint": None,
    "ec2_instance_type": None,
    "gpus": None,
    # "gpu": None,
    "extra": None,
    "vcpu": None,
}


class NXFProcess(SinfoRow):
    mem_min: int = 1
    cpu_min: int = 1


class NXFSlurmConfig(SInfoTable):
    processes: Optional[Dict[str, NXFProcess]]
    default_processes: Optional[Dict[str, NXFProcess]]

    @validator("processes", pre=True, always=True)
    def set_processes(cls, v, values, **kwargs) -> Dict[str, NXFProcess]:
        nxf_processes = {}
        rows = values.get("rows", [])
        for row in rows:
            row_data = row.__dict__
            label = row_data["label"]
            nxf_processes[label] = NXFProcess(**row_data)
        return nxf_processes

    @validator("default_processes", pre=True, always=True)
    def set_default_processes(cls, v, values, **kwargs) -> Dict[str, NXFProcess]:
        # def set_default_processes(self) -> Dict[str, NXFProcess]:
        processes = values.get("processes", [])
        # processes = self.processes
        default_processes = {
            "tiny": dict(label="tiny", mem_min=1, mem=6, cpu=1, **defaults),
            "low": dict(label="low", mem_min=2, cpu_min=1, mem=12, cpu=2, **defaults),
            "medium": dict(
                label="medium", mem_min=12, cpu_min=1, mem=36, cpu=6, **defaults
            ),
            "high": dict(
                label="high", mem_min=36, cpu_min=6, mem=72, cpu=12, **defaults
            ),
            "high_mem": dict(
                label="high_memory", mem_min=72, cpu_min=12, mem=200, cpu=12, **defaults
            ),
            "long": dict(
                label="long", mem_min=12, cpu_min=1, mem=36, cpu=6, **defaults
            ),
        }
        for key in default_processes.keys():
            # this doesn't take cpu into account...
            best_match = min(
                list(processes.keys()),
                key=lambda x: abs(processes[x].mem - default_processes[key]["mem"]),
            )
            d_process = processes[best_match].__dict__
            default_processes[key].update(d_process)

        t_default_processes = {}
        for k in default_processes.keys():
            default_process = default_processes[k]
            t_default_process = NXFProcess(**default_process)
            t_default_processes[k] = t_default_process
        return t_default_processes

    def print_slurm_config(self):
        config_template_file = os.path.join(
            os.path.dirname(__file__), "_templates", "slurm.config"
        )
        if not os.path.exists(config_template_file):
            raise ValueError(f"Config template does not exist")
        with open(config_template_file, "r") as f:
            config_template = f.read()
        rtemplate = Environment(loader=BaseLoader).from_string(config_template)
        use_memory = "3.1" not in PCLUSTER_VERSION
        data = {
            "processes": self.processes,
            "default_processes": self.default_processes,
            "pcluster_version": PCLUSTER_VERSION,
            "use_memory": use_memory,
        }
        return rtemplate.render(**data)
