from enum import auto
from .auto_name import AutoName

class Language(AutoName):
    """Enumeration used to declare locales as ISO-3166 codes (but only available in HAFAS ones)."""

    DE = auto()
    "German"

    DA = auto()
    "Danish"

    EN = auto()
    "English"

    ES = auto()
    "Spanish"

    FR = auto()
    "French"

    HU = auto()
    "Hungarian"

    IT = auto()
    "Italian"

    NL = auto()
    "Dutch"

    NO = auto()
    "Norwegian"

    PL = auto()
    "Polish"

    SV = auto()
    "Swedish"

    TR = auto()
    "Turkish"