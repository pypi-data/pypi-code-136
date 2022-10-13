"""FeaturesSets classes Module"""

from dataclasses import dataclass, field
from typing import Dict

@dataclass(init=False)
class VariableFeaturesSet:
    """Class to hold features extracted from a variable."""
    is_quantitative: bool = False
    missing_entries_ratio: float = 0

@dataclass(init=False)
class DataFeaturesSet:
    """Class to hold features extracted from a dataset."""
    rows_count: int = 0
    variables_count: int = 0
    ratio_of_continous_variables: float = 0
    is_response_quantitative: bool = False
    is_response_dichotomous: bool = False
    variables_features_set: Dict[str, VariableFeaturesSet] = field(
        default_factory= dict()
    )
