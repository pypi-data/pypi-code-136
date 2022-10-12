from __future__ import annotations

from typing import Mapping

from ._discovery import DiscoveryCube, DiscoveryDimension, DiscoveryHierarchy

DiscoveryHierarchyMapping = Mapping[str, DiscoveryHierarchy]
DiscoveryDimensionMapping = Mapping[str, DiscoveryHierarchyMapping]


def _get_hierarchies_mapping(
    dimension: DiscoveryDimension,
) -> DiscoveryHierarchyMapping:
    return {hierarchy["name"]: hierarchy for hierarchy in dimension["hierarchies"]}


def get_dimensions_mapping(cube: DiscoveryCube) -> DiscoveryDimensionMapping:
    """Make access to dimension by name more efficient."""
    return {
        dimension["name"]: _get_hierarchies_mapping(dimension)
        for dimension in cube["dimensions"]
    }
