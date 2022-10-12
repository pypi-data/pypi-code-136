# SPDX-License-Identifier: GPL-3.0-or-later

# Haketilo proxy payloads dependency resolution.
#
# This file is part of Hydrilla&Haketilo.
#
# Copyright (C) 2022 Wojtek Kosior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
# I, Wojtek Kosior, thereby promise not to sue for violation of this
# file's license. Although I request that you do not make use of this
# code in a proprietary program, I am not going to enforce this in
# court.

"""
This module contains logic to construct the dependency graph of Haketilo
packages and to perform dependency resolution.

The approach taken here is a very simplified one. Hopefully, this will at some
point be replaced by a solution based on some SAT solver.
"""

import dataclasses as dc
import typing as t
import functools as ft

from immutables import Map

from ..exceptions import HaketiloException
from .. import item_infos
from .. import url_patterns


@dc.dataclass(frozen=True)
class ImpossibleSituation(HaketiloException):
    bad_mapping_identifiers: frozenset[str]


@dc.dataclass(frozen=True)
class MappingRequirement:
    identifier: str

    def is_fulfilled_by(self, info: item_infos.MappingInfo) -> bool:
        return True

@dc.dataclass(frozen=True)
class MappingRepoRequirement(MappingRequirement):
    repo: str

    def is_fulfilled_by(self, info: item_infos.MappingInfo) -> bool:
        return info.repo == self.repo

@dc.dataclass(frozen=True)
class MappingVersionRequirement(MappingRequirement):
    version_info: item_infos.MappingInfo

    def __post_init__(self):
        assert self.version_info.identifier == self.identifier

    def is_fulfilled_by(self, info: item_infos.MappingInfo) -> bool:
        return info == self.version_info


@dc.dataclass(frozen=True)
class ResourceVersionRequirement:
    mapping_identifier: str
    version_info:       item_infos.ResourceInfo

    def is_fulfilled_by(self, info: item_infos.ResourceInfo) -> bool:
        return info == self.version_info


@dc.dataclass
class ComputedPayload:
    mapping_identifier: str

    resources: list[item_infos.ResourceInfo] = dc.field(default_factory=list)

    allows_eval:        bool = False
    allows_cors_bypass: bool = False

@dc.dataclass
class MappingChoice:
    info:                 item_infos.MappingInfo
    required:             bool                               = False
    mapping_dependencies: t.Sequence[item_infos.MappingInfo] = ()

    payloads: dict[url_patterns.ParsedPattern, ComputedPayload] = \
        dc.field(default_factory=dict)


MappingsGraph = t.Union[
    t.Mapping[str, set[str]],
    t.Mapping[str, frozenset[str]]
]

def _mark_mappings(
        identifier:      str,
        mappings_graph:  MappingsGraph,
        marked_mappings: set[str]
) -> None:
    if identifier in marked_mappings:
        return

    marked_mappings.add(identifier)

    for next_mapping in mappings_graph.get(identifier, ()):
            _mark_mappings(next_mapping, mappings_graph, marked_mappings)


ComputedChoices = dict[str, MappingChoice]

def _compute_inter_mapping_deps(choices: ComputedChoices) \
    -> dict[str, frozenset[str]]:
    mapping_deps: dict[str, frozenset[str]] = {}

    for mapping_choice in choices.values():
        specs_to_resolve = [*mapping_choice.info.required_mappings]

        for computed_payload in mapping_choice.payloads.values():
            for resource_info in computed_payload.resources:
                specs_to_resolve.extend(resource_info.required_mappings)

        depended = frozenset(spec.identifier for spec in specs_to_resolve)
        mapping_deps[mapping_choice.info.identifier] = depended

    return mapping_deps

@dc.dataclass(frozen=True)
class _ComputationData:
    resources_map: item_infos.MultirepoResourceInfoMap
    mappings_map:  item_infos.MultirepoMappingInfoMap

    mappings_to_reqs: t.Mapping[str, t.Sequence[MappingRequirement]]

    mappings_resources_to_reqs: t.Mapping[
        tuple[str, str],
        t.Sequence[ResourceVersionRequirement]
    ]

    def _satisfy_payload_resource_rec(
            self,
            resource_identifier: str,
            processed_resources: set[str],
            computed_payload:    ComputedPayload
    ) -> t.Optional[ComputedPayload]:
        if resource_identifier in processed_resources:
            # We forbid circular dependencies.
            return None

        multirepo_info = self.resources_map.get(resource_identifier)
        if multirepo_info is None:
            return None

        key = (computed_payload.mapping_identifier, resource_identifier)
        resource_reqs = self.mappings_resources_to_reqs.get(key)

        if resource_reqs is None:
            info = multirepo_info.default_info
        else:
            found = False
            # From newest to oldest version.
            for info in multirepo_info.get_all(reverse_versions=True):
                if all(req.is_fulfilled_by(info) for req in resource_reqs):
                    found = True
                    break

            if not found:
                return None

        if info in computed_payload.resources:
            return computed_payload

        processed_resources.add(resource_identifier)

        if info.allows_eval:
            computed_payload.allows_eval = True

        if info.allows_cors_bypass:
            computed_payload.allows_cors_bypass = True

        for dependency_spec in info.dependencies:
            if self._satisfy_payload_resource_rec(
                    dependency_spec.identifier,
                    processed_resources,
                    computed_payload
            ) is None:
                return None

        processed_resources.remove(resource_identifier)

        computed_payload.resources.append(info)

        return computed_payload

    def _satisfy_payload_resource(
            self,
            mapping_identifier:  str,
            resource_identifier: str
    ) -> t.Optional[ComputedPayload]:
        return self._satisfy_payload_resource_rec(
            resource_identifier,
            set(),
            ComputedPayload(mapping_identifier)
        )

    def _compute_best_choices(self) -> ComputedChoices:
        choices = ComputedChoices()

        for multirepo_info in self.mappings_map.values():
            choice: t.Optional[MappingChoice] = None

            reqs = self.mappings_to_reqs.get(multirepo_info.identifier)
            if reqs is None:
                choice = MappingChoice(multirepo_info.default_info)
            else:
                # From newest to oldest version.
                for info in multirepo_info.get_all(reverse_versions=True):
                    if all(req.is_fulfilled_by(info) for req in reqs):
                        choice = MappingChoice(info=info, required=True)
                        break

                if choice is None:
                    continue

            failure = False

            for pattern, resource_spec in choice.info.payloads.items():
                computed_payload = self._satisfy_payload_resource(
                    mapping_identifier  = choice.info.identifier,
                    resource_identifier = resource_spec.identifier
                )
                if computed_payload is None:
                    failure = True
                    break

                if choice.info.allows_eval:
                    computed_payload.allows_eval = True

                if choice.info.allows_cors_bypass:
                    computed_payload.allows_cors_bypass = True

                choice.payloads[pattern] = computed_payload

            if not failure:
                choices[choice.info.identifier] = choice

        return choices

    def compute_payloads(self) -> ComputedChoices:
        choices = self._compute_best_choices()

        mapping_deps = _compute_inter_mapping_deps(choices)

        reverse_deps: dict[str, set[str]] = {}

        for depending, depended_set in mapping_deps.items():
            for depended in depended_set:
                reverse_deps.setdefault(depended, set()).add(depending)

        bad_mappings: set[str] = set()

        for depended_identifier in reverse_deps.keys():
            if depended_identifier not in choices:
                _mark_mappings(depended_identifier, reverse_deps, bad_mappings)

        bad_required_mappings: list[str] = []

        for identifier in self.mappings_to_reqs.keys():
            if identifier in bad_mappings or identifier not in choices:
                bad_required_mappings.append(identifier)

        if len(bad_required_mappings) > 0:
            raise ImpossibleSituation(frozenset(bad_required_mappings))

        for identifier in bad_mappings:
            choices.pop(identifier, None)

        required_mappings: set[str] = set()

        for identifier in self.mappings_to_reqs.keys():
            _mark_mappings(identifier, mapping_deps, required_mappings)

        for identifier in required_mappings:
            choices[identifier].required = True

        for mapping_choice in choices.values():
            depended_set = mapping_deps[mapping_choice.info.identifier]
            mapping_choice.mapping_dependencies = \
                tuple(choices[identifier].info for identifier in depended_set)

        return choices

def compute_payloads(
        resources:             t.Iterable[item_infos.ResourceInfo],
        mappings:              t.Iterable[item_infos.MappingInfo],
        mapping_requirements:  t.Iterable[MappingRequirement],
        resource_requirements: t.Iterable[ResourceVersionRequirement]
) -> ComputedChoices:
    resources_map: item_infos.MultirepoResourceInfoMap = \
        ft.reduce(item_infos.register_in_multirepo_map, resources, Map())
    mappings_map: item_infos.MultirepoMappingInfoMap = \
        ft.reduce(item_infos.register_in_multirepo_map, mappings, Map())

    mappings_to_reqs: dict[str, list[MappingRequirement]] = {}
    for mapping_req in mapping_requirements:
        mappings_to_reqs.setdefault(mapping_req.identifier, [])\
            .append(mapping_req)

    mappings_resources_to_reqs: dict[
        tuple[str, str],
        list[ResourceVersionRequirement]
    ] = {}
    for resource_req in resource_requirements:
        info = resource_req.version_info
        key = (resource_req.mapping_identifier, info.identifier)
        mappings_resources_to_reqs.setdefault(key, [])\
            .append(resource_req)

    return _ComputationData(
        mappings_map               = mappings_map,
        resources_map              = resources_map,
        mappings_to_reqs           = mappings_to_reqs,
        mappings_resources_to_reqs = mappings_resources_to_reqs
    ).compute_payloads()
