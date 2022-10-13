import re
from typing import Pattern

formerly = r"""
    (?P<formerly>
        [\[\(]
        \s*
        (FORMERLY|Formerly|Former|From)\:?
        (?P<old_name>[\w\s\-\.\&]+)
        \s*
        [\)\]]
        \W*
    )
"""

pp = r"""
    (?P<pp>
        \b
        (?P<extra_pages_label>
            p\.
            |
            pp\.
        )
        \s*
        \b
        (?P<extra_page_numbers_under_pp>
            [\d-]+
        )
        \b
        \W*
    )
"""


EXTRA: Pattern = re.compile(rf"{formerly}", re.I | re.X)


def cull_extra(text: str):
    """Remove text like `formerly... from` the given text string"""
    return EXTRA.sub("", text)
