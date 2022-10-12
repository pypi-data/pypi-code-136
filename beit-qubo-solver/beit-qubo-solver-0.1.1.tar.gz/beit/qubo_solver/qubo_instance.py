from dataclasses import dataclass
from typing import cast, Dict, Hashable, Mapping, Optional, Tuple, Union

import numpy as np

QuboInstance = Mapping[Tuple[Hashable, Hashable], Union[float, np.floating, np.integer]]

@dataclass
class QuboSolution:
    state: Tuple[int]
    energy: Optional[float]
    boltzmann_probability: Optional[float]

    @classmethod
    def from_json(cls, js: dict) -> 'QuboSolution':
        solution_mapping = cast(Tuple[int], tuple(js['state']))
        energy = float(js['energy']) if 'energy' in js else None
        boltzmann_probability = float(js['probability']) if 'probability' in js else None
        return QuboSolution(solution_mapping, energy, boltzmann_probability)
