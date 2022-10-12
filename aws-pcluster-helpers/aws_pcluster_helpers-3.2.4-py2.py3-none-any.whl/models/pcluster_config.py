import yaml
from pcluster.config.cluster_config import SlurmClusterConfig
from pcluster.schemas.cluster_schema import ClusterSchema


def remove_null(d):
    if isinstance(d, list):
        for i in d:
            remove_null(i)
    elif isinstance(d, dict):
        for k, v in d.copy().items():
            if v is None:
                d.pop(k)
            else:
                remove_null(v)


class PClusterConfig(SlurmClusterConfig):
    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_yaml(cls, yaml_file: str):
        data = yaml.safe_load(open(yaml_file).read())
        del data["Tags"]
        remove_null(data)
        cluster = ClusterSchema(cluster_name="clustername").load(data)
        return cluster
