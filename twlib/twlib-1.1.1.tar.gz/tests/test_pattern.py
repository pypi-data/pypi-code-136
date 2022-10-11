import re

import pytest


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("remote_execute_jenkin%.java", "remote_execute_jenkin%.jav"),
        ("remote_execute___jenkin%.java", "remote_execute_jenkin%.jav"),
        ("remote_execute____jenkin%.java", "remote_execute____jenkin%.jav"),
    ),
)
def test_substitution_conditional(input, expected):
    r = re.sub(
        r"""
            (?<!_)              # negative lookbehind to assert that what is on the left side is not an _
            _{1,2}              # match _ 1 or 2 times
            (?=_[^_])           # positive lookahead to assert that what follows is an _ followed by not an _
            |(?<=\.jav)a$
        """,
        repl="",
        string=input,
        count=99,
        flags=re.VERBOSE,
    )
    assert r == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ("remote_execute_jenkin%.java", "remote_execute_jenkin%.jav"),
        ("remote_execute___jenkin%.java", "remote_execute_jenkin%.jav"),
        ("remote_execute____jenkin%.java", "remote_execute_jenkin%.jav"),
    ),
)
def test_substitute_absolute(input, expected):
    r = re.sub(
        r"""
            _(?=_)              # Match _ and use positive lookahead to assert that what follows is an underscore which MATCH all leading underscores but not the last
            |                   # or
            (?<=\.jav)a         # Positive lookbehind to assert that what is on the left side is .jav and MATCH ON 'a' at the end of the line
            $                   # EOS
        """,
        repl="",
        string="remote_execute___jenkin%.java",
        count=3,
        flags=re.VERBOSE,
    )
    assert r == expected
