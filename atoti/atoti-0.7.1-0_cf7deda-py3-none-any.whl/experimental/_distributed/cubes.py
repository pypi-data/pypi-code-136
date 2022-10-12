from dataclasses import dataclass

from atoti_core import keyword_only_dataclass
from typeguard import typeguard_ignore

from ..._local_cubes import LocalCubes
from .cube import DistributedCube


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class DistributedCubes(LocalCubes[DistributedCube]):
    """Manage the distributed cubes."""
