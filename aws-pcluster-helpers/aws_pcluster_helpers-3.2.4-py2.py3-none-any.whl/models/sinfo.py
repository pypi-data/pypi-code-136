from typing import Any
from typing import List, Optional

import pandas as pd
from aws_pcluster_helpers import (
    PClusterConfig,
    PClusterInstanceTypes,
    InstanceTypesMappings,
    size_in_gib,
)
from aws_pcluster_helpers.models.config import PClusterConfigFiles
from aws_pcluster_helpers.utils.logging import setup_logger
from pcluster.config.cluster_config import SlurmClusterConfig
from pydantic import BaseModel
from pydantic import validator
from rich.table import Table

logger = setup_logger(logger_name="sinfo")


class SinfoRow(BaseModel):
    sinfo_name: Optional[str]
    label: Optional[str]
    queue: Optional[str]
    constraint: Optional[str]
    ec2_instance_type: Optional[str]
    mem: Optional[int]
    mem_mib: Optional[int]
    cpu: Optional[int]
    scheduleable_memory: Optional[int] = 0.95
    scheduleable_memory_mib: Optional[int]
    scheduleable_memory_gib: Optional[int]
    vcpu: Optional[int]
    gpus: Optional[List]
    extra: Optional[dict]


# TODO add custom ami lookup


class SInfoTable(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    table_columns: List[Any] = [
        {"label": "Queue", "key": "queue"},
        {"label": "Constraint", "key": "constraint"},
        {"label": "Mem(Gib)", "key": "mem"},
        {"label": "VCPU", "key": "vcpu"},
        {"label": "CPU", "key": "cpu"},
        {"label": "EC2", "key": "ec2_instance_type"},
    ]
    pcluster_config_files: PClusterConfigFiles = PClusterConfigFiles()
    instance_type_mappings: Optional[InstanceTypesMappings]
    pcluster_instance_types: Optional[PClusterInstanceTypes]
    pcluster_config: Optional[SlurmClusterConfig]
    rows: Optional[List[SinfoRow]]
    dataframe: Optional[pd.DataFrame]

    @validator("instance_type_mappings", pre=True, always=True)
    def set_instance_type_mappings(cls, v, values, **kwargs):
        pcluster_config_files = values.get("pcluster_config_files")
        return InstanceTypesMappings.from_json(
            pcluster_config_files.instance_name_type_mappings_file
        )

    @validator("pcluster_instance_types", pre=True, always=True)
    def set_pcluster_instance_types(cls, v, values, **kwargs):
        pcluster_config_files = values.get("pcluster_config_files")
        return PClusterInstanceTypes.from_json(
            pcluster_config_files.instance_types_data_file
        )

    @validator("pcluster_config", pre=True, always=True)
    def set_pcluster_config(cls, v, values, **kwargs):
        pcluster_config_files = values.get("pcluster_config_files")
        return PClusterConfig.from_yaml(pcluster_config_files.pcluster_config_file)

    @validator("rows", pre=True, always=True)
    def set_rows(cls, v, values, **kwargs) -> List[SinfoRow]:
        pcluster_config_files = values.get("pcluster_config_files")
        instance_types_mappings = values.get("instance_type_mappings")
        pcluster_instance_types = values.get("pcluster_instance_types")
        pcluster_config = values.get("pcluster_config")

        sinfo_records = []
        for slurm_queue in pcluster_config.scheduling.queues:
            compute_resources = slurm_queue.compute_resources
            queue = slurm_queue.name
            for compute_resource in compute_resources:
                sinfo_label = {}
                sinfo_instance_type = compute_resource.name
                ec2_instance_type = instance_types_mappings.sinfo_instance_types[
                    sinfo_instance_type
                ]["ec2_instance_type"]
                pcluster_instance_type = pcluster_instance_types.instance_type_data.get(
                    ec2_instance_type
                )
                mem_in_mib = pcluster_instance_type.data["data"]["MemoryInfo"][
                    "SizeInMiB"
                ]
                mem_in_gib = size_in_gib(mem_in_mib)
                gpus = []
                if "GpuInfo" in pcluster_instance_type.data["data"]:
                    gpu = pcluster_instance_type.data["data"]["GpuInfo"]
                    gpu_total_mem_in_mib = gpu["TotalGpuMemoryInMiB"]
                    gpu_total_mem_in_gib = size_in_gib(gpu_total_mem_in_mib)
                    gpu["TotalGpuMemoryInGiB"] = gpu_total_mem_in_gib
                    gpus.append(gpu)
                cpu = pcluster_instance_type.data["data"]["VCpuInfo"]["DefaultCores"]
                vcpu = pcluster_instance_type.data["data"]["VCpuInfo"]["DefaultVCpus"]
                p_type = "dy"
                if compute_resource.min_count > 0:
                    p_type = "st"
                label = f"{slurm_queue.name.replace('-', '_')}_{p_type}__{ec2_instance_type.replace('.', '_')}"
                sinfo_name = f"{slurm_queue.name}-{p_type}-{sinfo_instance_type}"

                sinfo_label["name"] = label
                sinfo_label["max_mem"] = int(mem_in_gib)
                sinfo_label["max_cpu"] = cpu
                sinfo_label["queue"] = queue
                sinfo_label["constraint"] = sinfo_instance_type
                sinfo_label["vcpu"] = vcpu
                scheduleable_memory = getattr(
                    compute_resource, "scheduleable_memory", 0.95
                )
                scheduleable_memory_mib = mem_in_mib * scheduleable_memory
                scheduleable_memory_gib = mem_in_gib * scheduleable_memory

                sinfo_records.append(
                    SinfoRow(
                        mem=int(mem_in_gib),
                        mem_mib=int(mem_in_mib),
                        cpu=cpu,
                        scheduleable_memory=scheduleable_memory,
                        scheduleable_memory_mib=scheduleable_memory_mib,
                        scheduleable_memory_gib=scheduleable_memory_gib,
                        vcpu=vcpu,
                        sinfo_name=sinfo_name,
                        queue=queue,
                        constraint=sinfo_instance_type,
                        ec2_instance_type=ec2_instance_type,
                        label=label,
                        gpus=gpus,
                        extra={},
                        # gpu=None,
                    )
                )
        return sinfo_records

    @validator("dataframe", pre=True, always=True)
    def set_dataframe(cls, v, values, **kwargs) -> pd.DataFrame:
        records = []
        rows = values.get("rows")
        for record in rows:
            records.append(record.__dict__)
        df = pd.DataFrame.from_records(records)
        df.sort_values(by=["queue", "mem", "vcpu", "cpu"], inplace=True)
        return df

    def get_table(self):
        if not len(self.rows):
            logger.error(f"SLURM SInfo - none found... exiting")
            raise ValueError(f"SLURM SInfo - none found ... exiting")

        table = Table(title="SLURM SInfo", show_lines=True)
        colors = [
            "turquoise4",
            "purple4",
            "deep_sky_blue3",
            "hot_pink3",
            "dodger_blue1",
        ]
        queue_colors = {}
        for column in self.table_columns:
            table.add_column(column["label"], justify="right", no_wrap=True)
        table.add_column("SBATCH", justify="left")
        colors_index = 0
        for row in self.dataframe.to_records():
            if colors_index == len(colors):
                colors_index = 0
            t_row = []
            if row["queue"] not in queue_colors:
                queue_colors[row["queue"]] = colors[colors_index]
            queue = row["queue"]
            constraint = row["constraint"]
            cpus = row["cpu"]
            vcpus = row["vcpu"]
            color = queue_colors[row["queue"]]
            for t in self.table_columns:
                key = t["key"]
                value = row[key]
                t_row.append(f"[{color}]{str(value)}")
            t_row.append(
                f"[{color}]#SBATCH --exclusive --partition={queue}\n#SBATCH --constraint={constraint}\n#SBATCH -c={vcpus}"
            )
            table.add_row(*t_row)
            colors_index = colors_index + 1

        return table
