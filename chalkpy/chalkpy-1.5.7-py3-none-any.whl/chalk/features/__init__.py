from typing import Optional, List

from .dataframe import DataFrame, DataFrameMeta
from .feature import (
    ChalkTime,
    Feature,
    Features,
    FeatureSetBase,
    Filter,
    after,
    before,
    unwrap_feature,
    unwrap_features,
    unwrap_features_or_none,
    unwrap_feature_or_none,
    process_unwrapped,
)
from .feature_set import feature, feature_time, features, has_many, has_one
from .hooks import after_all, before_all
from .resolver import Cron, MachineType, ScheduleOptions, offline, online, sink
from .tag import Environments, Tags
from ..feature_n import Feature2


def is_primary(f) -> bool:
    """
    Determine whether a feature is a primary key
    :param f: A feature (ie. User.email)
    :return: True if the feature is primary and False otherwise
    """
    return unwrap_feature(f).primary


def owner(f) -> Optional[str]:
    """
    Get the owner for a feature or feature class
    :param f: A feature (ie. User.email or User)
    :return: The owner for a feature or feature class, if it exists.
    Note that the owner could be inherited from the feature class.
    """
    return process_unwrapped(f, lambda x: x.__chalk_owner__, lambda y: y.owner)


def description(f) -> Optional[str]:
    """
    Get the description of a feature or feature class
    :param f: A feature or feature class (ie. User.email or User)
    :return: The description given for the feature or feature class.
    """
    return process_unwrapped(f, lambda x: x.__doc__, lambda y: y.description)


def tags(f) -> Optional[List[str]]:
    """
    Get the tags for a feature or feature class
    :param f: A feature or feature class (ie. User.email or User)
    :return: The tags given for the feature or feature class
    Note that the owner can be inherited from the feature class.
    """
    return process_unwrapped(f, lambda x: x.__chalk_tags__, lambda y: y.tags)


__all__ = [
    "ChalkTime",
    "Cron",
    "DataFrame",
    "DataFrameMeta",
    "Environments",
    "Feature",
    "Feature2",
    "FeatureSetBase",
    "Features",
    "Filter",
    "MachineType",
    "ScheduleOptions",
    "Tags",
    "after",
    "after_all",
    "before",
    "before_all",
    "description",
    "feature",
    "feature_time",
    "features",
    "has_many",
    "has_one",
    "is_primary",
    "offline",
    "online",
    "owner",
    "sink",
    "tags",
]
