from citation_docket.base import Num

separator = r"[,\.\s-]*"
digit = r"\d{3}[\d-]*"  # e.g. 323-23, 343-34
acronyms = r"""
    \s?
    (
        A|
        B|
        P|
        R|
        P|
        J|
        OCA|
        O\.C\.A\.|
        SDC|
        CTA|
        RTC|
        CFI|
        RTJ|
        MTJ|
        METC|
        MCTC|
        MTCC|
        MTC|
        HOJ|
        RET(?:\.)?|
        SCC?|
        SC(?:\-PHILJA)?|
        CA(?:\-J)?|
        SB(?:\-J)?
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


ipi = r"""
    (
        (IPI)|(I\.P\.I\.)
    )
"""

am_key = rf"""
    (
        (
            a
            {separator}
            m
            {separator}
        )|
        (
            \b
            adm(in)?
            {separator}
            (?:
                \b
                (
                    Matter|
                    Mat\. # ADM. MAT. NO. P-97-1241
                )
                \s* # optional space
            )?
        )
    )
"""

am_oca_ipi_num = rf"""
    (
        {am_key}?
        OCA
        \s*
        (
            IPI|
            I\.P\.I\.
        )
        \s*
        {Num.AM.allowed}
    )
"""

am_num = rf"""
    (
        {am_key}
        {Num.AM.allowed}
    )
"""

required = rf"""
    (?P<am_init>
        {am_oca_ipi_num}| # AM OCA IPI No. / OCA IPI No.
        {am_num}| # AM No.
        {am_key} # AM
    )
    (?P<am_middle>
        (
            ({letter})|
            ({digit})
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
    (?P<am_init_optional>
        {am_oca_ipi_num}|
        {am_num}
    )?
    (?P<am_middle_optional>
        {letter}|
        {digit}
    )?
    (?:
        (
            [\,\s,\-\&]|
            and
        )*
    )?
"""

am_phrases = rf"""
    (?P<am_phrase>
        ({required})
        ({optional}){{1,3}}
    )
"""
