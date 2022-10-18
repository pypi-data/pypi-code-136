from commandsheet.output import format_section_heading
from commandsheet.output import format_section_content
import pytest


def test_format_section_heading():
    text = 'heading'
    index = 1
    chars = '()'
    assert format_section_heading(text, index=index) == '[1. heading]'
    assert format_section_heading(text, index=None) == '[heading]'
    assert format_section_heading(text, index=None, surround=chars) == '(heading)'
    assert format_section_heading(text, index=None, surround='') == 'heading'
    assert format_section_heading(text, index=None, surround=None) == 'heading'


def test_format_section_content():
    cmd = 'ls --long'
    dsc = 'List in a long format'
    indent = 50
    fillchar = '.'
    max_width = 85
    expected = f'{cmd:{fillchar}<{indent}} {dsc}'
    assert format_section_content(
        cmd,
        dsc,
        indent=indent,
        fillchar=fillchar,
        max_width=max_width
    ) == expected
