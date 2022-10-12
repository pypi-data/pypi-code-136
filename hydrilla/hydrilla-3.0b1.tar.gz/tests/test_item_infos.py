# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import pytest
import pathlib
import re
import dataclasses as dc

from immutables import Map

from hydrilla import item_infos, versions, json_instances
from hydrilla.exceptions import HaketiloException

def test_make_item_specifiers_seq_empty():
    """...."""
    assert item_infos.make_item_specifiers_seq([]) == ()

def test_get_item_specifiers_seq_nonempty():
    """...."""
    ref_objs = [{'identifier': 'abc'}, {'identifier': 'def'}]

    result = item_infos.make_item_specifiers_seq(ref_objs)

    assert type(result) is tuple
    assert [ref.identifier for ref in result] == ['abc', 'def']

@pytest.fixture
def mock_make_item_specifiers_seq(monkeypatch):
    """...."""
    def mocked_make_item_specifiers_seq(ref_objs):
        """...."""
        assert ref_objs == getattr(
            mocked_make_item_specifiers_seq,
            'expected',
            [{'identifier': 'abc'}, {'identifier': 'def'}]
        )

        return (
            item_infos.ItemSpecifier('abc'),
            item_infos.ItemSpecifier('def')
        )

    monkeypatch.setattr(item_infos, 'make_item_specifiers_seq',
                        mocked_make_item_specifiers_seq)

    return mocked_make_item_specifiers_seq

def test_make_required_mappings_compat_too_low():
    """...."""
    assert item_infos.make_required_mappings('whatever', 1) == ()

@pytest.mark.usefixtures('mock_make_item_specifiers_seq')
def test_make_required_mappings_compat_ok():
    """...."""
    ref_objs = [{'identifier': 'abc'}, {'identifier': 'def'}]

    assert item_infos.make_required_mappings(ref_objs, 2) == \
        (item_infos.ItemSpecifier('abc'), item_infos.ItemSpecifier('def'))

def test_make_file_specifiers_seq_empty():
    """...."""
    assert item_infos.make_file_specifiers_seq([]) == ()

def test_make_file_specifiers_seq_nonempty():
    """...."""
    ref_objs = [{'file': 'abc', 'sha256': 'dummy_hash1'},
                {'file': 'def', 'sha256': 'dummy_hash2'}]

    result = item_infos.make_file_specifiers_seq(ref_objs)

    assert type(result) is tuple
    assert [ref.name for ref in result]   == ['abc', 'def']
    assert [ref.sha256 for ref in result] == ['dummy_hash1', 'dummy_hash2']

def test_generated_by_make_empty():
    """...."""
    assert item_infos.GeneratedBy.make(None) == None

@pytest.mark.parametrize('_in, out_version', [
    ({'name': 'abc'},                     None),
    ({'name': 'abc', 'version': '1.1.1'}, '1.1.1')
])
def test_generated_by_make_nonempty(_in, out_version):
    """...."""
    generated_by = item_infos.GeneratedBy.make(_in)

    assert generated_by.name    == 'abc'
    assert generated_by.version == out_version

def test_load_item_info(monkeypatch):
    """...."""
    def mocked_read_instance(instance_or_path):
        """...."""
        assert instance_or_path == 'dummy_path'
        return 'dummy_instance'

    monkeypatch.setattr(json_instances, 'read_instance', mocked_read_instance)

    def mocked_validate_instance(instance, schema_fmt):
        """...."""
        assert instance == 'dummy_instance'
        assert schema_fmt == 'api_resource_description-{}.schema.json'
        return 7

    monkeypatch.setattr(json_instances, 'validate_instance',
                        mocked_validate_instance)

    class MockedLoadedType:
        """...."""
        def make(instance, schema_compat, repo, repo_iteration):
            """...."""
            assert instance       == 'dummy_instance'
            assert schema_compat  == 7
            assert repo           == 'somerepo'
            assert repo_iteration == 1
            return 'dummy_item_info'

        type = item_infos.ItemType.RESOURCE

    assert item_infos._load_item_info(
        MockedLoadedType,
        'dummy_path',
        'somerepo',
        1
    ) == 'dummy_item_info'

def test_make_payloads(monkeypatch):
    """...."""
    payloads_obj = {'http*://example.com/': {'identifier': 'someresource'}}

    def mocked_parse_pattern(pattern):
        """...."""
        assert pattern == 'http*://example.com/'

        yield 'dummy_parsed_pattern_1'
        yield 'dummy_parsed_pattern_2'

    monkeypatch.setattr(item_infos, 'parse_pattern', mocked_parse_pattern)

    assert item_infos.make_payloads(payloads_obj) == Map({
        'dummy_parsed_pattern_1': item_infos.ItemSpecifier('someresource'),
        'dummy_parsed_pattern_2': item_infos.ItemSpecifier('someresource')
    })

@pytest.mark.parametrize('info_mod, in_mod', [
    ({},                     {}),
    ({'uuid': 'dummy_uuid'}, {}),
    ({},                     {'uuid': 'dummy_uuid'}),
    ({'uuid': 'dummy_uuid'}, {'uuid': 'dummy_uuid'}),
    ({},                     {'identifier': 'abc', '_initialized': True}),
    ({},                     {'items': Map({(1, 2): 'dummy_old_info'})})
])
def test_versioned_item_info_register(info_mod, in_mod):
    """...."""
    class DummyInfo:
        """...."""
        uuid       = None
        identifier = 'abc'
        version    = (1, 2)

    for name, value in info_mod.items():
        setattr(DummyInfo, name, value)

    in_fields = {
        'uuid':         None,
        'identifier':   '<dummy>',
        'items':        Map(),
        '_initialized': False,
        **in_mod
    }
    out_fields = {
        'uuid':         DummyInfo.uuid or in_mod.get('uuid'),
        'identifier':   DummyInfo.identifier,
        'items':        Map({(1, 2): DummyInfo}),
        '_initialized': True
    }

    versioned     = item_infos.VersionedItemInfo(**in_fields)
    new_versioned = versioned.register(DummyInfo)

    assert dc.asdict(versioned)     == in_fields
    assert dc.asdict(new_versioned) == out_fields

def test_versioned_item_info_register_bad_uuid():
    """...."""
    versioned = item_infos.VersionedItemInfo(
        identifier='abc',
        uuid='old_uuid'
    )

    class DummyInfo:
        """...."""
        uuid       = 'new_uuid'
        identifier = 'abc'
        version    = (1, 2)

    with pytest.raises(HaketiloException, match='^uuid_mismatch_abc$'):
        versioned.register(DummyInfo)

@pytest.mark.parametrize('registrations, out', [
    (Map(),                       True),
    (Map({(1, 2): 'dummy_info'}), False)
])
def test_versioned_item_info_is_empty(registrations, out):
    """...."""
    versioned = item_infos.VersionedItemInfo(
        identifier  = 'abc',
        items       = registrations
    )

    assert versioned.is_empty() == out

@pytest.mark.parametrize('versions, out', [
    ([(1, 2), (1, 2, 1), (0, 9999, 4), (1, 0, 2)],    (1, 2, 1)),
    ([(1, 2)],                                        (1, 2))
])
def test_versioned_item_info_newest_version(versions, out):
    """...."""
    versioned = item_infos.VersionedItemInfo(
        identifier = 'abc',
        items      = Map((ver, 'dummy_info') for ver in versions)
    )

    assert versioned.newest_version == out

def test_versioned_item_info_newest_version_bad(monkeypatch):
    """...."""
    monkeypatch.setattr(
        item_infos.VersionedItemInfo,
        'newest_version',
        'dummy_ver1'
    )

    versioned = item_infos.VersionedItemInfo(
        identifier = 'abc',
        items      = Map(dummy_ver1='dummy_info1', dummy_ver2='dummy_info2')
    )

    assert versioned.newest_info == 'dummy_info1'

def test_versioned_item_info_get_by_ver():
    """...."""
    versioned = item_infos.VersionedItemInfo(
        identifier = 'abc',
        items      = Map({(1, 2): 'dummy_info1', (3, 4, 5): 'dummy_info2'})
    )

    assert versioned.get_by_ver(range(1, 3)) == 'dummy_info1'

@pytest.mark.parametrize('versions, out', [
    ([(1, 2), (0, 999, 4), (1, 0, 2)], ['(0, 999, 4)', '(1, 0, 2)', '(1, 2)']),
    ([],                               [])
])
def test_versioned_item_get_all(versions, out):
    """...."""
    versioned = item_infos.VersionedItemInfo(
        identifier = 'abc',
        items      = Map((ver, str(ver)) for ver in versions)
    )

    assert [*versioned.get_all()] == out

sample_resource_obj = {
    'source_name':          'somesource',
    'source_copyright':     [{'file': 'ABC', 'sha256': 'dummy_sha256'}],
    'version':              [1, 2, 3, 0],
    'identifier':           'someid',
    'uuid':                 None,
    'long_name':            'Some Thing',
    'description':          'Do something somewhere',
    'permissions':          {'eval': True, 'cors_bypass': False},
    'max_haketilo_version': [10],
    'required_mappings':    [{'identifier': 'required1'}],
    'generated_by':         {'name': 'sometool', 'version': '1.1.1'},
    'revision':             4,
    'dependencies':         [{'identifier': 'abc'}, {'identifier': 'def'}],
    'scripts':              [{'file': 'ABC', 'sha256': 'dummy_sha256'}]
}

sample_mapping_obj = {
    **sample_resource_obj,
    'payloads': {
        'https://example.com/': {'identifier': 'someresource'}
    }
}

del sample_mapping_obj['dependencies']
del sample_mapping_obj['scripts']

@pytest.fixture(scope='session')
def sample_resource_info():
    """...."""
    return item_infos.ResourceInfo(
        repo               = 'somerepo',
        repo_iteration     = 2,
        source_name        = 'somesource',
        source_copyright   = (item_infos.FileSpecifier('ABC', 'dummy_sha256'),),
        version            = (1, 2, 3),
        identifier         = 'someid',
        uuid               = None,
        long_name          = 'Some Thing',
        description        = 'Do something somewhere',
        allows_eval        = True,
        allows_cors_bypass = False,
        min_haketilo_ver   = versions.normalize([1]),
        max_haketilo_ver   = versions.normalize([10]),
        required_mappings  = (item_infos.ItemSpecifier('required1'),),
        generated_by       = item_infos.GeneratedBy('sometool', '1.1.1'),
        revision           = 4,
        dependencies       = (item_infos.ItemSpecifier('abc'),
                              item_infos.ItemSpecifier('def')),
        scripts            = (item_infos.FileSpecifier('ABC', 'dummy_sha256'),)
    )

@pytest.fixture(scope='session')
def sample_mapping_info():
    """...."""
    payloads = Map({
        'https://example.com/': item_infos.ItemSpecifier('someresource')
    })

    return item_infos.MappingInfo(
        repo               = 'somerepo',
        repo_iteration     = 2,
        source_name        = 'somesource',
        source_copyright   = (item_infos.FileSpecifier('ABC', 'dummy_sha256'),),
        version            = (1, 2, 3),
        identifier         = 'someid',
        uuid               = None,
        long_name          = 'Some Thing',
        description        = 'Do something somewhere',
        allows_eval        = True,
        allows_cors_bypass = False,
        min_haketilo_ver   = versions.normalize([2]),
        max_haketilo_ver   = versions.normalize([10]),
        required_mappings = (item_infos.ItemSpecifier('required1'),),
        generated_by       = item_infos.GeneratedBy('sometool', '1.1.1'),
        payloads           = payloads
    )

@pytest.fixture(scope='session')
def sample_info_base_init_kwargs(sample_resource_info):
    kwargs = {}
    for datclass_type in (item_infos.ItemInfoBase, item_infos.ItemIdentity):
        for field_name in datclass_type.__annotations__.keys():
            kwargs[field_name] = getattr(sample_resource_info, field_name)

    return Map(kwargs)

def test_resource_info_versioned_identifier(sample_resource_info):
    """...."""
    assert sample_resource_info.versioned_identifier == 'someid-1.2.3-4'

def test_mapping_info_versioned_identifier(sample_mapping_info):
    assert sample_mapping_info.versioned_identifier == 'someid-1.2.3'

@pytest.fixture
def mock_make_file_specifiers_seq(monkeypatch):
    """...."""
    def mocked_make_file_specifiers_seq(ref_objs):
        """...."""
        assert ref_objs == getattr(
            mocked_make_file_specifiers_seq,
            'expected',
            [{'file': 'ABC', 'sha256': 'dummy_sha256'}]
        )

        return (item_infos.FileSpecifier(name='ABC', sha256='dummy_sha256'),)

    monkeypatch.setattr(item_infos, 'make_file_specifiers_seq',
                        mocked_make_file_specifiers_seq)

    return mocked_make_file_specifiers_seq

@pytest.mark.parametrize('missing_prop', [
    'required_mappings',
    'generated_by',
    'uuid'
])
@pytest.mark.usefixtures(
    'mock_make_item_specifiers_seq',
    'mock_make_file_specifiers_seq'
)
def test_item_info_get_base_init_kwargs(
        missing_prop,
        monkeypatch,
        sample_resource_info,
        sample_info_base_init_kwargs,
        mock_make_file_specifiers_seq
):
    """...."""
    monkeypatch.delitem(sample_resource_obj, missing_prop)

    def mocked_normalize_version(version):
        return {
            (1, 2, 3, 0): (1, 2, 3),
            (10,):        (10,)
        }[tuple(version)]

    monkeypatch.setattr(versions, 'normalize', mocked_normalize_version)

    def mocked_make_required_mappings(ref_objs, schema_compat):
        """...."""
        if missing_prop == 'required_mappings':
            assert ref_objs == []
        else:
            assert ref_objs == [{'identifier': 'required1'}]

        assert schema_compat == 2

        return (item_infos.ItemSpecifier('required1'),)

    monkeypatch.setattr(item_infos, 'make_required_mappings',
                        mocked_make_required_mappings)

    def mocked_generated_by_make(generated_by_obj):
        """...."""
        if missing_prop == 'generated_by':
            assert generated_by_obj == None
        else:
            assert generated_by_obj == {'name': 'sometool', 'version': '1.1.1'}

        return item_infos.GeneratedBy(name='sometool', version='1.1.1')

    monkeypatch.setattr(item_infos.GeneratedBy, 'make',
                        mocked_generated_by_make)

    expected = sample_info_base_init_kwargs
    if missing_prop == 'uuid':
        expected = expected.set('uuid', None)

    Base = item_infos.ItemInfoBase
    assert Base._get_base_init_kwargs(sample_resource_obj, 2, 'somerepo', 2) \
        == expected

@pytest.fixture
def mock_get_base_init_kwargs(monkeypatch, sample_info_base_init_kwargs):
    """...."""
    def mocked_get_base_init_kwargs(
            item_obj,
            schema_compat,
            repo,
            repo_iteration
    ):
        """...."""
        assert schema_compat          == 2
        assert item_obj['identifier'] == 'someid'
        assert repo                   == 'somerepo'
        assert repo_iteration         == 2

        return sample_info_base_init_kwargs

    monkeypatch.setattr(item_infos.ItemInfoBase, '_get_base_init_kwargs',
                        mocked_get_base_init_kwargs)

@pytest.mark.parametrize('missing_prop', ['dependencies', 'scripts'])
@pytest.mark.usefixtures('mock_get_base_init_kwargs')
def test_resource_info_make(
        missing_prop,
        monkeypatch,
        sample_resource_info,
        mock_make_item_specifiers_seq,
        mock_make_file_specifiers_seq
):
    """...."""
    _in = sample_resource_obj
    monkeypatch.delitem(_in, missing_prop)

    if missing_prop == 'dependencies':
        mock_make_item_specifiers_seq.expected = []
    elif missing_prop == 'scripts':
        mock_make_file_specifiers_seq.expected = []

    assert item_infos.ResourceInfo.make(_in, 2, 'somerepo', 2) == \
        sample_resource_info

@pytest.mark.parametrize('missing_payloads', [True, False])
@pytest.mark.usefixtures(
    'mock_get_base_init_kwargs',
    'mock_make_item_specifiers_seq'
)
def test_mapping_info_make(missing_payloads, monkeypatch, sample_mapping_info):
    """...."""
    _in = sample_mapping_obj
    if missing_payloads:
        monkeypatch.delitem(_in, 'payloads')

    def mocked_make_payloads(payloads_obj):
        """...."""
        if missing_payloads:
            assert payloads_obj == {}
        else:
            assert payloads_obj == \
                {'https://example.com/': {'identifier': 'someresource'}}

        return Map({
            'https://example.com/': item_infos.ItemSpecifier('someresource')
        })

    monkeypatch.setattr(item_infos, 'make_payloads', mocked_make_payloads)

    assert item_infos.MappingInfo.make(_in, 2, 'somerepo', 2) == \
        sample_mapping_info

@pytest.mark.parametrize('type_name', ['ResourceInfo', 'MappingInfo'])
@pytest.mark.parametrize('repo_iter_arg', [10, 'default'])
def test_make_item_info(type_name, repo_iter_arg, monkeypatch):
    """...."""
    info_type = getattr(item_infos, type_name)

    def mocked_load_item_info(
            _info_type,
            instance_or_path,
            repo,
            repo_iteration
    ):
        """...."""
        assert _info_type       == info_type
        assert instance_or_path == 'dummy_path'
        assert repo             == 'somerepo'
        if repo_iter_arg == 'default':
            assert repo_iteration == -1
        else:
            assert repo_iteration == 10

        return 'dummy_info'

    monkeypatch.setattr(item_infos, '_load_item_info', mocked_load_item_info)

    extra_args = {}
    if repo_iter_arg != 'default':
        extra_args['repo_iteration'] = repo_iter_arg

    assert info_type.load('dummy_path', 'somerepo', **extra_args) \
        == 'dummy_info'

def test_resource_info_hash(sample_resource_info):
    """...."""
    hash(sample_resource_info)

def test_mapping_info_hash(sample_mapping_info):
    """...."""
    hash(sample_mapping_info)
