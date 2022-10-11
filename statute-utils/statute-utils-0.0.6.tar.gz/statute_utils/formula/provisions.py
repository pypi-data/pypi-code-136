import re
from typing import Match


class ProvisionLabel:
    paragraph = r"""
        \b
        (sub-?)?pars?
        (
            \.
            |agraphs?
        )?
        \b
    """

    article = r"""
        \b
        (A|a)rts?
        (
            \.
            |(icles?\b)
        )?
    """

    article_capped = r"""
        \b
        ARTS?\.?
        \b
    """

    section = r"""
        \b
        (S|s)
        ec
        (
            \.
            |(tions?)\b
        )?

    """

    section_capped = r"""
        \b
        SEC(TION)?S?\.?
        \b
    """

    chapter = r"""
        \b
        (C|c)h
        (
            \.
            |apters?
        )?
        \b
    """

    book = r"""
        \b
        (B|b)
        (
            (ook)
            |(k.?)
        )
        \b
    """

    title = r""" # excludes the following "Title" from being considered a provision
        (?<![Cc]ertificate\sof\s) # without s Original Certificate of Title
        (?<![Cc]ertificates\sof\s) # with s # Transfer Certificates of Title
        \b
        (T|t)it
        (
            \.
            |le
        )?
        \b
    """

    rule = r"""
        \bRule\b
    """

    canon = r"""
        \bCanon\b
    """

    section_symbol = r"""
        §§?\s*
    """

    options = [
        rule,
        canon,
        paragraph,
        article,
        article_capped,
        section,
        section_capped,
        title,
        chapter,
        book,
    ]
    link_options = (rf"{i}\s+" for i in options)
    formula = rf"({'|'.join(link_options)}|{section_symbol})"

    @classmethod
    def parse(cls, text) -> Match | None:
        return re.compile(cls.formula, re.X).search(text)

    @classmethod
    def isolate_digit(cls, text) -> str | None:
        """Removes label e.g. Art., Section from the query_text"""
        if match := cls.parse(text):
            return re.sub(match.group(), "", text).strip()
        return None


class ProvisionSubject:
    just_digits = r"""
        (
            \d+
        )
    """

    simple_roman = r"""
        (
            [IXV]+\b
        ) #\b ensures that in cases like "Section 6 of PD 902-A provides:"SECTION 6. In " SECTION 6. excludes an additional "I"
    """

    simple_letters = r"""
        (
            \- # ensures that -A, -B, -C is used; prevents matching of `B.P.`
            [ABC]
            \b
        )
    """

    bracketed_character = r"""
        (
            \(
            \w{1,3}
            \)
        )
    """

    connector = r"""
        (
            and|
            of|
            \,|
            \.|
            \s|
            \-
        )
    """

    formula = rf"""
        ( # must start with an initial object
            {just_digits}|
            {simple_roman}|
            {bracketed_character}
        ) # may end with multiple objects
        (
            {simple_letters}|
            {simple_roman}|
            {just_digits}|
            {bracketed_character}|
            {connector}
        )*
    """

    @classmethod
    def parse(cls, text) -> Match | None:
        return re.compile(cls.formula, re.X).search(text)


ProvisionFormula = rf"""
        (
            ({ProvisionLabel().formula})
            {ProvisionSubject().formula}
        )+
    """
ProvisionPattern = re.compile(rf"({ProvisionFormula})", re.X)
"""
A `PROVISION` style refers to a pattern object based on the `UNIT` regex formula. Examples include:
1. Sec. 1
2. Art. 2350 (a)
3. Bk V
4. Title XV
"""


def match_provision(text: str) -> Match | None:
    """
    >>> sample = "prior to its amendment by Republic Act (RA) No. 8424, otherwise known as the Tax Reform Act of 1997; Section 533 of Rep. Act 7160 reads in part:"
    >>> match_provision(sample)
    <re.Match object; span=(101, 116), match='Section 533 of '>
    """
    return ProvisionPattern.search(text)


def match_provisions(text: str) -> list[Match]:
    """
    >>> sample = "prior to its amendment by Republic Act (RA) No. 8424, otherwise known as the Tax Reform Act of 1997; Section 533 of Rep. Act 7160 reads in part:"
    >>> match_provisions(sample)
    [<re.Match object; span=(101, 116), match='Section 533 of '>]
    """
    return list(ProvisionPattern.finditer(text))
