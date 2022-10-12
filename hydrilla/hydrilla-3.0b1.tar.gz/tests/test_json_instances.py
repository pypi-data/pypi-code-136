# SPDX-License-Identifier: CC0-1.0

# Copyright (C) 2022 Wojtek Kosior <koszko@koszko.org>
#
# Available under the terms of Creative Commons Zero v1.0 Universal.

import pytest
import re

from hydrilla import json_instances, versions
from hydrilla.exceptions import HaketiloException

sample_json_no_comments = '{\n"so/me":\n"//json//"\n}\n'

@pytest.mark.parametrize('_in', [
    '{\n"so/me":\n"//json//"\n}\n',
    '{//we\n"so/me"://will\n"//json//"//rock\n}//you\n'
])
def test_strip_json_comments(_in):
    """...."""
    assert json_instances.strip_json_comments(_in) == sample_json_no_comments

@pytest.mark.parametrize('_in, line, char', [
    ('/{\n"so/me":\n"//json//"\n}\n',                                 1, 1),
    ('{\n"so/me":/\n"//json//"\n}/\n',                                2, 9),
    ('{\n"so/me":/ huehue, I am an invalid comment\n"//json//"\n}\n', 2, 9)
])
def test_strip_json_comments_bad(_in, line, char):
    """...."""
    error_regex = f'^bad_json_comment_line_{line}_char_{char}$'
    with pytest.raises(HaketiloException, match=error_regex):
        json_instances.strip_json_comments(_in)

@pytest.mark.parametrize('schema_name, full_schema_name', [
    ('package_source-1.0.1.schema.json', 'package_source-1.0.1.schema.json'),
    ('package_source-1.0.schema.json',   'package_source-1.0.1.schema.json'),
    ('package_source-1.schema.json',     'package_source-1.0.1.schema.json'),
    ('package_source-2.schema.json',     'package_source-2.schema.json')
])
def test_get_schema(schema_name, full_schema_name):
    """...."""
    url_prefix = 'https://hydrilla.koszko.org/schemas/'

    for prefix in ('', url_prefix):
        schema1 = json_instances._get_schema(prefix + schema_name)
        assert schema1['$id'] == url_prefix + full_schema_name

        schema2 = json_instances._get_schema(prefix + schema_name)
        assert schema2 is schema1

@pytest.mark.parametrize('_in', ['dummy_uri', {'$id': 'dummy_uri'}])
def test_validator_for(_in, monkeypatch):
    """...."""
    def mocked_get_schema(schema_id):
        """...."""
        assert schema_id == 'dummy_uri'
        return {'$id': 'dummy_uri'}

    monkeypatch.setattr(json_instances, '_get_schema', mocked_get_schema)

    def MockedRefResolver(base_uri, referrer, handlers):
        """....<function replaces a class...>"""
        assert base_uri == referrer['$id']
        assert referrer == {'$id': 'dummy_uri'}
        assert handlers == {'https': mocked_get_schema}
        return 'dummy_resolver'

    monkeypatch.setattr(json_instances, 'RefResolver', MockedRefResolver)

    def MockedDraft7Validator(schema, resolver):
        """....<same as above>"""
        assert schema == {'$id': 'dummy_uri'}
        assert resolver == 'dummy_resolver'
        return 'dummy_validator'

    monkeypatch.setattr(json_instances, 'Draft7Validator',
                        MockedDraft7Validator)

    assert json_instances.validator_for(_in) == 'dummy_validator'

def test_parse_instance(monkeypatch):
    """...."""
    def mocked_strip_json_comments(text):
        """...."""
        assert text == 'dummy_commented_json'
        return '{"dummy": 1}'

    monkeypatch.setattr(json_instances, 'strip_json_comments',
                        mocked_strip_json_comments)

    assert json_instances.parse_instance('dummy_commented_json') == {'dummy': 1}


def test_read_instance(monkeypatch, tmpdir):
    """...."""
    def mocked_parse_instance(text):
        """...."""
        assert text == 'dummy_JSON_text'
        return {'dummy': 1}

    monkeypatch.setattr(json_instances, 'parse_instance', mocked_parse_instance)

    somepath = tmpdir / 'somefile'
    somepath.write_text('dummy_JSON_text')

    for instance_or_path in (somepath, str(somepath), {'dummy': 1}):
        assert json_instances.read_instance(instance_or_path) == {'dummy': 1}

def test_read_instance_bad(monkeypatch, tmpdir):
    """...."""
    monkeypatch.setattr(json_instances, 'parse_instance', lambda: 3 / 0)

    somepath = tmpdir / 'somefile'
    somepath.write_text('dummy_JSON_text')

    error_regex = f'^err.util.text_in_{re.escape(str(somepath))}_not_valid_json$'
    with pytest.raises(HaketiloException, match=error_regex):
        json_instances.read_instance(somepath)

@pytest.mark.parametrize('instance, ver_str', [
    ({'$schema': 'a_b_c-1.0.1.0.schema.json'},   '1.0.1.0'),
    ({'$schema': '9-9-9-10.5.600.schema.json'},  '10.5.600'),
    ({'$schema': 'https://ab.cd-2.schema.json'}, '2')
])
def test_get_schema_version(instance, ver_str, monkeypatch):
    """...."""
    def mocked_parse_normalize(_ver_str):
        """...."""
        assert _ver_str == ver_str
        return 'dummy_version'

    monkeypatch.setattr(versions, 'parse_normalize', mocked_parse_normalize)

    assert json_instances.get_schema_version(instance) == 'dummy_version'

@pytest.mark.parametrize('instance', [
    {'$schema': 'https://ab.cd-0.schema.json'},
    {'$schema': 'https://ab.cd-02.schema.json'},
    {'$schema': 'https://ab.cd-2.00.schema.json'},
    {'$schema': 'https://ab.cd-2.01.schema.json'},
    {'$schema': 'https://ab.cd-2.schema.json5'},
    {'$schema': 'https://ab.cd-2.schema@json'},
    {'$schema': 'https://ab.cd_2.schema.json'},
    {'$schema': '2.schema.json'},
    {'$schema': 'https://ab.cd-.schema.json'},
    {'$schema': b'https://ab.cd-2.schema.json'},
    {},
    'not dict'
])
def test_get_schema_version_bad(instance):
    """...."""
    error_regex = '^no_schema_number_in_instance$'
    with pytest.raises(HaketiloException, match=error_regex):
        json_instances.get_schema_version(instance)

def test_get_schema_major_number(monkeypatch):
    """...."""
    def mocked_get_schema_version(instance):
        """...."""
        assert instance == 'dummy_instance'
        return (3, 4, 6)

    monkeypatch.setattr(json_instances, 'get_schema_version',
                        mocked_get_schema_version)

    assert json_instances.get_schema_major_number('dummy_instance') == 3

def test_validate_instance(monkeypatch):
    """...."""
    def mocked_get_schema_major_number(instance):
        """...."""
        assert instance == 'dummy_instance'
        return 4

    monkeypatch.setattr(json_instances, 'get_schema_major_number',
                        mocked_get_schema_major_number)

    class mocked_validator_for:
        """....<class instead of function>"""
        def __init__(self, schema_name):
            """...."""
            assert schema_name == 'https://ab.cd/something-4.schema.json'

        def validate(self, instance):
            """...."""
            assert instance == 'dummy_instance'

    monkeypatch.setattr(json_instances, 'validator_for', mocked_validator_for)

    schema_name_fmt = 'https://ab.cd/something-{}.schema.json'
    assert json_instances.validate_instance(
        'dummy_instance',
        schema_name_fmt
    ) == 4
