# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import pytest
import re
import dataclasses as dc

from immutables import Map

from hydrilla import pattern_tree

from .url_patterns_common import *

@pytest.mark.parametrize('_in, out', [
    (Map(),                                                  True),
    ({'children': Map(non_empty='non_emtpy')},               False),
    ({'literal_match': 'non-None'},                          False),
    ({'children': Map(non_empty='non_emtpy')},               False),
    ({'literal_match': 'non-None', 'children': 'non-empty'}, False)
])
def test_pattern_tree_node_is_empty(_in, out):
    """...."""
    assert pattern_tree.PatternTreeNode(**_in).is_empty() == out

def test_pattern_tree_node_update_literal_match():
    """...."""
    node1 = pattern_tree.PatternTreeNode()
    node2 = node1.update_literal_match('dummy match item')

    assert node1.literal_match is None
    assert node2.literal_match == 'dummy match item'

def test_pattern_tree_node_get_child():
    """...."""
    node = pattern_tree.PatternTreeNode(children=Map(dummy_key='dummy_val'))

    assert node.get_child('dummy_key') == 'dummy_val'
    assert node.get_child('other_key') is None

def test_pattern_tree_node_remove_child():
    """...."""
    node1 = pattern_tree.PatternTreeNode(children=Map(dummy_key='dummy_val'))
    node2 = node1.remove_child('dummy_key')

    assert node1.children == Map(dummy_key='dummy_val')
    assert node2.children == Map()

def test_pattern_tree_node_set_child():
    """...."""
    node1 = pattern_tree.PatternTreeNode(children=Map(dummy_key='dummy_val'))
    node2 = node1.set_child('other_key', 'other_val')

    assert node1.children == Map(dummy_key='dummy_val')
    assert node2.children == Map(dummy_key='dummy_val', other_key='other_val')

@pytest.mark.parametrize('root_empty', [True, False])
def test_pattern_tree_branch_is_empty(root_empty):
    """...."""
    class DummyEmptyRoot:
        """...."""
        is_empty = lambda: root_empty

    branch = pattern_tree.PatternTreeBranch(root_node=DummyEmptyRoot)
    assert branch.is_empty() == root_empty

# def test_pattern_tree_branch_copy():
#     """...."""
#     class DummyRoot:
#         """...."""
#         pass

#     branch1 = pattern_tree.PatternTreeBranch(root_node=DummyRoot)
#     branch2 = branch1.copy()

#     assert branch1 is not branch2
#     for val_b1, val_b2 in zip(dc.astuple(branch1), dc.astuple(branch2)):
#         assert val_b1 is val_b2

@pytest.fixture
def empty_branch():
    """...."""
    return pattern_tree.PatternTreeBranch(
        root_node = pattern_tree.PatternTreeNode()
    )

@pytest.fixture
def branch_with_a_b():
    """...."""
    return pattern_tree.PatternTreeBranch(
        root_node = pattern_tree.PatternTreeNode(
            children = Map(
                a = pattern_tree.PatternTreeNode(
                    children = Map(
                        b = pattern_tree.PatternTreeNode(
                            literal_match = frozenset({'myitem'})
                        )
                    )
                )
            )
        )
    )

def test_pattern_tree_branch_update_add_first(empty_branch, branch_with_a_b):
    """...."""
    updated_branch = empty_branch.update(
        ['a', 'b'],
        lambda s: frozenset({*(s or []), 'myitem'})
    )

    assert updated_branch                  == branch_with_a_b
    assert empty_branch.root_node.children == Map()

def test_pattern_tree_branch_update_add_second(branch_with_a_b):
    """...."""
    updated_branch = branch_with_a_b.update(
        ['a', 'b'],
        lambda s: frozenset({*(s or []), 'myotheritem'})
    )

    leaf_node = updated_branch.root_node.children['a'].children['b']
    assert leaf_node.literal_match == frozenset({'myitem', 'myotheritem'})

def test_pattern_tree_branch_update_add_different_path(branch_with_a_b):
    """...."""
    updated_branch = branch_with_a_b.update(
        ['a', 'not_b'],
        lambda s: frozenset({*(s or []), 'myotheritem'})
    )

    for segment, item in [('b', 'myitem'), ('not_b', 'myotheritem')]:
        leaf_node = updated_branch.root_node.children['a'].children[segment]
        assert leaf_node.literal_match == frozenset({item})

# def test_pattern_tree_branch_update_is_value_copied(branch_with_a_b):
#     """...."""
#     updated_branch = branch_with_a_b.update(['a', 'b'], lambda s: s)

#     leaf_node_orig = updated_branch.root_node.children['a'].children['b']
#     leaf_node_new  = branch_with_a_b.root_node.children['a'].children['b']

#     assert leaf_node_orig.literal_match == leaf_node_new.literal_match
#     assert leaf_node_orig.literal_match is not leaf_node_new.literal_match

def test_pattern_tree_branch_remove(branch_with_a_b, empty_branch):
    """...."""
    updated_branch = branch_with_a_b.update(['a', 'b'], lambda s: None)

    assert updated_branch == empty_branch

def test_pattern_tree_branch_search_empty(empty_branch):
    """...."""
    assert [*empty_branch.search(['a', 'b'])] == []

@pytest.fixture
def branch_with_wildcards():
    """...."""
    return pattern_tree.PatternTreeBranch(
        root_node = pattern_tree.PatternTreeNode(
            children = Map(
                a = pattern_tree.PatternTreeNode(
                    children = Map(
                        b = pattern_tree.PatternTreeNode(
                            children = Map({
                                'c': pattern_tree.PatternTreeNode(
                                    literal_match = 'dummy/c'
                                ),
                                '*': pattern_tree.PatternTreeNode(
                                    literal_match = 'dummy/*'
                                ),
                                '**': pattern_tree.PatternTreeNode(
                                    literal_match = 'dummy/**'
                                ),
                                '***': pattern_tree.PatternTreeNode(
                                    literal_match = 'dummy/***'
                                )
                            })
                        )
                    )
                )
            )
        )
    )

@pytest.mark.parametrize('_in, out', [
    (['a'],                       []),
    (['a', 'x', 'y', 'z'],        []),
    (['a', 'b'],                  ['dummy/***']),
    (['a', 'b', 'c'],             ['dummy/c', 'dummy/*', 'dummy/***']),
    (['a', 'b', 'u'],             ['dummy/*', 'dummy/***']),
    (['a', 'b', '*'],             ['dummy/*', 'dummy/***']),
    (['a', 'b', '**'],            ['dummy/**', 'dummy/*', 'dummy/***']),
    (['a', 'b', '***'],           ['dummy/***', 'dummy/*']),
    (['a', 'b', 'u', 'l'],        ['dummy/**', 'dummy/***']),
    (['a', 'b', 'u', 'l', 'y'],   ['dummy/**', 'dummy/***'])
])
def test_pattern_tree_branch_search_wildcards(_in, out, branch_with_wildcards):
    """...."""
    assert [*branch_with_wildcards.search(_in)] == out

def test_filter_by_trailing_slash(sample_url_parsed):
    """...."""
    sample_url_parsed2 = dc.replace(sample_url_parsed, has_trailing_slash=True)
    item1 = pattern_tree.StoredTreeItem('dummy_it1', sample_url_parsed)
    item2 = pattern_tree.StoredTreeItem('dummy_it2', sample_url_parsed2)

    assert pattern_tree.filter_by_trailing_slash((item1, item2), False) == \
        frozenset({item1})

    assert pattern_tree.filter_by_trailing_slash((item1, item2), True) == \
        frozenset({item2})

@pytest.mark.parametrize('register_mode',  [True, False])
@pytest.mark.parametrize('empty_at_start', [True, False])
@pytest.mark.parametrize('empty_at_end',   [True, False])
def test_pattern_tree_privatemethod_register(
        register_mode,
        empty_at_start,
        empty_at_end,
        monkeypatch,
        sample_url_parsed
):
    """...."""
    dummy_it       = pattern_tree.StoredTreeItem('dummy_it', sample_url_parsed)
    other_dummy_it = pattern_tree.StoredTreeItem(
        item    = 'other_dummy_it',
        pattern = sample_url_parsed
    )

    class MockedTreeBranch:
        """...."""
        def is_empty(self):
            """...."""
            return empty_at_end

        def update(self, segments, item_updater):
            """...."""
            if segments == ('com', 'example'):
                return self._update_as_domain_branch(item_updater)
            else:
                assert segments == ('aa', 'bb')
                return self._update_as_path_branch(item_updater)

        def _update_as_domain_branch(self, item_updater):
            """...."""
            for updater_input in (None, MockedTreeBranch()):
                updated = item_updater(updater_input)
                if empty_at_end:
                    assert updated is None
                else:
                    assert type(updated) is MockedTreeBranch

            return MockedTreeBranch()

        def _update_as_path_branch(self, item_updater):
            """...."""
            set_with_1_item  = frozenset()
            set_with_2_items = frozenset({dummy_it, other_dummy_it})
            for updater_input in (None, set_with_1_item, set_with_2_items):
                updated = item_updater(updater_input)
                if register_mode:
                    assert dummy_it in updated
                elif updater_input is set_with_2_items:
                    assert dummy_it not in updated
                else:
                    assert updated is None

            return MockedTreeBranch()

    monkeypatch.setattr(pattern_tree, 'PatternTreeBranch', MockedTreeBranch)

    initial_root = Map() if empty_at_start else \
        Map({('http', 80): MockedTreeBranch()})

    tree = pattern_tree.PatternTree(_by_scheme_and_port=initial_root)

    new_tree = tree._register(
        sample_url_parsed,
        'dummy_it',
        register=register_mode
    )

    assert new_tree is not tree

    if empty_at_end:
        assert new_tree._by_scheme_and_port == Map()
    else:
        assert len(new_tree._by_scheme_and_port) == 1
        assert type(new_tree._by_scheme_and_port[('http', 80)]) is \
            MockedTreeBranch

# @pytest.mark.parametrize('register_mode', [True, False])
# def test_pattern_tree_privatemethod_register(
#         register_mode,
#         monkeypatch,
#         sample_url_parsed
# ):
#     """...."""
#     registered_count = 0

#     def mocked_parse_pattern(url_pattern):
#         """...."""
#         assert url_pattern == 'dummy_pattern'

#         for _ in range(2):
#             yield sample_url_parsed

#     monkeypatch.setattr(pattern_tree, 'parse_pattern', mocked_parse_pattern)

#     def mocked_reconstruct_url(self):
#         """...."""
#         return 'dummy_reconstructed_pattern'

#     monkeypatch.setattr(pattern_tree.ParsedUrl, 'reconstruct_url',
#                         mocked_reconstruct_url)

#     def mocked_register_with_parsed_pattern(
#             self,
#             parsed_pat,
#             wrapped_item,
#             register=True
#     ):
#         """...."""
#         nonlocal registered_count

#         assert parsed_pat is sample_url_parsed
#         assert wrapped_item.pattern == 'dummy_reconstructed_pattern'
#         assert register == register_mode

#         registered_count += 1

#         return 'dummy_new_tree' if registered_count == 2 else dc.replace(self)

#     monkeypatch.setattr(
#         pattern_tree.PatternTree,
#         '_register_with_parsed_pattern',
#         mocked_register_with_parsed_pattern
#     )

#     pattern_tree = pattern_tree.PatternTree()

#     new_tree = pattern_tree._register(
#         'dummy_pattern',
#         'dummy_item',
#         register_mode
#     )

#     assert new_tree == 'dummy_new_tree'

@pytest.mark.parametrize('method_name, register_mode', [
    ('register',   True),
    ('deregister', False)
])
def test_pattern_tree_register(method_name, register_mode, monkeypatch):
    """...."""
    def mocked_privatemethod_register(self, parsed_pat, item, register=True):
        """...."""
        assert (parsed_pat, item, register) == \
            ('dummy_pattern', 'dummy_url', register_mode)

        return 'dummy_new_tree'

    monkeypatch.setattr(
        pattern_tree.PatternTree,
        '_register',
        mocked_privatemethod_register
    )

    method = getattr(pattern_tree.PatternTree(), method_name)
    assert method('dummy_pattern', 'dummy_url') == 'dummy_new_tree'

@pytest.fixture
def mock_parse_url(monkeypatch, sample_url_parsed):
    """...."""
    def mocked_parse_url(url):
        """...."""
        assert url == 'dummy_url'
        return dc.replace(
            sample_url_parsed,
            **getattr(mocked_parse_url, 'url_mod', {})
        )

    monkeypatch.setattr(pattern_tree, 'parse_url', mocked_parse_url)

    return mocked_parse_url

@pytest.mark.usefixtures('mock_parse_url')
def test_pattern_tree_search_empty(sample_url_parsed):
    """...."""
    for url in ('dummy_url', sample_url_parsed):
        assert [*pattern_tree.PatternTree().search(url)] == []

@pytest.mark.parametrize('url_mod, out', [
    ({},
     ['dummy_set_A', 'dummy_set_B', 'dummy_set_C']),

    ({'has_trailing_slash': True},
     ['dummy_set_A_with_slash', 'dummy_set_A',
      'dummy_set_B_with_slash', 'dummy_set_B',
      'dummy_set_C_with_slash', 'dummy_set_C'])
])
def test_pattern_tree_search(
        url_mod,
        out,
        monkeypatch,
        sample_url_parsed,
        mock_parse_url,
):
    """...."""
    mock_parse_url.url_mod = url_mod

    dummy_tree_contents = [
        ['dummy_set_A', 'dummy_set_B'],
        [],
        ['dummy_empty_set'] * 3,
        ['dummy_set_C']
    ]

    def mocked_filter_by_trailing_slash(items, with_slash):
        """...."""
        if items == 'dummy_empty_set':
            return frozenset()

        return items + ('_with_slash' if with_slash else '')

    monkeypatch.setattr(pattern_tree, 'filter_by_trailing_slash',
                        mocked_filter_by_trailing_slash)

    class MockedDomainBranch:
        """...."""
        def search(self, labels):
            """...."""
            assert labels == sample_url_parsed.domain_labels

            for item_sets in dummy_tree_contents:
                class MockedPathBranch:
                    """...."""
                    def search(self, segments, item_sets=item_sets):
                        """...."""
                        assert segments == sample_url_parsed.path_segments

                        for dummy_items_set in item_sets:
                            yield dummy_items_set

                yield MockedPathBranch()

    tree = pattern_tree.PatternTree(
        _by_scheme_and_port = {('http', 80): MockedDomainBranch()}
    )

    for url in ('dummy_url', mock_parse_url('dummy_url')):
        assert [*tree.search(url)] == out
