# SPDX-License-Identifier: GPL-3.0-or-later

# Data structure for querying URL patterns.
#
# This file is part of Hydrilla&Haketilo.
#
# Copyright (C) 2021, 2022 Wojtek Kosior
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
This module defines data structures for querying data using URL patterns.
"""

import typing as t
import dataclasses as dc

from immutables import Map

from .url_patterns import ParsedPattern, ParsedUrl, parse_url#, catchall_pattern
from .translations import smart_gettext as _


WrapperStoredType = t.TypeVar('WrapperStoredType', bound=t.Hashable)

@dc.dataclass(frozen=True, unsafe_hash=True, order=True)
class StoredTreeItem(t.Generic[WrapperStoredType]):
    """
    In the Pattern Tree, each item is stored together with the pattern used to
    register it.
    """
    item:    WrapperStoredType
    pattern: ParsedPattern


NodeStoredType = t.TypeVar('NodeStoredType')

@dc.dataclass(frozen=True)
class PatternTreeNode(t.Generic[NodeStoredType]):
    """...."""
    SelfType = t.TypeVar('SelfType', bound='PatternTreeNode[NodeStoredType]')

    ChildrenType = Map[str, SelfType]

    children:      'ChildrenType'             = Map()
    literal_match: t.Optional[NodeStoredType] = None

    def is_empty(self) -> bool:
        """...."""
        return len(self.children) == 0 and self.literal_match is None

    def update_literal_match(
            self:           'SelfType',
            new_match_item: t.Optional[NodeStoredType]
    ) -> 'SelfType':
        """...."""
        return dc.replace(self, literal_match=new_match_item)

    def get_child(self: 'SelfType', child_key: str) -> t.Optional['SelfType']:
        """...."""
        return self.children.get(child_key)

    def remove_child(self: 'SelfType', child_key: str) -> 'SelfType':
        """...."""
        try:
            children = self.children.delete(child_key)
        except:
            children = self.children

        return dc.replace(self, children=children)

    def set_child(self: 'SelfType', child_key: str, child: 'SelfType') \
        -> 'SelfType':
        """...."""
        return dc.replace(self, children=self.children.set(child_key, child))


BranchStoredType = t.TypeVar('BranchStoredType')

BranchItemUpdater = t.Callable[
    [t.Optional[BranchStoredType]],
    t.Optional[BranchStoredType]
]

@dc.dataclass(frozen=True)
class PatternTreeBranch(t.Generic[BranchStoredType]):
    """...."""
    SelfType = t.TypeVar(
        'SelfType',
        bound = 'PatternTreeBranch[BranchStoredType]'
    )

    root_node: PatternTreeNode[BranchStoredType] = PatternTreeNode()

    def is_empty(self) -> bool:
        """...."""
        return self.root_node.is_empty()

    def update(
            self:         'SelfType',
            segments:     t.Iterable[str],
            item_updater: BranchItemUpdater
    ) -> 'SelfType':
        """
        .......
        """
        node = self.root_node
        nodes_segments = []

        for segment in segments:
            next_node = node.get_child(segment)

            nodes_segments.append((node, segment))

            node = PatternTreeNode() if next_node is None else next_node

        node = node.update_literal_match(item_updater(node.literal_match))

        while nodes_segments:
            prev_node, segment = nodes_segments.pop()

            if node.is_empty():
                node = prev_node.remove_child(segment)
            else:
                node = prev_node.set_child(segment, node)

        return dc.replace(self, root_node=node)

    def search(self, segments: t.Sequence[str]) -> t.Iterable[BranchStoredType]:
        """
        Yields all matches of this segments sequence against the tree. Results
        are produced in order from greatest to lowest pattern specificity.
        """
        nodes = [self.root_node]

        for segment in segments:
            next_node = nodes[-1].get_child(segment)
            if next_node is None:
                break

            nodes.append(next_node)

        nsegments = len(segments)
        cond_literal = lambda: len(nodes) == nsegments
        cond_wildcard = [
            lambda: len(nodes) + 1 == nsegments and segments[-1] != '*',
            lambda: len(nodes) + 1 <  nsegments,
            lambda: len(nodes) + 1 != nsegments or  segments[-1] != '***'
        ]

        while nodes:
            node = nodes.pop()

            wildcard_matches = [node.get_child(wc) for wc in ('*', '**', '***')]

            for match_node, condition in [
                    (node, cond_literal),
                    *zip(wildcard_matches, cond_wildcard)
            ]:
                if match_node is not None:
                    if match_node.literal_match is not None:
                        if condition():
                            yield match_node.literal_match


FilterStoredType  = t.TypeVar('FilterStoredType', bound=t.Hashable)
FilterWrappedType = StoredTreeItem[FilterStoredType]

def filter_by_trailing_slash(
        items: t.Iterable[FilterWrappedType],
        with_slash: bool
) -> t.FrozenSet[FilterWrappedType]:
    """...."""
    return frozenset(wrapped for wrapped in items
                     if with_slash == wrapped.pattern.has_trailing_slash)

TreeStoredType = t.TypeVar('TreeStoredType', bound=t.Hashable)

StoredSet      = t.FrozenSet[StoredTreeItem[TreeStoredType]]
PathBranch     = PatternTreeBranch[StoredSet]
DomainBranch   = PatternTreeBranch[PathBranch]
TreeRoot       = Map[t.Tuple[str, t.Optional[int]], DomainBranch]

@dc.dataclass(frozen=True)
class PatternTree(t.Generic[TreeStoredType]):
    """
    "Pattern Tree" is how we refer to the data structure used for querying
    Haketilo patterns. Those look like 'https://*.example.com/ab/***'. The goal
    is to make it possible to quickly retrieve all known patterns that match
    a given URL.
    """
    SelfType = t.TypeVar('SelfType', bound='PatternTree[TreeStoredType]')

    _by_scheme_and_port: TreeRoot = Map()

    def _register(
            self:           'SelfType',
            parsed_pattern: ParsedPattern,
            item:           TreeStoredType,
            register:       bool = True
    ) -> 'SelfType':
        """
        Make an item wrapped in StoredTreeItem object queryable through the
        Pattern Tree by the given parsed URL pattern.
        """
        wrapped_item = StoredTreeItem(item, parsed_pattern)

        def item_updater(item_set: t.Optional[StoredSet]) \
            -> t.Optional[StoredSet]:
            """...."""
            if item_set is None:
                item_set = frozenset()

            if register:
                item_set = item_set.union((wrapped_item,))
            else:
                item_set = item_set.difference((wrapped_item,))

            return None if len(item_set) == 0 else item_set

        def path_branch_updater(path_branch: t.Optional[PathBranch]) \
            -> t.Optional[PathBranch]:
            """...."""
            if path_branch is None:
                path_branch = PatternTreeBranch()

            path_branch = path_branch.update(
                parsed_pattern.path_segments,
                item_updater
            )

            return None if path_branch.is_empty() else path_branch

        key         = (parsed_pattern.scheme, parsed_pattern.port)
        domain_tree = self._by_scheme_and_port.get(key, PatternTreeBranch())

        new_domain_tree = domain_tree.update(
            parsed_pattern.domain_labels,
            path_branch_updater
        )

        if new_domain_tree.is_empty():
            try:
                new_root = self._by_scheme_and_port.delete(key)
            except KeyError:
                new_root = self._by_scheme_and_port
        else:
            new_root = self._by_scheme_and_port.set(key, new_domain_tree)

        return dc.replace(self, _by_scheme_and_port=new_root)

    def register(
            self:           'SelfType',
            parsed_pattern: ParsedPattern,
            item:           TreeStoredType
    ) -> 'SelfType':
        """
        Make item queryable through the Pattern Tree by the given URL pattern.
        """
        return self._register(parsed_pattern, item)

    def deregister(
            self:           'SelfType',
            parsed_pattern: ParsedPattern,
            item:           TreeStoredType
    ) -> 'SelfType':
        """
        Make item no longer queryable through the Pattern Tree by the given URL
        pattern.
        """
        return self._register(parsed_pattern, item, register=False)

    def search(self, url: t.Union[ParsedUrl, str]) -> t.Iterable[StoredSet]:
        """
        ....
        """
        parsed_url = parse_url(url) if isinstance(url, str) else url

        key = (parsed_url.scheme, parsed_url.port)
        domain_tree = self._by_scheme_and_port.get(key)
        if domain_tree is None:
            return

        if parsed_url.has_trailing_slash:
            slash_options = [True, False]
        else:
            slash_options = [False]

        for path_tree in domain_tree.search(parsed_url.domain_labels):
            for item_set in path_tree.search(parsed_url.path_segments):
                for with_slash in slash_options:
                    items = filter_by_trailing_slash(item_set, with_slash)
                    if len(items) > 0:
                        yield items
