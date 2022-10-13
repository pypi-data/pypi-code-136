from citation_docket.base import Num

separator = r"[,\.\s-]*"
two_digits = r"[\d-]{2,}"
l_digits = rf"\bL\-{two_digits}"
digits_alone = rf"\b\d{two_digits}"

acronyms = r"""
    \s?
    (
        P| # A.C. No. P-88-198, February 25, 1992, 206 SCRA 491.
        J| # Adm. Case No. 129-J, July 30, 1976, 72 SCRA 172.
        CBD| # A.C. No. CBD-174
        SB # A.C. No. SB-95-7-P
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

ac_key = rf"""
    (
        (
            a
            {separator}
            c
            {separator}
            (?:
                CBD # see A.C. CBD No. 190
                \s* # optional space
            )? # optional CBD,
        )|
        (
            \b
            adm(in)?
            {separator}
            (?:
                \b
                Case
                \s* # optional space
            )?
        )
    )
"""

ac_num = rf"""
    (
        {ac_key}
        {Num.AC.allowed}
    )
"""

required = rf"""
    (?P<ac_init>
        {ac_num}
    )
    (?P<ac_middle>
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
    (?P<ac_init_optional>
        {ac_num}
    )?
    (?P<ac_middle_optional>
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

ac_phrases = rf"""
    (?P<ac_phrase>
        ({required})
        ({optional}){{1,3}}
    )
"""
