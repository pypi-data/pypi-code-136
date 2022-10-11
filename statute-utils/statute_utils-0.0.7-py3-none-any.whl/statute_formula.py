import re
from collections import Counter
from enum import Enum, unique
from typing import Any, Iterator, Match, NamedTuple, Pattern

from statute_utils.formula import (
    AdministrativeMatter,
    BarMatter,
    BatasPambansa,
    CircularOCA,
    CircularSC,
    CommonwealthAct,
    ExecutiveOrder,
    LegacyAct,
    LetterInstruction,
    NamedStatute,
    NamedStatuteIndeterminate,
    PresidentialDecree,
    RepublicAct,
    ResolutionEnBanc,
    VetoMessage,
)
from statute_utils.statute_objs import StatuteLabel


class Connector(Enum):
    Generic = "No."
    Tagalog = "Blg."
    Date = "dated"
    Dash = "-"
    Blank = ""


class StatuteTitleAspect(NamedTuple):
    """Statutes are serialized based on their prefixing aspect."""

    category: str
    connector: str
    shortcut: str
    helptext: str
    constructor: Any | None  # TODO: must change Any

    @property
    def full_serial_start(self):
        """For StatuteID.RA, this would be 'Republic Act No.' where `Republic Act` refers to the category and `No.` refers to the connector."""
        return " ".join([self.category, self.connector]).strip()


@unique
class StatuteID(Enum):
    RA = StatuteTitleAspect(
        category="Republic Act",
        connector=Connector.Generic.value,
        shortcut="RA",
        helptext="President approved after Congressional deliberations",
        constructor=RepublicAct,
    )
    CA = StatuteTitleAspect(
        category="Commonwealth Act",
        connector=Connector.Generic.value,
        shortcut="CA",
        helptext="Laws passed, with presidential approval, during the Philippine Commonwealth under American Occupation",
        constructor=CommonwealthAct,
    )
    ACT = StatuteTitleAspect(
        category="Act",
        connector=Connector.Generic.value,
        shortcut="ACT",
        helptext="Governing statutes during American Occupation after the Treaty of Paris",
        constructor=LegacyAct,
    )
    CONST = StatuteTitleAspect(
        category="Constitution",
        connector=Connector.Blank.value,
        shortcut="CONST",
        helptext="Three recognized constitutions of the Philippine Republic: 1935, 1973 and 1989",
        constructor=None,
    )
    SPAIN = StatuteTitleAspect(
        category="Spanish",
        connector=Connector.Blank.value,
        shortcut=Connector.Blank.value,
        helptext="Legacy codes during Spanish colonization",
        constructor=None,
    )
    BP = StatuteTitleAspect(
        category="Batas Pambansa",
        connector=Connector.Tagalog.value,
        shortcut="BP",
        helptext="The Tagalog Version of Republic Act",
        constructor=BatasPambansa,
    )
    PD = StatuteTitleAspect(
        category="Presidential Decree",
        connector=Connector.Generic.value,
        shortcut="PD",
        helptext="Legislated presidential laws during the initial Marcos regime",
        constructor=PresidentialDecree,
    )
    EO = StatuteTitleAspect(
        category="Executive Order",
        connector=Connector.Generic.value,
        shortcut="EO",
        helptext="Legislated presidential laws during (a) the initial Marcos regime, prior to the People Power Revolution; and (b) the initial Aquino regime, prior to the adoption of the 1987 Constitution",
        constructor=ExecutiveOrder,
    )
    LOI = StatuteTitleAspect(
        category="Letter of Instruction",
        connector=Connector.Generic.value,
        shortcut="LOI",
        helptext="Legislated presidential laws during (a) the initial Marcos regime, prior to the People Power Revolution; and (b) the initial Aquino regime, prior to the adoption of the 1987 Constitution",
        constructor=LetterInstruction,
    )
    VETO = StatuteTitleAspect(
        category="Veto Message",
        connector=Connector.Dash.value,
        shortcut="Veto",
        helptext="Presidential vetoes allowed under the 1987 Constitution",
        constructor=VetoMessage,
    )
    ROC = StatuteTitleAspect(
        category="Rules of Court",
        connector=Connector.Blank.value,
        shortcut="ROC",
        helptext="Issuances that are now the sole preregative of the Philippine Supreme Court",
        constructor=None,
    )
    RULE_BM = StatuteTitleAspect(
        category="Bar Matter",
        connector=Connector.Generic.value,
        shortcut="BM",
        helptext="SC rule-based issuances involving the admission to the Philippine Bar",
        constructor=BarMatter,
    )
    RULE_AM = StatuteTitleAspect(
        category="Administrative Matter",
        connector=Connector.Generic.value,
        shortcut="AM",
        helptext="SC rule-based issuances involving the administration of justice",
        constructor=AdministrativeMatter,
    )
    RULE_RESO = StatuteTitleAspect(
        category="Resolution of the Court En Banc",
        connector=Connector.Date.value,
        shortcut="SC Reso.",
        helptext="Rule-based resolutions adopted by the Supreme Court",
        constructor=ResolutionEnBanc,
    )
    OCA_CIR = StatuteTitleAspect(
        category="OCA Circular",
        connector=Connector.Generic.value,
        shortcut="OCA Cir.",
        helptext="Rule-based resolutions adopted by the Office of the Court Administrator",
        constructor=CircularOCA,
    )
    SC_CIR = StatuteTitleAspect(
        category="SC Circular",
        connector=Connector.Generic.value,
        shortcut="SC Cir.",
        helptext="Rule-based resolutions adopted by the Supreme Court",
        constructor=CircularSC,
    )

    @classmethod
    def serializables(cls):
        for _, serial_member in cls.__members__.items():
            if serial_member.value.constructor:
                yield serial_member.value

    @classmethod
    def assign_label(cls, candidate: Match):
        """Each `constructor` contains a `matcher()` method.
        >>> from statute_utils import StatuteID
        >>> sample = StatuteID.match_statute('Section 2 of Presidential Decree No. 1474-B')
        >>> sample
        <re.Match object; span=(13, 43), match='Presidential Decree No. 1474-B'>
        >>> StatuteID.assign_label(sample)
        StatuteLabel(category='PD', identifier='1474-B')
        """
        if label := NamedStatute.matcher(candidate):
            return label
        for s in cls.serializables():
            # serializables() checks if the constructor method exists
            if label := s.constructor.matcher(candidate):
                return label
        return NamedStatuteIndeterminate.matcher(candidate)

    @classmethod
    def patterns(cls) -> Pattern:
        """
        A `STATUTE` style refers to a pattern object based on various regex options. Examples include:
        1. CONST,
        2. RA 354
        3. Republic Act No. (RA) 354
        """
        numbered = [s.constructor().formula for s in cls.serializables()]
        named = [NamedStatute.formula]  # needs to be first
        indeterminate = [NamedStatuteIndeterminate.formula]  # needs to be last
        compiled = named + numbered + indeterminate
        return re.compile(rf"({'|'.join(compiled)})", re.X)

    @classmethod
    def match_statute(cls, text: str) -> Match | None:
        """
        >>> from statute_utils import StatuteID
        >>> sample = "prior to its amendment by Republic Act (RA) No. 8424, otherwise known as the Tax Reform Act of 1997; Section 533 of Rep. Act 7160 reads in part:"
        >>> StatuteID.match_statute(sample)
        <re.Match object; span=(26, 52), match='Republic Act (RA) No. 8424'>
        """
        return cls.patterns().search(text)

    @classmethod
    def match_statutes(cls, text: str) -> list[Match]:
        """
        >>> from statute_utils import StatuteID
        >>> sample = "prior to its amendment by Republic Act (RA) No. 8424, otherwise known as the Tax Reform Act of 1997; Section 533 of Rep. Act 7160 reads in part:"
        >>> StatuteID.match_statutes(sample)
        [<re.Match object; span=(26, 52), match='Republic Act (RA) No. 8424'>, <re.Match object; span=(116, 129), match='Rep. Act 7160'>]
        """
        return list(cls.patterns().finditer(text))

    @classmethod
    def get_statute_matches(cls, text: str) -> list[StatuteLabel] | None:
        if matches := cls.match_statutes(text):
            return [cls.assign_label(match) for match in matches]
        return None

    @classmethod
    def get_statute_labels(cls, text: str) -> list[StatuteLabel] | None:
        if matches := cls.match_statutes(text):
            return [cls.assign_label(match) for match in matches]
        return None

    def get_legacy_spanish_code(self, text: str):
        """Legacy docs don't have serialized identifiers"""
        remainder = text.removeprefix("Spanish ").lower()
        if "civil" in remainder:
            return "civil"
        elif "commerce" in remainder:
            return "commerce"
        elif "penal" in remainder:
            return "penal"

    def get_legacy_spanish_text(self, idx: str):
        if code := self.get_legacy_spanish_code(f"Spanish {idx}"):
            if code == "civil" or code == "penal":
                return f"Spanish {code.title()} Code"
            elif code == "commerce":
                return "Spanish Code of Commerce"

    def get_idx(self, txt: str) -> str:
        """Given text e.g. `Spanish Civil Code` or `Executive Order No. 111`, get the serial number"""
        if self.name == "SPAIN" and (
            code := self.get_legacy_spanish_code(txt)
        ):
            return code  # special case
        return txt.replace(self.value.full_serial_start, "").strip()  # regular

    def search_pair(self, txt: str) -> tuple[str, str] | None:
        """Return shortcut tuple of member name and identifier, if found."""
        return (
            (self.name, self.get_idx(txt))
            if self.value.category in txt
            else None
        )

    def make_title(self, idx: str, is_shortcut=False) -> str:
        """Return full title; notice inverted order for Rules of Court, Constitution"""

        # invert
        if self.name in ["ROC", "CONST"]:
            if is_shortcut:
                return f"{idx} {self.value.shortcut}"  # e.g. 1987 CONST
            return f"{idx} {self.value.full_serial_start}"  # e.g. 1987 Constitution

        # special
        elif self.name == "SPAIN":
            if code := self.get_legacy_spanish_text(idx):
                return code

        # default
        if is_shortcut:
            return f"{self.value.shortcut} {idx}"  # e.g. RA 1231
        return f"{self.value.full_serial_start} {idx}"  # e.g. Republic Act No. 1231

    @classmethod
    def get_statute_choices(cls) -> list[tuple[str, str]]:
        return [
            (name, m.value.category) for name, m in cls.__members__.items()
        ]

    @classmethod
    def get_member(cls, query: str):
        """Get the StatuteID object representing the name, e.g. 'ra', 'oca_cir', etc."""
        for name, member in cls.__members__.items():
            if name == query.upper():
                return member
        return None

    @classmethod
    def extract_shortcut(cls, query: str) -> str | None:
        """`Republic Act No. 386` becomes `RA 386`"""
        for name, member in cls.__members__.items():
            if pair := member.search_pair(query):
                return f"{member.value.shortcut} {pair[1]}"
        return None

    @classmethod
    def extract_pair(
        cls,
        text: str,
    ) -> tuple[str, str] | None:
        """Given statutory text, e.g. "Republic Act No. 386", get a matching category ("RA") and identifier ("386") by going through each member of the `StatuteID` enumeration"""
        for _, member in cls.__members__.items():
            if pair := member.search_pair(text):
                return pair
        return None


def shorten_item(text: str):
    """Replace the item's long form keyword with its shorthand format, if possible."""
    return StatuteID.extract_shortcut(text)


class StatuteCounted(NamedTuple):
    statute: StatuteLabel
    mentions: int

    @classmethod
    def extract_statutes(cls, content: str) -> Iterator[str]:
        """Extract iterator of statute serial texts so that these can be counted via `Counter()`"""
        if statutes := StatuteID.get_statute_labels(content):
            for s in statutes:
                if isinstance(s, StatuteLabel):  # cat + idx exists
                    if s.is_single:
                        yield f"{s.category} {s.identifier}"
                    else:  # more than one StatuteLabel should exist
                        for dx in s.deconstructed_identifiers:
                            if isinstance(
                                dx, StatuteLabel
                            ):  # cat + idx exists
                                yield f"{dx.category} {dx.identifier}"

    @classmethod
    def count_statutes(cls, content: str):
        statutes_detected = list(cls.extract_statutes(content))
        counted = Counter(statutes_detected)
        for i in iter(set(statutes_detected)):
            yield cls(statute=StatuteLabel(*i.split()), mentions=counted[i])
