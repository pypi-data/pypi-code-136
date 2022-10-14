import datetime
from enum import Enum
from typing import Iterator

from citation_docket.simple_matcher import updated_cat_idx
from citation_report import Publisher, Report, get_reports
from dateutil.parser import parse
from pydantic import BaseModel
from slugify import slugify

from .constructors import CitationType, Docket, Style
from .helpers import filter_out_docket_reports


class DocketCategory(str, Enum):
    GR = Style.GR.value.short_category
    AM = Style.AM.value.short_category
    AC = Style.AC.value.short_category
    BM = Style.BM.value.short_category


class Citation(BaseModel):
    docket: str | None = None
    docket_category: DocketCategory | None = None
    docket_serial: str | None = None
    docket_date: datetime.date | None = None
    phil: str | None = None
    scra: str | None = None
    offg: str | None = None

    class Config:
        use_enum_values = True

    @property
    def slug(self) -> str | None:
        els = [self.docket, self.scra, self.phil, self.offg]
        values = [el for el in els if el is not None]
        return slugify(" ".join(values)).strip() or None

    @classmethod
    def create_from_orig(cls, data: dict) -> "Citation" | None:
        """Requires `orig_idx`, `docket`, and `date_prom` keys set in the `data` dictionary. This enables creation of the Citation object from the originally scraped details.yaml"""
        if not all(data.get(i) for i in ["orig_idx", "docket", "date_prom"]):
            return None
        input = {"orig_idx": data["orig_idx"], "docket": data["docket"]}
        res = updated_cat_idx(input)
        if "cat" in res and "idx" in res:
            d = parse(data["date_prom"]).strftime("%b %-d, %Y")
            cat = res["cat"].upper()
            idx = res["idx"].upper()
            try:
                return next(cls.find_citations(f"{cat} {idx}, {d}"))
            except StopIteration:
                return None
        return None

    @classmethod
    def get_styles(cls, raw: str) -> list[CitationType]:
        """Combine `Docket`s (which have `Reports`), and filtered `Report` models, if they exist."""
        if dockets := list(
            Style.extract(raw)
        ):  # each docket may have a report
            if reports := list(
                get_reports(raw)
            ):  # duplicate reports now possible
                if undocketed := filter_out_docket_reports(
                    raw, dockets, reports
                ):
                    return dockets + list(undocketed)  # ensures unique reports
                return dockets + reports
            return dockets
        else:
            if reports := list(get_reports(raw)):
                return reports
        return []

    @classmethod
    def find_citations(cls, text: str) -> Iterator["Citation"]:
        for c in cls.get_styles(text):
            citation_data = {}
            if isinstance(c, Docket) and c.ids:
                citation_data = {
                    "docket": str(c),
                    "docket_category": c.short_category,
                    "docket_serial": c.first_id,
                    "docket_date": c.docket_date,
                }
            if isinstance(c, Report):
                citation_data |= {
                    "phil": f"{c.volume} Phil. {c.page}"
                    if c.publisher == Publisher.Phil.label
                    else None,
                    "scra": f"{c.volume} SCRA {c.page}"
                    if c.publisher == Publisher.Scra.label
                    else None,
                    "offg": f"{c.volume} O.G. {c.page}"
                    if c.publisher == Publisher.Offg.label
                    else None,
                }
            yield cls(**citation_data)
