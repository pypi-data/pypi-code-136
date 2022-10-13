from citation_docket.base import Num

separator = r"[,\.\s-]*"
two_digits = r"[\d-]{2,}"
l_digits = rf"\bL\-{two_digits}"
digits_alone = rf"\b\d{two_digits}"

acronyms = r"""
    \s?
    (
        SBC # B.M. SBC-591, December 1, 1977
    )
    \s?
"""
letter = rf"""
    (
        \b
        {acronyms}
    )?
    [\d-]{{3,}} #  at least two digits and a dash
    ( # don't add \b  to capture "-Ret.""
        {acronyms}
    )?
"""

bm_key = rf"""
    (
        (
            b
            {separator}
            m
            {separator}
        )|
        (
            \b
            bar
            \s+
            matter
            \s*
        )
    )
"""

bm_num = rf"""
    (
        {bm_key}
        {Num.BM.allowed}
    )
"""

required = rf"""
    (?P<bm_init>
        {bm_num}
    )
    (?P<bm_middle>
        (
            ({letter})|
            ({l_digits})|
            ({digits_alone})
        )
    )
    (?:
        (
            [\,\s,\-\&]|
            and
        )*
    )?
"""

optional = rf"""
    (?P<bm_init_optional>
        {bm_num}
    )?
    (?P<bm_middle_optional>
        ({letter})|
        ({l_digits})|
        ({digits_alone})
    )?
    (?:
        (
            [\,\s,\-\&]|
            and
        )*
    )?
"""

bm_phrases = rf"""
    (?P<bm_phrase>
        ({required})
        ({optional}){{1,3}}
    )
"""
