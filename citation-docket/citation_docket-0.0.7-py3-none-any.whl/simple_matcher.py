import re
from datetime import date
from typing import Iterator, Match, NoReturn, Optional, Pattern, Union

from dateutil.parser import parse

MAX_LENGTH_IDX = 100


def parse_date_if_exists(text: str | None) -> date | None:
    "If the variable contains text with more than 5 characters, parse possible date."
    if not text:
        return None
    elif text and len(text) < 5:
        return None
    elif not (parsed := parse(text)):
        return None
    return parsed.date()


def construct_docket_categories() -> Iterator[str]:
    for i in ("gr", "am", "ac", "bm"):
        yield rf"(?P<{i}>{i[0]}\s*\.?\s*{i[1]}\s*\.?)"


DOCKET_OPTIONS: str = "|".join(construct_docket_categories())
SIMPLE_DOCKET_WITHOUT_DATE: Pattern = re.compile(
    rf"""(?P<undated>
        (?P<cat>{DOCKET_OPTIONS})
        \s*
        (no
            s?
            \.?
        )? # number keyword
        \s*
        (?P<idx>[\w-]+) # dashed word character
        \s*
    )""",
    re.I | re.X,
)


def simple_two_letter_docket_category(raw: str) -> Optional[str]:
    """Return if possible either: 'gr', 'am', 'ac', 'bm'"""
    pattern = re.compile(DOCKET_OPTIONS, re.I)
    return res.lastgroup if (res := pattern.search(raw)) else None


def get_cat_idx_from_orig(
    raw: str, simple_category: str, regex_string: str
) -> Optional[dict]:
    if not (match := re.compile(regex_string, re.I | re.X).search(raw)):
        return None
    match_string = match.group()
    culled = raw.removeprefix(match_string).strip(" *")
    if culled.startswith("No."):
        culled = culled.removeprefix("No.")
    elif culled.startswith("NO."):
        culled = culled.removeprefix("No.")
    return {"cat": simple_category, "idx": culled}


def get_cat_idx_from_docket(
    raw: str, simple_category: str, text_to_remove: str
) -> Optional[dict]:
    if not text_to_remove in raw:
        return None
    culled = raw.removeprefix(text_to_remove)
    separated = culled.split(",")
    return {"cat": simple_category, "idx": separated[0]}


def updated_cat_idx(d: dict) -> dict:
    from .base import formerly
    from .regexes import ac_key, am_key, bm_key, gr_key

    def process_idx_further(text: str) -> str:
        pattern = re.compile(formerly, re.X)
        replaced = pattern.sub("", text)
        result = replaced.split()[0].strip()
        return result

    def source_docket(raw: str) -> dict | None:
        return (
            get_cat_idx_from_docket(raw, "am", "Administrative Matter")
            or get_cat_idx_from_docket(raw, "ac", "Administrative Case")
            or get_cat_idx_from_docket(raw, "bm", "Bar Matter")
            or get_cat_idx_from_docket(raw, "gr", "General Register")
        )

    def source_orig(raw: str) -> Optional[dict]:
        return (
            get_cat_idx_from_orig(raw, "am", am_key)
            or get_cat_idx_from_orig(raw, "ac", ac_key)
            or get_cat_idx_from_orig(raw, "bm", bm_key)
            or get_cat_idx_from_orig(raw, "gr", gr_key)
        )

    def source_simple(raw: str) -> Optional[dict]:
        idx = " ".join(i for i in raw.split() if re.search(r"\d+|&|(and)", i))
        text = " ".join(
            i for i in raw.split() if not re.search(r"\d+|&|(and)", i)
        )
        if not (cat := simple_two_letter_docket_category(text)):
            return None

        return {"cat": cat, "idx": idx}

    if d.get("orig_idx", None):
        if res := source_simple(d["orig_idx"]):
            if res.get("idx", None):
                res["idx"] = process_idx_further(res["idx"])
                return res
        if res := source_orig(d["orig_idx"]):
            if res.get("idx", None):
                res["idx"] = process_idx_further(res["idx"])
                return res
    if d.get("docket", None):
        if res := source_docket(d["docket"]):
            if res.get("idx", None):
                res["idx"] = process_idx_further(res["idx"])
                return res
    return {}


def valid_idx(candidate: str) -> Union[NoReturn, str]:
    if isinstance(candidate, int):
        candidate = str(candidate)
        if len(candidate) >= MAX_LENGTH_IDX:
            raise Exception("Valid idx - presently less than 100 characters")
    return candidate


def get_date(raw: str, match: Match) -> Optional[date]:
    """Remove the docket (e.g. GR 1231) from the docket string (e.g. GR 1231, Dec. 1, 2000), to get the date text; parse this into a date object."""
    if docket_serial_text := match.group("undated"):
        return parse_date_if_exists(raw.removeprefix(docket_serial_text))
    return None


def is_docket(raw: str) -> Optional[dict]:
    """Get dict sourced from a compiled regex pattern, with the date if possible"""
    raw = raw.strip().lower()

    if not (m := SIMPLE_DOCKET_WITHOUT_DATE.match(raw)):
        return None

    if not (cat := simple_two_letter_docket_category(m.group("cat"))):
        return None
    res = {"docket_cat": cat}

    if not (idx := valid_idx(m.group("idx").upper())):
        return None
    res |= {"docket_idx": idx}

    if (dt := get_date(raw, m)) and (formatted := dt.strftime("%Y-%m-%d")):
        res |= {"docket_dated": formatted}

    return res
