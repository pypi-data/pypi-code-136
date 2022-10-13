from citation_docket.base import Num

separator = r"[,\.\s-]*"
digit = r"\d{3}[\d-]*"  # e.g. 323-23, 343-34


gr_key = rf"""
    (
        (
            (?<!CA\s)  # CA GR
            (?<!CA-)  # CA-GR
            (?<!C\.A\.) # C.A.G.R.
            (?<!C\.A\.\s) # C.A. G.R.
            \b
            g
        )
        {separator}
        r
        {separator}
    )
"""

l_key = rf"""
    (
        \b # prevent capture of Angara v. Electoral Commission, 63 Phil. 139,
        (
            l|
            i # I is a mistype: De Ramos v. Court of Agrarian Relations, I-19555, May 29, 1964;
        )
        {separator} # Makes possible G.R. L-No. 5110  | # L. No. 464564
    )
"""


digits = rf"""
    (
        \b
        ({l_key})?
        {digit}
        \b
        \W* # possible comma
        (&\s*|and\s*)? # possible and between
    ){{1,5}}
    (
        {digit}
        \b
    )?
"""


gr_regular = rf"""
( # G.R. L-No. 5110, G.R. No. 5110, GR 100
    {gr_key}
    ({l_key})?
    ({Num.GR.allowed})?
    {digits}
)
"""

l_irregular = rf"""
( # L-No. 5110, L 5110, No
    {l_key}
    ({Num.GR.allowed})?
    {digits}
)
"""

n_irregular = rf"""
( # , Nos.
    \,\s+
    ({Num.GR.allowed})
    {digits}
)
"""

gr_phrases = rf"""
    (?P<gr_phrase>
        (
            (?P<gr_mid>
                (?P<gr_gist_r>{gr_regular})|
                (?P<gr_gist_l>{l_irregular})|
                (?P<gr_gist_n>{n_irregular})
            )
        ){{1,5}}
    )
"""
