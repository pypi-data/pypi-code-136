import calendar
import re
from dataclasses import dataclass
from datetime import date, timedelta
from typing import IO, List, Tuple

from boatrace.models import RaceGrade, RaceKind, StadiumTelCode
from boatrace.official.exceptions import ScrapingError
from boatrace.official.v1707.decorators import no_content_handleable
from bs4 import BeautifulSoup


@dataclass(frozen=True)
class Event:
    stadium_tel_code: StadiumTelCode
    title: str
    starts_on: date
    days: int
    grade: RaceGrade
    kind: RaceKind


@no_content_handleable
# note: 命名について
# scrape_events にしようと思ったが scrape の目的語はスクレイピング対象のWebページだから違和感ある
# get_events はアクセサメソッド見たいなニュアンスがあって違和感ある
# 引数のWebページのHTMLからデータを抜き出すという意味で extract が合ってると思ったので以下の名前にした
def extract_events(file: IO) -> List[Event]:
    soup = BeautifulSoup(file, "html.parser")

    schedule_rows = soup.select("table.is-spritedNone1 tbody tr")
    if len(schedule_rows) != 24:
        # 公式サイトの仕様では場を指定できるが、用途がまだないのでYAGNI原則を遵守して未実装
        raise ScrapingError

    _, current_month = _parse_calendar(soup)
    offset_day = _parse_offset_date(soup)

    data = []

    for stadium_tel_code, row in enumerate(schedule_rows, 1):
        date_pointer = offset_day

        for series_cell in row.select("td"):
            series_days_str = series_cell.get("colspan")
            if series_days_str is None:
                date_pointer = date_pointer + timedelta(1)
                continue

            series_days = int(series_days_str)
            title = series_cell.get_text()

            if title and (date_pointer.month == current_month):
                data.append(
                    Event(
                        stadium_tel_code=StadiumTelCode(stadium_tel_code),
                        title=title,
                        starts_on=date_pointer,
                        days=series_days,
                        grade=_parse_race_grade_from_html_class(series_cell["class"][0])
                        or _parse_race_grade_from_event_title(title)
                        or RaceGrade.NO_GRADE,
                        kind=_parse_race_kind_from_html_class(series_cell["class"][0])
                        or _parse_race_kind_from_event_title(title)
                        or RaceKind.UNCATEGORIZED,
                    )
                )

            date_pointer = date_pointer + timedelta(series_days)

    return data


def _parse_calendar(soup: BeautifulSoup) -> Tuple[int, int]:
    """どの年月の月間スケジュールかを返す

    Args:
        soup (BeautifulSoup): bs4でパースされた月間スケジュールのHTML

    Returns:
        Tuple[int, int]: 西暦と月のタプル
    """
    if match := re.search(
        r"\?ym=(\d{6})", soup.select_one("li.title2_navsLeft a")["href"]
    ):
        return calendar._nextmonth(
            year=int(match.group(1)[:4]), month=int(match.group(1)[4:])
        )
    else:
        raise ScrapingError


def _parse_offset_date(soup: BeautifulSoup) -> date:
    """月間スケジュールの起点となる日付を返す

    例えば、スクレイピング対象の月間スケジュールが2015年11月の場合でも、カレンダーは11/01から始まっているとは限らない
    前月の28日などから始まっている可能性があり、月により開始日はまちまちである。それを動的に取得する

    Args:
        soup (BeautifulSoup): bs4でパースされた月間スケジュールのHTML

    Returns:
        Tuple[int, int]: 西暦と月のタプル
    """
    year, month = _parse_calendar(soup)

    if match := re.search(
        r"(\d{1,2})", soup.select_one("table thead tr").select("th")[1].get_text()
    ):
        start_day = int(match.group(1))
        if start_day == 1:
            return date(year, month, 1)
        else:
            year_of_last_month, last_month = calendar._prevmonth(year, month)
            return date(year_of_last_month, last_month, start_day)

    else:
        raise ScrapingError


def _parse_race_grade_from_event_title(event_title: str):
    if match := re.search(
        r"G[1-3]{1}", event_title.translate(str.maketrans("ＧⅠⅡⅢ１２３", "G123123"))
    ):
        try:
            return RaceGrade(match.group(0))
        except ValueError:
            return None
    else:
        return None


def _parse_race_grade_from_html_class(html_class: str):
    if match := re.match(r"is-gradeColor(SG|G[123])", html_class):
        return RaceGrade(match.group(1))

    if html_class == "is-gradeColorLady":
        return RaceGrade.G3

    return None


def _parse_race_kind_from_event_title(event_title: str):
    if match := re.search(r"男女[wWＷ]優勝戦", event_title):
        return RaceKind.DOUBLE_WINNER
    else:
        return None


def _parse_race_kind_from_html_class(html_class: str):
    if html_class == "is-gradeColorRookie":
        return RaceKind.ROOKIE
    elif html_class == "is-gradeColorVenus":
        return RaceKind.VENUS
    elif html_class == "is-gradeColorLady":
        return RaceKind.ALL_LADIES
    elif html_class == "is-gradeColorTakumi":
        return RaceKind.SENIOR
    else:
        return None
