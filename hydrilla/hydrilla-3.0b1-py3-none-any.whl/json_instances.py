# SPDX-License-Identifier: GPL-3.0-or-later

# Handling JSON objects.
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
This module contains utilities for reading and validation of JSON instances.
"""

import re
import json
import os
import io
import typing as t

from pathlib import Path, PurePath

from jsonschema import RefResolver, Draft7Validator # type: ignore

from .translations import smart_gettext as _
from .exceptions import HaketiloException
from . import versions

here = Path(__file__).resolve().parent

_strip_comment_re = re.compile(r'''
^ # match from the beginning of each line
( # catch the part before '//' comment
  (?: # this group matches either a string or a single out-of-string character
    [^"/] |
    "
    (?: # this group matches any in-a-string character
      [^"\\] |          # match any normal character
      \\[^u] |          # match any escaped character like '\f' or '\n'
      \\u[a-fA-F0-9]{4} # match an escape
    )*
    "
  )*
)
# expect either end-of-line or a comment:
# * unterminated strings will cause matching to fail
# * bad comment (with '/' instead of '//') will be indicated by second group
#   having length 1 instead of 2 or 0
(//?|$)
''', re.VERBOSE)

def strip_json_comments(text: str) -> str:
    """
    Accept JSON text with optional C++-style ('//') comments and return the text
    with comments removed. Consecutive slashes inside strings are handled
    properly. A spurious single slash ('/') shall generate an error. Errors in
    JSON itself shall be ignored.
    """
    stripped_text = []
    for line_num, line in enumerate(text.split('\n'), start=1):
        match = _strip_comment_re.match(line)

        if match is None: # unterminated string
            # ignore this error, let the json module report it
            stripped = line
        elif len(match[2]) == 1:
            msg_fmt = _('bad_json_comment_line_{line_num}_char_{char_num}')

            raise HaketiloException(msg_fmt.format(
                line_num = line_num,
                char_num = len(match[1]) + 1
            ))
        else:
            stripped = match[1]

        stripped_text.append(stripped)

    return '\n'.join(stripped_text)

_schema_name_re = re.compile(r'''
(?P<name_base>[^/]*)
-
(?P<ver>
  (?P<major>[1-9][0-9]*)
  (?: # this repeated group matches the remaining version numbers
    \.
    (?:[1-9][0-9]*|0)
  )*
)
\.schema\.json
$
''', re.VERBOSE)

schema_paths: t.Dict[str, Path] = {}
for path in (here / 'schemas').rglob('*.schema.json'):
    match = _schema_name_re.match(path.name)
    assert match is not None

    schema_name_base = match.group('name_base')
    schema_ver_list = match.group('ver').split('.')

    for i in range(len(schema_ver_list)):
        schema_ver = '.'.join(schema_ver_list[:i+1])
        schema_paths[f'{schema_name_base}-{schema_ver}.schema.json'] = path

schema_paths.update([(f'https://hydrilla.koszko.org/schemas/{name}', path)
                     for name, path in schema_paths.items()])

schemas: t.Dict[Path, t.Dict[str, t.Any]] = {}

class UnknownSchemaError(HaketiloException):
    pass

def _get_schema(schema_name: str) -> t.Dict[str, t.Any]:
    """Return loaded JSON of the requested schema. Cache results."""
    path = schema_paths.get(schema_name)
    if path is None:
        raise UnknownSchemaError(_('unknown_schema_{}').format(schema_name))

    if path not in schemas:
        schemas[path] = json.loads(path.read_text())

    return schemas[path]

def validator_for(schema: t.Union[str, t.Dict[str, t.Any]]) -> Draft7Validator:
    """
    Prepare a validator for the provided schema.

    Other schemas under '../schemas' can be referenced.
    """
    if isinstance(schema, str):
        schema = _get_schema(schema)

    resolver = RefResolver(
        base_uri=schema['$id'],
        referrer=schema,
        handlers={'https': _get_schema}
    )

    return Draft7Validator(schema, resolver=resolver)

def parse_instance(text: str) -> object:
    """Parse 'text' as JSON with additional '//' comments support."""
    return json.loads(strip_json_comments(text))

InstanceSource = t.Union[Path, str, io.TextIOBase, t.Dict[str, t.Any], bytes]

def read_instance(instance_or_path: InstanceSource) -> object:
    """...."""
    if isinstance(instance_or_path, dict):
        return instance_or_path

    if isinstance(instance_or_path, bytes):
        encoding = json.detect_encoding(instance_or_path)
        text = instance_or_path.decode(encoding)
    elif isinstance(instance_or_path, io.TextIOBase):
        try:
            text = instance_or_path.read()
        finally:
            instance_or_path.close()
    else:
        text = Path(instance_or_path).read_text()

    try:
        return parse_instance(text)
    except:
        if isinstance(instance_or_path, str) or \
           isinstance(instance_or_path, Path):
            fmt = _('err.util.text_in_{}_not_valid_json')
            raise HaketiloException(fmt.format(instance_or_path))
        else:
            raise HaketiloException(_('err.util.text_not_valid_json'))

def get_schema_version(instance: object) -> versions.VerTuple:
    """
    Parse passed object's "$schema" property and return the schema version tuple.
    """
    ver_str: t.Optional[str] = None

    if isinstance(instance, dict) and type(instance.get('$schema')) is str:
        match = _schema_name_re.search(instance['$schema'])
        ver_str = match.group('ver') if match else None

    if ver_str is not None:
        return versions.parse_normalize(ver_str)
    else:
        raise HaketiloException(_('no_schema_number_in_instance'))

def get_schema_major_number(instance: object) -> int:
    """
    Parse passed object's "$schema" property and return the major number of
    schema version.
    """
    return get_schema_version(instance)[0]

def validate_instance(instance: object, schema_name_fmt: str) -> int:
    """...."""
    major = get_schema_major_number(instance)
    schema_name = schema_name_fmt.format(major)
    validator = validator_for(schema_name)

    validator.validate(instance)

    return major
