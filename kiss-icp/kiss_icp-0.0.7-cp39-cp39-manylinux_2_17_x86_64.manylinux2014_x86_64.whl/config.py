from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional

from easydict import EasyDict
import yaml

# TODO(Nacho)! Make sure that default values are read from this config file when not provided


@dataclass
class KISSConfig:
    out_dir: str = "results"
    use_cache: bool = True

    @dataclass
    class data:
        preprocess: bool = True
        correct_scan: bool = True
        max_range: float = 100.0
        min_range: float = 5.0
        lidar_frequency: float = 10.0

    @dataclass
    class mapping:
        voxel_size: float  # default: take it from data
        max_points_per_voxel: int = 20

    @dataclass
    class adaptive_threshold:
        fixed_threshold: Optional[float]
        initial_threshold: float = 1.0
        min_motion_th: float = 0.01

    @staticmethod
    def from_dict(config: Dict) -> KISSConfig:
        return EasyDict(config)


def load_config(path) -> KISSConfig:
    try:
        return EasyDict(yaml.safe_load(open(path)))
    except FileNotFoundError as err:
        raise FileNotFoundError(f"{path} file doesn't exist") from err


def write_config(config: KISSConfig, filename: str):
    with open(filename, "w") as outfile:
        yaml.dump(config.__dict__, outfile, default_flow_style=False)
